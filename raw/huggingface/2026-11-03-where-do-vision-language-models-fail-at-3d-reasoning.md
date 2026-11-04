---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.39639
url: https://huggingface.co/papers/2610.39639
arxiv_url: https://arxiv.org/abs/2610.39639
date: 2026-11-03
---

# Where Do Vision Language Models Fail at 3D Reasoning?

Vision-language models can get individual judgments right while struggling to recover and consistently use the exact properties of a 3D object. To characterize this gap, we introduce BedBench, a controlled benchmark of thirteen procedurally generated tasks spanning individual judgments and composite answers. Across twelve open-weight and four frontier models, per-color counting exposes a pronounced weakness: humans achieve 93.3% accuracy, compared with 7.2% for the best model. Targeted fine-tuning raises one model's accuracy from 3.0% to 68.6%, but reveals a further difficulty: its answers about the most common colors remain inconsistent with its own per-color counts. Supplying those counts as text improves its judgments, showing that recovering a property does not mean using it consistently. Reasoning, scaling, and added visual cues each improve individual judgments, but none makes exact answers reliable. To locate the difficulty, we probe Qwen3.5-27B: exact per-color counts remain recoverable at the language model's input, yet the model's answers rarely recover them (65.0% for the probe vs. 3.0% for the model). Image-removal controls further show that some apparent successes require no visual evidence. These findings motivate evaluating 3D reasoning by exact correctness, consistent use, and image dependence, rather than accuracy alone. Code and dataset are publicly available: https://github.com/leduckhai/BedBench
