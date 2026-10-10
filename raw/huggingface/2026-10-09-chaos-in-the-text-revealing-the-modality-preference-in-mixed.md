---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417052+00:00
arxiv_id: 2610.11816
url: https://huggingface.co/papers/2610.11816
arxiv_url: https://arxiv.org/abs/2610.11816
date: 2026-10-09
---

# Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers

Dense retrievers have made significant progress on text and image corpora, but whether these capabilities extend reliably to mixed corpora containing text, image, and fused text-image documents remains unclear. In this paper, we systematically examine retrievers across architectures and find that their performance is highly sensitive to modality composition. As image documents are progressively replaced with semantically corresponding text representations, retrieval performance follows a pronounced V-shaped curve, remaining strong on single-modality corpora but degrading substantially when modalities coexist. In particular, irrelevant text causes more severe degradation than an equal number of irrelevant images, a phenomenon we term Chaos in the Text. Further analysis reveals modality preference, whereby text representations receive systematically higher similarity scores, allowing irrelevant text to outrank relevant images. To mitigate this bias, we introduce Trident, which constructs text, image, and fused text-image views of each document as co-equal positives and jointly optimizes relevance discrimination and positive-view balance through Multi-Positive View InfoNCE. Experiments across visual document and natural image benchmarks show that trident improves mixed-modality retrieval on both CLIP-based and VLM-based architectures, reduces sensitivity to modality composition and text distractors, and increases average single-modality retrieval performance.
