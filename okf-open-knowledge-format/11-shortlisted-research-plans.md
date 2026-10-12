# Shortlisted MTP Research Plans

The following plans were independently developed after idea screening and targeted novelty checks. They are proposals, not final claims of novelty.

## Fractal-feature stability across sampling/tools

# MTP Research Plan

## 1. Proposed title

**Fractal-Feature Stability in Depth-Indexed Well Logs Under Sampling, Filtering, and Logging-Tool Perturbations: Synthetic Recovery and Public-Log Validation**

The title deliberately describes a robustness and measurement-effects study. It does not imply that Hurst exponents, fractal dimensions, or multifractal estimators are new.

## 2. Central research question

**Under controlled changes in depth sampling, smoothing/tool-response degradation, noise, gaps, and preprocessing, which established fractal features remain quantitatively stable and recover their known values, and under what finite-scale conditions do they fail on real well logs?**

Secondary questions:

1. Do spectral, variogram, and R/S estimates exhibit different bias and variance under the same perturbation?
2. Can a physically interpretable lower-scale cutoff be identified from synthetic recovery and then used to constrain real-log scaling fits?
3. Are differences between logging tools larger than estimator uncertainty, or can they be explained by sampling and response degradation?
4. Does explicit segmentation into approximately homogeneous intervals improve agreement compared with estimating one feature over an entire composite log?

## 3. Hypotheses

**H1 — Sampling stability:** For a fixed physical scale range above the Nyquist limit and above the tool-response cutoff, estimated features will remain approximately invariant as the sampling interval increases. Fits that include unresolved short wavelengths will show systematic bias.

**H2 — Estimator-specific degradation:** Spectral and variogram estimates will generally have lower variance than R/S estimates for sufficiently long, approximately stationary signals, while R/S will be particularly sensitive to detrending, segmentation, and whether it is applied to raw fBm-like logs or their increments.

**H3 — Tool-response effect:** Low-pass convolution will primarily suppress short-scale variance and alter the estimated scaling slope when the regression range overlaps the response roll-off. Restricting the fit to resolvable wavelengths will reduce this bias but increase uncertainty.

**H4 — Regime mixing:** Combining intervals with different means, trends, or scaling exponents will produce apparent crossovers and can create misleading whole-log estimates. Homogeneous-window analysis will improve cross-estimator agreement.

**H5 — Real-log conditional stability:** Some log channels and depth intervals will exhibit stable finite-range scaling, but no single estimator or universal H/D threshold will be valid across all tools, formations, and wells.

**H6 — Optional multifractal extension:** If included, apparent multifractal width will be substantially reduced by shuffling or phase-randomized controls in some intervals, demonstrating that broad spectra cannot automatically be interpreted as genuine geological multifractality. This is a secondary analysis, not the main contribution.

## 4. Scope and contribution claim

The primary contribution is a **reproducible controlled-perturbation benchmark** for established fractal features in 1-D well-log-like signals, combining:

- known-signal recovery from synthetic fBm/fGn and multifractal controls;
- a factorial perturbation design covering sampling, smoothing, response degradation, noise, missingness, and preprocessing;
- explicit physical-scale and tool-resolution exclusion rules;
- uncertainty estimates and block-bootstrap intervals;
- a leakage-free public-log demonstration across wells and available tool channels;
- a failure-mode catalogue rather than only a ranking of estimators.

The work should not claim to invent H, beta, variogram dimension, R/S, DFA, wavelet leaders, or a new fractal estimator. It should not claim that fractal attributes universally identify lithology, hydrocarbon zones, porosity, permeability, or geological processes. A defensible novelty statement is: **existing estimators are evaluated in a unified, well-log-specific, artifact-controlled recovery and stability protocol, with explicit physical-scale cutoffs and public reproducibility.** Even this claim must be checked against recent literature before submission.

## 5. Data plan

### 5.1 Primary real-log data

Use public LAS or equivalent depth-indexed data satisfying, where possible:

- at least three wells or independent borehole intervals;
- at least two channels among GR, RHOB, NPHI, DT/sonic, SP, or resistivity;
- documented or inferable depth sampling interval;
- enough continuous data for several windows at multiple scales;
- formation or facies markers if available;
- tool/channel metadata or acquisition notes if available.

Candidate sources to investigate during the first two weeks include publicly released multiwell datasets such as the FORCE 2020/related open well-log collections, the Equinor Volve dataset, SEG or university well-log datasets, and open LAS repositories. Dataset inclusion must be based on actual downloadability, licensing, completeness, and sampling metadata rather than the source name alone.

### 5.2 Preferred design

Select two or three datasets if feasible:

1. a multiwell dataset with consistent channels and blind-well evaluation;
2. a dataset containing multiple tool types or channels with different effective resolution;
3. one high-resolution channel suitable for controlled synthetic degradation and recovery.

Treat different channels as different physical measurements, not as repeated observations of the same latent signal. Comparisons across tools are conditional and should be described as measurement-response comparisons.

### 5.3 Fallback hierarchy

- **Fallback A:** one public high-resolution channel from several wells, with all tool perturbations simulated by known convolution, resampling, noise, and gaps.
- **Fallback B:** one or two public wells with long continuous intervals; perform within-well held-out-interval validation and avoid unsupported cross-tool claims.
- **Fallback C:** synthetic signals plus a small public-log demonstration showing only preprocessing, scale-range selection, and estimator behavior.
- **Fallback D:** if raw LAS access is inadequate, use published digitizable examples only for qualitative illustration, while keeping all quantitative claims synthetic.

Do not use proprietary or inaccessible data as a necessary acceptance criterion.

## 6. Preprocessing protocol

Preserve the original LAS files and create a machine-readable provenance table containing well, channel, units, depth range, original increment, missing-value code, and every transformation applied.

1. Parse LAS headers and curves; convert depth to a consistent unit.
2. Sort by depth, remove duplicate depths, and record irregular spacing rather than silently forcing regularity.
3. Mask invalid values and physically impossible values using channel-specific rules; never replace them before recording their locations.
4. For quantitative scaling analysis, resample only when required, using linear interpolation for small gaps and a documented maximum gap length. Exclude windows containing excessive gaps.
5. Apply channel-specific transformations only when justified, such as log10 for resistivity; report both transformed and untransformed analyses where relevant.
6. Analyze raw, globally detrended, locally detrended, and increment series as distinct estimands. Do not mix their H/D interpretations.
7. Standardize within each training or analysis interval only; no global normalization that uses held-out wells.
8. Segment at formation/facies boundaries where available and also create automatic candidate homogeneous windows using change-point or stationarity diagnostics. Automatic segmentation is exploratory unless it is fixed before testing.
9. Use physical depth scales, not sample indices, in all regression axes. For each perturbation, restrict comparisons to the common resolvable wavelength/lag range.
10. Flag edge-affected portions after convolution, wavelet transforms, and windowed estimates.

Diagnostics per interval: mean/variance trend, autocorrelation, distribution skew/kurtosis, missingness, stationarity tests used as descriptive evidence, log-log regression residuals, scale crossovers, and effective number of observations.

## 7. Estimators and equations

### 7.1 Spectral exponent

For a uniformly sampled signal x(z), estimate the power spectral density P(k) using Welch averaging with a documented window and overlap. Fit

`log P(k) = a - beta log k + error`

only over a pre-specified approximately linear physical-wavenumber range. For fGn-like increments, use `H = (beta + 1)/2`; for fBm-like integrated signals, use `H = (beta - 1)/2`. State explicitly which convention is used. Do not infer fractality from a high R-squared value alone.

### 7.2 Variogram dimension

Compute the empirical semivariogram

`gamma(h) = (1/(2 n_h)) sum_i [x(z_i+h)-x(z_i)]^2`.

Fit `gamma(h) = c h^b` over the selected scaling range. For a 1-D graph under the adopted convention, report `D_var = 2 - b/2`. Also report the fitted slope and valid lag range because the dimension conversion is conditional on self-affine assumptions.

### 7.3 Rescaled-range estimate

For increments or an explicitly justified stationary series, divide the sequence into blocks of length n. In each block, calculate the cumulative-deviation range R(n) and standard deviation S(n), then fit

`E[R(n)/S(n)] = C n^H`.

Estimate H as the slope of `log(R/S)` versus `log n`. Report both the estimate and the block/scale choices. Raw fBm-like logs and increment series must be analyzed separately; direct R/S on raw fBm-like signals is expected to overestimate H in some cases.

### 7.4 Optional DFA baseline

Use first-order DFA as a robustness baseline for locally detrended scaling:

`F_2(s) = [ (1/N_s) sum_v F_v(s)^2 ]^(1/2)`,

with `F_2(s) proportional to s^alpha` and alpha interpreted according to whether the input is fGn-like or fBm-like. DFA is optional and should be removed if it expands the scope without improving the comparison.

### 7.5 Optional multifractal analysis

Include only after monofractal validation. Define the measure explicitly; do not call multifractal spectra measure-independent. Candidate measures are:

- positive raw-property mass after an auditable positivity rule;
- absolute increments at specified lags;
- transformed-property mass;
- wavelet coefficient/leader magnitudes.

For a positive measure `mu_i(epsilon)`, compute

`Z_q(epsilon) = sum_i mu_i(epsilon)^q`,

fit `Z_q(epsilon) proportional to epsilon^(tau(q))`, and derive

`alpha(q) = d tau(q)/dq`,
`f(alpha) = q alpha - tau(q)`.

Use a conservative q-grid, for example `q in {-3,-2,-1,0,1,2,3}`, only if all moments are numerically stable. Report the valid scale range, linear-fit diagnostics, negative-q failures, and boundary handling. Compare MFDFA or wavelet leaders as a secondary estimator, not as the central novelty. Use shuffled and phase-randomized or nonstationarity-preserving surrogates where appropriate.

## 8. Controlled perturbation matrix

Construct perturbations from a clean synthetic or high-resolution real-log reference. The minimum factorial design is:

- sampling interval: original, 2x, 4x, and 8x where physically meaningful;
- anti-alias filter: none, boxcar, Gaussian, and low-pass filter with documented cutoff;
- tool response: convolution with Gaussian or measured/parameterized low-pass kernels, varying effective resolution;
- additive noise: independent white noise and correlated noise at low, medium, and high signal-to-noise ratios;
- gaps: none, short random gaps, clustered gaps, and regularly spaced missing sections;
- trend: none, linear trend, polynomial trend, and piecewise trend;
- preprocessing: raw, increment, global detrend, local detrend, and normalization;
- record length: short, medium, and long windows;
- regime structure: homogeneous signal versus concatenated signals with a change in H or mean.

