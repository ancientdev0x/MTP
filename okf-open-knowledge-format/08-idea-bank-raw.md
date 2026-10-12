# Raw MTP Idea Bank

Generated independently by five parallel ideation agents. These are candidates, not yet novelty-verified.

## Idea 1: Regime-Aware Monofractal Estimation of Well-Log Roughness

**Category:** Not specified
**Research question / hypothesis:** Can a regime-aware workflow distinguish genuine monofractal scaling in well logs from apparent scaling caused by facies changes, trends, and concatenated intervals?
**Contribution / method:** Develop and evaluate a reproducible workflow that first segments logs into statistically homogeneous intervals, then estimates H and fractal dimension using spectral slope, increment variance, and R/S analysis with method selection based on fBm/fGn diagnostics.
**Data:** One or more wells containing GR and sonic or density logs, depth sampling metadata, formation or facies markers if available, and optionally synthetic fBm/fGn signals with known H.
**Risk:** ['There may be too few homogeneous intervals for stable scaling fits.', 'Segmentation choices could dominate the estimated fractal attributes.', 'A strong log-log regression may still represent a finite-range artifact rather than true monofractality.']

## Idea 2: Tool-Resolution-Corrected Fractal Dimension for Thin-Bed Detection

**Category:** Not specified
**Research question / hypothesis:** Does correcting probe-averaging effects before monofractal analysis improve the detection of thin beds without creating artificial high-frequency fractal structure?
**Contribution / method:** Adapt Li and Cheng's local scale-law correction to modern well-log data, explicitly separating spectral improvement from petrophysical validation and identifying the scale range in which corrected H or D is trustworthy.
**Data:** High-resolution conductivity or resistivity logs, tool spacing and vertical-resolution metadata, thin-bed markers from image logs, cores, interpreted picks, or a synthetic layered reference model.
**Risk:** ['Tool-response metadata may be unavailable or insufficiently detailed.', 'The correction may amplify noise or ringing near sharp boundaries.', 'Improved spectral resolution may not correspond to improved geological accuracy.']

## Idea 3: Scale-Dependent Fractal Signatures for Automated Stratigraphic Boundary Correlation

**Category:** Not specified
**Research question / hypothesis:** Can changes in local monofractal attributes identify correlatable geological boundaries more robustly than amplitude similarity alone?
**Contribution / method:** Create a lightweight well-to-well correlation method combining local wavelet variance exponent, increment-based H, and mean log response, with scale windows constrained by estimated bed thickness and validated against manual boundaries.
**Data:** At least three wells with common GR logs and preferably CGR, RHOB, or DT; depth matching information; and manual boundary or core-based correlation for validation.
**Risk:** ['Wavelet exponents may be unstable for short layers.', 'The method may reproduce amplitude patterns rather than add independent fractal information.', 'Boundary labels may contain interpreter bias and may not represent a unique stratigraphic surface.']

## Idea 4: Fractal-Feature Stability Across Sampling Intervals and Logging Tools

**Category:** Not specified
**Research question / hypothesis:** Which monofractal attributes remain stable when the same geological interval is represented at different sampling intervals, tool resolutions, and preprocessing levels?
**Contribution / method:** Establish a practical stability protocol for H, spectral beta, variogram dimension, and R/S estimates, including empirical lower and upper scale cutoffs tied to sampling and tool response.
**Data:** Repeated or overlapping logs from different tools, logs with different sampling intervals, or one high-resolution log that can be systematically downsampled and smoothed; tool metadata and geological interval markers.
**Risk:** ['True repeated measurements may be unavailable, forcing reliance on simulated degradation.', 'Different tools may respond to different physical properties, not merely different resolutions.', 'A metric can appear numerically stable while its geological interpretation changes.']

## Idea 5: Fractal-Conditioned Filling of Missing Well-Log Intervals

