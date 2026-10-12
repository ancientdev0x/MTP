# Fractal Stability Pilot — Initial Results

## Status
This is a screening pilot, not a thesis result. Code: `pilot_fractal_stability.py`. Outputs: `pilot_results/pilot_results.json`, `pilot_results/pilot_summary.json`, and `pilot_results/pilot_metrics.json`.

## Executed design
- Synthetic Fourier power-law controls: H = 0.3, 0.5, 0.7, 0.9; 5 seeds per H.
- Conditions: original, factor-2 downsampling, Gaussian smoothing (sigma=2 samples).
- Real data: longest valid GR run per each of 118 FORCE 2020 LAS wells, minimum 2048 samples, capped at 8192 samples; same three conditions.
- Estimators: spectral H, variogram dimension, and R/S H applied to increments.
- Total synthetic records: 60.
- Total real-GR condition records: 354.
- Every estimator returned a finite value for all 60 synthetic and 354 real condition records in this pilot.

## Synthetic spectral-H recovery
The synthetic control was generated with a target raw-spectrum relation beta = 2H+1. Spectral-H results were:

| Condition | Mean bias | MAE | RMSE | Mean spectral R² |
|---|---:|---:|---:|---:|
| Original | -0.0923 | 0.0986 | 0.1771 | 0.9265 |
| Downsample ×2 | -0.0860 | 0.0939 | 0.1727 | 0.8984 |
| Smooth sigma=2 | +0.2513 | 0.4782 | 0.5725 | 0.9080 |

### Initial interpretation
- The synthetic generator/estimator combination has non-negligible finite-band bias even before perturbation.
- Factor-2 downsampling did not materially increase mean spectral-H error in this particular setup, although fit R² decreased.
- Smoothing produced a large positive spectral-H shift and much larger error. This is evidence that filtering can strongly alter an apparent fractal attribute.
- These results do **not** establish general estimator superiority. The scale-selection rule and synthetic generator must be refined and validated before formal conclusions.

## Real-GR stability
Differences are condition minus the same well’s original estimate, n=118 wells for every comparison.

| Feature | Downsample mean Δ | Downsample MAE | Smooth mean Δ | Smooth MAE |
|---|---:|---:|---:|---:|
| Spectral H | -0.1639 | 0.1655 | +0.6104 | 0.6131 |
| Variogram D | +0.0254 | 0.0255 | -0.0835 | 0.0835 |
| R/S H on increments | -0.0185 | 0.0190 | +0.1061 | 0.1061 |

Original real-GR summaries:

| Feature | n | Mean | SD | Min | Max |
|---|---:|---:|---:|---:|---:|
| Spectral H | 118 | 0.3673 | 0.1867 | -0.0687 | 0.9145 |
| Variogram D | 118 | 1.7371 | 0.0602 | 1.5972 | 1.8798 |
| R/S H on increments | 118 | 0.4208 | 0.0542 | 0.2678 | 0.5209 |

### Initial interpretation
- In this simple pilot, spectral H is highly sensitive to smoothing and moderately sensitive to downsampling.
- Variogram D is comparatively less sensitive to the tested perturbations, though smoothing still shifts it.
- R/S on increments is more stable than spectral H here, but its absolute interpretation remains dependent on the fBm/fGn convention and scale selection.
- The disagreement itself is scientifically useful: “fractal feature” is not a single acquisition-invariant quantity.

## Limitations and required fixes
1. The synthetic generator is a Fourier power-law control, not a full validated fBm/fGn generator; add a second generator or covariance-based control.
2. The current smoothing kernel is a generic Gaussian, not a measured logging-tool response.
3. The spectral fit uses a simple fixed band; the final protocol must report lower/upper scale cutoffs and contiguous linearity diagnostics.
4. Real-GR intervals were selected by longest-run length, not geological formation or facies segmentation; mixed regimes may remain.
5. No uncertainty intervals or formal paired statistical tests were included in this first pilot.
6. No lithology-conditioned or leave-one-well-out analysis was performed yet.
7. Real data are partially cleaned/despiked FORCE 2020 logs, so they are not raw instrument ground truth.
8. Smoothing and downsampling comparisons preserve approximate physical scales, but the protocol needs an explicit wavelength/depth-scale audit.

## Go/no-go decision
**GO for the primary MTP idea.** The pilot executed successfully and produced measurable, estimator-specific sensitivity—especially a strong filtering effect—while also revealing the exact methodological work needed: artifact-aware cutoffs, synthetic calibration, geological segmentation, and uncertainty reporting.

**Do not yet add the full multifractal extension.** First stabilize the monofractal benchmark and data protocol. Add multifractal analysis only after a clearly defined measure and surrogate-control pilot passes the same quality gates.
