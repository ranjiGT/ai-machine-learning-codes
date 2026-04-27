# Changelog

All notable changes to this repository are listed here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

---

## [1.4.0] — 2026-04-27

### Added
- **Topic 117** — Stream-Based & Adaptive Learning: Gama's adaptive learning definition, sufficient statistics on streams, recursive mean (Welford), ADWIN drift detection, online learning with `SGDClassifier.partial_fit`, Hoeffding Tree bound, and prequential evaluation.

---

## [1.3.0] — 2026-04-26

### Added
- **Topic 115** — End-to-End Real-World ML Project: Heart Disease Prediction capstone notebook covering EDA, preprocessing, PCA, SMOTE, multi-model benchmarking, hyperparameter tuning, ROC-AUC, and feature importance.
- `imbalanced-learn==0.12.4` added to `requirements.txt`.
- `nbstripout` added to `requirements.txt` and installed as a git filter — notebook outputs are now stripped automatically on every commit.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) — executes changed notebooks on every push/PR and uploads failed notebooks as artifacts.
- Binder URL validation script (`src/utils/check_binder_urls.py`).
- Difficulty tags (`🟢` / `🟡` / `🔴`) and prerequisite notes added to each README section.
- First-Time Setup section added to `CONTRIBUTING.md`.

### Fixed
- Replaced `fetch_openml` with `pandas.read_csv` in topic 115 notebook to avoid OpenML redirect errors.

---

## [1.2.0] — 2025-12-01

### Added
- Topics 108–114: Regression Evaluation Metrics, Linear Learning Machines, Kernel Function Matrix, Semi-Supervised Learning (SSL), Safe SSL, S3VM/TSVM, Softmax Activation Function.
- Deep Learning section (topics 91–107): Introduction through LSTM.

---

## [1.1.0] — 2025-06-01

### Added
- Topics 66–90: Association Rules through Case-Based Reasoning.
- Active Learning section (topics 47–56).
- Multi-label & Multi-class Classification section (topics 57–64).

---

## [1.0.0] — 2025-01-01

### Added
- Initial release with topics 01–65.
- Binder support for all notebooks.
- `requirements.txt`, `environment.yml`, `runtime.txt` for reproducible environments.
- `CONTRIBUTING.md` with branch strategy and naming conventions.
