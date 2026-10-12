MTP mid-semester submission review

Review date: 23 September 2026
Reviewed artifact: research_report/main.tex and generated research_report/main.pdf
Scope: decide whether the current work is suitable to send to the MTP guide as a mid-semester progress submission.

Verdict

CONDITIONALLY SUBMITTABLE as a mid-semester progress report, not as a final MTP/thesis result.

The work is technically credible as a bounded methodological pilot: the corrected fBm/fGn generator is implemented, the declared tests pass, the synthetic gate passes, and the real-data result is honestly reported as a narrow NO-GO for stable single-H interpretation. The report is appropriately cautious and does not overclaim geological meaning.

What was verified

- pilot/test_pilot.py: 4 passed in 2.37 s with pytest -q.
- LaTeX compilation: successful with pdflatex + BibTeX; generated main.pdf is 7 pages.
- No LaTeX Warning/undefined/Overfull messages were found in the final log.
- The rendered first page was visually inspected: no clipping or broken layout; body text is readable.
- Corrected pilot outputs exist under pilot/run_corrected/.
- Reported executed result is internally coherent: 12 synthetic records (3 H values x 4 seeds), 3 selected real intervals, synthetic gate=True, real robustness gate=False, decision=NO-GO for stable single-H interpretation.
- The current main.pdf is newer than research_report.pdf. They have different hashes; submit main.pdf or copy the freshly compiled file to the intended submission filename. Do not submit the stale research_report.pdf without replacing it.

Strong points

1. The report clearly separates known-answer synthetic validation from descriptive real-log sensitivity.
2. The fGn covariance, cumulative fBm-like levels, estimator conventions, physical-scale perturbations, deterministic selection, and rejection/no-go logic are documented.
3. Limitations are explicit: four seeds per H, three real intervals, processed FORCE data, generic smoothing, possible regime mixing, and no geological/petrophysical claims.
4. The negative real-data result is framed correctly: it rejects an unqualified stable single-H interpretation for the tested intervals, rather than rejecting the whole research direction.
5. The report includes source code, tests, prespecification, JSON outputs, selection manifest, figures, and generated pilot summary.

Before sending to the guide (recommended minimum edits)

P0 — must fix

- Replace the stale submission PDF: use the freshly compiled research_report/main.pdf. The similarly named research_report/research_report.pdf predates the current compilation and has a different SHA-256 hash.
- Add author name, roll number, department/programme, guide name, institute, and a short submission label if the guide expects an identifiable report. The current author line is only “Master's Thesis Project (MTP)”.
- Add a dataset citation and URL/DOI for FORCE 2020/Zenodo. The report currently says the dataset was downloaded and verified but does not provide a formal dataset reference in the bibliography.

P1 — strongly recommended

- Add a one-paragraph “Progress against objectives” or “Work completed” section with concrete deliverables: literature synthesis, dataset audit, corrected generator, tests, prespecified pilot, executed outputs.
- Add a compact “Plan for the next phase” table with deliverable, method, and target timing. At minimum: >=30 synthetic realizations per H; uncertainty/paired variability reporting; stationarity/scale diagnostics; predetermined multi-window real-data selection; geological/context annotations; frozen passbands; then optional multifractal extension.
- State explicitly that the current pilot is not sufficient to claim general behavior across FORCE wells. This is already implied by the limitations, but making it a standalone sentence will prevent misreading.
- Include the actual source repository/project path or package snapshot instructions. Absolute local filesystem paths in the artifact index are not useful to a guide receiving only the PDF.
- Add one sentence describing what feedback/decision is requested from the guide, e.g. approval of the artifact-aware benchmark scope and the proposed next-stage validation protocol.

P2 — quality improvements

- Verify the bibliographic metadata and replace “n.d.”/“and others” for the reservoir-fractals book if complete metadata is available. The project progress log itself flags this as pending.
- Cite the FORCE 2020 dataset directly and distinguish the dataset paper/repository from application papers.
- Consider reporting fit R^2 and actual physical fit ranges in the main result table or appendix; the current report mentions these but does not show them.
- Consider adding a short table of selected intervals with source path, depth range, sample count, and SHA-256 prefix, while keeping the full manifest as an artifact.
- The title line is visually dense but acceptable; a line break between “Progress Report” and the study title would improve presentation.

What not to claim to the guide

- Do not call the pilot a validated geological fractal measurement.
- Do not claim the three intervals represent the FORCE population or that one estimator is superior.
- Do not present the NO-GO as failure of the MTP; it is a bounded result motivating calibration and scale/stationarity work.
- Do not add multifractal conclusions yet; the existing project notes correctly defer that extension.

Suggested submission package

1. Freshly compiled PDF (main.pdf renamed clearly, e.g. MTP_mid_semester_progress_report.pdf).
2. One-page note/email summarizing the verdict and requested guide feedback.
3. Optional supplementary ZIP containing pilot source, PRESPEC.md, tests, JSON outputs, figures, and selection manifest.
4. Dataset provenance/citation note; do not redistribute the dataset if its license/size makes that inappropriate.

Bottom line

Yes, sendable after the P0 fixes above. It is strong enough to demonstrate serious progress and a defensible preliminary result, but it should be presented explicitly as a methodological progress report and bounded pilot—not as a completed thesis contribution.
