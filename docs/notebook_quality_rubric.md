# Notebook Quality Rubric

Use this rubric during review. Total score: 100.

## Scoring Bands
- 90-100: Publish-ready
- 75-89: Good, needs minor revision
- 60-74: Needs substantial revision
- <60: Rework required

## A) Learning Design (20)
- 0-5: Clear topic goals and prerequisites
- 0-5: Intuition is understandable for target level
- 0-5: Math section is correct and concise
- 0-5: Summary clearly explains when to use/not use

## B) Reproducibility (15)
- 0-5: Seeds and random states fixed
- 0-5: Notebook runs top-to-bottom without edits
- 0-5: Data source and assumptions are explicit

## C) Modeling Quality (20)
- 0-5: Correct preprocessing and split strategy
- 0-5: Baseline model included
- 0-5: Main model implementation is technically correct
- 0-5: Hyperparameters and choices are explained

## D) Evaluation Quality (20)
- 0-5: Appropriate metrics for the problem
- 0-5: Metrics are interpreted, not just printed
- 0-5: Overfitting/underfitting analysis is present
- 0-5: Failure cases are analyzed with evidence

## E) Practical Value (15)
- 0-5: Improvement roadmap is actionable
- 0-5: Production lens (latency/drift/monitoring) included
- 0-5: Interview lens (Q&A + tradeoff) included

## F) Readability and Structure (10)
- 0-5: Clean sectioning, coherent flow, concise explanations
- 0-5: Code clarity and naming quality

---

## Reviewer Decision Template

Copy this in PR comments:

```markdown
### Notebook Rubric Review

- Total score: <x>/100
- Decision: <approve | request changes>

#### Section scores
- Learning Design: <x>/20
- Reproducibility: <x>/15
- Modeling Quality: <x>/20
- Evaluation Quality: <x>/20
- Practical Value: <x>/15
- Readability and Structure: <x>/10

#### Top strengths
1. ...
2. ...

#### Required changes
1. ...
2. ...

#### Optional improvements
1. ...
```
