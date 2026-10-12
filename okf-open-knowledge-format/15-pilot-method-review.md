---
type: Methodology Review
title: Independent method audit for the bounded GR stability pilot
description: Correct fBm/fGn conventions, fixed-depth-scale comparisons, missingness rules, and falsifiable pilot gates.
status: draft
tags: [MTP, pilot, GR, spectral-analysis, variogram, methodology]
sources:
  - resource: ./12-final-mtp-recommendation.md
  - resource: ./14-force2020-data-audit.md
  - resource: ./02-book-chapters-1-4.md
  - resource: ./05-estimation-methods.md
  - resource: ../Literature/RS and Power spectral.pdf
  - resource: ../Literature/Use of Spectral method for the estimation of the Fractal Dimension.pdf
  - resource: ../Literature/fractals-in-reservoir-engineering.pdf
---

# Independent review: bounded pilot, not the full study

**Recommendation: proceed only as an estimator-calibration and processed-GR sensitivity pilot.** Do not treat a usable LAS archive as evidence that fractal recovery works. First establish known-answer performance; then analyze a few predetermined contiguous GR windows and make a go/no-go decision. This document is an independent methodological specification, not an audit of executed pilot code or a claim that any acceptance gate has passed. No files in `pilot/` were edited.

The [existing recommendation](./12-final-mtp-recommendation.md) is broader than the approved pilot. For this pilot retain **spectral H and second-order variogram H**, fBm/fGn controls, mild smoothing and antialiased downsampling, and approximately three real GR windows from distinct wells where eligible. Exclude R/S, multifractal widths, classification, reservoir-property prediction, well reconstruction, and full moving-window/formation studies. Missingness is principally an ingestion/rejection test, not a reconstruction experiment. Real logs are the downloaded **cleaned/despiked FORCE product**, not raw acquisitions; injected smoothing is a known numerical perturbation, not measured tool response or actual tool ground truth.

All numerical gates below are **proposed engineering tolerances for this pilot**, not literature-established universal thresholds. Freeze them before scoring independent evaluation seeds or real windows; record deviations instead of silently tuning until they pass.

## 1. One unambiguous stochastic convention

Let depth be `z_i = z_0 + i Δ`, with Δ in metres, and let `0 < H < 1` denote the **same Hurst parameter** for a fractional Brownian motion and its fractional Gaussian-noise increments. Let σ² set the variance at unit depth. Define the zero-mean Gaussian process B_H by

\[
E[B_H(z)B_H(w)] = \frac{\sigma^2}{2}\bigl(|z|^{2H}+|w|^{2H}-|z-w|^{2H}\bigr),\qquad B_H(0)=0.
\]

Consequently `Var B_H(z) = σ² |z|^(2H)` depends on position: **fBm is not stationary**. It has stationary increments. Define discrete fGn as `G_i = B_H((i+1)Δ) − B_H(iΔ)`; it is stationary and Gaussian, with

\[
C_G(k)=\frac{\sigma^2\Delta^{2H}}{2}
\left(|k+1|^{2H}-2|k|^{2H}+|k-1|^{2H}\right).
\]

These definitions, not empirical formulas from one paper, determine the known answers. Differencing changes spectral exponent but **does not change the underlying fGn H parameter from H to H−1**. The latter notation in Li (2003) is a generalized roughness exponent, not the parameter used here.

### Spectral slope and units

Use positive spatial frequency `f` in **cycles/metre**, wavelength `λ=1/f`, and

\[
P(f)\propto f^{-\beta},\qquad m=\frac{d\log P}{d\log f}=-\beta.
\]

| Input and model | Exponent relation | Reported H from fitted slope m |
|---|---|---|
| fBm levels | β = 2H + 1, with 1 < β < 3 | H_spec = (−m−1)/2 |
| fGn samples | β = 2H − 1, with −1 < β < 1 | H_spec = (1−m)/2 |

fGn's relation is a **low-frequency asymptotic**, not an exact power law across the discrete Nyquist band. fBm does not possess an ordinary stationary finite-variance PSD; its level-spectrum relation is a generalized/finite-record scaling relation. A tapered finite-record fit therefore requires simulation calibration, especially for persistent fBm and endpoint leakage.

For the discrete difference filter the exact infinite-sequence/filter transfer is

