---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.162137+00:00
arxiv_id: 2610.38681
url: https://huggingface.co/papers/2610.38681
arxiv_url: https://arxiv.org/abs/2610.38681
date: 2026-10-30
---

# Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large Reasoning Models

Self-distillation offers a way to improve reasoning models when a suitable external teacher is unavailable. However, common approaches rely on privileged information to construct a stronger self-teacher, limiting their use when only unlabeled prompts are available. In this paper, we introduce Weakening-Induced On-Policy Self-Distillation (WISD), which instead constructs a weaker counterpart of the original model and uses the contrast between the two as a training signal without requiring privileged information. We explore two ways to construct the weaker model: low-bit quantization and magnitude pruning. We evaluate WISD across diverse architectures and scales on mathematical and coding reasoning tasks. Across these benchmarks, quantization and pruning improve average accuracy over the original models by 4.0 and 5.5 percentage points, respectively, achieving state-of-the-art performance even without privileged information. Notably, pruning raises Qwen3.5-4B's accuracy from 57.7% to 70.5% on HMMT 2025 and from 39.1% to 56.7% on LiveCodeBench v6. Quantization raises Qwen3.6-35B-A3B's accuracy from 68.5% to 74.6% and from 61.8% to 69.5% on the same benchmarks, respectively. These results establish WISD as a novel and effective self-distillation framework for large reasoning models.