Use a fractional factorial design if the full cross-product is too large, but retain all main effects and the interactions most relevant to the hypotheses: sampling x filtering, filtering x estimator, record length x estimator, and regime mixing x detrending. Fix random seeds and generate at least 100 independent realizations per key synthetic condition.

## 9. Synthetic experiments

### S1: Monofractal recovery

Generate fBm and fGn with known `H` values spanning approximately 0.2, 0.4, 0.5, 0.6, and 0.8, using at least two generation methods or a trusted library. Use lengths representative of real windows, for example 512, 2048, 8192, and 32768 samples. Verify the clean reference estimates before perturbation.

Outputs: bias, RMSE, standard deviation, interval coverage, and failure rate by estimator, H, length, and scale range.

### S2: Tool and sampling degradation

Convolve the clean realization with known kernels, anti-alias filter before downsampling, then downsample. Compare estimated feature changes with the known response cutoff. This experiment tests whether excluding unresolved scales restores recovery.

### S3: Noise and missingness

Add white and correlated measurement noise and impose random and clustered gaps. Compare interpolation, omission, and gap-aware estimation. Treat imputation as a perturbation, not as ground truth.

### S4: Nonstationary and mixed-regime signals

Concatenate segments with different H, means, trends, or variances. Test whole-record estimation against fixed homogeneous windows and change-point-informed segmentation. The target result is identification of false crossover and mixing regimes, not forced recovery of a single global H.

### S5: Multifractal controls

Generate a binomial multiplicative cascade or another validated multifractal measure with known theoretical `tau(q)` and `f(alpha)`. Analyze positive measures and absolute increments separately. Add fBm, shuffled, phase-randomized, and mixed-regime controls to quantify apparent multifractality.

## 10. Real-log experiments

### R1: Descriptive scale maps

For each well and channel, calculate moving-window spectral beta/H, variogram dimension, and R/S H over fixed physical windows. Show the fitted scaling range and uncertainty, not only the attribute curve.

### R2: Perturbation replay

Apply the same sampling, smoothing, response, noise, gaps, and preprocessing perturbations to real logs. Compare changes relative to the original at only the common resolvable scales.

### R3: Cross-tool and cross-well comparison

Within each dataset, compare channels conditionally on matching depth intervals and window sizes. Use grouped well-level summaries and leave-one-well-out plots. Do not interpret disagreement as estimator failure until channel physics, depth alignment, and tool resolution have been considered.

### R4: Held-out interval or well validation

Pre-register all preprocessing, scale-selection rules, and estimator settings before evaluating the final held-out wells. If supervised labels exist, use them only as secondary validation; the primary endpoint is feature stability and recovery, not facies accuracy.

### R5: Optional multifractal demonstration

Select a small number of intervals that pass scaling diagnostics. Compare original results with shuffled and phase-randomized/nonstationarity-preserving surrogates. Report this as evidence about the origin and reproducibility of apparent multifractality, not proof of a geological mechanism.

## 11. Baselines

1. Raw pointwise log statistics: mean, standard deviation, range, coefficient of variation, skewness, and lag-1 autocorrelation.
2. Spectral slope without explicit cutoff exclusion.
3. Spectral slope with the proposed cutoff rule.
4. Variogram dimension.
5. R/S on raw data and on increments.
6. DFA, if retained.
7. A simple finite-difference roughness or RMS-increment baseline.
8. Whole-log estimation versus fixed-window estimation.
9. No-filter downsampling versus anti-aliased downsampling.
10. Optional multifractal MFDFA versus wavelet leaders, with a single pre-specified measure and scale range.

The baseline comparison must distinguish estimator performance from the effect of a better-selected scaling range.

## 12. Metrics

### Recovery and uncertainty

- bias: mean estimated value minus known value;
- absolute bias and RMSE;
- Monte Carlo standard deviation;
- median absolute error;
- empirical 95% interval coverage;
- average interval width;
- false-positive rate for declaring persistence, antipersistence, or multifractality;
- proportion of runs with an admissible scaling range.

### Stability

- relative change from the clean reference;
- coefficient of variation;
- intraclass correlation coefficient across perturbations;
- Spearman rank correlation of intervals/wells;
- Bland–Altman bias and limits of agreement;
- cross-estimator agreement, reported as correlation and disagreement in physical units;
- stability as a function of the ratio between fitted wavelength and response cutoff;
- valid-scale fraction and crossover-detection rate.

### Real-log reproducibility

Report per-well and pooled distributions, not only pooled averages. Use macro-level summaries so long wells do not dominate. If labels are available as an exploratory endpoint, report balanced accuracy and macro-F1 with well-wise splits, but do not make classification performance the principal claim.

## 13. Statistical analysis

Use block bootstrap or moving-block bootstrap because adjacent depth samples are dependent. For synthetic data, use independent realizations as the primary replication unit. For real logs, use well or geological interval as the higher-level replication unit.

- Fit mixed-effects models such as `error ~ sampling * filter * estimator + length + (1|signal_or_well)` for synthetic/real grouped analyses.
- Use paired permutation tests for clean-versus-perturbed differences within the same realization or interval.
- Compare estimators with bootstrap confidence intervals for paired RMSE, coverage, and stability differences.
- Use cluster-robust or well-clustered uncertainty for real logs.
- Correct multiple pairwise comparisons with Holm correction.
- Report effect sizes and confidence intervals, not only p-values.
- Treat `p < 0.05` as a pre-specified convention but emphasize practical effect sizes and coverage calibration.
- Avoid treating thousands of overlapping windows as independent observations.
- If normality or model assumptions fail, use permutation, bootstrap, or robust mixed models rather than uncritical parametric tests.

## 14. Expected figures

1. Workflow diagram from LAS input through preprocessing, perturbation, estimation, uncertainty, and reporting.
2. Synthetic clean fBm/fGn examples with known H and corresponding spectra/variograms/R-S plots.
3. Heatmaps of estimator bias and RMSE over H, record length, sampling interval, and filter cutoff.
4. Stability curves versus wavelength divided by tool-response cutoff.
5. Boxplots of estimates under each perturbation, separated by estimator.
6. Interaction plots for sampling x filtering and filtering x estimator.
7. Example mixed-regime signal showing false crossover and improvement from homogeneous-window analysis.
8. Coverage-versus-nominal-confidence plots for bootstrap intervals.
9. Real-log multi-track plot with raw log, perturbations, fitted scaling ranges, and local attributes.
10. Cross-well/channel stability heatmap and Bland–Altman plots.
11. Optional multifractal spectra for original and surrogate controls, with valid q and scale ranges marked.
12. Failure-mode panel showing aliasing, roll-off, finite-length, missingness, and regime-mixing examples.

## 15. Expected tables

1. Dataset inventory: wells, channels, depth ranges, sampling, missingness, metadata, and license.
2. Preprocessing and perturbation parameter table.
3. Estimator definitions, assumptions, input type, and conversion conventions.
4. Synthetic recovery results: bias, RMSE, standard deviation, coverage, and failure rate.
5. Mixed-effects or permutation-test results with effect sizes and adjusted p-values.
6. Real-log per-well stability summaries.
7. Recommended estimator-specific operating ranges and known failure modes.
8. Optional multifractal measure comparison, including q-range validity and surrogate rejection rates.

## 16. Risks and mitigation

**Insufficient public multiwell data:** make synthetic degradation of one or more high-resolution public channels the quantitative core and restrict real-log claims.

**Unknown tool-response kernels:** call them simulated effective-resolution perturbations, not measured tool physics; use generic kernels and sensitivity ranges.

**No true geological ground truth:** make synthetic parameter recovery the ground-truth experiment; treat facies or interpreted zones only as secondary contextual validation.

**Finite-length bias:** include multiple lengths, block bootstrap, minimum-window rules, and explicit admissible-scale criteria.

**Nonstationarity and facies mixing:** analyze segmented intervals and report crossovers; do not force one global exponent.

**Irregular depth sampling and gaps:** retain native depth coordinates, document interpolation, and exclude windows exceeding a gap threshold.

**Estimator convention errors:** maintain a unit-tested reference implementation and verify fBm/fGn relationships on synthetic signals before real data.

**Overly broad multifractal scope:** make multifractality optional and secondary; drop it rather than weakening the monofractal study.

**Multiple testing from overlapping windows:** use wells/independent realizations as replication units and avoid pseudoreplication.

**Novelty overclaim:** conduct citation chaining and a final targeted search before writing the contribution statement. Phrase results as a benchmark and empirical stability map, even if the outcome is negative.

**No meaningful estimator winner:** this is an acceptable result. The thesis can identify conditional operating regimes and show that preprocessing and scale choice dominate estimator choice.

## 17. Acceptance criteria and go/no-go decisions

By week 4, at least one public dataset or a complete synthetic-only fallback must be operational. By week 6, clean synthetic recovery must be within a pre-specified tolerance for at least two estimators on known fBm/fGn signals. By week 8, the perturbation pipeline must reproduce expected aliasing and low-pass roll-off effects. By week 10, real-log results must include uncertainty and valid-scale diagnostics for multiple independent wells or intervals.

Go/no-go rules:

- If public data have fewer than three independent wells, remove cross-well generalization claims.
- If tool metadata are unavailable, replace tool-specific language with controlled response-degradation language.
- If multifractal estimates fail basic scaling and surrogate diagnostics, omit them from the main conclusions.
- If no estimator is consistently superior, report conditional stability rather than selecting a universal best method.

## 18. 14-week task sequence

**Week 1:** Freeze research question, hypotheses, estimator conventions, novelty wording, and inclusion/exclusion criteria. Build a bibliography matrix from the local notes and verify the most similar papers.

**Week 2:** Audit and acquire candidate public datasets; inspect LAS quality, licenses, channels, sampling, gaps, and well count. Select the primary dataset and fallback.

**Week 3:** Implement provenance-preserving LAS ingestion, depth regularization, missing-value handling, transformations, and diagnostic plots. Add unit tests for depth and fBm/fGn conventions.

**Week 4:** Implement spectral, variogram, R/S, and optional DFA estimators with explicit scale-range selection and uncertainty wrappers. Reproduce clean synthetic sanity checks.

**Week 5:** Implement fBm/fGn generators, independent random seeds, Monte Carlo runner, and ground-truth recovery metrics.

**Week 6:** Run S1 across H and record length. Fix estimator and convention errors; freeze the core parameter grid.

**Week 7:** Implement anti-alias filtering, downsampling, smoothing, response convolution, additive/correlated noise, gaps, and trends. Validate each perturbation independently.

**Week 8:** Run S2–S4 and produce bias, RMSE, stability, cutoff, and interaction plots. Decide whether the optional multifractal extension is feasible.

**Week 9:** Implement block bootstrap, empirical coverage, mixed-effects/permutation analyses, and multiple-comparison correction.

