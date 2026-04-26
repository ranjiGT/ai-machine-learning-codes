# Contributing Guide

Thanks for contributing to this learning repository.

## Branch Strategy

- Create one branch per topic: `topic/<topic-name>`
- Keep pull requests focused and small.

## Folder and Naming Convention

- One folder per topic under `notebooks/`
- Notebook names use snake_case and end with `_starter.ipynb`
- Optional helper scripts go in `src/`

## First-Time Setup

After cloning and installing dependencies, run these once:

```bash
pip install -r requirements.txt
nbstripout --install   # strips notebook outputs before every commit
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

## Pull Request Checklist

- Notebook runs from top to bottom without errors.
- Notebook outputs are **not** committed (nbstripout handles this automatically).
- Code has clear section headers and short explanations.
- Add or update the topic tile in `README.md` (include difficulty tag).
- Keep dependencies minimal; add new packages to `requirements.txt` if needed.

## Co-Author Workflow

For collaboration with `yatchmaster`:

1. Add `yatchmaster` as a collaborator in repository settings.
2. Work on a feature branch and open a PR.
3. This repository includes a commit hook that auto-adds the co-author trailer for `yatchmaster` on every commit (enabled via First-Time Setup above).
4. If needed, you can still add the trailer manually:

```text
Co-authored-by: yatchmaster <yatchmaster@users.noreply.github.com>
```

## Suggested Commit Format

```text
feat(topic): add linear regression notebook
```

## Code Style

- Use Python 3.11+
- Prefer simple, readable code over advanced shortcuts.
- Add comments only where logic is not obvious.
