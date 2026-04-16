---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13515
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13515
published: 2026-04-16
authors: Xiaole Su, Kasey Zhang, Andy Lyu
---

# SFT-GRPO Data Overlap as a Post-Training Hyperparameter for Autoformalization

**arXiv:** https://arxiv.org/abs/2604.13515
**Authors:** Xiaole Su, Kasey Zhang, Andy Lyu

## Abstract

arXiv:2604.13515v1 Announce Type: cross  Abstract: Supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) is a common post-training recipe. We conduct a controlled ablation over SFT-GRPO data overlap, evaluating Qwen3-8B (thinking disabled) post-trained for Lean 4 autoformalization under six conditions that differ solely in training recipe: a base model, SFT-only, GRPO-only, and three SFT+GRPO configurations where 0 percent, 30 percent, or 100 percent of the GRPO prompts coincide with the SFT corpus. Keeping SFT and GRPO data disjoint consistently outperforms full overlap at zero additional compute cost. Evaluating on Gaokao-Formal and PutnamBench under both compile pass at k and semantic pass at k assessed by an LLM judge, we find that lower overlap is monotonically associated with higher compilation and semantic accuracy. At 0 percent overlap, GRPO yields a 10.4 percentage point semantic gain over SFT alone on Gaokao, while at 100 percent overlap both metrics remain flat, rendering the GRPO stage effectively redundant. We further show that dual-metric evaluation reveals compile semantic gaps exceeding 30 percentage points for the highest compiling models, a disparity invisible under compile-only benchmarking. To our knowledge, this is the first controlled investigation of SFT-GRPO data overlap as a post-training hyperparameter, demonstrating how model behavior varies based on the degree of data sharing between training stages.