**Week 10:** Pre-register or freeze the real-log preprocessing and scale-selection rules. Run descriptive real-log analyses and identify admissible intervals.

**Week 11:** Run real-log perturbation replay and cross-channel/cross-well comparisons. Maintain well-wise separation for any exploratory labels.

**Week 12:** Run held-out interval/well analyses and sensitivity checks for window length, detrending, interpolation, and common physical scale range.

**Week 13:** If justified, run the limited multifractal measure/surrogate experiment; otherwise strengthen the monofractal failure-mode analysis.

**Week 14:** Consolidate figures and tables, perform an independent code/data audit, update the literature and cautious novelty statement, and write Methods, Results, Limitations, and Conclusions.

A 16-week version can reserve week 15 for replication on a second dataset and week 16 for thesis formatting, defense preparation, and archival release.

## 19. Final thesis claim to target

The strongest realistic conclusion is likely conditional: **fractal features extracted from well logs are not invariant attributes of a curve independent of acquisition and preprocessing. Their reliability is finite-scale and estimator-specific. A reproducible protocol that respects physical depth scales, excludes unresolved wavelengths, uses appropriate input conventions, and reports calibrated uncertainty can distinguish recoverable scaling from artifacts caused by sampling, filtering, finite length, gaps, and mixed geological regimes.**

## Surrogate-controlled genuine multifractality

Title: Surrogate-Controlled and Segmentation-Aware Test for Genuine Multifractality in Well Logs.

Positioning and scope: Do not claim that MFDFA, wavelet leaders, surrogate testing, segmentation, or multifractal analysis of well logs is new. Prior work already applies MFDFA, wavelet/WTMM methods, Hurst attributes, shuffled data, phase-randomized surrogates, and synthetic fBm/fGn to well logs. The defensible contribution is a reproducible well-log QC and attribution protocol that quantifies how much apparent multifractality is attributable to regime mixing, trends, finite length, heavy tails, tool filtering, sampling, gaps, or genuinely multiscale amplitude organization, using calibrated synthetic mixtures and held-out wells. A negative result—showing that apparent multifractality is usually not identifiable or is not stable across wells—counts as a valid outcome.

Exact research question: For depth-indexed well-log intervals, after leakage-free segmentation into approximately homogeneous geological regimes and explicit correction for the instrument/sample scale range, does an observed multifractal spectrum contain reproducible information beyond monofractal persistence and marginal-distribution effects, and can a surrogate- and artifact-calibrated decision rule distinguish genuine multifractal structure from false multifractality caused by concatenated regimes, trends, finite samples, heavy tails, missingness, or tool-response filtering on held-out wells?

Primary estimand and declared measure: The primary estimand is the excess multifractal curvature of the scaling function, not the raw width of an estimated spectrum. For each fixed segment and scale range, define the primary positive measure from absolute increments at lag one sample: m_i = |x_{i+1}-x_i| + epsilon, normalized as mu_i = m_i / sum_i m_i, where epsilon is prespecified as 10^-6 times the segment median nonzero m_i and is sensitivity-tested. The primary q range is q in {-4,-3,-2,-1,0,1,2,3,4}; q<0 is reported only when the minimum-mass diagnostic passes. This measure is chosen because it is sign-safe and targets scale-dependent fluctuation organization, but it is not physically canonical and must not be described as the geological measure of the reservoir.

Secondary measure families, declared before analysis: (A) positive raw-property mass after a prespecified positivity transform, using either min-shift plus epsilon or a physically positive channel such as density/porosity when justified; (B) absolute increments at lags one and four samples; (C) robust transformed-property mass, for example log-resistivity only when the channel is strictly positive; and (D) absolute discrete-wavelet coefficient or leader magnitudes. Raw values, increments, transformed values, and wavelet magnitudes are different estimands and must never be pooled as interchangeable evidence. If the primary and secondary measures disagree, report measure dependence rather than selecting the most favorable spectrum.

Hypotheses:
H1 (genuine-structure hypothesis): In homogeneous segments generated by a true multifractal process, the primary scaling function tau(q) is non-linear over a prespecified common scale range, the curvature survives appropriate null surrogates, and the direction and magnitude of curvature are reproducible across adjacent windows and held-out wells.
H2 (regime-mixture artifact): Concatenating monofractal or ordinary heterogeneous regimes with different means, variances, trends, or Hurst exponents produces apparent multifractality; segmentation will reduce curvature and false-positive rates relative to log-wide analysis.
H3 (marginal-distribution artifact): Heavy-tailed but monofractal signals will often produce broad spectra under finite samples; distribution-matched phase-randomized or IAAFT nulls will remove the apparent excess curvature if the effect is primarily marginal-distribution-driven.
H4 (correlation-only explanation): Long-range-correlated monofractal signals will retain persistence but not significant multifractal curvature after comparison with correlation-preserving monofractal nulls; shuffled surrogates alone are insufficient to test this claim.
H5 (instrument artifact): Downsampling, smoothing, convolution with a tool-response kernel, irregular sampling, and gaps alter the usable scale range and can create or suppress apparent curvature. A valid decision must reject scales below the effective resolution and report perturbation sensitivity.
H6 (transferability): A genuine QC finding should replicate in held-out wells from the same formation or field more often than a regime- or tool-specific artifact. No universal H, Delta-alpha, or hydrocarbon threshold will be claimed.

Segmentation protocol: Preserve the original depth order and metadata. First perform quality control for duplicate depths, missing values, outliers, depth gaps, abrupt tool resets, and obvious environmental corrections. Do not interpolate across large gaps for the primary analysis. Segment using geological markers, interpreted formation/facies boundaries, and log-quality boundaries when available. Where labels are unavailable, use a training-only change-point procedure based on robust mean, variance, distribution, and slope changes, with a minimum segment length fixed before testing. Analyze three conditions: (1) log-wide concatenation, (2) marker-defined segments, and (3) algorithmic segments. A segment is eligible only if it contains at least 2^10 samples, or a smaller threshold justified by a simulation-based power analysis, and at least eight usable scales with adequate independent boxes. Exclude boundary buffers of at least the largest fitted scale on both sides of a boundary. Never use test-well geology, labels, or target outcomes to choose segmentation, q, wavelet, scale ranges, or the decision threshold.

Scale selection and preprocessing: Report sample spacing, tool resolution if available, anti-aliasing filter, missingness, and all transformations. Estimate the lower cutoff from the maximum of the nominal tool-response scale, anti-aliasing transition scale, sampling interval, and a simulation-calibrated artifact cutoff. Estimate the upper cutoff as no more than one-eighth of the eligible segment length unless calibration supports a different value. Select the common scale range using training data only, requiring acceptable log-log linearity, positive fluctuation functions, sufficient box counts, and no visible crossover or spectral roll-off. Compare raw, robustly detrended, and increment versions, but define one primary preprocessing path before looking at real-data outcomes. Polynomial detrending order is fixed at one for the primary MFDFA analysis; orders zero, two, and three are ablations. Use robust scaling for numerical stability but retain physical units for interpretation.

MFDFA method: For a segment x(i), form the profile Y(k)=sum_{i=1}^k[x(i)-mean(x)]. For each scale s, divide Y into forward and backward boxes, fit a polynomial trend of order m=1, and compute F^2(nu,s) as the mean squared residual in each box. Define F_q(s)=[(1/(2N_s)) sum_nu(F^2(nu,s))^{q/2}]^{1/q} for q != 0 and the logarithmic form for q=0. Estimate h(q) by robust regression of log F_q(s) on log s over the common training-selected scale range. Compute tau(q)=q h(q)-1, alpha(q)=d tau/dq by a prespecified local polynomial derivative, and f(alpha)=q alpha-tau(q). The primary multifractality statistic is excess curvature C_MF = the improvement in out-of-sample weighted residual error of a concave quadratic or cubic tau(q) model over a linear tau(q) model, evaluated against calibrated nulls. Delta-alpha, Delta-h=h(q_min)-h(q_max), and spectrum asymmetry are secondary descriptive statistics only. Do not infer multifractality from a broad spectrum or high regression R^2 alone.

Wavelet method: Use a discrete orthogonal wavelet transform with a primary compactly supported wavelet having at least two vanishing moments, selected before real-data testing; Haar and a Daubechies alternative are mandatory sensitivity analyses. Compute coefficients and leaders using a three-interval dilation, excluding boundary-contaminated coefficients via a cone-of-influence mask. For each dyadic scale j and q in the same prespecified range, estimate leader structure functions S_L(q,j)=mean(L_{j,k}^q), fit eta_L(q) only over scales passing linearity and support diagnostics, and obtain the corresponding curvature statistic C_WL. Because leaders can be unstable near boundaries and at negative q, require a minimum fraction of nonzero, non-contaminated leaders and report q-specific validity. Wavelet leaders are a corroborating estimator, not an automatic arbiter over MFDFA.

Surrogate classes and their purposes:
1. Random permutation/shuffle surrogates: preserve the empirical marginal distribution while destroying serial dependence. Use only to test correlation-related contributions; rejection against shuffles does not establish multifractality.
2. Fourier phase-randomized surrogates: preserve the linear power spectrum and approximately Gaussianize the marginal distribution. Useful for testing nonlinear phase/amplitude organization, but inappropriate as the sole null for strongly non-Gaussian logs.
3. IAAFT surrogates: approximately preserve both the marginal distribution and power spectrum. Use for stationary segments; verify that the generated surrogates actually match both diagnostics.
4. Block-shuffled or segment-permuted surrogates: preserve short-range local structure while destroying long-range ordering. Use as a regime-ordering/null control, not as a universal null.
5. Locally stationary or segment-wise surrogates: generate surrogates independently within homogeneous subsegments while preserving local means, variances, and spectra. Use for nonstationary logs where global IAAFT is invalid.
6. Correlation-matched monofractal nulls: simulate fGn/fBm with H estimated from the segment, matched length, variance, and sampling, with heavy-tailed innovations as a separate condition. These test whether persistence plus finite-sample effects explains the spectrum.
7. Artifact-preserving nulls: apply the estimated tool kernel, sampling, gaps, and trend to otherwise known monofractal or multifractal signals. These calibrate the actual measurement pipeline.
Use at least 1,000 surrogates per primary segment/null when computationally feasible, store random seeds, and calculate empirical p-values with the +1 correction. A surrogate class must be rejected as invalid if it fails prespecified distribution, autocorrelation, or power-spectrum matching tolerances.

