# PROMPT_FOR_FRIEND.md — Quickstart Guide & Prompt for Your Friend

> **Hey! Thanks for helping Priyanshu out with your laptop.**  
> Everything is pre-configured and reproducible. Follow the 3-step setup below, and then copy-paste the prompt into Claude so it can run autonomously without you having to figure out the math or geophysics!

---

## 🛠️ Step 1: Clone & Setup Environment (Terminal)

Open a Terminal on your laptop and run these commands:

```bash
# 1. Clone the repository
git clone https://github.com/ancientdev0x/MTP.git
cd MTP

# 2. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
# (On Windows PowerShell: .venv\Scripts\Activate.ps1)

# 3. Install required packages
pip install -r requirements.txt

# 4. Verify everything works (Runs the test suite)
cd pilot
pytest -q test_pilot.py
cd ..
# You should see: 4 passed in ~2.3 seconds!
```

---

## 🤖 Step 2: Copy-Paste Prompt for Claude

If you are using **Claude Code CLI** in terminal (`claude`), or using **Claude Chat in your browser (claude.ai)**, simply copy and paste the prompt below:

```markdown
Hi Claude! I am running this session on my laptop for my friend Priyanshu Gupta (`ancientdev0x`).
We have cloned his Master's Thesis Project (MTP) repository: https://github.com/ancientdev0x/MTP

### What This Project Is About
It is a computational geophysics thesis titled:
"Artifact-Aware Stability Benchmark for Fractal Attributes in Well-Log Characterization"

Priyanshu has already implemented:
1. Exact Davies-Harte circulant embedding synthetic generator (`fBm`/`fGn`) with unit tests in `pilot/test_pilot.py` (all passing).
2. Synthetic benchmark (PASSED): Correctly recovers Hurst exponent H for {0.2, 0.5, 0.8}.
3. Real well-log pilot on FORCE 2020 Gamma Ray logs (NO-GO for stable single-H): Proved that mild boxcar smoothing shifts spectral H by +0.61, meaning fractal features are sensitive to filtering artifacts rather than being rock properties.
4. Compiled artifacts:
   - 7-page LaTeX paper: `research_report/main.pdf`
   - 15-slide presentation: `research_presentation/main.pdf`
   - 28-page study guide: `defense_prep/MTP_simple_english_guide_complete.pdf`

### Your Instructions as Claude
- All context is documented in `CLAUDE.md`, `README.md`, and `PROJECT_STATE.md`.
- I might not be a geophysics expert myself, so please keep your explanations clear, actionable, and state exactly what commands or code you are modifying.
- If you need to run experiments, use the virtual environment (`source .venv/bin/activate`) and run inside `pilot/`.
- Priyanshu will tell me what specific task to run (like running more simulations, editing the LaTeX report, or checking code).

Please read the repo files and let me know you are ready to assist!
```

---

## 📋 Helpful Troubleshooting & Quick Commands

- **To run the experiment and regenerate figures:**
  ```bash
  cd pilot
  python experiment.py
  python plot.py
  # Figures are saved to pilot/run_corrected/Figure_1.pdf and Figure_2.pdf
  ```

- **To view existing PDFs:**
  - Research Report: `research_report/main.pdf`
  - Slide Presentation: `research_presentation/main.pdf`
  - Simple Defense Guide: `defense_prep/MTP_simple_english_guide_complete.pdf`
