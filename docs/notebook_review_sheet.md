# Notebook Review Sheet

Use this sheet for PR reviews and contributor self-reviews.

## 1) Quick Scorecard (0-2 each)

Scoring scale:
- 0 = Missing
- 1 = Partial / unclear
- 2 = Strong and complete

| Dimension | Score (0-2) | Reviewer notes |
|---|---:|---|
| Reproducibility |  |  |
| Baseline quality |  |  |
| Evaluation depth |  |  |
| Interview readiness |  |  |
| Production readiness |  |  |
| **Total** |  |  |

Interpretation:
- 9-10: Merge-ready
- 8: Minor fixes, then merge
- 6-7: Request changes
- <=5: Major rework needed

## 2) Full Rubric Score (0-100)

Reference rubric: `docs/notebook_quality_rubric.md`

- Learning Design: __ / 20
- Reproducibility: __ / 15
- Modeling Quality: __ / 20
- Evaluation Quality: __ / 20
- Practical Value: __ / 15
- Readability and Structure: __ / 10
- Total: __ / 100

Decision guide:
- >=90: Publish-ready
- 80-89: Approve with minor comments
- 70-79: Request targeted changes
- <70: Request major revision

## 3) Acceptance Gate Check

- [ ] Runs top-to-bottom without manual edits
- [ ] Fixed seeds and deterministic split strategy
- [ ] Baseline included and compared
- [ ] Failure analysis section present
- [ ] Production lens section present
- [ ] Interview lens section present

## 4) Reviewer Summary Template

```markdown
### Notebook Review

- Decision: <approve | request changes>
- Quick scorecard: <x>/10
- Full rubric: <x>/100

#### Strengths
1. ...
2. ...

#### Required changes
1. ...
2. ...

#### Optional improvements
1. ...
```
