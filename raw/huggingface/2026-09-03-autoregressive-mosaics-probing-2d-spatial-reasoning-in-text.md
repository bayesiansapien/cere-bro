---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.30751
url: https://huggingface.co/papers/2608.30751
arxiv_url: https://arxiv.org/abs/2608.30751
date: 2026-09-03
---

# Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models

Large language models (LLMs) trained only on text and code can sometimes generate programs that draw recognizable images. However, it is unclear whether this reflects an internal representation of 2D spatial layout or simply the ability to translate spatial descriptions into code. We introduce Autoregressive Mosaics (AM-Bench), a benchmark that separates these factors: First, a translation task gives a model a fully specified geometry of a picture in words as a prompt and asks for the code that produces it. Second, a layout task requires the model to compose an image from an underspecified prompt. Across eight open-weight text-and-code-only models, all models reliably translate specified geometry into code, but their open-ended layout performance differs substantially, indicating that these differences are not explained by code-generation ability alone. An output-medium ablation further shows that the interface or medium of expression that the model uses matters: replacing procedural code with raw SVG improves layout scores across all models. Finally, probing model activations shows that a coarse layout plan is present before generation, but reflects only the layout implied by the prompt. During generation, models track the evolving geometric state instead of executing an initially fixed plan. Overall, these results show that 2D spatial performance in text-only LLMs depends on both the model and the output medium, and is not explained by code-generation ability alone.
