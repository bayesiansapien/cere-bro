---
source: farmer/huggingface
farmed: 2026-09-23T14:55:25.993402
arxiv_id: 2609.25267
url: https://huggingface.co/papers/2609.25267
arxiv_url: https://arxiv.org/abs/2609.25267
date: 2026-09-23
---

# ImIR: Image-Instruction Tuning for All-in-One Image Restoration

Degradations vary widely across images, so a practical restoration system has to handle many degradation types with one model. A recent and effective recipe adapts a large pretrained image-editing model to restoration using a small low-rank adapter with a text prompt. We replace that prompt with an instruction derived from the degraded image itself. The image reaches the editor through two paths: its structure comes from the model's VAE, and its semantic instruction comes from a lightweight token mapper that shifts the degraded image's vision-language embedding toward the embedding a clean image would produce. Because the instruction is a continuous vector, scaling it yields a family of valid restorations for tasks whose target is not unique, such as low-light enhancement. We adapt one Qwen-Image-Edit model to six tasks with a single adapter trained in about three hours on one GPU. The image instruction outperforms text conditioning under a matched comparison, and it supports task agnostic restoration without a degradation label, which the text variant does not.
