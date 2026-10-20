---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22602
url: https://huggingface.co/papers/2610.22602
arxiv_url: https://arxiv.org/abs/2610.22602
date: 2026-10-19
---

# Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models

Retrieval is a fundamental task in multimodal systems: given an image or text query, the goal is to find the most relevant images or texts in a collection, often using a shared embedding space. Reliable retrieval requires these embeddings to capture not only which concepts are present, but also how they are composed. One key compositional challenge is attribute--object binding: encoding which attributes belong to which objects. Existing benchmarks provide a limited view of this capability, typically covering a subset of modality pairings, simple two-object swaps, or small attribute sets. Consequently, it remains unclear how robustly current models preserve attribute--object bindings across different modality pairings and more complex settings. We therefore introduce SABER, a controlled benchmark for evaluating attribute--object binding across all four image and text modality pairings, spanning diverse attribute types and scenes with up to ten objects. Evaluating models on SABER reveals substantial binding failures in both CLIP-style dual encoders and recent MLLM-based embedders. These findings motivate us to ask how binding can be improved efficiently. While multimodal supervision may be effective, collecting suitable images is difficult and costly. Text, on the other hand, is well suited to binding supervision: it is cheap to generate, supports a broader range of attributes and enables precisely controlled hard negatives. We thus finetune an MLLM-based embedder exclusively on synthetic attribute-binding text. Despite the absence of image supervision, the gains transfer to cross-modal and image--image retrieval while preserving general multimodal embedding performance. Our model achieves SOTA results on SABER while also improving on negation and instance-retrieval benchmarks, demonstrating broader benefits of our binding-focused supervision.