**Category:** Not specified
**Research question / hypothesis:** Can local H, spectral exponent, and variogram dimension improve conditional simulation of missing log intervals compared with conventional interpolation while preserving realistic heterogeneity?
**Contribution / method:** Build a small-scale conditional fBm/fGn simulation workflow that uses observed local fractal attributes to select or constrain realizations, and evaluate uncertainty rather than presenting a single deterministic reconstruction.
**Data:** Well logs with artificially masked and naturally missing intervals, preferably log-derived porosity plus core porosity or permeability in a subset; formation/facies markers and sampling metadata.
**Risk:** ['Fractal simulation may preserve variability but not the correct mean trend or facies transition.', 'H estimates from short neighboring intervals may be unreliable.', 'Core coverage may be too sparse for meaningful independent validation.']

## Idea 6: Separating Geological Persistence from Hydrocarbon-Screening Effects in Monofractal Log Attributes

**Category:** Not specified
**Research question / hypothesis:** Do reported Hurst-exponent differences between hydrocarbon-potential and non-potential intervals persist after controlling for lithology, facies, trend, and log-specific preprocessing?
**Contribution / method:** Reassess wavelet-based H differences using independent monofractal estimators, matched facies controls, surrogate tests, and held-out wells, thereby testing whether H adds information beyond conventional quick-look labels.
**Data:** Multiple wells with GR, SP, NPHI, RHOB, and resistivity logs; HC/NHC intervals; lithology or facies interpretations; and, if possible, fluid contacts, production tests, pressure data, or core saturation.
**Risk:** ['HC/NHC labels may be derived only from quick-look rules and therefore lack independent truth.', 'Resistivity may produce unstable wavelet-fractal estimates, as reported locally.', 'Fractal features may mainly encode lithology or interval thickness rather than fluid state.']

## Idea 7: A Monofractal Multi-Log Consistency Test for Reservoir Heterogeneity

**Category:** Not specified
**Research question / hypothesis:** Do related logs exhibit consistent scale-dependent persistence within the same geological interval, and can inconsistency identify facies transitions, borehole effects, or measurement artifacts?
**Contribution / method:** Introduce a cross-log consistency framework that compares H or spectral beta from GR, RHOB, NPHI, DT, and resistivity while retaining channel-specific physical interpretations instead of pooling them into one fractal score.
**Data:** Co-registered multi-log suites from several wells, formation/facies markers, borehole-condition indicators, and optional core porosity/permeability or image-log information.
**Risk:** ['Different logs measure different physical properties, so agreement is not always expected.', 'Cross-log correlations may be driven by common depth trends or preprocessing.', 'A lack of consistency may reflect tool quality rather than reservoir heterogeneity.']

## Idea 8: Finite-Scale Monofractal Maps of Facies-Transition Roughness

**Category:** Not specified
**Research question / hypothesis:** Can the depth evolution of local fractal dimension quantify the sharpness and thickness of facies transitions more reproducibly than amplitude-gradient measures?
**Contribution / method:** Develop a local fractal-dimension map using moving-window spectral and variogram estimates, with explicit finite-scale validity tests, to distinguish sharp boundaries, gradational transitions, and internally heterogeneous beds.
**Data:** High-resolution GR and at least one complementary log such as RHOB, NPHI, DT, or resistivity; interpreted facies boundaries or core descriptions; sampling and tool-resolution metadata.
**Risk:** ['Window overlap can create visually smooth but statistically dependent attribute maps.', 'A local fractal estimate may be invalid near boundaries where stationarity fails.', 'Transition sharpness may be confounded with tool smoothing and sampling.']

## Idea 9: Which Well-Log Measure Produces Reproducible Multifractality?