Synthetic benchmark and artifact mixtures: Generate independent realizations at lengths matching the real segments, with at least 100 realizations per condition and multiple random seeds. Include (i) monofractal fGn and fBm across H=0.3, 0.5, 0.7; (ii) binomial multiplicative cascades with at least two intermittency strengths; (iii) multifractal random walks or another established multifractal process; (iv) Gaussian and heavy-tailed innovations; (v) linear and piecewise trends; (vi) two- and three-regime concatenations with different means, variances, H values, and multifractal status; (vii) abrupt and gradual facies-like transitions; (viii) correlated additive measurement noise; (ix) moving-average and low-pass tool kernels with several resolution-to-sampling ratios; (x) downsampling with and without correct anti-aliasing; (xi) random and clustered gaps; and (xii) outliers and clipped values. Construct factorial mixtures in which one artifact is varied at a time and selected interactions are tested: regime mixing plus filtering, heavy tails plus finite length, and gaps plus downsampling. Preserve an untouched high-resolution parent as ground truth. Do not use synthetic data merely to demonstrate visually attractive spectra; calculate detection, attribution, bias, calibration, and recovery performance.

Real-data validation: Use publicly accessible wells with multiple conventional channels and, where possible, interpreted formation/facies markers, core measurements, repeated logging passes, or logs from tools with different resolutions. Keep all samples from a well on one side of an outer split. Preferred design is leave-one-well-out or leave-one-field/formation-out validation, with nested training-only choices for preprocessing, segmentation thresholds, q range, scale range, wavelet family, and decision thresholds. The primary real-data validation is reproducibility: compare decisions and effect sizes across held-out wells, adjacent non-overlapping windows, channels measuring related properties, and degraded versions of high-resolution curves. Secondary validation compares decisions against independent facies/core boundaries or quality flags. Do not use quick-look HC/NHC labels as independent physical truth; if such labels are used, call them interpretive labels and report the risk of circularity.

Decision rule, fixed before final real-data analysis: Declare a segment 'multifractality-supported' only if all conditions hold: (1) at least six q values have valid scaling fits over the common scale range; (2) MFDFA and wavelet-leader curvature have the same sign and overlapping uncertainty intervals, or the estimator disagreement is explicitly classified as unresolved; (3) C_MF exceeds the 95th percentile of the most conservative valid null among locally stationary, IAAFT, and correlation-matched monofractal surrogates after multiplicity correction; (4) the effect remains after excluding boundary buffers and tool-affected scales; (5) the decision is stable in at least 70% of prespecified adjacent-window or bootstrap-block replicates; and (6) it replicates in at least 50% of eligible held-out wells or held-out segments when such replication is possible. Otherwise classify the segment as 'not supported', 'artifact-consistent', or 'unresolved'. 'Not supported' is not evidence that the log is monofractal. A spectrum is specifically classified as 'regime-mixing consistent' when log-wide curvature is significant but marker-defined homogeneous segments lose significance, or when synthetic mixture calibration predicts the observed curvature. Classify as 'tool/sampling sensitive' when the decision changes under realistic resolution perturbation within the nominal usable range. Report calibrated false-positive probability rather than a binary geological claim.

Baselines:
1. Log-wide MFDFA without segmentation or surrogate testing.
2. Segmented MFDFA with shuffled surrogates only.
3. Standard wavelet variance/Hurst analysis.
4. Wavelet leaders without artifact calibration.
5. Positive partition-function analysis without MFDFA.
6. Monofractal spectral slope, variogram, and R/S estimates, with R/S applied to increments when the raw signal is fBm-like.
7. A simple linear tau(q) versus nonlinear tau(q) likelihood or information-criterion test without surrogates.
8. A conventional log-statistics baseline using variance, skewness, kurtosis, autocorrelation, and spectral slope.
9. A facies or quality classifier using raw logs only, if independent labels exist; this is secondary and must use well-wise splits.

Metrics:
Synthetic primary metrics are false-positive rate on monofractal and artifact-only nulls, true-positive rate on known multifractals, attribution accuracy among artifact classes, empirical p-value calibration, bias and RMSE of h(q), tau(q), Delta-alpha, and curvature, confidence-interval coverage, interval width, scale-range recovery, and estimator agreement. Report results by length, H, tail index, q, artifact severity, and sampling/tool condition. Real-data metrics are held-out-well replication rate, decision stability across windows, percentage of segments classified unresolved, estimator agreement, sensitivity to scale and preprocessing, null rejection rate, and effect-size distributions. If labels exist, report macro-F1, balanced accuracy, AUROC/AUPRC, calibration error, and per-well performance, but never treat classification gain as proof of genuine multifractality. Use hierarchical bootstrap or mixed-effects models with well as the grouping unit; do not pool rows as independent observations. Correct multiple testing across segments and channels using a prespecified false-discovery-rate procedure.

Ablations:
Remove segmentation; remove each surrogate class; use shuffle-only versus IAAFT versus locally stationary nulls; replace the primary increment measure with raw positive mass, transformed mass, lag-four increments, and wavelet magnitudes; vary q from [-2,2] to [-6,6]; remove negative q; vary MFDFA detrending order; vary wavelet family, vanishing moments, and leader dilation; vary minimum and maximum scales; compare overlapping and non-overlapping windows; add/remove boundary buffers; use raw versus increment signals; vary gap handling; vary anti-aliasing and tool kernels; compare fixed and training-selected scale ranges; compare global versus local normalization; and test whether a deliberately incorrect global surrogate produces inflated false positives. A key ablation is the complete decision protocol versus each component removed, measured by null calibration and held-out replication rather than only spectrum width.

Risks and harsh interpretation rules:
The largest risk is false multifractality. Trends, concatenated facies, abrupt boundaries, broad marginal distributions, isolated singularities, finite length, negative-q instability, missing samples, filtering, and poor scale selection can all broaden spectra. A straight line in a log-log plot, high R-squared, a large Delta-alpha, or a visually smooth inverted parabola is not sufficient evidence. Power-law spectra also discard phase information and cannot alone establish fractality. Shuffling is an inadequate null for nonstationary or heavy-tailed data. Global IAAFT surrogates can be invalid for nonstationary logs. Tool filtering can create crossovers and suppress the very scales being interpreted. Positive-measure construction can itself manufacture multifractality, especially for absolute increments of finite fBm/fLm samples. Negative q emphasizes small fluctuations and may be dominated by numerical epsilon, quantization, or noise. Wavelet leaders can be boundary- and basis-sensitive; MFDFA can be unstable for sparse or near-zero fluctuations. A high apparent association with facies or HC/NHC labels may reflect the fact that both the label and the fractal feature respond to the same GR trend or boundary. No causal geological interpretation is permitted from observational logs alone.

Fallback plan: If real logs lack reliable facies/core metadata, make the thesis a calibration and reproducibility study using public multiwell logs plus synthetic parent signals and report no petrophysical classification. If repeated tools or response kernels are unavailable, use documented synthetic convolution/downsampling and present real logs only as an exploratory demonstration. If segments are too short for stable negative-q analysis, restrict the primary q range to [0,4] or [−2,2] only if synthetic coverage demonstrates adequate calibration, and label the restriction. If wavelet leaders fail validity checks, retain MFDFA as the primary estimator and report wavelet failure as a result rather than tuning until agreement appears. If no measure is stable across wells, conclude that multifractality is measure-dependent and recommend against using a single spectrum as a well-log QC attribute. If the protocol cannot achieve calibrated false-positive control or held-out replication, narrow the claim to 'a failure analysis of multifractal estimators under well-log artifacts' rather than claiming a genuine-multifractality detector.

Deliverables: a preregistered analysis specification; versioned code for preprocessing, segmentation, MFDFA, wavelet leaders, surrogate generation, synthetic mixtures, and evaluation; machine-readable per-segment results including valid scales, q-specific fits, null diagnostics, p-values, uncertainty intervals, and decision labels; a synthetic benchmark table; a held-out-well results table; artifact sensitivity plots; and a limitations section that explicitly distinguishes measured signal regularity from geological interpretation. The central success criterion is not a large multifractal width. It is calibrated discrimination between known multifractal signals and realistic false-positive mechanisms, followed by reproducible, leakage-free behavior on held-out well logs.

## Uncertainty-calibrated attributes

## Working title
Uncertainty-Calibrated Fractal and Multifractal Attributes for Finite, Filtered, and Incomplete Well Logs

## Scope and contribution
The modest-MTP version should not claim a new fractal estimator or universal geological interpretation. It should deliver a reproducible, artifact-aware calibration benchmark for three existing estimators applied to depth-indexed well-log windows:

1. Spectral-slope Hurst estimate, converted to H under an explicitly stated fGn/fBm model.
2. Variogram power-law slope, converted to a graph fractal dimension D = 2 - b/2.
3. MFDFA multifractal width, using h(q) over a small, pre-specified q-grid and reporting Δh = h(q_min) - h(q_max).

The central contribution is an empirical uncertainty protocol that quantifies bias, interval coverage, calibration, and false-positive behavior under finite length, filtering/tool-resolution degradation, missingness, and local nonstationarity. The real-log component is a demonstration and external plausibility check, not proof that the estimated attributes have universal petrophysical meaning.

## Research question
When a well-log window is finite, filtered, incomplete, or locally nonstationary, which of the three selected estimators gives reliable point estimates and calibrated uncertainty intervals, and under what conditions should an apparent scaling or multifractal signal be rejected as artifact-sensitive?

## Testable hypotheses
H1: Nominal uncertainty intervals based on dependence-aware resampling achieve closer-to-nominal empirical coverage than iid bootstrap or asymptotic regression intervals.

H2: Filtering and downsampling primarily bias spectral and variogram estimates by removing or shifting the usable scale range; MFDFA is also affected, especially near the smallest scales and for negative q.

H3: Random missingness is less damaging than clustered gaps at the same missing fraction, while naive interpolation can create artificially smooth scaling.

H4: Concatenated regimes, trends, and facies-like mean/variance changes can create apparent multifractality even when each component is monofractal; shuffled and phase-randomized controls detect some, but not all, of these failures.

H5: A pre-registered validity rule based on scale-range adequacy, fit diagnostics, perturbation sensitivity, and surrogate comparisons is more reliable than reporting a point estimate alone.

## Estimands and estimator definitions
Analyze detrended, depth-ordered windows within geologically comparable intervals. Preserve the original sampling interval and record it explicitly. Do not pool across formation boundaries without a separate nonstationarity analysis.

For the spectral estimator, estimate the log-log slope of the power spectral density only over a pre-specified candidate frequency band that excludes the low-frequency trend region and the high-frequency tool/noise roll-off. Convert the slope to H using the appropriate fGn or fBm relationship, selected from diagnostics rather than assumed universally. Report the slope, H, fitted scale range, slope standard error, and goodness-of-fit.

