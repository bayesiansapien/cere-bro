# CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.19436](https://arxiv.org/abs/2605.19436) · [raw](../../raw/huggingface/2026-05-20-cepo-rlvr-self-distillation-using-contrastive-evidence-polic.md)

## TL;DR

Under RLVR (reinforcement learning with verifiable rewards) every token in a correct trajectory gets the same reward, whether it was the decisive reasoning step or a grammatical filler. The natural fix of conditioning the model on the correct answer as a teacher either leaks the answer into the gradient or produces a signal too weak to distinguish decisive tokens from filler. CEPO sharpens the question: not just "does the correct answer favor this token?" but "does the correct answer favor it while the wrong answer disfavors it?" The wrong-answer teacher is constructed from rejected rollouts already inside the training batch, at zero extra sampling cost. The paper proves CEPO inherits all structural safety guarantees of the prior state of the art while strictly sharpening credit at decisive tokens, with the improvement vanishing exactly at filler. Empirically, CEPO hits 43.43% and 60.56% average accuracy across five multimodal mathematical reasoning benchmarks at 2B and 4B, against 41.17% and 57.43% for GRPO under identical budgets. Distribution-matching self-distillation methods such as OPSD and SDPO fall below the untrained baseline, empirically confirming the information leakage the theory predicts.

## Why it matters

RLVR's blind spot has been the same as on-policy distillation's: credit assignment at the token level. CEPO does not invent a new sampling step. The wrong-answer teacher is the existing rejected rollouts, repurposed as a contrastive signal. That keeps the compute budget unchanged and adds the discriminative dimension that pure answer-conditioning lacks. Two papers in the same day (CEPO and AntiSD) both diagnose teacher-conditioning failures from the PMI angle and ship per-token fixes, which puts the reasoning-RL credit-assignment thread on its sharpest week yet.

## Mechanism

A correct-answer teacher is the same model conditioned on the verified answer. A wrong-answer teacher is the same model conditioned on a rejected rollout's wrong answer drawn from the same batch. The per-token advantage is the difference: tokens where the correct-answer teacher's confidence rises and the wrong-answer teacher's confidence falls are decisive. Tokens where both move the same way (or neither moves) are filler. The proof shows the prior method's safety guarantees carry over because the construction is a refinement of an existing soft-target signal, and the improvement vanishes at filler by construction.

## Open questions and gaps

Tested at 2B and 4B on multimodal math. Whether the contrast survives at frontier scale and across coding or agentic RL is open. The wrong-answer teacher relies on having rejected rollouts in the batch, which means CEPO can only act when GRPO-style group sampling produces both correct and incorrect trajectories. In hard-tail regimes where everything fails, CEPO degrades to a standard signal.

## Connections

- **AntiSD (today)** uses divergence ascent over PMI rather than descent, fixing the same teacher-bias problem from a different angle.
- **CopT (today)** sidesteps the credit-assignment problem entirely by reversing the order: answer first, then think.
- **The Many Faces of OPD (2026-05-13)** named the failure taxonomy CEPO's leak diagnosis falls under. The theory in CEPO formally bounds where on-policy distillation methods can and cannot work.
- **Sparse-to-Dense Reward Principle (2026-05-13)** said the allocation rule is "sparse RL upstream, OPD bridge, GRPO student-side." CEPO is the cleanest token-level instantiation of that bridge so far.
