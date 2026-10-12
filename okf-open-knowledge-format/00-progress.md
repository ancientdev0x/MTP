# Progress Log

## 2026-09-07
- Confirmed the project literature is stored in `Literature/`, not `/literature-review`.
- Inventoried 14 PDF sources.
- Applied the explicit scope restriction to read the book `fractals-in-reservoir-engineering.pdf` only through Chapter 4.
- Dispatched five parallel literature-reading agents; all completed and their reports were consolidated.
- Created detailed book notes, application-paper notes, theory notes, estimation-method notes, synthesis, research gaps, and bibliography.
- Generated 40 raw MTP ideas through five independent ideation agents.
- Independently screened all 40 ideas, identified duplicates, and saved the screening report.
- Ran five multi-round targeted novelty assessments on the strongest merged directions.
- Developed five detailed MTP research plans in parallel.
- Final recommendation saved in `12-final-mtp-recommendation.md`.

## Current status
- Literature reading: complete for assigned scope.
- Book reading: complete through Chapter 4 only; later chapters intentionally excluded.
- Idea generation: complete; 40 raw candidates archived.
- Idea screening: complete; duplicates and low-value repeats identified.
- Novelty assessment: complete at targeted-search level; claims remain cautious because this was not an exhaustive systematic review.
- Detailed planning: complete for five shortlisted directions.
- Recommended primary direction: artifact-aware stability benchmark for fractal features under sampling/filtering/tool perturbations.
- Recommended ambitious alternative: surrogate-controlled and segmentation-aware genuine-multifractality testing.
- Downloaded and verified the public FORCE 2020 dataset from Zenodo (MD5 verified); extracted 118 LAS wells and audited 2,337,639 rows.
- Confirmed common 0.152 m sampling and common availability of GR, RHOB, NPHI, DTC, RDEP, and lithology fields.
- Initial strict four-channel coverage rule leaves 10 wells with ≥80% valid samples; GR-only and channel-specific eligibility will be audited next.

## Pending before implementation
- Complete channel-specific eligibility and depth-span audit.
- Run a small GR pilot before freezing the final scope.
- Pilot executed successfully: 60 synthetic records and 354 real-GR condition records; all three estimators returned finite outputs.
- Pilot result: smoothing strongly shifted spectral H (real mean Δ +0.6104; MAE 0.6131), while variogram D and R/S-on-increments were less sensitive in this setup.
- Primary idea received a provisional **GO**; multifractal extension deferred until monofractal calibration and a well-log measure/surrogate pilot pass quality gates.
- Verify bibliographic metadata and OCR-damaged equations before formal thesis citation.
- Corrected fBm/fGn generator implemented in `pilot/experiment.py` using exact circulant-embedding covariance for stationary fGn increments and cumulative levels for fBm.
- Verification completed: `pilot/test_pilot.py` = 4 passed; bounded run artifacts written to `pilot/run_corrected/`.
- Corrected bounded run: synthetic gate passed for H={0.2,0.5,0.8} using variogram and spectral estimators; real robustness gate failed for the three deterministic GR windows, so the result is **NO-GO for stable single-H interpretation** and should be treated as an artifact/sensitivity finding, not a failure of the implementation.
