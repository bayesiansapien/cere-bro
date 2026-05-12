# Reinforcement Learning for LLMs

Using RL to improve LLM reasoning and alignment — from RLHF to RLVR (verifiable rewards) to newer approaches that optimize the pre-training distribution directly.

## Current State (as of 2026-05-12)

**Latest additions (2026-05-12):** Two papers extend the "operational targets are sparse and locatable" thread (which is now six papers strong) into self-distillation territory. **RLRT (Rebellious Student)** reads the self-distillation signal in reverse: when the student succeeds along a path the teacher would not have predicted, those tokens are the student's own exploration and get reinforced inside a GRPO loop. Information asymmetry becomes a new design axis for RLVR. **G-Zero** drops external verifiers entirely. The intrinsic reward is **Hint-delta**: the predictive shift between the model's unassisted response and its hint-conditioned response. A Proposer (GRPO) finds blind spots, a Generator (DPO) internalizes the hint-guided improvements. Best-iterate suboptimality bound under exploration-coverage and noise-control assumptions. Together with **Geometry Conflict** (today, llms-foundation-models) and **Model Merging Scaling Laws** (today), the picture is: training dynamics are increasingly understood at the layer of "which updates compose without interference, which tokens carry the signal, which deltas constitute exploration." Six papers in two months (TIP, LongAct, Compliance vs Sensibility, Safety Drift, RLRT, G-Zero) make sparseness-and-locatability the dominant design pattern.

## Prior State (as of 2026-05-04)

The "operational targets are sparse and locatable" thread is now four papers strong: TIP (04-16, distillation signal in <10% of tokens), LongAct (04-18, saliency-driven sparse RL updates), Compliance vs Sensibility (05-02, reasoning mode is a linear direction), Safety Drift (05-02, safety is a vector-not-scalar across benchmarks). MIT's superposition explanation for scaling laws (05-03) gives the mechanistic substrate: features are encoded along approximately non-interfering directions, and that's why scaling works *and* why operationally relevant variables are linear and steerable. The structural prediction: most RL post-training behavior is a steerable manifold — the next paper makes activation-steering competitive with full RLHF on at least one task.

The reward-modeling bottleneck has shifted from "execution feedback only" to multi-criteria. Themis (05-04) is the first systematic multilingual code RM benchmark + 350K-pair preference dataset across 5 dimensions × 8 languages. Same root-cause as ViPO/Semi-DPO (05-02): collapsing multi-dimensional preferences to binary labels produces conflicting gradients. Three papers in three weeks make the same diagnosis from three domains.

The RL-rollout cost remains the dominant compute bottleneck of frontier RL post-training (NeMo-RL speculative decoding 04-30: 1.77× generation, 2.5× end-to-end projection at 235B). LWD (05-04) adds the offline-to-online dimension: distributional implicit value learning + Q-learning via adjoint matching for fleet-scale VLA post-training. The robotics paper, but the primitives transfer.

## Prior State (as of 2026-04-22)

The RL era for LLMs is firmly established. RLVR (RL with verifiable rewards) is the dominant paradigm for reasoning models. New work is pushing beyond the conditional distribution P(y|x) — into pre-train space optimization (PreRL) and now into optimal-transport-based policy optimization (VGF) that eliminates explicit policy parameterization entirely.

## Key Papers

**RLRT / Rebellious Student (2026-05-12)** — Reads the self-distillation signal in reverse: when the student succeeds along a path the teacher would not have predicted, those tokens reflect the student's own reasoning and are reinforced inside a GRPO augmentation. Information asymmetry between teacher and student becomes a principled exploration axis. Beats self-distillation and exploration-based baselines across base, instruction-tuned, and thinking-tuned Qwen3 checkpoints. → [summary](2026-05-12-rebellious-student-rlrt.md)

**G-Zero (2026-05-12)** — Verifier-free, co-evolutionary self-improvement. Intrinsic reward = predictive shift between unhinted and hinted responses (Hint-delta). Proposer trained via GRPO to find blind spots, Generator trained via DPO to internalize improvements. Provable best-iterate suboptimality bound under exploration-coverage and noise-control assumptions. Bypasses the verifier ceiling for open-ended generation. → [summary](2026-05-12-g-zero-verifier-free-self-play.md)

**PreRL / DSRL (2026-04-16)** — Applies RL directly to the marginal distribution P(y) rather than P(y|x), bypassing the ceiling imposed by the base model's output distribution. Negative Sample Reinforcement (NSR) prunes wrong reasoning paths and boosts reflection. DSRL combines PreRL + standard RL for best results. → [summary](2026-04-16-prerl-rl-in-pretrain-space.md)