**Category:** Not specified
**Research question / hypothesis:** The apparent multifractal spectrum of a well-log interval depends materially on how the positive measure is defined; a physically interpretable measure based on normalized absolute increments or local property mass should be more stable across wells than the raw log-value measure.
**Contribution / method:** For each formation-consistent interval, compare three explicit measures on depth boxes of width epsilon: (1) raw positive measure mu_i(epsilon) = sum_{k in box i} max(x_k - x_min + delta, 0), (2) increment measure mu_i(epsilon) = sum_{k in box i} |x_{k+1} - x_k|, and (3) transformed-property measure based on log-resistivity or another justified monotonic transform. Normalize each box measure so that sum_i mu_i(epsilon) = 1. Estimate Z_q(epsilon) = sum_i mu_i(epsilon)^q, tau(q) from log-log slopes, and f(alpha) through alpha = d tau/dq and f(alpha) = q alpha - tau(q). Independently estimate h(q) and f(alpha) with MFDFA on the same intervals, using stated detrending order and q range.
**Data:** At least several LAS wells containing GR, density, neutron, sonic, and resistivity where available; formation tops or facies intervals; sample interval and tool-resolution metadata; enough points per interval for multiple scale levels, preferably several hundred or more.
**Risk:** Not specified

## Idea 10: Wavelet Leaders versus MFDFA for Facies-Conditioned Well-Log Multifractality

**Category:** Not specified
**Research question / hypothesis:** Wavelet leaders will provide more spatially localized and stable estimates of singularity spectra near thin beds and facies transitions, whereas MFDFA may be more sensitive to polynomial trends and window placement.
**Contribution / method:** Segment logs into facies- or formation-consistent windows. For wavelet leaders, compute discrete wavelet coefficients c_{j,k}, define each leader L_{j,k} as the maximum absolute coefficient over the dyadic interval and its neighboring dilated intervals, and estimate S_L(q,j) = 2^{-j} sum_k L_{j,k}^q. For MFDFA, form Y(k) = sum_{i=1}^k (x_i - mean(x)), divide into windows of scale s, detrend each with polynomial order m, and compute F_q(s) from q-order residual variances. Estimate h(q), tau(q), alpha, and f(alpha) for both methods.
**Data:** High-resolution GR, density, neutron, sonic, and resistivity logs from multiple wells, with facies or lithological markers and reliable depth sampling. Ordinary Python packages such as NumPy, SciPy, PyWavelets, pandas, and matplotlib are sufficient.
**Risk:** Not specified

## Idea 11: Separating Genuine Multifractality from Facies-Mixing Artifacts

**Category:** Not specified
**Research question / hypothesis:** A substantial portion of broad multifractal spectra measured over complete wells may result from concatenating statistically different geological regimes rather than from multifractal dynamics within individual formations.
**Contribution / method:** For each log, compare three analysis levels: the complete well, automatically segmented stationary regimes, and fixed-length windows. Define a positive increment measure mu_i(epsilon) proportional to the sum of absolute detrended increments in box i. Estimate tau(q) and f(alpha) using partition functions, and estimate h(q) using MFDFA. Identify candidate regime boundaries using rolling mean, variance, distributional change tests, and spectral-slope changes. Select scaling ranges separately in each regime using contiguous scales with high regression fit, low slope uncertainty, and sufficient box counts.
**Data:** Several complete wells with long logged intervals, formation tops or facies labels, and at least one high-resolution curve such as GR. Optional core or image-log information would strengthen geological validation but is not essential.
**Risk:** Not specified

## Idea 12: Tool-Resolution-Aware Multifractal Cutoffs in Well Logs

**Category:** Not specified
**Research question / hypothesis:** Multifractal scaling inferred below the effective tool-response length is unreliable, and explicitly estimating a lower scale cutoff will improve agreement between logs from tools with different vertical resolutions.
**Contribution / method:** Model each measured curve as y(z) = (g * x)(z) + noise, where g is an approximate tool-response kernel. Use calibration information or plausible kernels to estimate the effective resolution length. Compute wavelet-leader structure functions and MFDFA fluctuation functions across depth scales. Exclude scales below the resolution cutoff and scales above one-third of the analyzed interval, while selecting the final range by regression stability, residual diagnostics, and minimum independent-window count. Define the measure from positive absolute increments or leader magnitudes, with normalization stated explicitly.
**Data:** Repeated or co-located logs of the same property acquired with different vertical resolutions, tool specifications, and sample intervals. If unavailable, public or synthetic convolution experiments can provide the primary test, with a smaller real-log demonstration.
**Risk:** Not specified

