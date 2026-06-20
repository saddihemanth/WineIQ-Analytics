# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | ✅ Active           |
| 1.0.x   | ⚠️ Best-effort only |

## Reporting a Vulnerability

If you discover a security vulnerability in WineIQ Analytics, please **do
not** open a public issue. Instead, report it privately via the contact
listed in [`SUPPORT.md`](SUPPORT.md), or through GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)
feature on this repository.

Please include:

- A description of the vulnerability and its potential impact
- Steps to reproduce (proof of concept if possible)
- Any suggested remediation

You can expect an initial response within **5 business days**.

## Known Issues & Hardening Notes

This project started as a learning/portfolio project, so a few things are
worth calling out explicitly rather than hiding:

- **`config.yml` contains a plaintext demo password.** This file ships with
  `streamlit-authenticator` scaffolding that is **not currently wired into
  `app.py`** — the app has no live authentication layer today. If you enable
  authentication:
  - Never commit real credentials. `config.yml` is now in `.gitignore`;
    use `config.example.yml` as the template.
  - Hash passwords with `bcrypt` (via `streamlit-authenticator`'s `Hasher`)
    instead of storing them in plaintext.
  - Generate a long, random `cookie.key` per deployment and load secrets
    from environment variables or `st.secrets`, not from a committed file.
- **Model files (`models/*.pkl`) are loaded with `joblib.load`.** Only load
  `.pkl` files from sources you trust — pickle-based formats can execute
  arbitrary code on load. Don't accept user-uploaded model files without
  sandboxing.
- **`data/predictions.csv` accumulates user-submitted input.** It contains
  no personal data by default (only chemical feature values), but if you
  extend the form to collect personal information, treat that file as
  sensitive and exclude it from version control (already covered in
  `.gitignore`).
- **Dependencies** are pinned in `requirements.txt`. Run
  `pip list --outdated` periodically and update, especially `streamlit`,
  `scikit-learn`, and `reportlab`.

## Disclosure Policy

Once a reported vulnerability is confirmed, we aim to:

1. Acknowledge the report within 5 business days.
2. Release a fix or mitigation in a timely manner appropriate to severity.
3. Credit the reporter (if desired) in `CHANGELOG.md`.