# Notebook Quality Template

Use this template for every new topic notebook (for example: `*_starter.ipynb`).
The goal is to keep each notebook practical, reproducible, and interview-ready.

## 1) Header Cell (Markdown)

Required fields:
- Topic name
- Difficulty: Beginner / Intermediate / Advanced
- Prerequisites (2-5 bullets)
- Learning outcomes (3-5 bullets)
- Estimated time

Suggested format:

```markdown
# Topic: <Name>

**Difficulty:** <Beginner|Intermediate|Advanced>

## Prerequisites
- ...

## What you will learn
- ...

## Estimated time
- <xx minutes>
```

## 2) Intuition First (Markdown)

Before formulas or code, explain:
- What problem this method solves
- Why it matters
- Typical real-world use cases
- Common mistakes beginners make

Keep this section short and concrete.

## 3) Math Core (Markdown)

Include only the minimum math needed to understand behavior:
- Key formula(s)
- Meaning of each symbol
- 1 short interpretation note ("what changes if this term increases?")

Avoid long derivations unless the topic specifically requires it.

## 4) Reproducible Setup (Code)

Must include:
- Fixed random seed(s)
- Explicit imports
- Dataset source declaration
- Data shape checks

Example requirements:
- `np.random.seed(...)`
- `random_state=...` for sklearn splits/models
- Printed dataset shape summary

## 5) Data Split and Baseline (Code + Markdown)

Always include:
- Train/validation/test strategy
- Baseline model (or naive baseline)
- Why this baseline is reasonable

You should compare your method against at least one baseline.

## 6) Main Model Build (Code)

Keep model code in clearly separated blocks:
- Preprocessing
- Model definition
- Training
- Inference

Add short comments only where logic is not obvious.

## 7) Evaluation Block (Markdown + Code)

Mandatory outputs:
- Metrics table
- Confusion matrix / error metric plots when relevant
- Brief interpretation

Minimum evaluation checklist:
- Which metric is primary and why
- Is model overfitting or underfitting?
- Where model fails most often

## 8) Error Analysis (Markdown)

Add a section called "Failure Cases" containing:
- 2-5 concrete failure patterns
- Likely reason for each
- One mitigation idea per failure

## 9) Improvement Ideas (Markdown)

Provide prioritized next steps:
- Quick win (low effort)
- Medium effort
- Advanced extension

## 10) Production Lens (Markdown)

Add a short practical section:
- Inference latency considerations
- Data drift risk
- Retraining trigger suggestion
- Monitoring metric to watch in production

## 11) Interview Lens (Markdown)

Include:
- 3-5 likely interview questions
- 1-2 sentence answers each
- 1 tradeoff question

## 12) Final Summary (Markdown)

Close with:
- What to remember
- When to use this method
- When not to use it

---

## Notebook Acceptance Gate

A notebook is "ready" only if all items below are true:
- Runs top-to-bottom without manual edits
- Uses fixed seeds for reproducibility
- Includes baseline + comparison
- Includes failure analysis section
- Includes production lens section
- Includes interview lens section
