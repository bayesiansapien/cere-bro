# AntiSD: Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.11609](https://arxiv.org/abs/2605.11609) · [raw](../../raw/huggingface/2026-05-20-anti-self-distillation-for-reasoning-rl-via-pointwise-mutual.md)

## TL;DR

On-policy self-distillation, where a student is pulled toward a copy of itself conditioned on a privileged context such as a verified solution, has produced inconsistent gains on math reasoning even where the same recipe works elsewhere. A pointwise mutual information (PMI) analysis traces the failure to the privileged context: it inflates the teacher's confidence on tokens already implied by the solution (structural connectives, verifiable claims) and deflates it on deliberation tokens like "Wait", "Let", "Maybe" that actually drive multi-step search. AntiSD ascends a divergence between student and teacher rather than descending it, flipping the per-token sign and yielding a naturally bounded advantage in one step. An entropy-triggered gate disables the term once teacher entropy collapses. Across five models from 4B to 30B on math benchmarks, AntiSD reaches GRPO baseline accuracy in 2 to 10x fewer training steps and lifts final accuracy by up to 11.5 points.

## Why it matters

The wiki's running thread on on-policy distillation has been mapping where the per-token signal actually lives. TIP (2026-04-16, the paper that found only 10% of teacher-generated tokens carry signal) said the distribution is sparse. LongAct (2026-04-18) said it is saliency-localized at the gradient level. The Many Faces of OPD (2026-05-13) gave the failure taxonomy. The Extrapolation Cliff (2026-05-14) gave the closed-form collapse threshold. AntiSD identifies a specific failure mode inside the same family: when the privileged context is a verified solution, the conditioning pushes teacher confidence in the wrong direction on exactly the deliberation tokens that matter for math. The PMI diagnostic is the cleanest token-by-token analysis the wiki has on why teacher conditioning can hurt.

## Mechanism

Standard on-policy self-distillation minimizes KL between student and a teacher copy conditioned on the privileged context. AntiSD ascends this KL instead. The per-token sign reversal makes the advantage naturally bounded, which removes the need for clip-and-tune that other variants rely on. Entropy-triggered gating disables the term once teacher entropy collapses, preventing the ascent from running off into pure noise once deliberation has resolved.

## Open questions and gaps

The PMI analysis is the load-bearing claim and is shown on math benchmarks across five model sizes; whether the same PMI signature appears on code, agentic tool use, or long-form generation is untested. AntiSD assumes the privileged context is a verified solution; whether the same flip applies when the context is partial feedback or a hint is open. The entropy gate is a hyperparameter that ships unspecified across model sizes.

## Connections

- **TIP (2026-04-16, sparse-token signal)** and **The Many Faces of OPD (2026-05-13, failure taxonomy)** identify that on-policy distillation has problems. AntiSD identifies a specific PMI mechanism behind one failure mode and ships a one-line fix.
- **CEPO (today, 2605.19436)** asks the same question (which tokens are decisive credit-bearers) from a different angle, using a contrastive wrong-answer teacher to sharpen credit at decisive tokens. The two papers compose: AntiSD diagnoses the bias in conditioned teachers, CEPO supplies a cleaner contrastive signal.
- **CopT (today, 2605.20075)** reverses the answer-then-think order. All three are part of one week's evidence that the credit-assignment surface inside reasoning RL is being reworked from the inside.
