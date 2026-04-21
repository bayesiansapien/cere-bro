# GFT: SFT is Degenerate Policy Gradient — and Group Fine-Tuning Fixes It

**Date:** 2026-04-21  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.14258](https://arxiv.org/abs/2604.14258)  
**Raw:** [raw/huggingface/2026-04-21-gft-from-imitation-to-reward-fine-tuning-with-unbiased-group.md](../../raw/huggingface/2026-04-21-gft-from-imitation-to-reward-fine-tuning-with-unbiased-group.md)

---

## TL;DR

GFT shows mathematically that supervised fine-tuning (SFT) is a special case of policy gradient optimization — but a pathological one: implicit reward is maximally sparse (only correct completions get signal), probability weighting is unstable (high-probability tokens get upweighted, causing gradient explosion), and optimization collapses to single-path dependency. Group Fine-Tuning repairs this with (1) group advantage learning (generate diverse responses, derive contrastive supervision) and (2) dynamic coefficient rectification (bound the inverse-probability weights). GFT consistently outperforms SFT and integrates more smoothly with subsequent RL training.

---

## Key Findings

- **SFT's three pathologies** diagnosed as RL failures:
  1. **Reward sparsity**: SFT assigns full reward to correct outputs and zero to others — implicit reward is a Dirac delta
  2. **Inverse-probability instability**: the policy gradient weight is 1/π(a|s) — high-confidence (high π) outputs get down-weighted, low-confidence outputs get upweighted, creating unstable gradients
  3. **Single-path dependency**: SFT trains on one reference output per input, so the policy collapses toward that path and fails to explore
- **Group Advantage Learning**: generates a diverse group of responses per input, computes normalized contrastive advantages — similar to GRPO's group relative policy optimization, but unified with the SFT objective
- **Dynamic Coefficient Rectification**: adaptively bounds the inverse-probability weight to prevent explosion while preserving knowledge injection
- **Results**: consistently beats SFT across multiple benchmarks; the downstream RL training that follows GFT converges faster and to higher performance than RL following standard SFT

---

## Why It Matters for the Wiki

This is the third paper in a week making the same structural argument from different directions:

| Paper | Claim |
|-------|-------|
| PreRL (04-16) | Standard RL on P(y\|x) is ceiling-limited by the base model — optimize P(y) instead |
| VGF (04-19) | Don't parameterize a policy at all — use optimal transport on particles |
| GFT (04-21) | SFT is broken RL — fix it with group contrastive supervision |

All three are saying the same thing: the standard SFT → RL pipeline is suboptimal at a fundamental level, not just an engineering level. GFT is the most practically deployable of the three: it's a drop-in replacement for SFT that needs no RL machinery and produces better post-training checkpoints.

---

## Open Questions

- Does GFT's benefit hold at frontier scale (70B+)? The experiments appear to be on smaller models.
- The "integrates smoothly with subsequent RL" claim is important: does GFT checkpoint initialization specifically help GRPO/DAPO convergence, or just any RL fine-tuning?
- GFT and GRPO are architecturally similar (both use group relative advantages). The key difference is that GFT's groups come from diverse generation during fine-tuning, while GRPO's come from on-policy rollouts during RL. Could they be unified into a single training phase?

---

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [PreRL/DSRL: RL in Pretrain Space](2026-04-16-prerl-rl-in-pretrain-space.md)
- [VGF: Value Gradient Flow](2026-04-19-vgf-value-gradient-flow-rl.md)
