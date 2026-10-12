# Bounded pilot — prespecified before execution

Scope: no full MTP, no geological accuracy claims. FORCE is already cleaned/despiked, not raw-tool truth.

Synthetic: stationary Gaussian fGn with covariance r(k)=((k+1)^(2H)-2k^(2H)+|k-1|^(2H))/2 via PSD-checked exact circulant embedding; cumulative sum yields nonstationary fBm levels. H={0.2,0.5,0.8}, seeds={11,22,33,44}, 8192 increments each. Variogram on levels: slope/2. Spectral estimator on first differences of levels: H=(1-slope)/2, a low-frequency fGn approximation; never apply the fBm level formula to increments. Fit wavelengths/lags 20–160 synthetic samples. Welch Hann, 2048-sample segments (physical equivalent for variants), 50% overlap, constant detrending. No clipping H.

Synthetic gate: for each H and each estimator, absolute mean bias <=0.12 and RMSE <=0.18 across four seeds. Not a comprehensive estimator validation. Tests cover covariance reconstruction, Brownian covariance, exact cumulative increments, gap segmentation, uniform spacing, scale grids, anti-alias suppression, invalid short/constant data, and saved artifacts.

Real selection: sorted relative LAS paths; first three eligible wells, longest contiguous finite GR block (earliest tie), first 4097 points. Split at invalid depth/GR, nonpositive spacing, or spacing deviating from declared STEP by >0.0005 m (LAS decimal rounding tolerance). Require metre depth unit and at least 4097 points. Record rejected wells/reasons. Never join blocks or interpolate gaps.

Variants: baseline; Gaussian smoothing sigma=0.304 m; polyphase anti-aliased downsample by 2 and 4 (SciPy resample_poly Kaiser 5, line padding). Trim 40 native points at each end on all variants to remove filter boundaries. Same depth endpoints and physical lags: native multiples of 4 within 3.04–24.32 m (real STEP determines actual retained grid, recorded). Spectral fixed frequency band 1/24.32–1/3.04 cycles/m and segment physical length 311.296 m. Require >=512 variant points, >=20 lags, >=100 pairs at largest lag, >=20 in-band spectral bins and >=2 Welch segments. Nyquist must exceed band maximum. Report actual scales and fit R², not infer scaling from R² alone.

Real robustness gate (descriptive, no uncertainty guarantee): all absolute H changes from baseline <=0.10 per method/variant/well AND baseline estimator differences <=0.15. Failure means NO-GO for interpreting a stable single H on these intervals, not failure of the underlying science. Proceed to broader research only if synthetic gate and real robustness gate pass. Save all failures; do not tune thresholds/seeds/scales after results.

Figures: Figure_1 estimates versus known H with individual seeds and mean; Figure_2 real H change relative to baseline per variant with +/-0.10 guides. PNG 300 dpi plus vector PDF; colorblind-safe palette, >=8pt labels. Record commands, dependency freeze, source hashes, arrays, manifest, JSON, logs and cautious report.