For the variogram estimator, calculate the empirical semivariogram over depth lags, identify a candidate power-law range, fit log γ(h) = a + b log h using a robust regression, and compute D = 2 - b/2. Report the lag range, number of usable pairs, fit diagnostics, and whether the estimated dimension lies in a physically interpretable range.

For MFDFA, integrate the demeaned window, divide it into forward and reverse segments, detrend each segment with a fixed low-order polynomial, and estimate F_q(s) over common scales. Use q = {-2,-1,0,1,2} for the main experiment; treat negative q as secondary because sparse support and small amplitudes make it unstable. Estimate h(q), then use the primary scalar Δh = h(-2) - h(2), with h(q) curves and the Legendre-derived spectrum shown only when scaling diagnostics pass. A multifractal claim requires more than a broad spectrum: it must survive the surrogate/null tests and show adequate linear scaling over a defensible common range.

Use identical windows, boundary handling, scale ranges where possible, and preprocessing labels across estimators. The primary analysis should use fixed scale ranges selected before inspecting test outcomes. A secondary sensitivity analysis may compare fixed ranges with training-data-only automated range selection.

## Synthetic ground truth
Construct Monte Carlo datasets with known generating parameters and at least 500 independent realizations per major condition if computationally feasible; use 100-200 during development and increase for final coverage estimates.

Ground-truth families:

1. Monofractal fGn with H in {0.3, 0.5, 0.7} and several finite lengths representative of logs, for example N in {256, 512, 1024, 2048}.
2. Monofractal fBm or integrated fGn for testing the effect of applying an estimator to the wrong process class.
3. A binomial multiplicative cascade or multifractal random walk with known multifractal strength, converted into a one-dimensional signal suitable for MFDFA. The primary truth should be the generating h(q) curve or Δh, not an unqualified claim that every estimator estimates the same quantity.
4. A null with independent or short-memory noise to measure false scaling detections.
5. A piecewise monofractal signal with two or three regimes, different H values, means, variances, or trends. This is the ground truth for false multifractality caused by nonstationarity and facies mixing.

For every realization retain the clean signal and apply perturbations to that same realization, so recovery error is paired across conditions.

Perturbation matrix:

- Additive white and correlated measurement noise at several signal-to-noise ratios.
- Low-pass convolution with simple Gaussian/boxcar kernels and optional asymmetric kernels as proxies for tool response; downsample only after anti-alias filtering.
- Random point missingness at 5%, 10%, and 20%.
- Clustered gaps with controlled gap lengths and total missing fraction.
- Two missing-data treatments: listwise/available-pair estimation where supported, and interpolation performed strictly within the observed window. Interpolation is a baseline, not ground truth.
- Linear and polynomial trends.
- Abrupt level/variance changes and concatenated regimes.
- Optional irregular depth spacing, resampled to a documented regular grid only in a sensitivity experiment.

The full factorial design is too large for a modest MTP. Use a balanced core design: clean signal, noise, filtering/downsampling, random gaps, clustered gaps, and nonstationarity separately, followed by a small two-factor interaction set: filtering × gaps, and nonstationarity × filtering.

## Uncertainty procedures
For each observed window produce a point estimate and a nominal 80% and 95% interval.

Primary method: moving-block bootstrap, with block length selected from a small pre-registered set or estimated from the training realization, preserving short-range dependence. Recompute the entire estimator, including scaling-fit selection if that procedure is part of the method, within every bootstrap replicate. Use a stationary bootstrap as a sensitivity check.

For MFDFA, also use surrogate ensembles to quantify null variability and test whether Δh exceeds what is expected from a monofractal process with comparable distribution and dependence. Use:

- Shuffled surrogates to destroy temporal/depth dependence while preserving the marginal distribution.
- Phase-randomized or IAAFT surrogates to preserve approximately linear autocorrelation and the marginal distribution while removing nonlinear structure.
- For piecewise nonstationary signals, segmented or regime-preserving surrogates where feasible; do not treat stationary IAAFT surrogates as universally valid for nonstationary logs.

Secondary baselines are iid bootstrap, asymptotic regression intervals from the log-log fit, and model-based intervals using the known synthetic generating family. The model-based interval is an oracle/reference condition, not an available real-log procedure.

For gaps, bootstrap the observed data without allowing resampling to invent information across a missing cluster. Report the gap mask and distinguish uncertainty due to estimator variability from uncertainty due to unobserved samples. If a method cannot natively handle gaps, use a clearly labeled imputation pipeline and compare multiple imputations rather than hiding imputation uncertainty.

## Evaluation metrics
For synthetic data, compare estimates against the known generating truth:

- Bias and signed bias.
- MAE and RMSE.
- Median absolute error and Monte Carlo standard deviation.
- Empirical coverage of nominal 80% and 95% intervals.
- Mean and median interval width.
- Interval score or weighted interval score, combining sharpness and missed coverage.
- Coverage error, defined as empirical coverage minus nominal coverage.
- Calibration curves across nominal levels from 50% to 99%.
- Quantile or rank-uniformity diagnostics for bootstrap intervals.
- Failure rate: proportion of windows with insufficient usable scales, nonphysical estimates, nonconvergent fits, or invalid MFDFA scaling.
- Scale-range recovery and crossover-detection accuracy where the perturbation has a known cutoff.
- For multifractality, false-positive rate on monofractal and shuffled/null data, detection power on multifractal data, Δh bias, and agreement between the observed statistic and surrogate distribution.

For real logs, do not use coverage claims unless independent truth exists. Report within-well and held-out-well stability, interval width, estimator disagreement, sensitivity to scale range and preprocessing, and the fraction of windows passing the validity rule. If core or interpreted facies markers are available, use them only as secondary external comparisons; do not convert association into causal or universal geological claims.

## Baselines
Use the following baselines:

1. Point estimates with no uncertainty interval.
2. Asymptotic ordinary-least-squares intervals from the log-log scaling regression.
3. IID bootstrap intervals, expected to fail under dependence.
4. Moving-block bootstrap intervals, the primary proposed protocol.
5. Stationary-bootstrap sensitivity intervals.
6. Shuffled and phase-randomized/IAAFT surrogate nulls for multifractality.
7. Simple conventional roughness controls: standard deviation of first differences, lag-1 autocorrelation, and RMS increment versus lag. These are not competing fractal estimators; they show whether the selected attributes add information beyond basic variability summaries.

If an external labeled task is available, compare fractal attributes with conventional log-window statistics and a simple logistic regression or random forest. This classification is optional and must remain secondary to calibration.

## Ablation plan
Run ablations in this order:

1. Remove dependence preservation: iid bootstrap versus block bootstrap.
2. Remove filtering-aware scale exclusion.
3. Replace clustered gaps with random gaps and compare equal missing fractions.
4. Compare no interpolation, linear interpolation, and multiple imputation where implementation permits.
5. Remove trend/detrending safeguards.
6. Replace regime-preserving surrogates with stationary IAAFT surrogates.
7. Vary window length and minimum number of scales.
8. Vary MFDFA q-range, polynomial detrending order, and wavelet/filter choices only as secondary sensitivity tests.
9. Compare each estimator alone with a simple consensus rule that flags a window only when at least two estimators pass their scaling checks and their intervals overlap substantially.

The primary result should be the calibration/failure table, not a cherry-picked best estimator.

## Real-log demonstration
Use one accessible public multiwell well-log dataset with depth-indexed channels and documented sampling, preferably including gamma ray plus one or more density, neutron, sonic, or resistivity channels. A public facies benchmark such as FORCE-2020/Hugoton-Panoma may be considered if licensing, channel availability, and well identifiers are verified before analysis. Otherwise use any accessible open LAS collection and state clearly that it is a methodological demonstration.

Recommended real-log protocol:

- Select one primary channel, preferably GR because it has direct precedent and commonly available depth coverage; use one secondary channel only if quality and sampling are adequate.
- Remove duplicated depths, document missing values, align channels, and retain formation/facies markers when available.
- Analyze windows within each well and avoid windows crossing known boundaries in the primary analysis.
- Hold out complete wells for the external demonstration; never split rows from the same well across train and test for any optional classification.
- Apply synthetic degradation to a high-quality observed segment as a controlled real-log stress test, while explicitly calling the original segment a proxy reference rather than perfect ground truth.
- Show point estimates, uncertainty bands, valid-scale flags, estimator disagreement, and surrogate results as depth-indexed tracks.
- Include at least one example where the protocol rejects an apparent scaling result because of a boundary, filtering cutoff, inadequate length, or poor calibration. Negative findings are scientifically useful.

## Decision and reporting rules
Pre-register or freeze before final evaluation:

- Estimator formulas and fGn/fBm conversion convention.
- Window lengths and overlap.
- Candidate and accepted scale ranges.
- q-grid and MFDFA detrending order.
- Bootstrap type, replicate count, block-length rule, and interval construction.
- Surrogate count and decision threshold.
- Minimum number of usable scales and valid-pair counts.
- Handling of gaps and boundary windows.

A result is called reliable only if it has adequate scale support, no obvious boundary or tool-roll-off contamination, a stable estimate under the primary perturbation sensitivity checks, and uncertainty intervals with acceptable synthetic coverage. Define acceptable coverage before results are seen; for example, treat coverage within a pre-specified tolerance band around nominal as calibrated, with the exact tolerance justified by the Monte Carlo sample size. Do not invent a universal threshold for H, D, or Δh.

## Analysis outputs
Minimum tables and figures:

1. Synthetic bias/RMSE table by estimator and perturbation.
2. Coverage and interval-width table for 80% and 95% intervals.
3. Calibration curves and interval-score comparison.
4. Heatmaps of estimator error versus window length, filtering strength, and missingness.
5. False-positive/power curves for multifractality tests.
6. Example clean, filtered, gapped, and nonstationary synthetic signals with fitted scaling ranges.
7. Real-log depth tracks of estimates, intervals, validity flags, and surrogate p-values or effect sizes.
8. A failure-mode catalogue linking observed artifacts to estimator behavior.

## Feasible implementation for a modest MTP
A realistic core project is:

- Three estimators: spectral slope/H, variogram/D, and MFDFA/Δh.
- Four synthetic families: fGn, fBm, binomial-cascade or multifractal-random-walk, and piecewise monofractal null.
- Six core conditions: clean, noise, filtering/downsampling, random gaps, clustered gaps, and nonstationarity.
- Moving-block bootstrap plus iid-bootstrap baseline and two surrogate types.
- One public multiwell log dataset, one primary channel, and one held-out-well demonstration.
- A reproducible Python implementation, configuration file, unit tests against known synthetic cases, and fixed random seeds.

Defer wavelet leaders, tool-specific deconvolution, learned models, multi-property reservoir prediction, permeability/production claims, extensive cross-field transfer, and a full multifractal spectrum as primary outcomes. These are suitable future work but would make the MTP too broad.