\[
|1-e^{-2\pi i f\Delta}|^2=4\sin^2(\pi f\Delta)\geq0.
\]

It approaches `(2πfΔ)²` only for `fΔ ≪ 1`. Do not subtract two from a fitted exponent near Nyquist as an exact operation. Ordinary finite-record differences also change length/endpoints; do not claim an exact equality between independently tapered finite-record periodograms.

**Minimal specified implementation choice:** demean each spectral input, use a full-window Hann-tapered one-sided density periodogram, and state the normalization. For taper w_i and demeaned x_i, interior positive-frequency ordinates can be defined as `P(f_j)=2Δ |Σ w_i x_i exp(−2πij/N)|² / Σw_i²`, with `f_j=j/(NΔ)`. Exclude DC and Nyquist. Fit the log-power/log-frequency slope over a frozen physical band; either fit all raw in-band ordinates with equal weight or freeze a log-binning rule in advance. Do not switch binning or detrending per realization. If using bins, record bin edges, counts, frequency representative and power aggregation; logarithm of mean power and mean logarithm of power are different estimators. Welch is an alternative only if its segment length is specified in metres and its reduced longest usable wavelength is enforced.

Use linear detrending as a **separate, declared sensitivity condition**, not a hidden automatic correction. Match preprocessing on calibration and real inputs. A single global affine amplitude normalization leaves nonzero spectral/variogram slopes invariant; depth-varying normalization, clipping, despiking, log transformation, or moving-average detrending does not.

### Variogram: input matters as much as the formula

For a complete regular record x of N samples and positive integer lag k, use the Matheron semivariogram

\[
\widehat\gamma_x(k\Delta)=\frac{1}{2(N-k)}\sum_{i=0}^{N-k-1}(x_{i+k}-x_i)^2.
\]

Do not center the increments separately at each lag: this is a mean **squared difference**, not a sample variance of demeaned differences. For fBm,

\[
\gamma_B(r)=\frac{\sigma^2}{2}|r|^{2H},\qquad
\alpha=\frac{d\log\gamma_B}{d\log r}=2H,\qquad H_{var}=\alpha/2.
\]

Fit log semivariance against log **metre lag**, with an explicitly fixed integer-lag set and weighting. Do not substitute a spherical/exponential model's range or a fitted Matérn smoothness for this power-law slope. Drop lag zero, and return an invalid diagnostic for zero/nonpositive/nonfinite powers or variograms rather than adding an arbitrary epsilon to force a log fit.

For fGn itself, instead,

\[
\gamma_G(k\Delta)=C_G(0)-C_G(k).
\]

It approaches a sill and **is not generally proportional to r^(2H)**. At H=0.5 it is flat for nonzero lags; half its log slope tends to zero, not 0.5. The book's `a−b r^(2H−2)` is a large-lag covariance-derived form, not the fBm variogram power law.

**Bounded pilot route for fGn:** estimate H_spec on G; form `Y_0=0, Y_j=Σ_{i=0}^{j−1}G_i` and estimate H_var on Y. Label this `variogram_of_cumulative_fGn`, never `variogram_of_fGn`. Do not subtract the realization's sample mean before accumulation in the primary synthetic branch: doing so produces an endpoint-constrained bridge and changes finite-record increment statistics. A drift-removal branch must be calibrated separately. For real GR this cumulative route is only a labeled fGn-model sensitivity, not a reason to force all logs into one class.

For real levels, always retain **β and α as primary finite-band descriptors**. State whether an H conversion assumes fBm-like levels or fGn-like samples. Near a crossover, near β=1, outside admissible ranges, or under evident regime mixing, mark model assignment inconclusive rather than choosing whichever conversion makes estimators agree. Do not clip H into [0,1]. `D=2−H` concerns the graph of ideal fBm, not arbitrary sampled noise or a proven dimension of real GR; no dimension output is necessary here.

**Important dependence:** spectrum and variogram both describe second-order structure. For stationary processes the variogram is an integral of the spectrum against `1−cos(2πfr)` (with convention-dependent normalization). They are not statistically independent witnesses. Agreement is useful implementation/model consistency, **not proof of fractality, monofractality, random phase, or geological mechanism**. A lag r is also not a sharp spectral wavelength 1/f; the two estimators can emphasize different parts of a finite band.

