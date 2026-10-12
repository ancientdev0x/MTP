# Final MTP Idea Recommendation

## Executive decision

### Recommended primary idea — safest strong MTP

**Fractal-Feature Stability in Depth-Indexed Well Logs Under Sampling, Filtering, and Logging-Tool Perturbations**

**Core question:** Under controlled changes in sampling, smoothing/tool-response degradation, noise, gaps, and preprocessing, which established fractal features remain quantitatively stable and recover known values, and under what finite-scale conditions do they fail on real well logs?

**Why this is the primary recommendation:**
- It is directly grounded in the assigned book and well-log papers.
- It addresses a real methodological weakness rather than repeating a classifier application.
- It can be completed with synthetic signals plus public well logs even if repeated multi-tool acquisitions are unavailable.
- It supports objective ground truth through known synthetic H/D parameters.
- It naturally produces reproducible figures, tables, code, and a defensible negative result.
- Initial screening: scientific value 8/10, feasibility 8/10, likely novelty 7/10, data availability 8/10, validation strength 8/10, risk 3/10.

**Cautious novelty position:** Potentially novel as an integrated, reproducible perturbation-and-recovery benchmark. The component estimators are established, and exact priority is not proven by the web search. Do not claim that fractal features or Hurst estimation themselves are new.

### Recommended ambitious alternative

**Surrogate-Controlled and Segmentation-Aware Test for Genuine Multifractality in Well Logs**

This is scientifically stronger but somewhat riskier. It should be selected if the MTP has adequate time for careful multifractal implementation and sufficient wells. Its valid contribution is a quality-control and attribution protocol, not the invention of MFDFA, wavelet leaders, or surrogate testing.

### Other ranked candidates

| Rank | Candidate | Feasibility | Novelty potential | Risk | Decision |
|---:|---|---:|---:|---:|---|
| 1 | Fractal-feature stability under sampling/filtering/tool perturbations | High | Medium–high | Low | Primary |
| 2 | Surrogate-controlled, segmentation-aware genuine-multifractality test | Medium–high | Medium | Medium | Ambitious alternative |
| 3 | Uncertainty-calibrated fractal/multifractal attributes | Medium | Medium | Medium | Strong extension or backup |
| 4 | Robust multifractal measure selection | Medium–high | Medium | Medium | Focused multifractal option |
| 5 | Cross-well generalization of fractal reservoir features | Medium–low | Medium–high | High | Use only if labels and ≥3 eligible wells exist |

## Proposed primary methodology

1. **Data:** synthetic fBm/fGn and multifractal controls with known parameters; public LAS well logs, prioritizing GR and optionally density/sonic/neutron.
2. **Perturbations:** downsampling, smoothing/convolution with tool-like kernels, additive noise, gaps/missingness, detrending, and alternative window lengths.
3. **Estimators:** spectral slope/H, variogram power-law dimension, and R/S on increments; optionally one multifractal width estimator as an extension, not a requirement.
4. **Scale selection:** define lower cutoff from sampling/tool response and upper cutoff from finite-length constraints; retain only contiguous ranges with adequate log–log linearity and stable estimates.
5. **Synthetic metrics:** bias, RMSE, variance, interval coverage, failure rate, and recovery error relative to known H/D.
6. **Real-log metrics:** within-well repeatability, cross-well agreement, stability under controlled degradation, estimator disagreement, and sensitivity to geological segmentation.
7. **Controls:** compare whole-well estimates with formation/facies-segmented estimates; report when apparent scaling disappears.
8. **Validation:** bootstrap/repeated realizations, leave-one-well-out demonstration where possible, and explicit artifact sensitivity analysis.

## Expected contribution statement

> This study does not propose a new fractal estimator. It establishes an artifact-aware, finite-scale protocol for determining when established fractal attributes extracted from depth-indexed well logs are recoverable, stable, and interpretable under sampling, filtering, missingness, and geological-regime changes.

## What should not be claimed

- No universal H, D, or multifractal-width threshold for lithology, hydrocarbons, porosity, or permeability.
- No claim that a broad spectrum alone proves genuine multifractality.
- No claim that a corrected or sharper curve is necessarily more physically accurate.
- No claim that a result transfers across wells unless blind-well validation supports it.
- No claim of priority until citation chaining and direct full-text verification are complete.

## Go/no-go checks before implementation

Proceed with the primary study if at least one usable high-resolution log and a plausible public dataset are available. Proceed with the multifractal alternative only if intervals contain enough samples for multiple scales and a clear positive measure can be justified. Proceed with cross-well classification only if at least three eligible wells share channels and labels.

## Immediate implementation order

1. Download/inspect the selected LAS dataset and audit channels, sampling, nulls, and well count.
2. Implement synthetic fBm/fGn generation and validate each estimator against known parameters.
3. Add controlled sampling/filtering/noise/gap perturbations.
4. Implement formation-wise and moving-window real-log analysis.
5. Compare estimators and quantify uncertainty/stability.
6. Decide whether the multifractal extension passes the data and scaling-quality gate.
7. Freeze the final research question only after the data audit and pilot results.
