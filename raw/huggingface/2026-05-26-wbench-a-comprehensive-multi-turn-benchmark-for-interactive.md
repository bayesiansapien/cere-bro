---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.25874
url: https://huggingface.co/papers/2605.25874
arxiv_url: https://arxiv.org/abs/2605.25874
date: 2026-05-26
---

# WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation

Interactive world models are advancing rapidly, yet existing benchmarks cover only part of the required competencies, leaving no unified standard for systematic evaluation. To fill this gap, we introduce WBench, a comprehensive multi-turn benchmark for interactive world model evaluation along five dimensions, namely video quality, setting adherence, interaction adherence, consistency, and physics compliance. WBench contains 289 test cases and 1,058 interaction turns, where each case specifies a world setting and a multi-turn interaction sequence, covering diverse scenes, styles, subjects, and both first- and third-person perspectives, together with four interaction types, including navigation, subject action, event editing, and perspective switching. For navigation, WBench unifies text, 6-DoF pose, and discrete-action control, enabling evaluation of models with different native input interfaces. Evaluation uses 22 automatic sub-metrics that combine specialist vision models with large multimodal models, and all metrics are validated against human judgments. Across 20 state-of-the-art models, we find that no single model performs strongly across all dimensions. We provide detailed diagnostic insights into the characteristic strengths, weaknesses, and open challenges of each model. Code and data are available at https://github.com/meituan-longcat/WBench.
