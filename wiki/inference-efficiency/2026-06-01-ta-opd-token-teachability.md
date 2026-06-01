# TA-OPD: Token Teachability in On-Policy Distillation

On-policy distillation (OPD) trains a student model on its own generated rollouts, using token-level supervision from a teacher model. Recent selective-OPD methods prioritize high-entropy or high-disagreement tokens, on the assumption that the tokens where teacher and student disagree most are the ones worth training on. This paper asks a sharper question: which token signals are actually learnable? Using a fixed-context diagnostic that measures same-context teacher-student KL reduction, it shows that raw KL disagreement (how far apart the two distributions are) is a coarse proxy. It conflates learnable disagreement, where the teacher puts corrective probability mass on the student's top-K candidates so the student can actually move toward it, with incompatible disagreement, where the teacher's mass sits mostly off the student's current support so the student cannot reach it in one step. The paper formalizes "token teachability," a measure of local compatibility, and shows it predicts fixed-context improvement better than raw KL. TA-OPD then applies the OPD loss only at high-teachability token positions, with no reward model and no verifier. Across Qwen2.5 and Qwen3 teacher-student settings, TA-OPD often beats full-token OPD while using only 5% of tokens, and beats entropy-based and divergence-based selection baselines.

```
token disagreement (teacher vs student KL)
        │
        ├─► LEARNABLE: teacher mass lands on student top-K ►reachable ►KEEP (train here)
        │
        └─► INCOMPATIBLE: teacher mass off student support ►not reachable in one step ►SKIP
```

## Key points

- **Disagreement is not the same as learnability.** Two tokens can have identical KL disagreement, yet one is reachable from the student's current support and the other is not. Training on the unreachable one wastes signal.
- **Token teachability is the new selection criterion.** It measures whether the teacher's corrective mass falls inside the student's top-K candidates, that is, whether the student can move toward the teacher in a single step.
- **Teachability predicts improvement better than raw KL.** Under the fixed-context diagnostic, high-teachability tokens are the ones whose same-context KL actually shrinks after a step.
- **5% of tokens often beats 100%.** TA-OPD applies OPD loss only at high-teachability positions and frequently outperforms full-token OPD, while also beating entropy- and divergence-based selection.
- **No reward model, no verifier.** The teachability filter is purely a property of the teacher and student distributions, so it adds no extra model to the training loop.
- **It reframes selective OPD.** The goal is selecting learnable teacher signals, not merely salient or uncertain tokens.

## Gaps in the study

Tested on Qwen2.5 and Qwen3 families only, so cross-family generality is open. The "one-step learnable" framing may undervalue tokens that are not reachable now but become learnable over several steps as the student moves. The cost of computing the teachability diagnostic at scale is not fully characterized, which matters because the whole pitch is cheaper distillation.

## How it relates to prior wiki pages

The knowledge-distillation.md concept page tracks this exact "which tokens carry the signal" thread, and TA-OPD is the latest turn in it.

- **TIP (2026-04-16)**, which found that distillation signal lives in under 10% of tokens and identified high-entropy and overconfident-wrong token regions as where it concentrates, opened the question. TA-OPD refines TIP's answer to "which tokens": not just the salient or uncertain ones, but the ones whose teacher correction is actually reachable from the student's current support. It is a stricter filter on top of TIP's observation.
- **The Many Faces of OPD (2026-05-13)**, which named OPD failure modes including biased TopK reverse-KL gradients (where restricting the KL to top-K candidates skews the gradient), described a failure that TA-OPD directly addresses. By selecting only tokens whose teacher mass already lands in the student's top-K, TA-OPD trains where the TopK-restricted gradient is well-behaved and skips the positions where Many Faces showed it goes biased.
- **The Extrapolation Cliff (2026-05-14)**, which gave a closed-form threshold beyond which OPD collapses because the teacher is too far from the student to learn from, is the theory-side companion. TA-OPD's incompatible-disagreement category is the per-token version of the same idea: when teacher mass is off the student's support, that token is past its local cliff and should be skipped.

TA-OPD therefore sits at the intersection of all three: it operationalizes TIP's sparsity, dodges Many Faces' biased-TopK failure, and applies Extrapolation Cliff's "too far to learn" insight at the token level rather than the model level.

## Industrial implication

5%-token OPD means much cheaper distillation of reasoning models, since the bulk of the token-level loss computation is skipped without quality loss. The teachability filter is the natural successor to entropy-based token selection: same goal of training on the few tokens that matter, but with a criterion grounded in what the student can actually learn rather than where it is merely uncertain. Expect teachability-style filtering to replace entropy thresholds in production distillation pipelines for reasoning models over the next few quarters.

## Links

- Paper: [arXiv 2605.26844](https://arxiv.org/abs/2605.26844)
- Related concept page: [Knowledge distillation](knowledge-distillation.md)
- Related concept page: [RL for LLMs](../llms-foundation-models/rl-for-llms.md)

Raw source: [raw/huggingface/2026-06-01-not-all-disagreement-is-learnable-token-teachability-in-on-p.md](../../raw/huggingface/2026-06-01-not-all-disagreement-is-learnable-token-teachability-in-on-p.md)