## Idea 13: Local Multifractal Spectra as Indicators of Stratigraphic Boundaries

**Category:** Not specified
**Research question / hypothesis:** Abrupt changes in local multifractal parameters, especially leader-based alpha quantiles and MFDFA h(q), can identify stratigraphic boundaries more robustly than single-scale amplitude thresholds in heterogeneous intervals.
**Contribution / method:** Apply moving windows to GR, density, neutron, and sonic logs. Within each window, define a normalized measure from absolute detrended increments, and calculate local wavelet-leader spectra. In parallel, calculate MFDFA h(q) using several polynomial detrending orders. Extract features such as alpha_min, alpha_max, spectrum width Delta alpha, asymmetry, h(2), and tau curvature. Use neighboring-window contrasts and a change-point detector to generate candidate boundaries, while enforcing a scale range smaller than the geological layer thickness when that information is available.
**Data:** Three or more correlated wells with GR and at least two complementary logs, manually interpreted boundaries or formation tops, and sufficiently dense sampling around thin beds.
**Risk:** Not specified

## Idea 14: Multifractal Persistence of Porosity Proxies across Wells

**Category:** Not specified
**Research question / hypothesis:** The multifractal spectrum of a log-derived porosity proxy contains transferable information about vertical heterogeneity, but its transferability is conditional on formation, scale range, and preprocessing rather than being a universal reservoir signature.
**Contribution / method:** Derive porosity proxies from density-neutron combinations using a transparent petrophysical equation and retain uncertainty from input logs. Define a positive measure as normalized pore-volume proxy mass per depth box, mu_i(epsilon) = sum_{k in i} phi_k Delta z, after clipping or transforming only with documented physical justification. Estimate tau(q), D_q, and f(alpha) using partition functions, and estimate local h(q) with MFDFA. Analyze original, detrended, and depth-normalized versions separately.
**Data:** Multiple wells with density and neutron logs, formation tops, sample intervals, and preferably core porosity from at least one or more wells. A modest number of wells is sufficient if the validation is strictly well-wise.
**Risk:** Not specified

## Idea 15: Multifractal Effects of Trend Removal and Depth Warping

**Category:** Not specified
**Research question / hypothesis:** Detrending and depth alignment can change estimated multifractal spectra as much as the choice between wavelet leaders and MFDFA, particularly when thickness variations or compaction trends are present.
**Contribution / method:** For correlated wells, analyze each log under four preprocessing states: raw depth, local polynomial detrending, formation-wise standardized depth, and marker-based nonlinear depth warping. Define the measure explicitly as normalized absolute increments for partition-function analysis and use the profile-based MFDFA definition for fluctuation analysis. Estimate scale ranges independently after each preprocessing state; do not reuse a range if the depth transform changes physical scale. Record how alpha(q), f(alpha), h(q), and spectrum width vary.
**Data:** Two or more wells with reliable formation markers and logs sampled at sufficiently high density; sonic or density curves are useful for identifying compaction-related trends, but GR alone can support the basic experiment.
**Risk:** Not specified

## Idea 16: A Surrogate-Tested Multifractal Quality-Control Workflow for Well Logs