## 2. Valid comparisons after smoothing and downsampling

### Separate the two questions

1. **Common-band preservation:** does a mild, known perturbation preserve an estimate on physical scales where its transfer is approximately flat?
2. **Intentional degradation:** how does the estimate change where smoothing/aliasing is expected to distort those scales?

Only the first supports an invariance/recovery acceptance gate. Include a roll-off-band plot as a diagnostic if convenient, but do not require H to remain unchanged there. A filtered path need not have the original short-scale roughness: for sufficiently smooth convolution, small-lag semivariance becomes quadratic.

### Physical comparison contract

- Use the **same original realization or GR interval**, not independently generated examples. Preserve a depth coordinate at every stage. Compare paired changes `ΔH=H_perturbed−H_baseline` in addition to each synthetic estimate's error against input H.
- Choose downsampling factors in advance; `q ∈ {1,2,4}` is sufficient. New spacing is `Δ_q=qΔ`, new Nyquist is `1/(2Δ_q)`. Sampling interval is not native logging-tool resolution.
- Apply an explicit low-pass **before** decimation. Record coefficients/design, cutoff in cycles/metre, passband ripple, transition width, stopband attenuation, phase convention, and decimation offset. A boxcar followed by decimation is not automatically adequate antialiasing. Unfiltered decimation may be a labeled failure control, not the production comparison.
- State all smoothing widths in metres (Gaussian standard deviation, FWHM, or boxcar width must be named, not conflated). A fixed number of samples at different Δ is a different physical filter. Prefer filtering the original-grid record and then decimating; record any multiple filtering stages.
- Crop enough samples to exclude every filter's boundary influence, then crop baseline and all perturbations to their **common interior depth interval**. Include filter radius/settling length and taper handling in metadata. Do not zero-pad across gaps or treat reflected edges as observations. If a finite-support filter uses padding internally, discard the contaminated output.
- Freeze a shared wavelength interval `[λ_min, λ_max]` across conditions. Require `λ_min ≥ 8 Δ_coarsest` as a conservative sampling margin, and `λ_max ≤ L_common/8` to retain multiple cycles. Additional passband restrictions override this rule. For Welch, use segment length instead of full record length in the long-wave rule. Require at least one decade and at least 20 in-band raw Fourier ordinates; otherwise mark insufficient common band.
- Freeze a shared variogram lag interval `[r_min,r_max]`, preferably distinct from the spectral band's wavelength interval. Use `r_max ≤ L_common/8`, and conservatively `r_min ≥ max(4Δ_coarsest, 5R)` where R is the largest finite filter support radius in metres. This is a pilot heuristic, **not** a theorem of invariance; verify it on the known-answer controls. Require at least one decade and at least eight distinct nonzero lags. Choose lag distances realizable on all grids (multiples of the coarsest spacing); use the same subset and weights in each condition.
- Set the minimum valid-pair count per chosen lag to 200 for this pilot. Record actual counts. More pairs are not more independent pairs. Equal log-spaced lag weighting avoids silently allowing numerous large integer lags to dominate.
- Freeze the bands using record length, grids, filter response, and separate development simulations, **not** the H agreement or R² of the real windows. A failed band gate is a legitimate pilot result; do not widen into Nyquist/roll-off or lengthen the geological interval solely to get a pass.

**Passband criterion:** require total digital filter power response `|A(f)|²` within 5% of unity throughout the preservation band, and inspect its log-slope contribution. For a unit-area continuous Gaussian of standard deviation σ metres, `|A(f)|²=exp(−4π²σ²f²)`, so 5% maximum power loss requires `λ_min ≥ 27.743 σ`. Verify the actual truncated discrete kernel instead of substituting this continuous formula blindly. Cascaded filters multiply their power responses. A modest amplitude loss can still impose slope bias; synthetic paired checks remain mandatory. Variogram lags integrate a broad range of spectral contributions, so spectral passband flatness alone does not certify variogram preservation.

Illustration, not a selected real window: 4096 samples at the audited 0.152 m spacing span 622.44 m; at q=4 the eight-sample shortest wavelength margin is 4.864 m. Cropping, passband restrictions and the one-decade rule may make some proposed filter/window combinations ineligible. Compute eligibility rather than assuming these sample counts suffice.

