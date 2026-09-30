---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930123+00:00
arxiv_id: 2609.33780
url: https://huggingface.co/papers/2609.33780
arxiv_url: https://arxiv.org/abs/2609.33780
date: 2026-09-29
---

# Selecting Diverse SFT Traces Improves Post-RL Generalization

Verified solutions are not equally useful for preparing reasoning models for reinforcement learning (RL). We present a comprehensive study of route diversity, the variation in the sequences of reasoning steps in supervised fine-tuning (SFT) data, and propose a lightweight, rule-based fingerprint to select for it. From one pool at one budget, with matched training recipes and checkpoints, selecting diverse rather than similar routes improves post-RL problem coverage across puzzles and mathematics, including on problems harder than those seen in either training stage. In synthetic experiments, route-diverse SFT improves OLMo3-7B's pass@8 by 16.9 points on environments held out from SFT. In a single-model condition, where one model writes every candidate, diverse selection gains up to 6.2 points of mean pass@8 across 10 mathematics benchmarks. Pre-RL diagnostics suggest why: diverse SFT can produce both successful and failed attempts on more prompts despite slightly lower mean accuracy, giving group-relative RL more prompts with a learning signal. On 3 open-source corpora, our CPU-only selector, without model calls, outperforms more expensive alternatives in every comparison of mean post-RL performance. These results identify reasoning-route diversity as a practical criterion for selecting SFT data that better prepares models for RL.
