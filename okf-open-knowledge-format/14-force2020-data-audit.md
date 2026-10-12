# FORCE 2020 Dataset Audit

## Source
- Zenodo record: https://zenodo.org/records/4351156
- DOI: 10.5281/zenodo.4351156
- Downloaded archive: `data/force2020/FORCE2020_all_wells.zip`
- Official MD5: `da0d72d5783a780ac71779453d9fbfbf`
- Verified local MD5: `da0d72d5783a780ac71779453d9fbfbf`

## Local audit results
- LAS wells extracted: **118**
- Total data rows: **2,337,639**
- Common sampling step observed: **0.152 m**
- Curves present in every LAS file: `CALI`, `DEPT`, `DEPTH_MD`, `DTC`, `FORCE_2020_LITHOFACIES_CONFIDENCE`, `FORCE_2020_LITHOFACIES_LITHOLOGY`, `GR`, `NPHI`, `RDEP`, `RHOB`, `x_loc`, `y_loc`, `z_loc`
- Frequently useful channels confirmed: GR, RHOB, NPHI, DTC, RDEP, lithology, lithology-confidence.
- Wells with GR, RHOB, NPHI, and DTC each at ≥80% valid samples: **10** under the initial audit rule.

## Implications
- The dataset is suitable for the recommended stability benchmark and for a cautious held-out-well demonstration.
- The 0.152 m regular step supports controlled downsampling and smoothing experiments.
- All 118 wells contain lithology fields, but valid log coverage varies; eligibility must be determined per channel and per interval, not from well count alone.
- A primary GR-only pilot is likely to retain more wells than a four-channel pilot.
- The lithology field enables a secondary classification/generalization analysis, but that should not replace the primary reliability study.

## Next data steps
1. Quantify valid coverage and depth span per curve and per well.
2. Select a reproducible subset using explicit minimum-length and missingness criteria.
3. Build synthetic fBm/fGn and multifractal controls first.
4. Run the estimator stability pilot on GR, then replicate on one complementary channel.
5. Keep lithology labels for optional blind-well validation, while avoiding leakage from labels into feature extraction.