## 3. Nulls, depth regularity, and reproducible real windows

The [data audit](./14-force2020-data-audit.md) reports a common 0.152 m step, not universally adequate contiguous coverage. Direct inspection of `data/force2020/extracted/Force_2020_all_wells_train_test_blind_hidden_final/15_9-13.las` confirms metre DEPT, GR in gAPI, `NULL=-999.250000`, and actual sentinel-valued GR rows. Finite does not mean valid.

1. Read each LAS header's NULL and mask that value, NaN, and infinities **before** statistics, run finding, filtering, accumulation, or FFT. Keep the original file unchanged. Do not use positivity alone as the null rule and do not erase unusual valid GR values just because they are inconvenient. Any physical-range QC must be explicit and reported separately.
2. Use the actual depth column and units, check strict monotonicity, duplicates and spacing against the nominal grid. Float serialization jitter may be tolerated at a stated small tolerance; a defensible candidate is absolute step tolerance `max(1e−5 m, 0.001Δ)`. Verify the selected records against it. Never replace a real skipped row by assuming unit sample spacing. If only coordinate roundoff is snapped to a regular grid, record the maximum correction and do not resample amplitudes.
3. Split at every invalid GR value or genuine depth discontinuity. Choose wholly valid contiguous runs and extract windows **inside** them. Never `dropna()` and concatenate across a gap: that changes physical distances and creates false neighbors. No interpolation, forward fill, mean fill, zero fill or gap-spanning FFT in the primary pilot.
4. Select approximately three windows from distinct wells with a deterministic rule based on length/coverage/depth ordering, not spectral appearance or agreement. A target of 4096 samples per window is reasonable if eligible; state the actual interval, sample count and all rejection reasons. One window per well avoids pseudo-replication. Select common usable length and necessary context for filter cropping in advance. If there are insufficient windows, report that, not a substitute collection selected on favorable results.
5. Plot each selected GR interval and its first differences; record obvious trend, flat sections, spikes remaining after upstream processing, and regime boundaries. Continuity does not imply geological homogeneity. Do not claim a facies-homogeneous window without checking labels/context, and do not expand this pilot into supervised classification.
6. For a missingness smoke test, insert one interior sentinel/gap into a synthetic copy and confirm that it is rejected/split with depth retained. Test both the header sentinel and NaN. A pairwise-valid variogram could be a future branch using actual distance and pair counts, but it does not license an FFT across the same gap and is unnecessary here.
7. Filtering support must be entirely valid. Do not use normalized convolution that silently bridges invalid values. Empty, constant, too-short, irregular, or insufficient-band inputs must produce a reason-coded invalid result, not a numeric H with a warning buried in a log.

Real output is **sensitivity relative to the processed FORCE baseline**. Its H is unknown. Bias, RMSE against truth, physical recovery, tool correction accuracy, and native vertical resolution cannot be inferred from these data. Real-window differences are descriptive examples, not a population-wide cross-well validation.

## 4. Known-answer design and falsifiable gates

### Minimal test matrix

Use `H ∈ {0.2,0.5,0.8}` and at least 30 independent evaluation realizations per H at the actual analysis length; use the same seeds for paired perturbations. H=0 and H=1 are excluded. Construct Gaussian fGn using its target covariance (e.g. validated Davies–Harte/circulant embedding or Hosking), then cumulative sums for fBm. Check embedding eigenvalues and report any fallback rather than taking absolute values of materially negative eigenvalues. Do not validate a power-law FFT estimator solely on fixed-amplitude inverse-FFT signals designed to have that same slope; that is partly circular. Ensemble covariance/increment checks provide an independent generator check without adding another H estimator.

Known targets (algebra evaluated during this audit):

| H | β_fBm | β_fGn | α_var on fBm/cumulative fGn |
|---:|---:|---:|---:|
| 0.2 | 1.4 | −0.6 | 0.4 |
| 0.5 | 2.0 | 0.0 | 1.0 |
| 0.8 | 2.6 | 0.6 | 1.6 |

