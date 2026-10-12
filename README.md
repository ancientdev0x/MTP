# Artifact-Aware Stability Benchmark for Fractal Attributes in Well-Log Characterization (MTP)

**Master's Thesis Project (MTP)**  
**Author:** Priyanshu Gupta (`ancientdev0x`)  
**Domain:** Computational Geophysics / Well-Log Analysis / Fractal & Time-Series Modeling  

---

## 📌 Executive Summary

Fractal analysis and Hurst exponent ($H$) estimation are widely proposed in literature for lithofacies classification, reservoir heterogeneity mapping, and scale-invariance characterization in wireline logs. However, common workflows assume that estimated fractal dimensions represent intrinsic reservoir rock properties without first validating their mathematical stationarity or assessing sensitivity to standard log preprocessing operations (such as tool filtering, boxcar smoothing, and decimation).

This project establishes a reproducible, artifact-aware benchmark to test the hypothesis:
> *Are fractal attributes derived from wireline logs stable intrinsic features, or are they fragile artifacts of measurement scale, smoothing, and estimator choice?*

### 🔬 Key Findings to Date
1. **Synthetic Controlled Benchmark (fBm/fGn):** **PASSED**  
   Using an exact circulant-embedding generator (Davies-Harte), synthetic Fractional Gaussian Noise (fGn) increments and cumulative Fractional Brownian Motion (fBm) series with known $H \in \{0.2, 0.5, 0.8\}$ were recovered within strict error tolerances by both Power Spectral Density (PSD) and Variogram estimators.
2. **Real Well-Log Robustness Gate (FORCE 2020):** **NO-GO for Unqualified Single-$H$ Interpretation**  
   Evaluated on deterministic Gamma Ray (GR) intervals across 3 North Sea wells (`15/9-13`, `15/9-14`, `15/9-15`). Mild 5-point boxcar smoothing caused massive upward bias in spectral $H$ (mean shift $\Delta \approx +0.61$, MAE $\approx 0.613$), while the variogram was less sensitive.  
   **Conclusion:** The pilot rejects an unqualified single-$H$ interpretation on real logs. Fractal attributes are strongly estimator- and filter-dependent. This is a crucial methodological insight, not an experimental failure.

---

## 📂 Repository Structure

```
MTP/
├── README.md                      # This project guide & reproduction manual
├── CLAUDE.md                      # Context & operational rules for Claude Code
├── PROJECT_STATE.md               # In-depth technical status, theory & pilot numbers
├── PROMPT_FOR_ME.md               # Claude prompt tailored for Priyanshu
├── PROMPT_FOR_FRIEND.md           # Step-by-step Claude prompt tailored for your friend
├── MTP_SUBMISSION_REVIEW.md       # Mid-semester progress review & P0/P1 fixes
├── IDEA.md                        # Original project inception note
├── requirements.txt               # Python dependencies
│
├── pilot/                         # Core Python implementation & test suite
│   ├── experiment.py              # Exact fBm/fGn generator, PSD & variogram estimators, filtering controls
│   ├── plot.py                    # Publication-grade plotting scripts
│   ├── test_pilot.py              # Test suite (4 automated tests covering exact generator & controls)
│   ├── PRESPEC.md                 # Pre-registration of evaluation gates & tolerances
│   └── run_corrected/             # Output artifacts (Figure_1, Figure_2, final_info.json, report.md)
│
├── pilot_results/                 # Metric summaries & JSON run manifests
│   ├── pilot_metrics.json
│   ├── pilot_results.json
│   └── pilot_summary.json
│
├── data/
│   ├── sample_wells/              # 3 LAS wells used for the deterministic pilot (15_9-13, 14, 15)
│   └── force2020/                 # Download target for full 118-well FORCE 2020 Zenodo dataset
│
├── scripts/
│   └── download_force2020.py      # Automated Zenodo fetcher & MD5 integrity checker
│
├── okf-open-knowledge-format/     # 16-module literature synthesis, idea bank & audit reports
│   ├── 00-progress.md             # Chronological project progress log
│   ├── 01-source-inventory.md     # Inventory of 14 literature papers + textbooks
│   ├── 02-book-chapters-1-4.md    # Summary of Sahimi (Reservoir Engineering Fractals) Ch. 1-4
│   ├── 03-well-log-and-reservoir-papers.md
│   ├── 04-foundational-fractal-theory.md
│   ├── 05-estimation-methods.md
│   ├── 06-synthesis-and-research-gaps.md
│   ├── 08-idea-bank-raw.md        # 40 raw brainstormed research directions
│   ├── 09-idea-screening.md       # Rigorous screening & elimination matrix
│   ├── 10-novelty-assessments.md   # Prior art novelty check
│   ├── 11-shortlisted-research-plans.md
│   ├── 12-final-mtp-recommendation.md
│   ├── 13-force2020-data-audit.json # 118 wells / 2.34M rows audited
│   ├── 14-force2020-data-audit.md
│   ├── 15-pilot-method-review.md
│   └── 15-pilot-results.md
│
├── research_report/               # 7-page IEEE/ACM-style LaTeX research report
│   ├── main.tex                   # Source document
│   ├── main.pdf                   # Compiled PDF report
│   └── references.bib             # BibTeX citations
│
├── research_presentation/         # 15-slide Beamer presentation deck
│   ├── main.tex                   # Source presentation
│   └── main.pdf                   # Compiled slide deck
│
├── defense_prep/                  # Comprehensive viva & defense mastery resources
│   ├── MTP_simple_english_guide.tex # Simple English guide for non-native / clear explanations
│   ├── MTP_simple_english_guide_complete.pdf # 28-page complete mastery pack + source extracts
│   ├── MTP_mastery_pack.tex       # Complete technical defense Q&A
│   └── selected_literature_pages.pdf # Key paper excerpts for direct citation
│
└── Literature/                    # 14 original academic papers & book extracts (with OCR markdown)
```

---

## 🚀 Quickstart & Reproduction

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/ancientdev0x/MTP.git
cd MTP

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Verification Tests
```bash
cd pilot
pytest -q test_pilot.py
# Expected output: 4 passed in ~2.3s
cd ..
```

### 3. Re-run Pilot Experiments & Generate Figures
```bash
cd pilot
python experiment.py
python plot.py
# Outputs are generated in pilot/run_corrected/
cd ..
```

### 4. Compile LaTeX Documents (Optional)
Requires `texlive` / `pdflatex`:
```bash
# Compile research report
cd research_report
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
cd ..

# Compile Beamer presentation
cd research_presentation
pdflatex main.tex && pdflatex main.tex
cd ..
```

---

## 🎯 Next Steps / Research Roadmap

1. **Monte Carlo Expansion:** Increase synthetic runs from 4 seeds to $\ge 30$ realizations per $H \in \{0.2, 0.5, 0.8\}$ to report confidence intervals.
2. **Physical Scale Diagnostics:** Implement windowed stationarity tests to detect regime mixing across lithological boundaries (sand-shale transitions).
3. **Fixed Passband Filtering:** Test bandpass filters rather than naive lowpass smoothing to isolate genuine scale-invariant octaves.
4. **Multi-Well Scale Test:** Run the benchmark across all 10 high-coverage wells identified in the FORCE 2020 audit.
5. **Mid-Semester Submission Polish:** Add student details, supervisor attribution, and formal Zenodo citation to `research_report/main.tex`.
