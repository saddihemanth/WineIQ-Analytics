# Contributing to WineIQ Analytics

First off, thank you for considering contributing to WineIQ Analytics 🍷 —
whether that's a bug report, a new feature, a doc fix, or a UI polish pass,
all contributions are welcome.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Commit Message Convention](#commit-message-convention)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By
participating, you agree to uphold it.

## Getting Started

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/WineIQ-Analytics.git
   cd WineIQ-Analytics
   ```

2. **Create a virtual environment** and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Train the model** (generates `models/model.pkl` and `models/scaler.pkl`):

   ```bash
   python train.py
   ```

4. **Run the app locally**:

   ```bash
   streamlit run app/app.py
   ```

## Project Structure

```
WineIQ-Analytics/
├── app/                # Streamlit application
│   ├── app.py          # Page routing & layout
│   ├── assets/         # styles.css
│   └── components/     # Sidebar, charts, metrics, history, PDF report
├── data/                # Dataset + generated prediction history
├── models/              # Serialized model.pkl / scaler.pkl
├── notebooks/           # Exploratory analysis
├── train.py              # Model training pipeline
└── requirements.txt
```

## Development Workflow

1. Create a feature branch off `main`:

   ```bash
   git checkout -b feature/short-description
   ```

2. Make your changes, keeping commits focused and atomic.
3. Test the app manually (`streamlit run app/app.py`) and confirm:
   - All seven pages load without errors
   - Predictions still run end-to-end
   - No console warnings introduced by CSS/HTML changes
4. Push your branch and open a pull request against `main`.

## Coding Standards

- **Python**: follow [PEP 8](https://peps.python.org/pep-0008/). Prefer
  descriptive names over abbreviations (`feature_importance`, not `fi`).
- **Streamlit components**: keep page-rendering functions in `app/app.py`
  thin — push reusable UI/logic into `app/components/`.
- **CSS**: add new rules to `app/assets/styles.css` using the existing
  CSS variables (`--wine-*`, `--gold-*`, `--cream-*`) instead of hard-coded
  hex values, so the theme stays consistent.
- **Charts**: build new visuals through `ChartBuilder` in
  `app/components/charts.py` so they inherit the shared dark theme.

## Commit Message Convention

This project loosely follows [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add SHAP-based explainability tab
fix: correct prediction history file path
docs: update installation instructions
style: refine sidebar hover states
refactor: extract metric card grid renderer
```

## Submitting a Pull Request

- Reference any related issue (`Closes #12`).
- Describe **what** changed and **why**.
- Include a screenshot or short GIF for UI changes.
- Make sure `python train.py` and `streamlit run app/app.py` both run cleanly.

## Reporting Bugs

Open an issue with:

- A clear, descriptive title
- Steps to reproduce
- Expected vs. actual behavior
- Screenshots/console output if relevant
- Your environment (OS, Python version, browser)

## Suggesting Enhancements

Open an issue describing the use case, the proposed behavior, and (if
possible) a rough mockup or reference. Check `ROADMAP.md` first to see if
it's already planned.

---

Thanks again for helping make WineIQ Analytics better! 🍷