---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.001374+00:00
arxiv_id: 2611.18429
url: https://huggingface.co/papers/2611.18429
arxiv_url: https://arxiv.org/abs/2611.18429
date: 2026-11-16
---

# Do Underwater Image Quality Metrics Agree with Human Perception? A Benchmark with Human Choices, Simple Edits and Generative Drift

Underwater image enhancement is challenging to evaluate due to the lack of clean reference images, so researchers rely on no-reference image quality assessment (NR-IQA) metrics. However, it remains unclear whether these metrics agree with human judgments. We evaluate 73 handcrafted underwater, learned underwater, vision-language and general-purpose metrics against human preferences on five references: four published opinion-score sets and a new paired-comparison study. For each metric, we measure how often it selects the same image as people when comparing versions of the same scene. We further test whether simple image edits and small adversarial perturbations raise metric scores above the enhancement people preferred, and whether scores decrease as repeated generative edits add noise. Our results show that no metric consistently matches human preferences. The best worst-case Cohen's kappa over the five references is only 0.23 (Q-Align), while two raters in our study agree with a median kappa of 0.41. The widely used UCIQE often favors edits that people reject. On a Nano Banana Pro replica chain that should leave the image unchanged, only 22 of 73 scores decrease at every checkpoint, while noise grows by 2.5 times. We also introduce TrustUIQA, a benchmark that combines the human references, our study choices, the edited, attacked and generated images, and the scores of every metric on every image. The code is available at https://github.com/TrustUIQA/TrustUIQA and TrustUIQA at https://huggingface.co/datasets/TrustUIQA/TrustUIQA.
