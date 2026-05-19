---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.16865
url: https://huggingface.co/papers/2605.16865
arxiv_url: https://arxiv.org/abs/2605.16865
date: 2026-05-19
---

# MixSD: Mixed Contextual Self-Distillation for Knowledge Injection

Supervised fine-tuning (SFT) is widely used to inject new knowledge into language models, but it often degrades pretrained capabilities such as reasoning and general-domain performance. We argue this forgetting arises because fine-tuning targets from humans or external systems diverge from the model's autoregressive distribution, forcing the optimizer to imitate low-probability token sequences. To address this problem, we propose MixSD, a simple external-teacher-free method for distribution-aligned knowledge injection. Instead of training on fixed targets, MixSD constructs supervision dynamically by mixing tokens from two conditionals of the base model itself: an expert conditional that observes the injected fact in context, and a naive conditional that reflects the model's original prior. The resulting supervision sequences preserve the factual learning signal while remaining substantially closer to the base model's distribution. We evaluate MixSD on two synthetic corpora that we construct to study factual recall and arithmetic function acquisition in a controlled setting, together with established benchmarks for open-domain factual question answering and knowledge editing. Across multiple model scales and settings, MixSD consistently achieves a better memorization-retention trade-off compared to SFT and on-policy self distillation baselines, retaining up to 100% of the base model's held-out capability while maintaining near-perfect training accuracy, whereas standard SFT retains as little as 1%. We further show that MixSD produces substantially lower-NLL supervision targets under the base model and reduces harmful movement along Fisher-sensitive parameter directions. These results suggest that aligning supervision with the model's native generation distribution is a simple and effective principle for knowledge injection that mitigates catastrophic forgetting.
