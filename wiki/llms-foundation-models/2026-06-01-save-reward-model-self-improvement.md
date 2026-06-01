# SAVE: On-Policy Feedback for Reward Model Self-Supervised Improvement

**TL;DR.** Reward models (RMs, the models that score how good an LLM's response is during alignment) are bottlenecked by the cost of diverse, reliable preference data from humans or judge models. The problem gets worse as the policy evolves past the static RM's training distribution: the RM goes stale and starts grading off-distribution responses it never learned to score. SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback) grades on-policy responses (responses the current policy is actually producing) using the value function as feedback, and uses that to train the RM on-policy. It converts reward-graded on-policy responses into supervision with a prompt-specific value head as an adaptive anchor, computes RM advantages, filters ambiguous samples, and updates the RM with a contrastive objective. It is validated across six benchmarks, and improves results across three RL algorithms (GRPO, RLOO, GSPO) and different policy backbones.

```
policy on-policy responses
        │
        ▼
value-head anchor grades them
        │  RM advantages
        ▼
filter ambiguous samples
        │
        ▼
contrastive RM update  ──►  RM keeps up with the evolving policy
```

## Key points

- Targets RM staleness: a static RM degrades as the policy moves past its training distribution.
- Uses the value function as feedback to grade on-policy responses, with a prompt-specific value head as an adaptive anchor.
- Pipeline: grade on-policy responses, compute RM advantages, filter ambiguous samples, update the RM via a contrastive objective.
- No new human or judge-model preference data is required. The RM improves on-policy.
- Validated across six benchmarks, and improves three RL algorithms (GRPO, RLOO, GSPO) across different policy backbones.

## Gaps in the study

- The value head's quality bounds the self-supervision: a poor value estimate yields poor RM updates.
- Risk of RM and policy forming a feedback loop that reinforces shared errors, since the supervision is self-generated.
- The contrastive filtering thresholds for "ambiguous" samples are a tunable that may not transfer across settings.

## How it relates to prior wiki pages

The recurring wiki theme here is reward-model bottlenecks.

- **Themis (2026-05-04)** was a multilingual, multi-dimensional code RM benchmark that showed collapsing multi-dimensional preferences into a single binary label creates conflicting gradients. SAVE does not solve the multi-dimensional collapse, but it attacks a different RM weakness: staleness rather than label dimensionality.
- **Reward Hacking in Rubric-Based RL (2026-05-13)** found that rubrics reduce but do not eliminate reward hacking. SAVE's self-generated supervision raises the same caution, since an RM trained on its own signal could drift in ways that invite hacking.

SAVE's specific contribution: keep the RM improving on-policy as the policy evolves, without new human labels. It pairs with **SCOPE (today)**, which removes the curated-prompt and external-judge bottleneck for the policy. Both are same-day self-supervision moves, one on the reward side and one on the policy side.

## Links

- Paper: [arxiv 2605.30888](https://arxiv.org/abs/2605.30888)
- Related concept pages: [rl-for-llms.md](rl-for-llms.md)
- Raw source: [raw/huggingface/2026-06-01-the-flip-side-of-rlhf-on-policy-feedback-for-reward-model-se.md](../../raw/huggingface/2026-06-01-the-flip-side-of-rlhf-on-policy-feedback-for-reward-model-se.md)