**Category:** Not specified
**Research question / hypothesis:** A well-log interval should be labeled multifractal only when its observed spectrum exceeds the distribution produced by surrogates that preserve the relevant linear correlation and amplitude properties.
**Contribution / method:** Build a reproducible pipeline combining stationarity checks, missing-data QC, spectral screening, wavelet leaders, and MFDFA. Use a declared positive measure, such as normalized sums of absolute detrended increments or squared wavelet leaders. Estimate spectra over scale ranges selected using minimum length, tool-resolution lower bounds, one-third-length upper bounds, log-log residual tests, and stability under neighboring scale exclusions. Generate three surrogate classes: shuffled data, phase-randomized Fourier surrogates, and amplitude-adjusted phase-randomized surrogates. Define a multifractality score from Delta alpha, tau(q) curvature, and the difference between positive- and negative-q slopes.
**Data:** A collection of LAS wells with at least one or two high-quality curves, sample interval and null-value metadata, and preferably tool-resolution information. No specialized hardware or large dataset is required; the main cost is careful implementation and simulation.
**Risk:** Not specified

## Idea 17: Boundary-aware multifractal segmentation for geological zone picking

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Use local wavelet-leader spectra, spectral crossovers, and change-point detection jointly to identify intervals whose scaling regime changes at geological surfaces. The key contribution is separating true within-zone multifractality from artificial multifractality caused by concatenating different facies, trends, or tool-response regimes. Report valid scale ranges and uncertainty for every picked boundary.
**Data:** Not specified
**Risk:** Not specified

## Idea 18: Cross-log multifractal coupling for facies discrimination

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Estimate scale-dependent joint structure between GR, RHOB, NPHI, DT, and resistivity rather than computing independent Hurst values per log. Features would include cross-wavelet coherence, joint leader moments, scale-dependent correlation, and disagreement between logs. This tests whether facies are better characterized by coordinated multiscale responses than by single-log roughness.
**Data:** Not specified
**Risk:** Not specified

## Idea 19: Tool-response-invariant fractal representations for transferable facies classification

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Separate geological scaling signatures from acquisition artifacts by estimating the instrument transfer function and training a representation to remain stable under realistic resampling, smoothing, spectral roll-off, missing samples, and noise. The test is cross-tool and cross-field transfer, not within-well accuracy.
**Data:** Not specified
**Risk:** Not specified

## Idea 20: Fractal-spectrum change with stratigraphic scale for depositional architecture classification

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Use the scale at which multifractal spectra change shape or exhibit crossovers as an estimate of characteristic bed-pack or architectural-element thickness. Classify stacking patterns such as aggradation, progradation, fining-upward, and heterolithic alternation from the joint evolution of f(alpha), asymmetry, and persistence across nested windows.
**Data:** Not specified
**Risk:** Not specified

## Idea 21: Fractal heterogeneity signatures for flow-zone classification

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Predict hydraulic flow-zone or rock-quality classes from multiscale variability and intermittency in log-derived porosity, permeability proxies, and saturation-related logs, while testing whether multifractal width/asymmetry captures heterogeneity relevant to connectivity rather than merely lithology.
**Data:** Not specified
**Risk:** Not specified

## Idea 22: Uncertainty-aware multifractal fusion for missing-log reconstruction

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Reconstruct a missing or unreliable log conditional on other logs while preserving the target's scale-dependent multifractal statistics and cross-log coupling. Generate calibrated ensembles rather than one smoothed curve, and evaluate whether geological intervals and uncertainty are preserved.
**Data:** Not specified
**Risk:** Not specified

## Idea 23: Graph-constrained multiwell correlation using fractal signatures

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Represent each well as a sequence of multiscale fractal states and solve a globally constrained graph alignment across several wells, enforcing stratigraphic ordering, thickness plausibility, and uncertainty. Unlike pairwise boundary matching, the method should detect missing, truncated, or rapidly changing intervals.
**Data:** Not specified
**Risk:** Not specified

## Idea 24: Causal stress test of fractal attributes under facies and fluid confounding

**Category:** Not specified
**Research question / hypothesis:** Not specified
**Contribution / method:** Test whether fractal features respond to depositional texture or merely to confounders such as fluid type, borehole condition, tool filtering, depth trend, and uranium effects. Use controlled matched intervals and causal/conditional models to estimate the incremental geological information of each fractal attribute.
**Data:** Not specified
**Risk:** Not specified