A practical schedule is: weeks 1-2 literature finalization and estimator tests; weeks 3-5 clean synthetic Monte Carlo; weeks 6-8 bootstrap/surrogate implementation and calibration; weeks 9-10 perturbation experiments; weeks 11-12 real-log processing; weeks 13-14 figures, failure analysis, and thesis writing. Reduce the number of perturbation levels before reducing the number of independent synthetic replications.

## Risks and mitigations
Risk: the broad uncertainty contribution is not sufficiently novel. Mitigation: claim a calibrated, well-log-specific perturbation benchmark and transparent decision protocol, not generic bootstrap or surrogate testing; document the literature boundary carefully.

Risk: no public dataset has adequate metadata or long clean intervals. Mitigation: use LAS files with verified sampling and treat the real section as demonstration; make synthetic calibration the primary evidence.

Risk: estimator formulas disagree because they target different processes or measures. Mitigation: define separate estimands, test fGn versus fBm explicitly, and avoid forced consensus or averaging of H and D.

Risk: MFDFA gives spurious multifractality under finite length, trends, or gaps. Mitigation: restrict q, require scale-linearity diagnostics, use shuffled/phase-randomized and nonstationary controls, and report false positives.

Risk: bootstrap intervals are overconfident under long-range dependence. Mitigation: compare block lengths and stationary bootstrap, report sensitivity, and label calibration failures rather than tuning intervals until they look correct.

Risk: clustered gaps make some windows unusable. Mitigation: report a missingness-dependent failure rate and use a fallback analysis on complete windows; never silently fill large gaps.

Risk: synthetic processes are too idealized. Mitigation: include heavy-tailed noise, correlated noise, regime changes, and convolutional filtering; state that synthetic truth validates estimator behavior, not geological truth.

Risk: optional facies classification becomes a distracting weak claim. Mitigation: keep it secondary and omit it entirely if there is no independent label or enough wells for leakage-safe validation.

## Fallback plan
If MFDFA cannot be made stable and calibrated within the time budget, make the thesis a two-estimator monofractal study using spectral H and variogram D, retain the same perturbation matrix and uncertainty-calibration objectives, and present MFDFA only as an exploratory appendix. If real-log metadata or a held-out well is unavailable, report a fully synthetic calibration study plus a single carefully documented illustrative LAS interval without claiming external validation. If clustered-missingness experiments are computationally excessive, retain one random-gap and one clustered-gap level. If coverage is poor for every method, make the principal result a quantified failure analysis and recommendations for when fractal attributes should not be reported.

## Expected defensible conclusion
The strongest feasible conclusion is conditional: dependence-aware, artifact-aware intervals can be evaluated and may improve reliability over naive intervals, but calibration depends on estimator, window length, scale range, filtering, missingness, and stationarity. The study should identify regimes in which each estimator is trustworthy or fails, rather than declare one universally superior fractal or multifractal attribute.

## Cross-well generalization

Title: Cross-Well Generalization of Fractal Reservoir Features: A Leakage-Controlled Benchmark Against Conventional Well-Log Statistics.

1. Research question and scope
Primary research question: When predicting a geological interval class from well logs, do fractal and multiscale reservoir features provide transferable information on a previously unseen well beyond conventional log values and local statistical descriptors?

The target is cross-well transferability, not invention of a new fractal estimator and not a claim of a universal classifier. The study should determine whether fractal features are consistently useful, useful only for particular formations/tools, redundant with conventional features, or unstable under well-to-well distribution shift.

Secondary questions:
- Do fractal features improve performance over conventional features when the test well is geographically or statistically different from training wells?
- Which feature families transfer best: monofractal persistence, spectral scaling, variogram scaling, wavelet-scale energy, or their combinations?
- Are apparent gains caused by geological information, depth trends, tool identity, or leakage from preprocessing?
- How much performance degrades from random row-wise validation to genuinely blind-well validation?

2. Hypotheses
H1, transferability: A fractal-feature model will perform above a majority-class and conventional-simple baseline on held-out wells, but performance will vary by well and formation.
H2, incremental value: Fractal features will provide statistically significant incremental predictive value over conventional log statistics for at least some held-out wells, but the gain will not be universal.
H3, conditional generalization: Fractal features based on local multiscale structure will transfer better than raw global Hurst estimates when windows are restricted to geologically comparable intervals and preprocessing is performed within folds.
H4, redundancy/null result: After adding local means, variances, gradients, quantiles, and wavelet energies, the incremental value of fractal features may become small; a null result is scientifically meaningful evidence that fractal descriptors are descriptive rather than independently predictive.
H5, shift sensitivity: Performance and feature distributions will vary across wells because of formation composition, sampling interval, tool response, depth alignment, and class prevalence. Therefore no universal threshold for Hurst exponent, fractal dimension, or any feature will be claimed.
H6, leakage sensitivity: Random row-wise splitting will produce optimistically biased estimates relative to leave-one-well-out evaluation, especially for overlapping depth windows and spatially correlated logs.

3. Data and labels
Preferred data: a public multiwell dataset containing several wells with common log channels, consistent depth sampling or a documented resampling procedure, and independent interval/facies labels where available. Candidate channels are GR/CGR, RHOB, NPHI, DT/sonic, resistivity, SP, caliper, and derived porosity; the final channel list must be restricted to channels available in every evaluated well or handled by a predeclared missing-channel protocol.

Preferred labels, in descending order of independence:
1. Core- or expert-interpreted facies/lithofacies labels tied to depth.
2. Formation or stratigraphic-zone labels independently interpreted from markers and geological records.
3. Reservoir-quality classes supported by core porosity/permeability or documented petrophysical interpretation.
4. Hydrocarbon/non-hydrocarbon labels only if independently established by fluid, pressure, production, or validated formation-test evidence.

Quick-look labels derived from the same logs used as predictors must not be presented as independent geological truth. If used, they should be explicitly called operational or weak labels and analyzed separately.

Required preprocessing: retain well ID, formation/zone ID, measured depth, sampling interval, channel provenance, missingness, and label confidence. Remove duplicated depths, flag gaps, preserve original values, and document all exclusions. Align intervals using geological markers only when those markers are available without using the held-out labels.

Label-free fallback: If reliable labels cannot be obtained, make the primary study an unsupervised or self-supervised transferability benchmark. Within each training fold, learn clusters or a low-dimensional representation from conventional or fractal features; evaluate on the held-out well using cluster stability, nearest-neighbor retrieval of analogous intervals, rank correlation of multiscale heterogeneity profiles, distributional alignment, and masked-log reconstruction. Use synthetic signals with known persistence as a calibration task. Do not call the result facies classification or geological validation. A weaker fallback is to use formation/zone markers as structural evaluation targets while treating them as proxy labels.

4. Unit of prediction and leakage-safe design
Use fixed-depth windows centered at each valid sample, with one feature vector per window. Window lengths should be selected before final testing from a small predeclared grid, for example short, medium, and long windows corresponding to tool-scale, bed-scale, and formation-scale structure. Overlapping windows are allowed only within a fold; all windows from a well must remain in the same outer fold.

Primary evaluation: leave-one-well-out cross-validation (LOWO). For each outer fold, hold out one complete well and train on all remaining eligible wells. If multiple fields or formations exist, add grouped outer tests that hold out an entire field or formation where sample size permits.

Nested inner validation: within the training wells only, use grouped folds by well for hyperparameter selection, preprocessing selection, feature selection, and model calibration. Never use held-out-well samples to select channels, wavelets, scales, window lengths, thresholds, normalization rules, imputation values, or features.

Fold-safe operations:
- Fit imputation, scaling, transformations, and class weights on training wells only.
- Fit feature selection and dimensionality reduction inside the inner grouped folds.
- Estimate fractal scaling ranges using training data only when the range is learned rather than fixed a priori.
- Do not normalize each full well before splitting if the normalization uses statistics from the test well. A permitted test-time option is explicitly defined unsupervised per-well normalization, reported separately and applied without labels.
- Remove boundary windows that cross excluded gaps or geological discontinuities, or include a boundary-crossing indicator and test it in an ablation.
- Apply a purge gap around train/test depth boundaries only for within-well sensitivity checks; the primary LOWO split already separates wells.

Report both LOWO results and a clearly labeled random row-wise split only as an optimistic leakage-demonstration control, never as the main result.

5. Feature sets
A. Raw-log baseline: standardized raw samples or compact windows from each common channel. Use a simple linear or tree model so this baseline does not unfairly benefit from excessive capacity.

B. Conventional-statistics baseline: per-channel mean, median, standard deviation, interquartile range, minimum/maximum, selected quantiles, skewness, kurtosis, first differences, absolute-gradient statistics, lag-1 autocorrelation, local trend slope, residual variance after linear detrending, and cross-channel correlations. Include depth/window metadata only if scientifically justified.

C. Conventional multiscale baseline: moving averages, finite-difference roughness, autocorrelation at fixed lags, classical variogram values and ranges, and discrete wavelet detail energies without fractal slope interpretation.

D. Monofractal/fractal features:
- Hurst exponent estimated by at least two predeclared estimators, such as rescaled range and detrended fluctuation or spectral slope.
- Spectral exponent beta over a defensible finite scaling range, with the fitted range, R-squared, number of scales, and residual error recorded.
- Variogram slope and derived dimension over stated lags.
- Relative dispersion or scale-dependent fluctuation slopes where stable.
- Local wavelet variance/energy slope and wavelet standard-deviation exponent.
- Box-counting dimension only if the one-dimensional implementation and valid scale range are clearly justified; otherwise treat it as an optional sensitivity feature, not a core method.

Each fractal feature must include quality-control metadata: valid-scale count, regression fit quality, slope uncertainty, edge-handling flag, missing-data fraction, and whether the window passed stationarity or surrogate checks. Invalid estimates become missing values with fold-safe imputation rather than silently being assigned a numerical default.

E. Optional limited multifractal extension: use only if the dataset supports sufficiently long stationary windows. Predefine one measure, such as absolute increments or a documented positive transformed property, a narrow q range, and a surrogate/shuffle control. Candidate features are spectrum width, asymmetry, selected tau(q) slopes, and multifractal residual/error. This is a secondary extension, not the core MTP claim, because the local notes identify no canonical well-log multifractal measure and warn about spurious multifractality.

F. Combined feature set: conventional plus fractal features. Compare incremental value, not only absolute accuracy.

6. Models and baselines
Minimum predictive models, all tuned inside grouped inner folds:
- Majority-class predictor.
- Stratified training-well class-prior predictor.
- Logistic regression or multinomial logistic regression with regularization.
- Linear discriminant analysis or quadratic discriminant analysis where assumptions are reasonable.
- Random forest or extremely randomized trees.
- Gradient-boosted trees with constrained depth.
- Optional support-vector machine with a linear kernel and one nonlinear kernel.

