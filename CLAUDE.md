# CLAUDE.md — Agent Operating Context & Research Guidelines

> **Target Agent:** Claude Code / Claude 3.5 / Claude 3.7 / Anthropic Assistant  
> **Project:** Master's Thesis Project (MTP) — Computational Geophysics  
> **Repository:** `ancientdev0x/MTP`  
> **Maintainer:** Priyanshu Gupta  

---

## 1. Project Mission & Core Scientific Stance

This project investigates the stability and reproducibility of fractal features (Hurst exponent $H$, fractal dimension $D$) extracted from geophysical wireline well logs (FORCE 2020 dataset).

### ⚠️ Non-Negotiable Scientific Principles
1. **Never Assume $H$ Represents a Physical Reservoir Property:**  
   Always test whether the estimate is an artifact of preprocessing (filtering, smoothing, sampling interval) before drawing petrophysical conclusions.
2. **Negative / Robustness Results are Legitimate Contributions:**  
   Our real-data pilot demonstrated that mild 5-point boxcar smoothing causes a severe upward shift in spectral $H$ ($\Delta \approx +0.61$). The decision is **NO-GO for stable single-$H$ interpretation**.  
   *DO NOT* attempt to alter data or filters to artificially force a "pass". The instability of $H$ across preprocessing operations *is* our key scientific finding.
3. **Monofractal Calibration Before Multifractal Claims:**  
   Do not introduce multifractal spectrum ($f(\alpha)$) analysis until monofractal estimators are proven stable across physical scales.

---

## 2. Key Commands & Execution

### Environment Activation
```bash
# Always ensure virtualenv is activated
source .venv/bin/activate
# or python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

### Running Tests
```bash
cd pilot
pytest -q test_pilot.py
# Must return: 4 passed
```

### Running Experiment & Plot Generation
```bash
cd pilot
python experiment.py       # Runs synthetic + real-well analysis, saves npz and final_info.json
python plot.py             # Generates Figure_1.pdf/png (synthetic) & Figure_2.pdf/png (real data)
```

### Compiling LaTeX Documents
```bash
# 7-page Research Report:
cd research_report && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# 15-slide Presentation:
cd research_presentation && pdflatex main.tex && pdflatex main.tex

# 28-page Defense Guide:
cd defense_prep && pdflatex MTP_simple_english_guide.tex
```

---

## 3. Architecture & Repository Map

- `pilot/experiment.py`:
  - `fgn_circulant(n, H, seed)`: Exact Davies-Harte method using FFT on embedded covariance.
  - `fbm_from_fgn(fgn)`: Cumulative sum of stationary fGn increments.
  - `spectral_estimator(series, dx)`: Power Spectral Density slope $\beta$, converts via $\beta = 2H + 1$ (for fBm) or $\beta = 2H - 1$ (for fGn).
  - `variogram_estimator(series, dx, max_lag)`: Semivariance slope in log-log space ($\gamma(h) \propto h^{2H}$).
  - `boxcar_filter(series, window=5)`: Moving-average smoothing used as artifact perturbation.
  - `run_pilot()`: Evaluates gates on synthetic and real intervals.
- `pilot/test_pilot.py`:
  - `test_exact_generator`: Validates fGn autocovariance decay.
  - `test_estimation_and_controls`: Validates estimator recovery.
  - `test_contiguous_variants`: Validates NaN handling and contiguous slicing.
  - `test_bounded_run_artifacts`: Verifies output file generation.
- `data/sample_wells/`:
  - Contains three LAS 2.0 files from North Sea FORCE 2020: `15_9-13.las`, `15_9-14.las`, `15_9-15.las`.
- `okf-open-knowledge-format/`:
  - 16 exhaustive markdown files covering literature analysis, 40 brainstormed ideas, novelty screening, and data audit.

---

## 4. Current Work State & Immediate Next Tasks

### Phase 1: Completed ✅
- [x] Literature review (14 papers + Sahimi textbook Ch 1-4).
- [x] FORCE 2020 dataset audit (118 wells, 2.34M rows).
- [x] Exact fBm/fGn generator + unit tests (4/4 passing).
- [x] Prespecified pilot run completed (Synthetic PASS, Real Robustness NO-GO).
- [x] 7-page LaTeX paper compiled (`research_report/main.pdf`).
- [x] 15-slide Beamer presentation compiled (`research_presentation/main.pdf`).
- [x] Comprehensive defense study guide compiled (`defense_prep/MTP_simple_english_guide_complete.pdf`).

### Phase 2: In Progress / Next Up ⏳
1. **P0 Submission Details (`research_report/main.tex`):**
   - Fill in Student Name: Priyanshu Gupta, Roll No, Department, Guide Name, Institute.
   - Add formal Zenodo citation for FORCE 2020.
2. **Monte Carlo Expansion:**
   - Expand synthetic validation from 4 seeds to 30+ realizations per $H \in \{0.2, 0.5, 0.8\}$ to generate 95% confidence intervals and formal p-values.
3. **Stationarity & Scale Diagnostics:**
   - Implement Augmented Dickey-Fuller (ADF) and KPSS tests on real well segments to verify second-order stationarity before computing variograms.
   - Investigate lithology-stratified windows (sandstone vs. shale).
4. **Multi-Well Validation:**
   - Extend the pilot beyond the 3 sample wells to the top 10 continuous wells in FORCE 2020.

---

## 5. Defense & Professor Interaction Guidelines

When helping Priyanshu prepare explanations, defense arguments, or thesis text:
- **Tone:** Clear, mathematically grounded, intellectually honest.
- **Handling the "Negative Result":**  
  If asked *"Why did your real log pilot fail?"*, respond:  
  *"The code did not fail—the synthetic gate passed perfectly. Rather, the real-world data violated the assumption of stationary single-scale self-affinity. The Hurst exponent changed by +0.61 merely from 5-point smoothing. This proves that published papers attributing physical meaning to unvalidated H values are prone to reporting measurement artifacts."*
- **Avoid Hype:** Never claim that fractal dimensions can replace conventional petrophysical workflows (porosity, permeability, saturation). Frame fractals strictly as a diagnostic tool for spatial correlation and multiscale heterogeneity.
