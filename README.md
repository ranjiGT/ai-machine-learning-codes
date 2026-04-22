# AI & Machine Learning Practical Codes

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
git clone https://github.com/<your-username>/ai-machine-learning-codes.git
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
https://mybinder.org/v2/gh/<your-username>/ai-machine-learning-codes/HEAD
```

For this repo, after you push it, replace `<your-username>` with your GitHub username.

## Topic-to-Video Mapping

Create one folder per topic and map it to your YouTube video:

| Topic Folder | Notebook | Video Link |
| --- | --- | --- |
| `01_linear_regression` | `linear_regression_starter.ipynb` | Add video URL |
| `02_logistic_regression` | `logistic_regression_starter.ipynb` | Add video URL |
| `03_decision_trees` | `decision_tree_starter.ipynb` | Add video URL |

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