**RationalRewards (2026-04-16)** — Reward models that produce explicit multi-dimensional critiques before scoring. Test-time Generate-Critique-Refine loop matches RL fine-tuning without parameter updates. → [summary](../vision-audio-video/2026-04-16-rationalrewards-visual-generation.md)

**Value Gradient Flow / VGF (2026-04-19)** — Reframes behavior-regularized RL (used in offline RL and LLM fine-tuning) as an optimal transport problem. Moves particles (candidate outputs) from the reference distribution toward high-value regions via gradient flow, without explicit policy parameterization. Implicit KL regularization through transport budget. Adaptive test-time scaling by running more transport steps. SOTA on D4RL, OGBench, and LLM RL benchmarks. → [summary](2026-04-19-vgf-value-gradient-flow-rl.md)

**GFT: Group Fine-Tuning (2026-04-21)** — Proves mathematically that SFT is a degenerate case of policy gradient with maximally sparse implicit reward, unstable inverse-probability weighting, and single-path dependency. Group Advantage Learning constructs diverse response groups and derives contrastive supervision (same family as GRPO). Dynamic Coefficient Rectification stabilizes the inverse-probability weights. Outperforms SFT and integrates more smoothly with subsequent RL training. → [summary](2026-04-21-gft-sft-as-degenerate-rl.md)

**RLVR Under Weak Supervision (2026-04-21)** — Systematic study of when RLVR generalizes under scarce data, noisy rewards, and self-supervised proxy rewards. Key finding: reward saturation speed during training predicts generalization. Reasoning faithfulness (logical coherence of intermediate steps) predicts which regime a model enters pre-RL. Output diversity is uninformative. SFT on explicit reasoning traces is necessary preparation for weak-supervision RL. → [summary](2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md)

**TEMPO (2026-04-22)** — Test-time training (TTT) that doesn't plateau. Existing TTT methods run E-steps (reward evaluation) without M-steps (critic recalibration), causing reward drift and diversity collapse. TEMPO formalizes TTT as EM: alternates policy refinement on unlabeled test queries with periodic critic recalibration on a labeled calibration set. Tightens the ELBO and enables sustained improvement. OLMO3-7B AIME 2024: 33% → 51.1%; Qwen3-14B: 42.3% → 65.8%. → [summary](2026-04-22-tempo-test-time-training.md)

**LongAct (2026-04-18)** — Saliency-guided sparse RL updates: concentrates gradients only on weights associated with high-magnitude Q/K activations during long-context processing. 8% improvement on LongBench v2, universal across GRPO and DAPO. Cross-paradigm transfer from quantization research (high-magnitude = hard to quantize) to training (high-magnitude = where to train). → [summary](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md)

**Speculative Decoding for RL Rollouts (2026-04-30, NVIDIA)** — Integrates EAGLE-3 / MTP / external draft models into the RL training loop via NeMo-RL + vLLM. Lossless: target policy is verifier, log-probs and policy loss are computed against target. Sweet spot at k=3; draft alignment with rollout distribution dominates speedup. 1.77× generation, 1.41× per-step at 8B, no AIME accuracy loss; 2.5× end-to-end projection at 235B. → [summary](../inference-efficiency/2026-04-30-speculative-decoding-rl-rollouts.md)

**Themis Multilingual Code Reward Models (2026-05-04)** — First systematic multi-criteria multilingual code RM benchmark (5 dimensions × 8 languages) + 350K preference pair dataset (largest public). 50+ existing RMs profiled; most are strong only on functional correctness. Themis-RM 600M → 32B shows positive scaling and cross-lingual transfer. Code-domain analog of the ViPO/Semi-DPO (05-02) dimension-collapse diagnosis. → [summary](2026-05-04-themis-multilingual-code-reward-models.md)

**LWD Fleet-Scale RL for VLA Policies (2026-05-04, robotics)** — Offline-to-online RL closing the loop between fleet deployment and policy improvement. Distributional Implicit Value Learning (DIVL) + Q-learning via Adjoint Matching (QAM) for flow-based action generators. 16 dual-arm robots × 8 tasks → 95% average success. The DIVL/QAM primitives transfer to language-domain trajectory routing. → [summary](../agentic-systems/2026-05-04-lwd-fleet-rl-vla-policies.md)

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
