---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.421603+00:00
arxiv_id: 2610.02959
url: https://huggingface.co/papers/2610.02959
arxiv_url: https://arxiv.org/abs/2610.02959
date: 2026-10-09
---

# TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows

Recent text-to-image models have made substantial progress in photorealism, aesthetics, and text-image alignment. Yet visually appealing images can still violate real-world plausibility, exhibiting malformed object structures, impossible anatomy, physically implausible interactions, or inconsistent spatial relationships. Such failures are not well captured by existing fidelity, aesthetics, preference, or alignment metrics. To address this gap, we introduce TerraVis, a framework for evaluating world-grounded visual consistency in generated images. TerraVis defines a structured taxonomy of world-consistency violations spanning object-, interaction-, and scene-level failures, and employs a multi-stage evaluation framework to identify and quantify them. Given an image, TerraVis first uses an MLLM to assess its eligibility for evaluation, then detects violations across 18 taxonomy-defined types and classifies them as minor or major to derive an overall world-consistency score. Across diverse open-source and proprietary text-to-image models on two widely used benchmarks, TerraVis achieves the strongest correlation with human judgments of world consistency among existing metrics. Our benchmark results further show that models that achieve strong performance on conventional metrics can still exhibit substantial world-consistency failures. These findings highlight world consistency as a complementary evaluation dimension and demonstrate that TerraVis enables systematic quantification, diagnosis, and comparison of such failures. Our code is publicly available at https://github.com/ShyFoo/TerraVis.
