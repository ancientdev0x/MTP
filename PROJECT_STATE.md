# Detailed Project State & Technical Record (MTP)

**Project:** Artifact-Aware Stability Benchmark for Fractal Attributes in Well-Log Characterization  
**Degree:** Master's Thesis Project (MTP)  
**Last Updated:** October 2026  

---

## 1. Problem Definition & Research Hypothesis

In subsurface reservoir geophysics, spatial heterogeneity in rock properties (porosity, permeability, clay volume) is frequently characterized using fractal geometry and power-law scaling. A standard parameter is the **Hurst exponent ($H \in (0, 1)$)**, related to fractal dimension ($D$):
- For a 1D self-affine profile: $D = 2 - H$.
- $H > 0.5$: Persistent / long-range positive correlation.
- $H = 0.5$: Uncorrelated Brownian motion (random walk).
- $H < 0.5$: Anti-persistent / negatively correlated fluctuations.

### The Research Gap
Numerous papers in literature compute $H$ from wireline logs (Gamma Ray, Sonic, Resistivity) and correlate it directly to depositional facies, flow units, or fracture intensity. However, these studies routinely overlook:
1. **Measurement Scale & Bandwidth Limits:** Logging tools have finite vertical resolution (e.g., 0.15 m to 0.6 m). Fluctuations below the tool resolution are instrumentally smoothed.
2. **Preprocessing Artifacts:** Standard data cleaning involves moving-average filters, despiking, and decimation. 
3. **Non-stationarity & Lithology Boundaries:** A log traversing multiple formations is not a stationary fractional Brownian process.

**Hypothesis:**  
*Fractal features derived from wireline logs are hypersensitive to standard preprocessing filters and estimator choices. Without rigorous synthetic controls and scale-invariance testing, reported $H$ values reflect logging artifacts rather than intrinsic geological scaling.*

---

## 2. Mathematical & Algorithmic Framework

### 2.1 Synthetic Generator: Davies-Harte Circulant Embedding
To establish known-answer synthetic benchmarks, we model:
- **Fractional Gaussian Noise (fGn):** Stationary Gaussian sequence with autocovariance:
  $$\gamma(k) = \frac{\sigma^2}{2} \left( |k+1|^{2H} - 2|k|^{2H} + |k-1|^{2H} \right)$$
- **Fractional Brownian Motion (fBm):** Non-stationary self-affine process formed as cumulative sum of fGn:
  $$B_H(t) = \sum_{i=1}^t X_H(i)$$

We implement exact synthesis via circulant embedding of the covariance matrix, computed in $\mathcal{O}(N \log N)$ via FFT.

### 2.2 Estimators
1. **Power Spectral Density (PSD) Estimator:**
   For fBm, power spectrum decays as $S(f) \propto f^{-\beta}$, where $\beta = 2H + 1$.  
   For fGn, $S(f) \propto f^{-\beta}$, where $\beta = 2H - 1$.  
   $H$ is estimated via linear regression in log-log space: $\log S(f)$ vs $\log f$.
2. **Variogram (Semivariance) Estimator:**
   Semivariance $\gamma(h) = \frac{1}{2N} \sum (x_{i+h} - x_i)^2$.  
   For fBm, $\gamma(h) \propto h^{2H}$.  
   $H$ is estimated from the slope of $\log \gamma(h)$ vs $\log h$ for small spatial lags $h \le h_{\max}$.

### 2.3 Perturbation Controls
- **Smoothing Filter:** 5-point boxcar moving average filter ($w=5$).
- **Decimation:** Subsampling to evaluate frequency aliasing.

---

## 3. Experimental Validation Results

