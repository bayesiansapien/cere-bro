---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.902230+00:00
arxiv_id: 2611.34575
url: https://huggingface.co/papers/2611.34575
arxiv_url: https://arxiv.org/abs/2611.34575
date: 2026-11-26
---

# Sage-Med: Scaling Medical Multimodal Intelligence

Establishing effective scaling laws for medical multimodal large language models (MLLMs) remains a persistent and fundamental challenge. Our systematic evaluation shows that existing medical MLLMs tend to underperform frontier general-purpose MLLMs across a range of medical tasks, while scaling model size primarily improves text capabilities rather than multimodal perception, and enabling reasoning modes fails to close this visual gap. To investigate how medical multimodal intelligence scales in practice, we introduce Sage-Med-Preview, a 35B-parameter medical multimodal model with 3B activated parameters, built by combining stage-specific curation over 322.7 million candidate records with a progressive training curriculum spanning medical pretraining, staged supervised fine-tuning, and adaptive reinforcement learning. Across this curriculum, progressive supervised refinement and adaptive reinforcement learning yield consistent stage-wise gains, substantially advancing both specialized visual understanding and medical language capabilities. Evaluated against 77 competing models across 238 clinical tasks spanning 61 public and 13 private multi-center benchmarks in more than 40 modalities, Sage-Med-Preview achieves an average score of 58.26% on the 31 public multimodal benchmarks. It outperforms the state-of-the-art open-source medical model Hulu-Med-235B-A22B at 50.99% and the general scientific model Intern-S2-Preview at 52.24%, and approaches the advanced proprietary model GPT-6.2-Sol across multiple tasks such as comprehensive multimodal understanding, report generation, and visual grounding. Although substantial challenges remain in complex medical reasoning and multi-step clinical workflows, this report provides empirical evidence, actionable data and training recipes, and a rigorous benchmark toward scalable clinical multimodal intelligence.
