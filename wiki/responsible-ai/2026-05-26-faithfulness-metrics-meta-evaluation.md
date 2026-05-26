# Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

**Source:** [arXiv:2605.25052](https://arxiv.org/abs/2605.25052), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Interpretability / chain-of-thought faithfulness / metric evaluation.

## TL;DR

Chain-of-thought (CoT) traces have become the primary substrate for interpreting and auditing LLM behavior. Several faithfulness metrics have been proposed to measure whether a CoT actually reflects the computation behind the model's output. The problem is that prior work could not validate the metrics: internal computations are unobservable, ground truth is missing, and existing benchmarks rely on plausibility or importance proxies that are orthogonal to faithfulness. The paper constructs tasks whose outputs reveal which intermediate computations must have produced them, then builds an automated labeling pipeline that yields ground-truth faithfulness labels at both step and CoT levels. The result is BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models. Findings: most existing faithfulness metrics perform near chance, exhibit strong prediction biases, degrade on longer CoTs. The best CoT-level metric reaches 0.70 AUROC; the best step-level metric reaches 0.59. Neither transfers across settings, and both have prohibitively high compute cost.

## Why this matters

This is a meta-evaluation paper, the kind that exposes a quiet measurement crisis. Most interpretability work that claims to measure CoT faithfulness has been measuring something else (plausibility, importance, or just a correlated proxy). The paper's central technical contribution is a way to construct ground truth at all: design tasks where the output uniquely determines which intermediate computations the model must have performed, so the trace can be checked against necessary intermediate steps.

The implication is uncomfortable. The wiki's prior pages on CoT-based safety, interpretability, and audit (every line of work that uses "the model's reasoning is faithful enough to inspect") now needs a caveat. The metric most papers use to claim faithfulness is near chance on the new ground-truth benchmark.

## Key findings

- **Methodology**: tasks designed so output reveals required intermediate computations. Automated labeling yields ground-truth faithfulness labels at step and CoT level.
- **Benchmark**: BonaFide, 3,066 labeled CoTs, 13 tasks, 10 models.
- **Best CoT-level metric**: 0.70 AUROC (modest, well below the >0.85 most metric papers claim implicitly).
- **Best step-level metric**: 0.59 AUROC (essentially marginal over chance).
- **Bias diagnosis**: most metrics show strong prediction bias; they are biased toward labeling traces as faithful or unfaithful systematically, not based on actual faithfulness.
- **Length degradation**: metrics worsen on longer CoTs, the regime where they matter most.
- **Cross-setting transfer**: zero. A metric tuned on one task does not generalize to another.
- **Compute cost**: prohibitively high for the best-performing metrics.

## How this relates to prior wiki pages

This intersects multiple threads:

- **RLVR weak-supervision-reasoning-faithfulness (2026-04-21)** argued that RLVR's reward signals could induce CoT shortcuts that look faithful but are not. BonaFide's near-chance metric performance retroactively says: prior work could not have detected such shortcuts because the detection metric itself was unreliable.
- **Reward hacking rubric-based RL (2026-05-13)** and **Themis (2026-05-04)** rely on the assumption that a rubric reward can score CoT quality. BonaFide implies the rubric-based score correlates with faithfulness only weakly; reward hacking through unfaithful CoT remains plausible.
- **CiteVQA (2026-05-25)**'s finding that AI models give right answers but cite wrong sources is the citation-side instance of the same general problem: the model's output and the model's stated reasoning are loosely coupled, and the wiki's interpretation pipeline has been treating the coupling as tight.

## Research angle

This paper redirects the field's research target. Instead of inventing more faithfulness metrics that fit the existing proxy benchmarks, the next round of work should either (a) build evaluation tasks that have constructible ground truth (BonaFide's recipe), or (b) abandon CoT-level faithfulness as the unit and move to activation-level or attribution-level faithfulness. The 0.70 ceiling at AUROC says CoT-level interpretability is fundamentally lossy; the actual signal lives elsewhere in the model.

## Industrial implication

Safety teams that use CoT inspection as a regulatory or product-safety control should treat BonaFide as a calibration check. If your faithfulness metric scores poorly on BonaFide-style ground truth, the safety claim it underwrites is weaker than your compliance document says it is. This is the kind of finding that lands in front of EU AI Act conformity assessors and FDA software-as-medical-device reviewers within a year.
