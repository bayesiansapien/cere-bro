# Reinforcement Learning for LLMs

Using RL to improve LLM reasoning and alignment — from RLHF to RLVR (verifiable rewards) to newer approaches that optimize the pre-training distribution directly.

## Current State (as of 2026-04-30)

The RL-rollout cost is now the dominant compute bottleneck of frontier RL post-training: at 8B+ scale, autoregressive generation accounts for 65–72% of every step. Speculative decoding has crossed from inference-only into the training loop (NVIDIA, 04-30): 1.77× generation speedup at 8B, projected 2.5× end-to-end at 235B on 2048 GB200s. The training-time inference problem now rivals the gradient-update problem in importance.

## Prior State (as of 2026-04-22)

The RL era for LLMs is firmly established. RLVR (RL with verifiable rewards) is the dominant paradigm for reasoning models. New work is pushing beyond the conditional distribution P(y|x) — into pre-train space optimization (PreRL) and now into optimal-transport-based policy optimization (VGF) that eliminates explicit policy parameterization entirely.

## Key Papers

**PreRL / DSRL (2026-04-16)** — Applies RL directly to the marginal distribution P(y) rather than P(y|x), bypassing the ceiling imposed by the base model's output distribution. Negative Sample Reinforcement (NSR) prunes wrong reasoning paths and boosts reflection. DSRL combines PreRL + standard RL for best results. → [summary](2026-04-16-prerl-rl-in-pretrain-space.md)

**RationalRewards (2026-04-16)** — Reward models that produce explicit multi-dimensional critiques before scoring. Test-time Generate-Critique-Refine loop matches RL fine-tuning without parameter updates. → [summary](../multimodal/2026-04-16-rationalrewards-visual-generation.md)

**Value Gradient Flow / VGF (2026-04-19)** — Reframes behavior-regularized RL (used in offline RL and LLM fine-tuning) as an optimal transport problem. Moves particles (candidate outputs) from the reference distribution toward high-value regions via gradient flow, without explicit policy parameterization. Implicit KL regularization through transport budget. Adaptive test-time scaling by running more transport steps. SOTA on D4RL, OGBench, and LLM RL benchmarks. → [summary](2026-04-19-vgf-value-gradient-flow-rl.md)

**GFT: Group Fine-Tuning (2026-04-21)** — Proves mathematically that SFT is a degenerate case of policy gradient with maximally sparse implicit reward, unstable inverse-probability weighting, and single-path dependency. Group Advantage Learning constructs diverse response groups and derives contrastive supervision (same family as GRPO). Dynamic Coefficient Rectification stabilizes the inverse-probability weights. Outperforms SFT and integrates more smoothly with subsequent RL training. → [summary](2026-04-21-gft-sft-as-degenerate-rl.md)

**RLVR Under Weak Supervision (2026-04-21)** — Systematic study of when RLVR generalizes under scarce data, noisy rewards, and self-supervised proxy rewards. Key finding: reward saturation speed during training predicts generalization. Reasoning faithfulness (logical coherence of intermediate steps) predicts which regime a model enters pre-RL. Output diversity is uninformative. SFT on explicit reasoning traces is necessary preparation for weak-supervision RL. → [summary](2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md)

**TEMPO (2026-04-22)** — Test-time training (TTT) that doesn't plateau. Existing TTT methods run E-steps (reward evaluation) without M-steps (critic recalibration), causing reward drift and diversity collapse. TEMPO formalizes TTT as EM: alternates policy refinement on unlabeled test queries with periodic critic recalibration on a labeled calibration set. Tightens the ELBO and enables sustained improvement. OLMO3-7B AIME 2024: 33% → 51.1%; Qwen3-14B: 42.3% → 65.8%. → [summary](2026-04-22-tempo-test-time-training.md)

**LongAct (2026-04-18)** — Saliency-guided sparse RL updates: concentrates gradients only on weights associated with high-magnitude Q/K activations during long-context processing. 8% improvement on LongBench v2, universal across GRPO and DAPO. Cross-paradigm transfer from quantization research (high-magnitude = hard to quantize) to training (high-magnitude = where to train). → [summary](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md)

**Speculative Decoding for RL Rollouts (2026-04-30, NVIDIA)** — Integrates EAGLE-3 / MTP / external draft models into the RL training loop via NeMo-RL + vLLM. Lossless: target policy is verifier, log-probs and policy loss are computed against target. Sweet spot at k=3; draft alignment with rollout distribution dominates speedup. 1.77× generation, 1.41× per-step at 8B, no AIME accuracy loss; 2.5× end-to-end projection at 235B. → [summary](../inference-efficiency/2026-04-30-speculative-decoding-rl-rollouts.md)

## Key Concepts

- **RLHF**: RL from human feedback — aligns model outputs to human preferences
- **RLVR**: RL with verifiable rewards — uses ground-truth-checkable tasks (math, code) for reward signal
- **P(y|x) vs P(y)**: standard RL optimizes the conditional; PreRL optimizes the marginal, avoiding base model ceiling
- **Negative Sample Reinforcement**: learning from wrong outputs to prune incorrect reasoning subspaces
- **Optimal transport for RL**: VGF casts policy optimization as finding the transport map from reference to optimal distribution — implicit KL control through budget
- **Saliency-guided sparse updates (LongAct)**: not all gradient positions are equal; high-magnitude activation positions carry the signal for long-context reasoning
- **Transport budget**: in VGF, how far particles move from reference — the continuous analog of the KL penalty in standard RLHF
- **RL-rollout speculation**: lossless acceleration of the autoregressive trajectory generator inside the RL loop via a draft model whose proposals are exactly verified by the target policy — preserves the optimization regime, accelerates the dominant cost

## Related Pages

- [Knowledge Distillation](../inference-efficiency/knowledge-distillation.md)
- [Open vs Closed Models Mid-2026](2026-04-16-open-vs-closed-models-mid-2026.md)