## Idea 25: Tool-Resolution-Aware Fractal Correction for Well Logs

**Category:** Not specified
**Research question / hypothesis:** Does correcting the scale-dependent attenuation imposed by logging-tool response improve the reproducibility of monofractal and multifractal estimates without creating artificial high-frequency structure?
**Contribution / method:** A physically constrained preprocessing and validation framework that estimates the usable lower scale from tool-response information, compares raw, deconvolved, and Li-Cheng-style local fractal correction, and distinguishes improved signal resolution from improved petrophysical accuracy.
**Data:** Not specified
**Risk:** Not specified

## Idea 26: Preprocessing Multiverse for Fractal Well-Log Features

**Category:** Not specified
**Research question / hypothesis:** Which preprocessing choices—trend removal, normalization, transformation, interpolation, and increment formation—materially change fractal estimates and downstream reservoir-characterization conclusions?
**Contribution / method:** A reproducible sensitivity-analysis protocol that treats preprocessing as an explicit source of uncertainty rather than selecting one undocumented pipeline. It would identify estimands that are robust across plausible preprocessing choices.
**Data:** Not specified
**Risk:** Not specified

## Idea 27: Adaptive Geological Scale and Window Selection

**Category:** Not specified
**Research question / hypothesis:** Can scale ranges and window lengths be selected from local scaling diagnostics and geological constraints instead of fixed, arbitrary values while avoiding overfitting to facies boundaries?
**Contribution / method:** An adaptive estimator that selects valid scaling ranges using log-log linearity, residual structure, minimum point counts, tool-resolution cutoffs, and geological layer-thickness constraints, with a leakage-controlled selection procedure.
**Data:** Not specified
**Risk:** Not specified

## Idea 28: Uncertainty-Calibrated Fractal and Multifractal Attributes

**Category:** Not specified
**Research question / hypothesis:** Are confidence intervals for H, spectral slope, and multifractal-spectrum features calibrated under finite length, autocorrelation, missing data, tool filtering, and nonstationarity typical of well logs?
**Contribution / method:** A practical uncertainty framework combining block bootstrap, parametric synthetic calibration, and between-pipeline variability, producing uncertainty intervals and reliability flags for each interval-level fractal attribute.
**Data:** Not specified
**Risk:** Not specified

## Idea 29: Surrogate-Controlled Test for Genuine Multifractality

**Category:** Not specified
**Research question / hypothesis:** How much of the apparent multifractality in well logs is attributable to heavy-tailed amplitudes, trends, concatenated facies, linear correlations, or finite-size effects rather than nonlinear scale-dependent organization?
**Contribution / method:** A decision framework using phase-randomized, shuffled, amplitude-adjusted, segmented, and null-model surrogates to test whether observed multifractal width or nonlinear tau(q) exceeds artifacts expected under appropriate controls.
**Data:** Not specified
**Risk:** Not specified

## Idea 30: Cross-Well Generalization of Fractal Reservoir Features

**Category:** Not specified
**Research question / hypothesis:** Do fractal and multifractal attributes learned from one well generalize to unseen wells and formations, or do they mainly encode well-specific tool, sampling, and geological effects?
**Contribution / method:** A leakage-resistant cross-well evaluation protocol for fractal features, including well-held-out normalization, domain-shift diagnostics, and comparison with conventional log statistics.
**Data:** Not specified
**Risk:** Not specified

## Idea 31: Benchmarking Fractal Estimators Under Well-Log Conditions

**Category:** Not specified
**Research question / hypothesis:** Which monofractal and multifractal estimators provide the best bias-variance-robustness trade-off for finite, filtered, nonstationary, irregularly sampled well logs?
**Contribution / method:** A standardized estimator benchmark covering spectral slope, variogram, R/S, relative dispersion, box-counting, MFDFA, and wavelet leaders under controlled signal and well-log perturbations, with a public reproducible implementation.
**Data:** Not specified
**Risk:** Not specified

