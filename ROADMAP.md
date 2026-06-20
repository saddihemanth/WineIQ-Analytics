# Roadmap

This roadmap tracks where WineIQ Analytics is headed. Items are loosely
ordered by priority within each milestone — not promises of exact dates.

## ✅ v2.0 — Premium UI & Portfolio Polish (current)

- [x] Full visual redesign (wine-cellar dark theme, custom CSS)
- [x] Custom animated metric/KPI cards
- [x] Themed Plotly chart library
- [x] Redesigned sidebar navigation
- [x] Session-state-safe prediction → PDF report flow
- [x] Fixed prediction-history path bug
- [x] Professional README, governance docs, MIT license

## 🚧 v2.1 — Explainability & Data Quality

- [ ] Wire up real SHAP values (`components/explainability.py`) into the
      Explainability page instead of the current illustrative static table
- [ ] Add per-prediction SHAP waterfall/force plot to the Prediction page
- [ ] Input validation (realistic ranges/units) with inline guidance for
      each chemical attribute
- [ ] Data quality report (missing values, outliers, class balance) on the
      Analytics page

## 🔭 v2.2 — Authentication & Multi-User

- [ ] Properly wire `streamlit-authenticator` using hashed passwords and
      environment-based secrets (see `SECURITY.md`)
- [ ] Per-user prediction history instead of a single shared CSV
- [ ] Role-based access (admin vs. viewer)

## 🧪 v2.3 — Model Improvements

- [ ] Hyperparameter tuning (GridSearch/Optuna) tracked via MLflow or a
      simple experiment log
- [ ] Support for red **and** white wine datasets with a model selector
- [ ] Confidence scores / predicted probability alongside the class label
- [ ] Model versioning (store metadata: training date, dataset hash,
      metrics) alongside `model.pkl`

## 🚀 v3.0 — Deployment & Ops

- [ ] CI: add automated tests (see `tests/`) to `.github/workflows`
      alongside the existing training job
- [ ] Dockerfile for containerized deployment
- [ ] One-click deploy guide for Streamlit Community Cloud, Render, and
      Hugging Face Spaces
- [ ] Basic usage analytics (predictions per day, popular feature ranges)

## 💡 Ideas Under Consideration

- Batch prediction via CSV upload
- REST API wrapper (FastAPI) around the trained model
- Comparative "what changed" view between two predictions
- Internationalization (i18n) for the UI

---

Have a suggestion? Open an issue — see [CONTRIBUTING.md](CONTRIBUTING.md).