---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.33020
url: https://huggingface.co/papers/2611.33020
arxiv_url: https://arxiv.org/abs/2611.33020
date: 2026-11-25
---

# GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?

Despite strong performance on standard benchmarks, video reasoning models remain vulnerable to visual degradation, raising concerns about their reliability in safety-critical scenarios. Existing benchmarks address this concern in part by simulating visual degradation or probing model reasoning with challenging questions, leaving open how well models handle naturally degraded video and whether they can make the simpler judgments that matter for safe driving. To this end, we introduce GRAPE-Bench, which jointly evaluates video reasoning across visual degradation conditions and question difficulty. It combines a synthetic set spanning twelve corruption types across daily-life and driving videos with real-world footage of driving at night or in rain, snow, or fog. Each video is paired with three progressively challenging questions, from fundamental judgments with potential safety implications to demanding reasoning stress tests. Across open-weight and frontier models, we observe ranking reversals between synthetic and real-world conditions and level-specific weaknesses obscured by overall accuracy. Synthetic-data fine-tuning improves Qwen3.5-9B's real-world accuracy from 76.7% to 81.1%, while clean-privileged on-policy distillation reaches 80.4% in a separate reasoning-enabled setting. Through preference steering, we further demonstrate continuous control over a frozen model's trade-off between safety-relevant judgments and challenging reasoning, with little change in overall accuracy. Together, GRAPE-Bench provides a unified testbed for evaluating, improving, and controlling video reasoning under degraded visual conditions.