## Idea 32: Robust Multifractal Measure Selection for Reservoir Characterization

**Category:** Not specified
**Research question / hypothesis:** Which definition of the positive measure used in multifractal analysis—transformed log values, increments, absolute increments, wavelet coefficients, or leader magnitudes—produces the most stable and geologically interpretable spectra?
**Contribution / method:** A measure-selection study that makes the usually implicit multifractal input explicit and evaluates stability, null sensitivity, cross-well transfer, and relationship to reservoir heterogeneity rather than treating f(alpha) as measure-independent.
**Data:** Not specified
**Risk:** Not specified

## Idea 33: Benchmarking Monofractal Estimators for Depth-Indexed Well Logs

**Category:** low-risk comparison study
**Research question / hypothesis:** Spectral-slope estimation on an explicitly selected scaling range, combined with Hurst estimation from increments, is more stable and reproducible than applying R/S analysis directly to raw well logs.
**Contribution / method:** Perform depth resampling, missing-value handling, trend and stationarity checks, and tool-resolution screening. Estimate H and fractal dimension using power spectra, R/S on increments, variograms, relative dispersion and optionally box-counting. Report valid scale ranges and uncertainty from bootstrap or repeated synthetic realizations.
**Data:** Publicly accessible LAS well logs such as gamma ray, density, neutron porosity, sonic and resistivity from the FORCE 2020 dataset or another public multiwell collection; if external data are unavailable, synthetic fBm/fGn signals with known Hurst exponents plus locally generated facies-like piecewise signals.
**Risk:** low

## Idea 34: Do Fractal Attributes Improve Well-to-Well Boundary Correlation?

**Category:** low-risk comparison study
**Research question / hypothesis:** Wavelet-derived Hurst attributes and local spectral/variogram attributes provide more stable correlation cues across wells than raw-log cross-correlation alone, particularly where amplitude and baseline differ between wells.
**Contribution / method:** Normalize logs within comparable intervals; calculate windowed wavelet Hurst estimates, spectral slopes, variogram dimensions and raw-log features. Align wells using dynamic time warping or constrained correlation, then compare boundary locations inferred from each feature family.
**Data:** Two or more public wells with common gamma-ray, density, sonic or neutron logs and approximate formation tops. If reliable tops are unavailable, use synthetic depth-shifted wells with known boundaries.
**Risk:** low

## Idea 35: Facies-Aware Adaptive Scaling Windows for Well-Log Fractal Analysis

**Category:** medium-risk methodological idea
**Research question / hypothesis:** Estimating fractal attributes within statistically homogeneous adaptive windows reduces false scaling caused by concatenated facies, trends and formation boundaries compared with fixed-length windows.
**Contribution / method:** Detect candidate boundaries using change-point statistics, distribution shifts and multichannel gradients. Estimate local spectral slopes, Hurst exponents and variogram dimensions separately inside adaptive segments. Compare with fixed windows and explicitly reject windows lacking a defensible log-log scaling range.
**Data:** Public multiwell LAS data containing gamma ray, density, neutron, sonic and resistivity where possible; synthetic piecewise fBm/fGn logs with controlled boundary locations and known scaling parameters.
**Risk:** medium

## Idea 36: Fractal Correction of Probe-Averaged Logs for Thin-Bed Detection

**Category:** medium-risk methodological idea
**Research question / hypothesis:** A scale-dependent local singularity correction can recover thin-bed contrast more selectively than moving-average sharpening while avoiding excessive amplification of tool noise.
**Contribution / method:** Estimate a local exponent from the log-measure versus scale relation, reconstruct the corrected curve, and compare several window ranges and optional tool-response weights. Include safeguards based on local noise estimates and spectral roll-off. Preserve raw, corrected and residual curves.
**Data:** Public high-resolution conductivity, resistivity, gamma-ray or density logs with sampling metadata; synthetic logs generated by convolving ideal thin beds with known tool-response kernels and adding realistic noise.
**Risk:** medium