At H=0.5, independent Gaussian increments are a particularly transparent control. The exact normalized lag-one fGn covariances for these H values are approximately −0.340246, 0, and 0.515717; use ensemble uncertainty, not equality from one realization, when checking a generator. Use raw, smoothing-only, and antialiased q=2/q=4 branches if each retains a legal common band. An aggressive filter/no-passband condition can simply exercise the invalid-band gate. Do not add a large noise/gap/window-length factorial experiment.

### Gates and decision rule

| Gate | Proposed pass criterion | On failure |
|---|---|---|
| G0 — mathematical/input integrity | Correct fBm/fGn mappings and cumulative-fGn labeling; sentinel/NaN/gap, constant input, invalid H conversion, and insufficient-band cases handled explicitly; depth and filter metadata retained. No clipped H. | No-go for scientific interpretation; correct pipeline first. |
| G1 — clean known-answer recovery | For each H and each intended estimator/input route separately: absolute empirical bias ≤0.10, RMSE ≤0.20, valid-estimate fraction ≥0.90 over the frozen evaluation seeds. Do not pool H values to conceal failures. | No-go for the failing route; report the bias/domain failure. A reduced valid domain is a revised pilot, not a retrospective full pass. |
| G2 — mild common-band preservation | For every declared mild condition and H/route: absolute mean paired ΔH ≤0.10 and median absolute paired ΔH ≤0.15, with ≥0.90 paired valid fraction; the perturbed estimate must also satisfy G1. | No-go for a stability claim at that condition; distinguish filter distortion, limited band, finite-sample error and estimator bias. |
| G3 — real-data feasibility | At least two of the planned approximately three distinct-well windows have valid contiguous inputs and legal common physical bands for both diagnostics and at least one mild perturbation; retain and report every attempted window. | No-go for expansion on this window/filter specification; the dataset may still support a narrower pilot. |
| G4 — interpretation/report completeness | Provide per-realization estimates and flags, aggregate bias/RMSE/failure counts, paired differences, window provenance and plots with actual fit bands. Conclusions explicitly distinguish synthetic truth from real-baseline sensitivity. | Incomplete pilot, irrespective of favorable summary plots. |

Report whether G0–G4 pass **individually**. A full pilot go means these specified technical/feasibility gates pass and supports only a separately approved next phase. No-go is an acceptable scientific outcome. Mild real-window `|ΔH|>0.15` or cross-estimator `|H_spec−H_var|>0.20` should be flagged as descriptive instability/disagreement, **not** scored as error against an unknown true H. Real agreement is not itself a gate and cannot establish fractality.

Use Monte Carlo realizations as the uncertainty unit: report mean bias, RMSE, empirical spread/quantiles, valid counts and the standard error of mean error/mean paired change. With this small repeat count, mark values near a threshold as borderline and show their Monte Carlo uncertainty; do not claim precise interval calibration. OLS standard errors from correlated periodogram/variogram ordinates are not reliable H confidence intervals. Do not iid-bootstrap individual depths. Any bootstrap of evaluation metrics resamples whole independent realizations (paired baseline/perturbation together). Real windows warrant descriptive sensitivity, not formal confidence coverage; block bootstrap would need additional dependence assumptions and is out of scope.

Define bias and RMSE only on explicitly reported valid estimates, with invalid fraction beside them; do not replace failures by zero. A low survivor-only RMSE with many failures cannot pass. R² can be recorded as descriptive fit information, but is neither an acceptance criterion for fractality nor a reason to select a new band after looking at results.

## 5. Error register for earlier notes — do not silently propagate

Earlier documents remain untouched. Locations below refer to their current headings/line positions at review time.

