---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.413831+00:00
arxiv_id: 2610.12343
url: https://huggingface.co/papers/2610.12343
arxiv_url: https://arxiv.org/abs/2610.12343
date: 2026-10-09
---

# Reasoning-Informed Visual Editing

Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but still face challenges in visual editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input formats. To study this gap, we introduce RISEBench, the first benchmark for evaluating Reasoning-Informed viSual Editing (RISE), and extend it to RISEBench++, a more comprehensive and fine-grained benchmark for this emerging task. RISEBench++ extends the taxonomy into a hierarchical scheme spanning six reasoning dimensions: Temporal, Causal, Spatial, Logical, and Counterfactual Reasoning, together with Hybrid Reasoning integrating multiple reasoning types across multi-turn edits. These dimensions are further decomposed into 12 subcategories and 65 fine-grained task types. We expand input formats to include multi-image conditioning and scale the benchmark to 1000 human-annotated test cases, released in English and Chinese. We also improve our evaluation framework, assessing Instruction Reasoning, Appearance Consistency, and Visual Plausibility with human judges and an LMM-as-a-judge approach for more reliable and calibrated judgements. Beyond benchmarking, we introduce RISE-Agent, a training-free agentic framework integrating reasoning-driven planning, tool-augmented execution, and verifier-guided refinement, outperforming most strong existing approaches across diverse RISE tasks. We evaluate 58 visual editing approaches, including 34 open-source models, 19 closed-source models, and 5 agentic methods. The results reveal substantial challenges in reasoning-based visual editing, with even the strongest evaluated approach, GPT-Image-2.5 Sunburst, achieving only 56.6% accuracy. RISEBench++ highlights the limitations of contemporary editing models, provides insights, and indicates future directions for reasoning-aware visual editing.