## Idea 37: Wavelet-Leader Versus MFDFA Multifractal Spectra of Well Logs

**Category:** high-risk multifractal idea
**Research question / hypothesis:** Wavelet leaders provide more stable local multifractal spectra than MFDFA for finite, nonstationary well logs, especially at negative q and near heterogeneous intervals, provided the measure and scale range are defined explicitly.
**Contribution / method:** Define and compare positive measures based on transformed log values, absolute increments and wavelet-coefficient magnitudes. Estimate tau(q), alpha(q) and f(alpha) using wavelet leaders and MFDFA over justified q-ranges. Test wavelet family, leader dilation, detrending order, scale cutoffs and facies segmentation.
**Data:** Public multiwell gamma ray, density, neutron, sonic and resistivity logs; synthetic binomial cascades, multifractal random walks and piecewise monofractal controls with known spectra.
**Risk:** high

## Idea 38: Separating Genuine Multifractality from Facies Mixing and Tool Filtering

**Category:** high-risk multifractal idea
**Research question / hypothesis:** Much apparent multifractality in whole-well logs is caused by regime mixing, trends, heavy-tailed amplitudes or instrument filtering rather than a single multifractal geological process; facies-aware surrogate testing will quantify these contributions.
**Contribution / method:** Estimate multifractal spectra on whole wells, homogeneous windows and segmented intervals. Construct shuffled, phase-randomized, amplitude-adjusted and regime-preserving surrogates. Quantify spectrum width, asymmetry and curvature after controlling for finite length, missing data and tool-resolution cutoffs.
**Data:** Public multiwell logs with at least gamma ray and one complementary petrophysical curve; synthetic controls combining monofractal segments, boundary jumps, heavy-tailed noise and known tool filters.
**Risk:** high

## Idea 39: Linking Multifractal Heterogeneity to Porosity and Permeability Variability

**Category:** high-risk physics-linked idea
**Research question / hypothesis:** Multifractal spectrum width and asymmetry of log-derived or measured petrophysical sequences quantify heterogeneity that is related to the variance and scale dependence of porosity and permeability more effectively than a single Hurst exponent.
**Contribution / method:** Compute monofractal and multifractal descriptors for porosity, density, neutron-derived porosity and permeability where present. Relate spectrum width, alpha asymmetry, tau(q) curvature and scale-dependent variance to petrophysical heterogeneity. Use physically constrained regressions or hierarchical models rather than interpreting correlation as causation.
**Data:** Best case: public or local wells with log-derived porosity, core porosity and permeability, such as a dataset analogous to the carbonate-reservoir study in the source notes. Fallback: synthetic porosity/permeability fields generated with known multifractal or fBm covariance structures and sampled at well-log spacing.
**Risk:** high

## Idea 40: Scale-Dependent Fractal Indicators for Flow-Unit or Production-Zone Screening

**Category:** higher-risk reservoir-engineering idea
**Research question / hypothesis:** Combining local fractal persistence, multifractal spectrum features and conventional petrophysical variables can identify intervals with distinct flow-unit behavior better than conventional logs alone, but only when evaluated with leakage-controlled production or pressure data.
**Contribution / method:** Extract windowed H, spectral slope, variogram dimension, multifractal width and scale-dependent intermittency. Train a simple interpretable classifier or ordinal regression for flow-unit quality, with well-level splits and calibration. Couple predicted intervals to a 1-D flow simulation or upscaled permeability model to test engineering impact.
**Data:** Ideal dataset: multiple wells with GR, density, neutron, sonic, resistivity, interpreted flow units and production or pressure-test records. Public fallback: wells with facies labels and permeability/core measurements; otherwise use synthetic reservoir models with simulated logs and flow responses.
**Risk:** high
