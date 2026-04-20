---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.16272
url: https://huggingface.co/papers/2604.16272
arxiv_url: https://arxiv.org/abs/2604.16272
date: 2026-04-20
---

# VEFX-Bench: A Holistic Benchmark for Generic Video Editing and Visual Effects

As AI-assisted video creation becomes increasingly practical, instruction-guided video editing has become essential for refining generated or captured footage to meet professional requirements. Yet the field still lacks both a large-scale human-annotated dataset with complete editing examples and a standardized evaluator for comparing editing systems. Existing resources are limited by small scale, missing edited outputs, or the absence of human quality labels, while current evaluation often relies on expensive manual inspection or generic vision-language model judges that are not specialized for editing quality. We introduce VEFX-Dataset, a human-annotated dataset containing 5,049 video editing examples across 9 major editing categories and 32 subcategories, each labeled along three decoupled dimensions: Instruction Following, Rendering Quality, and Edit Exclusivity. Building on VEFX-Dataset, we propose VEFX-Reward, a reward model designed specifically for video editing quality assessment. VEFX-Reward jointly processes the source video, the editing instruction, and the edited video, and predicts per-dimension quality scores via ordinal regression. We further release VEFX-Bench, a benchmark of 300 curated video-prompt pairs for standardized comparison of editing systems. Experiments show that VEFX-Reward aligns more strongly with human judgments than generic VLM judges and prior reward models on both standard IQA/VQA metrics and group-wise preference evaluation.
