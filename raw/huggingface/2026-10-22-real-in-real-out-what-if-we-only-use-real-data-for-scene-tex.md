---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.191676+00:00
arxiv_id: 2610.27592
url: https://huggingface.co/papers/2610.27592
arxiv_url: https://arxiv.org/abs/2610.27592
date: 2026-10-22
---

# Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?

Aiming to modify textual content while preserving the original style, Scene Text Editing (STE) has significant practical value in many applications. STE typically requires paired images before and after editing for training. However, recent approaches rely heavily on synthetic paired data and complex disentanglement strategies. They struggle to faithfully capture the diversity and complexity of natural scenes, often producing artifacts or hallucinations. In this work, we challenge the common practice and investigate whether STE can be driven by turning each real sample into its own paired supervision. Concretely, we explore multiple ways to disrupt the original image (e.g., Crop, Shuffle, Mask) to construct self-paired training data, and build a strong baseline (TextRIRO}) upon a conditional diffusion architecture. Our experiments show that combining character-column shuffling with image cropping (Shuffle&Crop) effectively destroys text semantics while preserving key style cues, enabling the model to learn editing behaviors directly from the real text image. With this concise yet real-oriented design, TextRIRO achieves promising performance in both accuracy and visual realism across real-world benchmarks, substantially mitigating the synthetic-to-real domain gap. Furthermore, we leverage TextRIRO to build TextRIRO-3M, a large-scale realistic dataset for long-text recognition by concatenating edited and original images. Experimental results show that training recognition models with TextRIRO-3M significantly improves recognition accuracy, demonstrating that TextRIRO provides highly useful training resources for downstream tasks. Overall, TextRIRO lifts STE to realistic, reliable, and widely applicable new levels. Code is available at https://github.com/YesianRohn/TextRIRO.
