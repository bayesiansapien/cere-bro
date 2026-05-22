# RELEX: RLVR Weight Trajectories are Rank-1, Extrapolate from 15% of Training

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.21468 · [paper](https://arxiv.org/abs/2605.21468) · [raw](../../raw/huggingface/2026-05-21-you-only-need-minimal-rlvr-training-extrapolating-llms-via-r.md)
**Topic:** llms / RLVR / reasoning
**Authors:** Zhepei Wei, Xinyu Zhu, Wei-Lin Chen, Yu Meng (UVA), Chengsong Huang, Jiaxin Huang (WashU)

## TL;DR

RELEX shows that the parameter deltas accumulated during RLVR (reinforcement learning with verifiable rewards) training are extremely low-rank, with the majority of downstream performance gains captured by a rank-1 approximation whose magnitude evolves near-linearly with training step. From a short observation window (15% of full RLVR steps), the rank-1 subspace and its scalar trajectory can be estimated and the future checkpoints projected forward with linear regression alone. Across Qwen2.5-Math-1.5B, Qwen3-4B-Base, and Qwen3-8B-Base, the extrapolated checkpoints match or exceed full RLVR training on in-domain and out-of-domain benchmarks, and can predict checkpoints 10-20x beyond the observation window with continued improvement.

## What is new

The structural claim is sharp. RLVR weight updates are not low-dimensional only in some abstract sense; the dominant direction is rank-1, and the magnitude of the projection onto that direction increases near-linearly with steps. That is enough for a closed-form extrapolation: estimate the rank-1 subspace by SVD over a short observation prefix, fit a scalar magnitude trajectory by linear regression, and project forward. Higher subspace ranks do not help. Non-linear magnitude models do not help either. The ablation analysis confirms minimalist sufficiency.

The mechanism is described as "denoising": projecting RLVR updates onto the rank-1 subspace discards stochastic optimization noise that would otherwise degrade performance during extrapolation. The model is not learning new directions over training; RLVR's role is to walk further along a direction the pre-trained model already establishes.

## Why it matters

This is the second strong piece of evidence in three days that RLVR's role is narrower than the field assumed. The Unlearnability Phenomenon (today's companion paper, 2605.16787) showed from the failure side that a substantial subset of hard examples remains unlearnable even when correct rollouts are present, because the underlying representation is fundamentally wrong. RELEX shows from the success side that for examples RLVR does help on, the direction of help is essentially set in the first 15% of training. Together the two papers point at the same conclusion: RLVR is amplifying capabilities the pre-trained model already has, in a direction the model already knows, and what RLVR cannot do is teach the model new directions.

This connects directly to AntiSD (2026-05-20, ascending the KL divergence to fix teacher conditioning on already-implied tokens) and the Sparse-to-Dense Reward Principle (2026-05-13, the allocation rule between sparse-RL and OPD bridges). The wiki's reasoning-RL credit-assignment thread had been treating RLVR as a search procedure that improved through better credit signals; RELEX reframes it as an extrapolation along a fixed direction whose discovery time is short.

## Research angle

Three open questions are now load-bearing. First, the rank-1 claim is shown across three Qwen models in the 1.5B-8B range. Whether the rank-1 structure holds at frontier scale (30B+, MoE) decides whether RELEX is a small-model phenomenon or a substrate-level claim about RLVR. Second, if RLVR moves along a fixed rank-1 direction, what does the direction look like geometrically? Cross-task analysis of the rank-1 subspaces across math, code, and agentic RLVR would test whether the direction is universal (one direction shared across reward functions) or reward-specific (one direction per reward). Third, the extrapolation framing changes the cost calculus: pre-train compute is fixed and large, RLVR compute can drop by 5-7x via RELEX. The question becomes whether the savings can be spent on more pre-train (where RLVR's direction is determined) or on broader RLVR coverage (more reward functions, more domains).

The cross-paper composition: AntiSD plus CEPO during the observation window (faster step convergence, sharper credit) plus RELEX past the window (extrapolate the trajectory). The compound: a 4B reasoning RLVR run that reaches GRPO-trained-from-scratch parity at ~3-5% of the original compute budget. The diagnostic is whether the rank-1 direction AntiSD and CEPO induce remains the same as the rank-1 direction vanilla GRPO induces; if yes, the methods commute, if no, the early-window choice matters.

## Related wiki pages

- [Unlearnability Phenomenon in RLVR (2026-05-21)](2026-05-21-unlearnability-rlvr.md)
- [AntiSD (2026-05-20)](2026-05-20-antisd-anti-self-distillation-pmi-divergence-ascent.md)
- [CEPO (2026-05-20)](2026-05-20-cepo-contrastive-evidence-policy-optimization.md)
- [GFT: SFT as degenerate RL (2026-04-21)](2026-04-21-gft-sft-as-degenerate-rl.md)
- [VGF Value Gradient Flow (2026-04-19)](2026-04-19-vgf-value-gradient-flow-rl.md)