Keep model capacity matched across feature sets. A fractal feature set should not be compared with a heavily tuned deep model while conventional features receive a weak model. A neural model is optional only if the number of wells is sufficient; it should not replace interpretable tabular baselines.

Primary comparisons:
1. conventional statistics versus fractal-only;
2. conventional statistics versus conventional-plus-fractal;
3. raw logs versus compact features;
4. fixed-scale features versus multiscale features;
5. one estimator family versus multiple-estimator consensus.

7. Metrics
For classification, report per held-out well and pooled out-of-fold results:
- Macro-F1 as the primary metric for class imbalance.
- Balanced accuracy.
- Per-class precision, recall, and F1.
- Matthews correlation coefficient when binary or multiclass-compatible.
- Accuracy only as a secondary descriptive metric.
- One-vs-rest AUROC and macro-AUPRC when probabilities and class support permit.
- Log loss and Brier score for probabilistic calibration.
- Confusion matrices and calibration curves.

For label-free transferability, report cluster agreement/stability, retrieval precision at k if proxy matches exist, reconstruction error, rank correlation across analogous windows, and distribution-shift measures such as Wasserstein distance or energy distance. These are not substitutes for geological validation.

Report macro-averages across wells so large wells do not dominate, pooled out-of-fold metrics, median and interquartile range across wells, and the worst-well result. Include confidence intervals from a well-level bootstrap, not an iid row bootstrap that ignores depth correlation.

8. Statistical comparison
The primary unit for paired comparison is the held-out well. For each outer fold, calculate the difference between two feature sets using the same test samples and model protocol.

Use a paired permutation test or Wilcoxon signed-rank test across wells for feature-set comparisons when the number of wells is adequate; otherwise report effect sizes and uncertainty without overstating significance. Use a hierarchical bootstrap that resamples wells first and windows second only within resampled wells. Correct for multiple pairwise comparisons using Holm correction.

Report mean and median paired improvement, 95% confidence interval, standardized effect size, number of wells showing improvement, and the fraction of folds in which the improvement exceeds a predeclared practical threshold, such as 0.03 macro-F1. Treat statistical significance without practical improvement as insufficient evidence.

For per-well domain shift, compare feature distributions between training and held-out wells and relate shift measures to performance degradation using rank correlations or a simple prespecified regression. This is associative, not causal.

9. Ablation plan
A1: conventional statistics only versus fractal only versus combined.
A2: each fractal family removed in turn: Hurst/R-S, spectral, variogram, wavelet, and optional multifractal.
A3: single-channel versus all common channels.
A4: raw values versus detrended values versus increments; transformations such as log-resistivity must be evaluated only where physically justified.
A5: short, medium, and long windows.
A6: fixed versus training-fold-selected scale ranges.
A7: one wavelet family versus a small predeclared alternative set; report sensitivity rather than selecting the best wavelet on the test well.
A8: with and without feature-quality metadata.
A9: training-well normalization only versus permitted unsupervised test-well normalization.
A10: random row-wise split versus grouped well split to quantify optimistic bias.
A11: original logs versus shuffled or phase-randomized surrogates to test whether predictive performance depends on ordering rather than marginal distributions.
A12: remove boundary-crossing windows and compare with all windows.
A13: real labels versus weak/quick-look labels if both exist.
A14: optional synthetic calibration with known fGn/fBm persistence, trends, regime changes, correlated noise, gaps, and tool-like smoothing/downsampling. Measure estimator bias, rank recovery, and feature stability before using real data.

10. Risks and mitigations
Risk: too few wells. Mitigation: use LOWO as exploratory repeated evaluation, report fold-level uncertainty, avoid claims of population-wide generalization, and seek a second dataset or field-level holdout.
Risk: inconsistent formations or channel availability. Mitigation: restrict the primary analysis to common channels and matched geological zones; stratify or report results by formation.
Risk: labels are weak or derived from predictors. Mitigation: prioritize core/expert labels, separate proxy-label experiments, and state the validation target precisely.
Risk: fractal estimates are unstable for short windows, trends, mixed facies, and tool-filtered data. Mitigation: require minimum window length, detrend only by a prespecified rule, test stationarity, report valid scale ranges and estimator uncertainty, and reject invalid estimates.
Risk: spurious multifractality. Mitigation: keep multifractality secondary, use shuffled/phase-randomized or nonstationarity-preserving surrogates, and do not interpret broad spectra without null rejection and scale-range diagnostics.
Risk: overlapping windows inflate sample counts. Mitigation: split by well, report well-level uncertainty, and avoid iid confidence intervals.
Risk: domain shift causes poor performance. Mitigation: make failure analysis a result, report per-well metrics and feature-distribution shifts, and avoid universal thresholds.
Risk: feature engineering becomes a large multiple-testing search. Mitigation: preregister core features, use nested selection, cap hyperparameter grids, and preserve a final untouched well or dataset if available.
Risk: apparent fractal benefit is merely a smoother or wavelet representation. Mitigation: include conventional multiscale and wavelet-energy baselines and compare matched feature dimensions.
Risk: depth markers or formation labels leak target information. Mitigation: use only markers available independently of the target and perform all label-dependent segmentation inside training folds.

11. Expected outputs
- Data audit and a reproducible preprocessing report.
- A table of per-well and pooled performance for every feature/model family.
- A leakage audit documenting every fold-dependent operation.
- Feature stability and cross-well distribution-shift analysis.
- Synthetic calibration plots for estimator bias and scale-range recovery, if feasible.
- Ablation and statistical comparison tables.
- Error analysis identifying wells, formations, channels, and classes where fractal features help or fail.
- Reproducible code, configuration files, fixed random seeds, environment specification, and machine-readable results.

12. Realistic contribution statement
Application novelty: The study evaluates an underexplored application question: whether established fractal and multiscale well-log descriptors transfer to unseen wells for reservoir or facies-related prediction, rather than merely separating intervals within one well or correlating boundaries within one field. The application contribution is conditional and empirical: it may show that fractal features improve, fail to improve, or improve only under specific geological and acquisition conditions.

Methodological novelty: Leave-one-well-out validation and leakage prevention are established practices and must not be claimed as new algorithms. The defensible methodological contribution is a reproducible, fold-safe benchmark protocol that compares conventional and fractal feature families under cross-well distribution shift, records estimator validity and scaling-range diagnostics, and quantifies incremental value with well-level uncertainty and ablations. This is methodological rigor and an integrated evaluation design; it becomes stronger only if the study demonstrates a new, validated transferability diagnostic or reveals previously undocumented failure regimes.

Conservative final claim: This work provides a leakage-controlled benchmark of when fractal reservoir features transfer across wells and whether they add predictive information beyond conventional log statistics. It does not establish a universal classifier, universal fractal threshold, universal geological interpretation of Hurst or multifractal parameters, or superiority of fractal features in every reservoir.

13. Minimum viable MTP sequence
Phase 1: select and audit one multiwell labeled dataset; freeze the target definition and common channels.
Phase 2: implement grouped data objects, fold-safe preprocessing, and leakage tests.
Phase 3: implement conventional, raw-log, and core monofractal feature extractors with synthetic calibration.
Phase 4: run LOWO baselines and primary comparisons.
Phase 5: run statistical tests, ablations, and per-well failure analysis.
Phase 6: add the label-free or optional multifractal extension only if labels, window lengths, and compute remain adequate.
Phase 7: package code, configs, fold manifests, figures, tables, and a limitations-focused thesis discussion.

Go/no-go criteria: proceed to the final thesis analysis only if at least three eligible wells remain after quality control, every outer test well has the primary channels and labels, the fractal estimators produce valid features in a documented fraction of windows, and the split audit confirms that no test-well information entered preprocessing, tuning, or feature selection.

## Robust multifractal measure selection

# MTP-ready plan: Robust Multifractal Measure Selection for Reservoir Characterization

## 1. Scope and research question

**Research question:** For a fixed well-log channel and a fixed, auditable preprocessing protocol, which of two explicitly defined positive measures produces multifractal attributes that are most reproducible within wells, transferable across held-out wells, and resistant to finite-sample, trend, sampling, and tool-resolution artifacts?

The study is deliberately limited to **two measures**, one primary estimator, and one cross-check. It is not an unrestricted comparison of multifractal algorithms.

Primary channel: gamma ray (GR), because it is commonly available, has direct lithological relevance, and has fewer fluid/borehole complications than resistivity. RHOB or NPHI may be used only as a pre-specified secondary replication channel if the dataset contains them consistently across wells.

Primary estimator: **discrete wavelet leaders (WL)**. Cross-check: **partition-function scaling** computed from the same two measures. The main contribution is measure selection and reproducibility, not invention of either estimator.

## 2. Explicit measures

For each uniformly resampled, depth-indexed window x_1,...,x_N, use robust within-window normalization only after defining the window independently of labels. Let Q_1 and Q_99 be the 1st and 99th percentiles and let s=Q_99-Q_1. Winsorize x to [Q_1,Q_99] and define z_i=(x_i-m)/s, where m is the window median.

### M1: positive level measure

Define a nonnegative level signal

u_i^(L) = max(z_i - min(z) + epsilon, epsilon),

where epsilon=10^(-6) times the window median of the positive values. Normalize it to a probability measure:

mu_i^(L) = u_i^(L) / sum_{r=1}^N u_r^(L).

This is a transparent positive-mass representation of the log level. Its limitation is that the additive positivity rule can affect the spectrum; therefore the offset is fixed before analysis and its sensitivity is reported as an ablation, not tuned per well.

### M2: absolute-increment measure

Define first increments

d_i = z_{i+1} - z_i,

and the positive increment measure

u_i^(Delta) = |d_i| + epsilon_Delta,

mu_i^(Delta) = u_i^(Delta) / sum_{r=1}^{N-1} u_r^(Delta),

with epsilon_Delta=10^(-6) times the median nonzero absolute increment. This measure targets scale-dependent roughness and is less directly affected by absolute log level, but is more sensitive to noise, sampling interval, and tool filtering.

No third measure is introduced in the primary experiment. Raw signed values, squared increments, transformed resistivity, wavelet coefficient magnitudes, and other alternatives are excluded from the main comparison to prevent scope expansion.

## 3. Primary estimator: wavelet leaders

Use an orthogonal discrete wavelet transform with a pre-registered compact-support wavelet, preferably Daubechies-2 or Haar. Haar is the fallback because it is transparent and widely available. The mother wavelet, boundary rule, and number of vanishing moments must be fixed before testing held-out wells.

For dyadic scale j and interval k, let c_{j,k} be the detail coefficients. Define the leader

