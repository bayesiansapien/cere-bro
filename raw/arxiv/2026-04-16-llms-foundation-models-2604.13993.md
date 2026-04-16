---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13993
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13993
published: 2026-04-16
authors: Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana
---

# Reward Design for Physical Reasoning in Vision-Language Models

**arXiv:** https://arxiv.org/abs/2604.13993
**Authors:** Derek Lilienthal, Manisha Mukherjee, Sameera Horawalavithana

## Abstract

arXiv:2604.13993v1 Announce Type: new  Abstract: Physical reasoning over visual inputs demands tight integration of visual perception, domain knowledge, and multi-step symbolic inference. Yet even state-of-the-art Vision Language Models (VLMs) fall far short of human performance on physics benchmarks. While post-training algorithms such as Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) have demonstrated strong reasoning gains in language models, how reward design shapes VLM physical reasoning behavior remains poorly understood. We present a systematic reward ablation study for GRPO-based VLM training on physical reasoning. We compare four reward signals of increasing semantic richness: format compliance, answer accuracy, a composite rubric reward (answer correctness, physics principle identification, and unit consistency), and a novel internal reward derived from model attention weights over input image regions. We evaluate on PhyX, a 3,000-problem benchmark spanning six physics domains and six reasoning types across multiple-choice and open-ended formats, using IBM Granite Vision 3.3 (2B). Across both formats, GRPO with accuracy-based rewards outperforms SFT on most domains, though gains vary substantially by reward type and domain. Reward design does not uniformly improve performance. Instead, it induces domain-specific reasoning behaviors. Accuracy-based rewards provide the strongest overall gains. Rubric rewards improve structured reasoning quality without consistent accuracy improvements. Attention-based rewards enhance spatial reasoning while degrading performance in symbolic domains. Our internal attention-weight reward requires no spatial annotations and improves spatial relation accuracy from 0.27 to 0.50, suggesting that supervising where the model attends during generation is a promising direction for visually grounded physical reasoning.
