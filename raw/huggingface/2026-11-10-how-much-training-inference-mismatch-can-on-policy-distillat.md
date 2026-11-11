---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.324535+00:00
arxiv_id: 2611.11450
url: https://huggingface.co/papers/2611.11450
arxiv_url: https://arxiv.org/abs/2611.11450
date: 2026-11-10
---

# How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?

On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher. Generating these responses is expensive, so systems use quantized inference and asynchronous rollouts to reduce the cost. Both, however, introduce training-inference mismatch between the rollout engine and the model being trained. Such mismatch can destabilize reinforcement learning (RL), but its effects on OPD remain unclear. This paper investigates how much mismatch OPD tolerates, where its effects arise, and how training systems can use this tolerance. Measuring all mismatch sources on one scale, we examine quantization across three student-teacher pairs, with additional tests of weight staleness and injected noise on one pair. OPD tolerates substantial mismatch without meaningful loss of training quality but degrades at higher levels, revealing an empirical mismatch budget. Both the quality cost of mismatch and the mismatch introduced by quantization depend on the model, with some layers particularly sensitive to reduced precision. In controlled comparisons, OPD remains stable under rollout configurations that destabilize RL methods. Under weight noise, mismatch also shifts the prefixes reached during generation, introducing errors that per-token corrections cannot address. To put these findings into practice, we introduce a lightweight admission check that screens rollout configurations against a calibrated budget without requiring a full training run for each candidate. Model-specific FP8 recipes preserve training quality while providing capacity for at least 1.93times as many KV-cache tokens as BF16. Combining FP8 with asynchronous rollouts reaches the same training quality 1.62times sooner than synchronous BF16 training. Code is available at https://github.com/benyucong/train-inference-mismatch-opd
