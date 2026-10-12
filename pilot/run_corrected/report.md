# Bounded MTP pilot

NO-GO for stable single-H interpretation

Synthetic gate: True. Real robustness gate: False.

| Known H | Method | Mean bias | RMSE | Pass |
|---|---|---|---|---|
|0.2|variogram|-0.0135|0.0270|True|
|0.2|spectral|-0.0143|0.0653|True|
|0.5|variogram|-0.0199|0.0333|True|
|0.5|spectral|0.0051|0.0637|True|
|0.8|variogram|-0.0285|0.0463|True|
|0.8|spectral|0.0068|0.0637|True|

| Well | Baseline variogram H | Baseline spectral H | Largest absolute variant change | Pass |
|---|---|---|---|---|
|15_9-13|0.3867|-0.1087|0.0945|False|
|15_9-14|0.3382|0.1143|0.0944|False|
|15_9-15|0.3050|0.0163|0.0946|False|

## Limits and next step
FORCE is already cleaned/despiked: baseline means supplied GR, not raw-tool truth. No geological accuracy, lithology prediction or graph-dimension claims. Gaussian nonstationary fBm levels have stationary fGn increments; real GR is not established to follow either model.
Four seeds per known H and three deterministically selected intervals are a sanity check, not a population study. Welch frequency ordinates and variogram lags are dependent; regression R² is descriptive, not a confidence interval or proof of scaling. Spectral H uses the low-frequency fGn asymptote after differencing, with possible finite-frequency/discretization bias.
Intervals may cross geological regimes. Nominal uniform spacing accepts LAS rounding within 0.0005 m; actual extrema are in the manifest. Smoothing and resampling measure processing sensitivity, not restoration or ground-truth error.
If NO-GO: investigate stationarity, scale dependence and estimator disagreement before any geological or fractal interpretation. If GO: only expand controlled validation, not a full MTP build. No thresholds or seeds were tuned after results.
