# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [2.0.0] — 2026-06-20

### Added
- Complete visual redesign — "Cellar at Midnight" theme (deep bordeaux +
  aged gold on near-black), with Playfair Display / Inter typography.
- Custom animated KPI/metric cards (`MetricsCard.render_grid`) replacing
  bare `st.metric` calls on the Dashboard and History pages.
- New `ChartBuilder.alcohol_vs_quality` chart for dashboard variety.
- SVG brand assets: `assets/banner.svg`, `assets/logo.svg`.
- `load_history()` helper in `components/history.py` with safe empty-state
  handling.
- `config.example.yml` as a safe template for `streamlit-authenticator`
  configuration.
- Project governance docs: `CODE_OF_CONDUCT.md`, `SUPPORT.md`,
  `ROADMAP.md`, this `CHANGELOG.md`.
- `SECURITY.md` with an explicit, honest note about the demo credentials
  in `config.yml`.

### Changed
- Sidebar rewritten with a brand crest, icon-labelled navigation, and an
  info card; styled via CSS into a pill-style nav instead of a plain radio
  list.
- All Plotly charts now share a single themed layout (transparent
  background, brand color scale, consistent fonts) via `ChartBuilder`.
- `requirements.txt` now includes `reportlab` (previously used by
  `report_generator.py` but missing from the dependency list) and pins
  versions consistently.
- `.gitignore` populated (was previously empty) — excludes
  `__pycache__/`, virtual envs, `data/predictions.csv`, generated PDF
  reports, and `config.yml`.
- README fully rewritten with badges, architecture/ML-pipeline diagrams,
  and a recruiter-oriented structure.

### Fixed
- **Prediction history file path** (`components/history.py`) — previously
  used a bare relative path (`"data/predictions.csv"`) that broke when the
  app was launched from a different working directory; now resolved
  relative to the file's own location, matching the pattern already used
  for the model/scaler paths.
- **PDF report button losing state on rerun** (`prediction_page`) — the
  "Generate PDF Report" button was nested inside the same conditional as
  the "Predict" button, so clicking it triggered a rerun that hid the
  prediction results. Prediction output is now stored in
  `st.session_state`, so results and the PDF flow persist correctly.
- **Broken inline import** — `from app.components.report_generator import
  generate_pdf` inside `prediction_page` (using an incorrect `app.`
  prefix) removed in favor of the top-level import.
- **Duplicate chart on Dashboard** — the quality-distribution histogram
  was rendered twice; the second occurrence is now a distinct
  alcohol-vs-quality chart.
- **Low-contrast button text** — `.stButton button` previously set an
  orange/brown text color (`rgb(204, 94, 9)`) against a purple-pink
  gradient; replaced with a themed, accessible-contrast button style.
- **Malformed `data/predictions.csv` header** — a missing newline between
  the header row and the first data row caused `Timestamp` and the first
  record to merge into a single cell; `save_prediction` now writes the
  header safely and only once.

## [1.0.0] — Initial Release

### Added
- Streamlit dashboard with Dataset Overview, Prediction, Analytics, Model
  Insights, Explainability, and About pages.
- Random Forest wine-quality classifier (plus Logistic Regression, KNN,
  and Decision Tree comparisons) trained via `train.py`.
- Plotly-based quality distribution, correlation heatmap, feature
  importance, and model comparison charts.
- PDF report generation via ReportLab.
- Basic dark-themed custom CSS and prediction history logging.