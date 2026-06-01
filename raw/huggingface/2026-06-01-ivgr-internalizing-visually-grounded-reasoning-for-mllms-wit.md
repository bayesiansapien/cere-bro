---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.31096
url: https://huggingface.co/papers/2605.31096
arxiv_url: https://arxiv.org/abs/2605.31096
date: 2026-06-01
---

# iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning

While visually grounded Chain-of-Thought (CoT) has emerged as a promising paradigm to enhance fine-grained perception in multimodal large language models (MLLMs), its efficacy during the inference phase remains underexplored. In this work, we empirically find that mandating explicit object boxes in visually grounded CoT during inference often degrades performance compared to standard textual CoT, which reasons without explicit visual grounding. We hypothesize that the visual localization capability can be internalized into the textual CoT and that the mandatory explicit grounding introduces unnecessary interference with the model's primary objective of answer prediction. To address this problem, we propose Internalizing Visually Grounded Reasoning (iVGR), a novel reinforcement learning framework that transfers localization capabilities into the textual reasoning process. We employ a dual-stream training strategy, where a textual stream is aligned with a high-quality visually grounded stream via a proposed consistency reward, enabling the model to localize accurately without explicit grounding during inference.
