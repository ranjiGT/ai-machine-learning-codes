# AI & Machine Learning Practical Codes

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD)
[![Open Linear Regression Notebook](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/01_linear_regression/linear_regression_starter.ipynb)

Practical Python examples for Machine Learning and Data Science topics from my YouTube channel.

- Channel: [RanjiRaj18](https://www.youtube.com/@RanjiRaj18)
- Playlist: [Machine Learning and Data Science Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR)

This repository is designed for learners who want:
- topic-wise practical code
- Jupyter notebooks that can run locally
- one-click cloud execution using Binder

## Repository Goals

- Keep each topic short, practical, and beginner-friendly.
- Map every video to runnable Python code.
- Make it easy for subscribers to fork, run, and learn.

## Project Structure

```text
.
├── notebooks/
│   └── 01_linear_regression/
│       └── linear_regression_starter.ipynb
├── src/
│   ├── data/
│   ├── ml_basics/
│   └── utils/
├── requirements.txt
├── runtime.txt
├── environment.yml
├── CONTRIBUTING.md
└── README.md
```

## Run Locally (Jupyter)

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Start Jupyter Lab.

```bash
git clone https://github.com/ranjiGT/ai-machine-learning-codes.git
cd ai-machine-learning-codes

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

jupyter lab
```

## Run in the Cloud (Binder)

Once the repo is pushed to GitHub, anyone can open notebooks without local setup.

Use this URL format:

```text
https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD
```

### Binder Troubleshooting

- First build can take several minutes. If it times out, retry once.
- If `HEAD` fails, verify your default branch contains `requirements.txt`, `runtime.txt`, and `environment.yml`.
- Avoid pinning conflicting Jupyter packages. This repo uses `jupyterlab>=4.3,<5` and does not pin `notebook`.
- If Binder reports dependency resolution errors, simplify version pins in `requirements.txt` and rebuild.

## Topic-to-Video Mapping

Create one folder per topic and map it to your YouTube video:

| Topic | Notebook | Run on Binder | YouTube |
| --- | --- | --- | --- |
| Linear Regression | `notebooks/01_linear_regression/linear_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/01_linear_regression/linear_regression_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=e9VYOWWP6zM) |
| Logistic Regression | `notebooks/02_logistic_regression/logistic_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/02_logistic_regression/logistic_regression_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=S4IG2wv9Lnk) |
| Decision Trees | `notebooks/03_decision_trees/decision_tree_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/03_decision_trees/decision_tree_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=k3SYtpv5y6Y) |
| Random Forest | `notebooks/04_random_forest/random_forest_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/04_random_forest/random_forest_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=p2arCEdJ8Fk) |
| KNN | `notebooks/05_knn/knn_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/05_knn/knn_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=Pqo9o0286Qs) |
| PCA | `notebooks/06_pca/pca_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/06_pca/pca_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=7bpjiA2VDZE) |
| Naive Bayes | `notebooks/07_naive_bayes/naive_bayes_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/07_naive_bayes/naive_bayes_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Underfitting vs Overfitting | `notebooks/08_underfitting_overfitting/underfitting_overfitting_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/08_underfitting_overfitting/underfitting_overfitting_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Reduced Error Pruning | `notebooks/09_reduced_error_pruning/reduced_error_pruning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/09_reduced_error_pruning/reduced_error_pruning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Random Sampling | `notebooks/10_random_sampling/random_sampling_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/10_random_sampling/random_sampling_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cross Validation | `notebooks/11_cross_validation/cross_validation_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/11_cross_validation/cross_validation_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Nested Cross Validation | `notebooks/12_nested_cross_validation/nested_cross_validation_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/12_nested_cross_validation/nested_cross_validation_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |

## Co-Author Setup

If you want to co-author with [yatchmaster](https://github.com/yatchmaster):

1. Add `yatchmaster` as a collaborator in GitHub repository settings.
2. Use feature branches and pull requests.
3. Add co-author trailers in commit messages when both contribute:

```text
Co-authored-by: yatchmaster <their-email@users.noreply.github.com>
```

See `CONTRIBUTING.md` for a full workflow.

## Contributing

Contributions are welcome from subscribers and learners.
Please read `CONTRIBUTING.md` before opening pull requests.

## License

This project is open for educational use. Add your preferred license file (MIT recommended).
