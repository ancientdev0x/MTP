#!/usr/bin/env python3
"""Bounded pilot for fractal-feature stability in depth-indexed well logs.

This is a screening experiment, not a production petrophysics pipeline.
It uses synthetic spectral-slope controls and GR intervals from FORCE 2020.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
DATA_ROOT = ROOT / "data/force2020/extracted"
OUT = ROOT / "pilot_results"
OUT.mkdir(exist_ok=True)

STEP_M = 0.152
NULL = -999.25
RNG = np.random.default_rng(20260908)


def parse_gr(path: Path) -> np.ndarray:
    curves = []
    data = False
    values = []
    for raw in path.read_text(errors="replace").splitlines():
        s = raw.strip()
        if s.upper().startswith("~CURVE"):
            data = False
            continue
        if s.upper().startswith("~ASCII"):
            data = True
            continue
        if s.startswith("~"):
            data = False
        if not data and curves is not None and s and not s.startswith("#"):
            # Curve lines occur only before ~Parameter; stop at the first section.
            if not curves and s.split()[0].upper() == "DEPT":
                curves.append("DEPT")
            elif curves and len(curves) < 100 and s.split()[0].upper() not in {"DEPT"}:
                # This branch is intentionally not used; curve extraction below is safer.
                pass
        if data and s and not s.startswith("#"):
            try:
                row = [float(x) for x in s.split()]
            except ValueError:
                continue
            values.append(row)
    # Re-read curve section with section boundaries.
    curve_names = []
    in_curve = False
    for raw in path.read_text(errors="replace").splitlines():
        s = raw.strip()
        if s.upper().startswith("~CURVE"):
            in_curve = True
            continue
        if s.startswith("~"):
            in_curve = False
        if in_curve and s and not s.startswith("#"):
            curve_names.append(s.split()[0])
    try:
        idx = next(i for i, name in enumerate(curve_names) if name.upper() == "GR")
    except StopIteration:
        return np.array([])
    out = np.array([row[idx] for row in values if len(row) > idx], dtype=float)
    out[(out == NULL) | ~np.isfinite(out)] = np.nan
    return out


def longest_valid_run(x: np.ndarray, minimum: int = 2048) -> np.ndarray:
    good = np.isfinite(x)
    padded = np.r_[False, good, False]
    starts = np.flatnonzero(~padded[:-1] & padded[1:])
    ends = np.flatnonzero(padded[:-1] & ~padded[1:])
    if not len(starts):
        return np.array([])
    lengths = ends - starts
    i = int(np.argmax(lengths))
    if lengths[i] < minimum:
        return np.array([])
    return x[starts[i] : ends[i]]


def detrend(x: np.ndarray) -> np.ndarray:
    t = np.arange(len(x), dtype=float)
    return x - np.polyval(np.polyfit(t, x, 1), t)


def spectral_h(x: np.ndarray, step: float) -> tuple[float, float, int]:
    y = detrend(x)
    p = np.abs(np.fft.rfft(y)) ** 2
    f = np.fft.rfftfreq(len(y), d=step)
    valid = (f > 0) & (p > 0)
    # Exclude the two highest-frequency bins and use a finite long-scale band.
    valid &= f <= 0.25 / step
    valid &= f >= 4.0 / (len(y) * step)
    if valid.sum() < 8:
        return math.nan, math.nan, int(valid.sum())
    slope, intercept = np.polyfit(np.log10(f[valid]), np.log10(p[valid]), 1)
    beta = -float(slope)
    h = (beta - 1.0) / 2.0
    pred = slope * np.log10(f[valid]) + intercept
    ss_res = float(np.sum((np.log10(p[valid]) - pred) ** 2))
    ss_tot = float(np.sum((np.log10(p[valid]) - np.mean(np.log10(p[valid]))) ** 2))
    return h, 1.0 - ss_res / ss_tot if ss_tot else math.nan, int(valid.sum())


def variogram_dimension(x: np.ndarray) -> tuple[float, float, int]:
    y = detrend(x)
    maxlag = max(8, min(len(y) // 4, 2048))
    lags = np.unique(np.geomspace(1, maxlag, 24).astype(int))
    gamma = np.array([0.5 * np.mean((y[k:] - y[:-k]) ** 2) for k in lags])
    valid = np.isfinite(gamma) & (gamma > 0)
    if valid.sum() < 8:
        return math.nan, math.nan, int(valid.sum())
    slope, intercept = np.polyfit(np.log10(lags[valid]), np.log10(gamma[valid]), 1)
    dim = 2.0 - float(slope) / 2.0
    pred = slope * np.log10(lags[valid]) + intercept
    ss_res = float(np.sum((np.log10(gamma[valid]) - pred) ** 2))
    ss_tot = float(np.sum((np.log10(gamma[valid]) - np.mean(np.log10(gamma[valid]))) ** 2))
    return dim, 1.0 - ss_res / ss_tot if ss_tot else math.nan, int(valid.sum())


def rs_h(x: np.ndarray) -> tuple[float, float, int]:
    # R/S is applied to increments, following the direct well-log literature.
    z = np.diff(x)
    scales = np.unique(np.geomspace(8, max(16, len(z) // 8), 16).astype(int))
    rs = []
    used = []
    for n in scales:
        chunks = len(z) // n
        if chunks < 2:
            continue
        vals = []
        for c in range(chunks):
            seg = z[c * n : (c + 1) * n]
            dev = np.cumsum(seg - np.mean(seg))
            s = np.std(seg, ddof=1)
            if s > 0:
                vals.append((np.max(dev) - np.min(dev)) / s)
        if vals:
            used.append(n)
            rs.append(np.mean(vals))
    if len(rs) < 6:
        return math.nan, math.nan, len(rs)
    slope, intercept = np.polyfit(np.log10(used), np.log10(rs), 1)
    pred = slope * np.log10(used) + intercept
    ss_res = float(np.sum((np.log10(rs) - pred) ** 2))
    ss_tot = float(np.sum((np.log10(rs) - np.mean(np.log10(rs))) ** 2))
    return float(slope), 1.0 - ss_res / ss_tot if ss_tot else math.nan, len(rs)


def synthetic_powerlaw(n: int, h: float, rng: np.random.Generator) -> np.ndarray:
    # Fourier power-law control: raw fBm-like target beta = 2H+1.
    f = np.fft.rfftfreq(n)
    amp = np.zeros_like(f)
    amp[1:] = f[1:] ** (-(2.0 * h + 1.0) / 2.0)
    phase = rng.uniform(0, 2 * np.pi, len(f))
    spec = amp * np.exp(1j * phase)
    spec[0] = 0.0
    y = np.fft.irfft(spec, n=n)
    return (y - y.mean()) / y.std()


def smooth(x: np.ndarray, sigma: float = 2.0) -> np.ndarray:
    radius = int(math.ceil(4 * sigma))
    t = np.arange(-radius, radius + 1)
    kernel = np.exp(-(t * t) / (2 * sigma * sigma))
    kernel /= kernel.sum()
    return np.convolve(x, kernel, mode="same")


def features(x: np.ndarray, step: float) -> dict:
    sh, sr2, sn = spectral_h(x, step)
    vd, vr2, vn = variogram_dimension(x)
    rh, rr2, rn = rs_h(x)
    return {"spectral_H": sh, "spectral_R2": sr2, "spectral_n": sn,
            "variogram_D": vd, "variogram_R2": vr2, "variogram_n": vn,
            "rs_H_increment": rh, "rs_R2": rr2, "rs_n": rn}


def main() -> None:
    synthetic = []
    for h in (0.3, 0.5, 0.7, 0.9):
        for seed in range(5):
            x = synthetic_powerlaw(4096, h, np.random.default_rng(seed))
            for condition, y, step in [("original", x, 1.0), ("downsample2", x[::2], 2.0), ("smooth2", smooth(x), 1.0)]:
                synthetic.append({"true_H": h, "condition": condition, "seed": seed, **features(y, step)})
    real = []
    for p in sorted(DATA_ROOT.rglob("*.las")):
        x = longest_valid_run(parse_gr(p), minimum=2048)
        if len(x) < 2048:
            continue
        x = x[: min(len(x), 8192)]
        for condition, y, step in [("original", x, STEP_M), ("downsample2", x[::2], STEP_M * 2), ("smooth2", smooth(x), STEP_M)]:
            real.append({"well": p.stem, "n": len(y), "condition": condition, **features(y, step)})
    result = {"metadata": {"synthetic_series": len(synthetic), "real_records": len(real), "step_m": STEP_M, "note": "screening pilot; not a thesis result"}, "synthetic": synthetic, "real_gr": real}
    (OUT / "pilot_results.json").write_text(json.dumps(result, indent=2, allow_nan=True), encoding="utf-8")
    # Compact summary for inspection.
    summary = {"metadata": result["metadata"]}
    for group in ("synthetic", "real_gr"):
        vals = result[group]
        summary[group] = {"records": int(len(vals)), "valid_spectral": int(sum(np.isfinite(v["spectral_H"]) for v in vals)), "valid_variogram": int(sum(np.isfinite(v["variogram_D"]) for v in vals)), "valid_rs": int(sum(np.isfinite(v["rs_H_increment"]) for v in vals))}
    (OUT / "pilot_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