### 3.1 Synthetic Benchmark (Controlled Known-Answer Gate)
Evaluated across 4 independent seeds for $H \in \{0.2, 0.5, 0.8\}$ on series of length $N = 2048$:
- **$H = 0.2$:** Recovered mean spectral $H = 0.21 \pm 0.04$, variogram $H = 0.19 \pm 0.03$. (Error $< 0.05$)
- **$H = 0.5$:** Recovered mean spectral $H = 0.50 \pm 0.03$, variogram $H = 0.49 \pm 0.02$. (Error $< 0.05$)
- **$H = 0.8$:** Recovered mean spectral $H = 0.78 \pm 0.04$, variogram $H = 0.81 \pm 0.03$. (Error $< 0.05$)

**Gate Result:** **PASS** (Both estimators reliably recover true Hurst exponents on mathematically stationary series).

### 3.2 Real Well-Log Pilot (FORCE 2020 North Sea Dataset)
Evaluated on three deterministic, high-quality Gamma Ray intervals from three distinct wells:
- Well 1: `15/9-13` (Interval: 1750.0 m – 1950.0 m, $N = 1315$ points at 0.152 m sampling).
- Well 2: `15/9-14` (Interval: 2100.0 m – 2300.0 m, $N = 1315$ points).
- Well 3: `15/9-15` (Interval: 2400.0 m – 2600.0 m, $N = 1315$ points).

#### Perturbation Results Under 5-Point Boxcar Smoothing:
| Well | Raw Spectral $H$ | Smoothed Spectral $H$ | $\Delta H$ (Spectral) | Raw Variogram $H$ | Smoothed Variogram $H$ | $\Delta H$ (Variogram) |
|---|---|---|---|---|---|---|
| `15/9-13` | 0.42 | 1.04 | **+0.62** | 0.38 | 0.41 | +0.03 |
| `15/9-14` | 0.39 | 0.99 | **+0.60** | 0.36 | 0.39 | +0.03 |
| `15/9-15` | 0.44 | 1.05 | **+0.61** | 0.41 | 0.45 | +0.04 |

**Gate Result:** **FAIL / NO-GO for Unqualified Single-$H$ Interpretation**.  
- Moving-average smoothing attenuates high frequencies, steepening the power spectral slope $\beta$ and falsely inflating the estimated Hurst exponent into the hyper-persistent regime ($H > 1.0$).
- Variogram estimates are stabilized at short lags but still exhibit scale distortion.
- **Scientific Significance:** Real wireline logs cannot be treated as stationary monofractal processes without bandpass bounding and filter normalization.

---

## 4. Dataset Details: FORCE 2020 Machine Learning Benchmark

- **Source:** Zenodo / FORCE Machine Learning Competition 2020.
- **Total Wells Audited:** 118 LAS wells from Norwegian North Sea.
- **Total Rows Audited:** 2,337,639 depth samples.
- **Common Depth Increment:** 0.1524 m (0.5 ft).
- **Core Channels Audited:** `GR` (Gamma Ray), `RHOB` (Bulk Density), `NPHI` (Neutron Porosity), `DTC` (Compressional Slowness), `RDEP` (Deep Resistivity), `FORCE_2020_LITHOFACIES` (Ground truth lithology).
- **Continuous Coverage:** 10 wells exhibit $\ge 80\%$ simultaneous coverage across the 4 primary petrophysical curves.

---

## 5. Artifact & Deliverables Inventory

1. **LaTeX Research Report:** `research_report/main.pdf` (7 pages, compiled with pdflatex + bibtex, clean compilation).
2. **Beamer Presentation Deck:** `research_presentation/main.pdf` (15 slides, detailed problem statement, figures, results, viva responses).
3. **Defense Mastery Pack:** `defense_prep/MTP_mastery_pack.pdf` and `defense_prep/MTP_simple_english_guide_complete.pdf` (28 pages containing plain-English explanations, viva Q&A, and excerpts from foundational papers).
4. **Python Implementation:** `pilot/experiment.py`, `pilot/plot.py`, `pilot/test_pilot.py` (4 unit tests passing).
5. **OKF Knowledge Vault:** `okf-open-knowledge-format/` (16 structured markdown documents covering source literature, idea matrices, and data audits).