| Earlier location | Issue | Required treatment in pilot |
|---|---|---|
| `02-book-chapters-1-4.md`, line 70 (book PDF p.66, printed p.47) | Says fBm is stationary and nonergodic. Direct PDF extraction confirms the stationarity statement is in the book, not merely a note typo. | Standard fBm levels are Gaussian and nonstationary; use the covariance definition above. Avoid unqualified ergodicity claims for a nonstationary process. |
| `05-estimation-methods.md`, line 57; Li PDF p.2, §2 | Calls fBm non-Gaussian. The local Li PDF itself contains this error. | fBm is Gaussian; real well-log values may be non-Gaussian. A histogram along one nonstationary sample path is not a test of Gaussian finite-dimensional distributions. |
| `05-estimation-methods.md`, line 55; Li eqs.12–14 | `H_fGn ≈ H_fBm−1` without a sufficiently prominent convention warning invites a one-unit error. | Preserve one common stochastic H; distinguish Li's generalized roughness exponent explicitly. |
| Li PDF p.2, extracted eq.10 | A negative coefficient appears after an absolute square. Whether typesetting or extraction, it cannot be a power transfer. | Use nonnegative `4 sin²(πfΔ)`; derivative limit has positive `(2πfΔ)²`. Do not copy the negative sign. |
| `02-book-chapters-1-4.md`, eqs.2.3–2.5 versus `05-estimation-methods.md`, lines 39/55 | Book uses `S∝ω^β` (signed slope), whereas other notes use `S∝f^(−β)` (decay exponent). Neither convention alone is wrong. | Store signed regression slope m and define β=−m; never reuse β across these conventions without conversion. |
| `02-book-chapters-1-4.md`, eq.3.1, versus `03-well-log-and-reservoir-papers.md`, variogram method | fGn sill-minus-covariance form and fBm increment power law are different models. | Half a log-variogram slope gives fBm H, not direct fGn H. Use cumulative fGn for the latter test route. |
| `03-well-log-and-reservoir-papers.md`, lines 33–34 | `r^(2H−2)` is presented as a correlation of fBm levels. | This is the asymptotic increment/fGn covariance behavior; fBm level covariance depends on both positions. |
| `03-well-log-and-reservoir-papers.md`, line 49 | Reports `D_F=D_E+2H−1` as a source formula. | Not the graph-dimension conversion for 1-D fBm. Do not use it; this pilot need not report D. |
| `05-estimation-methods.md`, line 11, outside current pilot | Box-count spectrum is written `f(α)=lim log N_ε(α)/log ε`, missing the minus sign when ε is shrinking box size. | Quarantine for any future multifractal work; correct denominator is `log(1/ε)` under that convention. No multifractal implementation now. |
| `12-final-mtp-recommendation.md`, methods/validation; `14-force2020-data-audit.md`, implications | Broad study ambitions and dataset availability could be mistaken for approved scope or demonstrated validity. | Retain the bounded pilot and its go/no-go gate. Whole-well coverage does not establish contiguous-band eligibility; lithology labels do not supply true H or tool ground truth. |

## 6. Source grounding and scope of this audit

- Read [the recommendation](./12-final-mtp-recommendation.md), [dataset audit](./14-force2020-data-audit.md), [book chapter notes](./02-book-chapters-1-4.md), [method notes](./05-estimation-methods.md), and the relevant carbonate-paper method excerpt in [well-log notes](./03-well-log-and-reservoir-papers.md).
- Directly read the local Li PDF, principally PDF pp.1–6: process distinctions, equations, synthetic comparison and tool-roll-off warning. Its historical recommendations are useful, but the mathematical mistakes listed above are not adopted.
- Directly inspected Hough (1989), **local PDF p.2/printed p.674**, as a rendered image after text extraction returned only license notices. This page warns about nonstationary Wiener–Khinchin extensions, spectra with constructed nonrandom phases, and differentiability for β>3. It supports caution, not a universal random-phase certification rule for all possible fractal signals.
- Read the Schepers et al. local OCR markdown, `Literature/md/datalab-output-Four_methods_to_estimate_the_fractal_dimension_from_self-affine_signals_medical_application.pdf.md`, especially generator dependence and fBm/fGn distinctions. Direct PDF text extraction was uninformative; OCR equations are not treated as sole mathematical authority.
- Book inspection was **strictly confined to chapters 1–4**: chapter-bounded notes and a direct extraction of PDF p.66 in Chapter 2. No Chapter 5+ content was read or used. That direct check verifies the earlier stationarity error's provenance.
- A LAS header/data excerpt was inspected for concrete null and unit handling; this review did not repeat the full dataset audit or choose implementation windows.

**Actionable handoff:** freeze the common-H convention and explicit estimator inputs; freeze physical bands and filter/cropping rules; require G0 before interpreting G1/G2; then run the few predefined GR windows and report G3/G4. Store the eventual pilot configuration, per-realization/paired result tables, real-window selection/rejection ledger, and fit-band plots alongside the implementer's artifacts. This review does not authorize expansion beyond that decision point.