L_{j,k} = sup{|c_{j',k'}| : j' >= j and I_{j',k'} is contained in the 3I_{j,k} neighborhood}.

For q in Q={-2,-1,0,1,2,3,4}, compute

S_L(q,j) = 2^{-j} sum_k L_{j,k}^q,

and fit

log_2 S_L(q,j) = a_q + zeta_L(q) j + error.

For q=0, use the number of valid leaders or the limiting convention rather than numerical 0^0. Estimate the singularity spectrum by the Legendre transform

alpha(q) = d zeta_L(q)/dq,

f_L(alpha(q)) = q alpha(q) - zeta_L(q) + 1.

The +1 term corresponds to a one-dimensional depth signal. Derivatives should be estimated by a fixed centered finite difference or a quadratic local fit, with the same rule in every fold.

Use only scales satisfying all of the following: at least 16 valid coefficients/leaders per scale, no obvious boundary-dominated region, wavelength above the empirically determined tool-resolution cutoff, and acceptable log-scale linearity. The admissible scale interval is selected using training wells only and then frozen for the held-out well.

Primary summary attributes per window and measure:

1. alpha_0: alpha at the maximum of f(alpha), representing the dominant regularity;
2. Delta-alpha = alpha_max - alpha_min over the pre-specified q range;
3. c_2: quadratic curvature of zeta(q), estimated from a fixed quadratic fit; c_2=0 is the monofractal limit.

Do not interpret a broad spectrum as genuine multifractality unless it exceeds surrogate-derived null variability and survives the cross-check.

## 4. Cross-check: partition-function scaling

Using exactly the same positive measures, divide each window into non-overlapping boxes of length epsilon and define

Z_mu(q,epsilon) = sum_b mu_b(epsilon)^q,

where mu_b(epsilon) is the sum of the measure within box b. Fit

log Z_mu(q,epsilon) = tau_mu(q) log(epsilon) + b_q.

Derive

alpha_mu(q) = d tau_mu(q)/dq,

f_mu(alpha_mu(q)) = q alpha_mu(q) - tau_mu(q).

The partition function is a validation estimator, not a second optimization track. Use the same q values, the same admissible physical wavelength range, and the same scale-linearity acceptance rule as for WL. The principal cross-checks are the Spearman correlation and absolute difference between WL and partition-function estimates of alpha_0, Delta-alpha, and c_2. Large disagreement is reported as estimator instability rather than resolved by choosing the more favorable result.

## 5. Data and preprocessing

Preferred data: a public multi-well dataset with at least five wells, common GR curves, recorded depth sampling, and independently available facies, core, or interpreted reservoir-zone labels. The preferred minimum is four wells for development and one completely held-out well per outer fold; six or more wells is preferable.

Required preprocessing:

- retain raw curves and metadata;
- convert depth to a common uniform increment using documented interpolation only where gaps are short;
- flag gaps longer than a fixed threshold and exclude windows crossing them;
- remove duplicate depths and physically impossible values using a documented QC table;
- do not smooth in the primary analysis;
- use fixed-length windows, selected in physical depth rather than sample count;
- avoid windows crossing formation boundaries in the main analysis, with boundary-crossing windows reserved for a boundary ablation;
- perform all scaling, offset estimation, scale-range selection, and feature selection inside the training wells only.

A reasonable initial window is 256 samples or an equivalent physical interval, subject to the dataset's sampling rate. Test only two pre-registered alternatives, 128 and 512 samples, as a stability analysis. The smallest analyzed wavelength must exceed both approximately four samples and the measured tool-resolution cutoff.

Fallback data plan: if no suitable public multi-well labeled dataset is accessible, use (i) the best available public multi-well logs without labels for reproducibility/stability analysis, and (ii) synthetic depth signals with known parameters: fractional Brownian motion/fractional Gaussian noise with H in {0.3,0.5,0.7}, binomial multiplicative cascades with known multifractal width, additive heavy-tailed noise, linear trends, concatenated regimes, gaps, downsampling, and moving-average tool kernels. Synthetic data cannot substitute for geological validation, so the thesis must state that the empirical transfer claim is then limited.

## 6. Cross-well validation and reservoir relevance

The outer evaluation is grouped by well: leave-one-well-out cross-validation or grouped folds with no depth windows from the held-out well entering training. All preprocessing decisions that can learn from data are nested within the training fold.

Primary validation target: reproducibility and transferability of the three multifractal attributes, not maximum classification accuracy. For each held-out well, report:

- within-well split-half and block-bootstrap stability;
- between-well distribution shift in each attribute;
- cross-well rank stability of windows or facies groups;
- if labels exist, macro-F1, balanced accuracy, AUROC where appropriate, and per-well performance for a simple regularized logistic model using only the three attributes;
- performance of a pre-specified threshold-free model and not a threshold chosen on the test well.

Reservoir characterization is secondary. Compare whether multifractal attributes improve prediction of facies or reservoir/non-reservoir intervals beyond conventional features, while allowing a negative result. If core porosity/permeability exists, evaluate held-out-well correlation or rank correlation, but do not imply causality from correlation.

## 7. Surrogate and null controls

For every real window, generate a fixed number of deterministic-seed surrogates, preferably 100 per condition:

1. random shuffle: destroys serial dependence while approximately retaining the marginal distribution;
2. Fourier phase-randomized surrogate: approximately preserves the power spectrum and marginal Gaussian structure, testing whether apparent multifractality is explained by linear correlations;
3. IAAFT surrogate: approximately preserves both the marginal distribution and spectrum;
4. block-shuffle surrogate: preserves short-range dependence but destroys long-range ordering;
5. segmented or facies-preserving shuffle when the window contains demonstrable nonstationarity, preventing a false null caused by concatenated regimes.

The multifractality claim is supported only if the observed Delta-alpha or c_2 is outside the appropriate surrogate distribution after multiplicity control, has acceptable scaling linearity, and is consistent between WL and the partition-function check. A spectrum that disappears under phase randomization is described as correlation-induced rather than automatically geological.

## 8. Reproducibility and stability metrics

Report the following for every measure, estimator, well, and scale condition:

- median and interquartile range of alpha_0, Delta-alpha, and c_2;
- robust coefficient of variation and median absolute deviation;
- split-half intraclass correlation coefficient and block-bootstrap 95% interval;
- Spearman rank correlation under window perturbation;
- absolute change under 10% window-length change, resampling, and moderate smoothing;
- scaling-fit R-squared, slope standard error, and number of accepted scales;
- WL-versus-partition-function Bland–Altman bias and limits of agreement;
- synthetic bias, RMSE, and empirical 95% interval coverage relative to known parameters;
- false-positive rate for multifractality on monofractal and surrogate controls;
- between-well variance divided by total variance as a transferability indicator.

Predefine a stability rule: a measure is considered robust only if it has acceptable scaling fits in at least 80% of eligible windows, median split-half ICC >=0.75, median perturbation change below 10% of the pooled attribute range, and surrogate false-positive rate <=5% after correction. These are decision criteria, not claims that the literature has established universal thresholds; sensitivity to these thresholds must be reported.

## 9. Baselines and ablations

Baselines:

1. conventional log statistics: mean, standard deviation, median, interquartile range, skewness, and local trend;
2. monofractal spectral slope/H estimate on the same windows;
3. variogram slope as an independent roughness baseline;
4. conventional-only classifier versus multifractal-only classifier versus combined classifier.

Ablations, limited to the following:

- M1 versus M2;
- WL versus partition function;
- raw level versus increment preprocessing;
- q range [-2,4] versus a restricted nonnegative range [0,4];
- Haar versus Daubechies-2 wavelet;
- window lengths 128, 256, and 512 samples;
- no smoothing versus one fixed moderate moving-average degradation;
- original sampling versus 2x downsampling with anti-alias filtering;
- windows wholly inside a facies/formation versus boundary-crossing windows;
- observed data versus each surrogate class.

No additional multifractal estimator, learned representation, or large feature grid is added unless a failure of the primary protocol requires it and the change is documented as a deviation.

## 10. Risks and mitigations

- **Positivity-induced multifractality:** report the exact offset rule, compare M1 with M2, and use surrogate controls.
- **Nonstationarity and facies concatenation:** segment by geological intervals, test boundary windows separately, and use nonstationarity-preserving surrogates.
- **Tool filtering and sampling artifacts:** estimate a lower-scale cutoff from metadata or controlled convolution/downsampling experiments; do not fit below it.
- **Finite sample and negative-q instability:** keep q limited to {-2,...,4}, report valid-scale counts, and repeat with q>=0.
- **Boundary effects in the wavelet transform:** exclude cone-of-influence/boundary-dominated coefficients and use a fixed extension rule.
- **Cross-well leakage:** split by well before all learned preprocessing and feature selection.
- **Weak or inconsistent labels:** treat facies labels as secondary validation and report label provenance; do not convert quick-look interpretation into ground truth.
- **Failure to find multifractality:** retain the negative result as a valid outcome; the study tests reliability, not the assumption that all logs are multifractal.

## 11. Expected outputs

1. A version-controlled preprocessing and analysis pipeline with configuration files, fixed random seeds, environment specification, and machine-readable per-window results.
2. A data/QC table documenting wells, channels, sampling, missingness, tool metadata, and excluded intervals.
3. Synthetic calibration figures showing bias, RMSE, coverage, and false positives.
4. WL and partition-function scaling plots with accepted scale ranges for both measures.
5. Cross-well stability tables and per-well transfer plots.
6. Surrogate null distributions and a decision table identifying robust, measure-induced, estimator-induced, and unresolved cases.
7. A final recommendation: select M1, select M2, or conclude that neither measure is sufficiently stable for the chosen channel and dataset.
8. A cautious reservoir-characterization result showing whether the selected attribute set adds value beyond conventional statistics.

## 12. Novelty positioning

Do not claim novelty for multifractal analysis, wavelet leaders, partition functions, surrogate testing, or cross-well validation individually; each has substantial precedent. The defensible claim is narrower and conditional: this MTP develops a reproducible, leakage-controlled benchmark for selecting between two explicitly defined positive measures of the same well-log signal, using wavelet leaders as the primary estimator, partition-function scaling as a cross-check, realistic surrogate/degradation controls, and held-out-well stability evaluation. The contribution is potentially novel if the exact integrated protocol is not found in citation chaining and if it reveals actionable differences in measure robustness or failure regimes. If both measures behave similarly or neither transfers across wells, that negative result remains publishable as evidence against unqualified multifractal reservoir interpretation. Any final novelty statement must be updated after direct citation chaining from the local precedents on generalized multifractal geological analysis, well-log MFDFA/WTMM, wavelet-fractal well-log studies, and apparent or spurious multifractality.
