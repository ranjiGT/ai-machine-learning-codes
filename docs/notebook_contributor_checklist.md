# Notebook Contributor Checklist

Use this checklist before opening a PR.

## Content
- [ ] Topic title, difficulty, and prerequisites are present
- [ ] Learning outcomes are listed
- [ ] Intuition section is clear and concise
- [ ] Math section includes key formulas and symbol meaning
- [ ] Final summary includes use and non-use cases

## Code and Reproducibility
- [ ] Notebook runs top-to-bottom without manual fixes
- [ ] Seeds/random states are fixed
- [ ] Data loading is deterministic and clearly documented
- [ ] No unnecessary or duplicate imports

## Modeling and Evaluation
- [ ] Train/validation/test strategy is defined
- [ ] Baseline model is implemented
- [ ] Main model is compared against baseline
- [ ] Metrics are appropriate to task
- [ ] Failure cases are analyzed

## Practical Add-ons
- [ ] Improvement ideas are prioritized
- [ ] Production lens section is included
- [ ] Interview lens section is included

## Quality Score Gate (Self-Check)

Score each item as 0 (missing), 1 (partial), or 2 (strong).

- Reproducibility (seeded + deterministic split + runnable): 0/1/2
- Baseline quality (reasonable baseline + comparison): 0/1/2
- Evaluation depth (metric choice + interpretation + failure cases): 0/1/2
- Interview readiness (3-5 Q&A + one tradeoff): 0/1/2
- Production readiness (latency + drift + retraining trigger + monitoring): 0/1/2

Passing recommendation:
- Self-check score >= 8/10
- Rubric score >= 80/100 (see `docs/notebook_quality_rubric.md`)

## Repository Hygiene
- [ ] Notebook output cells are stripped (nbstripout)
- [ ] New dependencies (if any) added to requirements/environment files
- [ ] README mapping updated when adding a new topic
- [ ] Naming follows `<topic>_starter.ipynb`

## Optional but Recommended
- [ ] Add one small visualization to support interpretation
- [ ] Add one challenge exercise for learners
- [ ] Add one "common pitfall" note
