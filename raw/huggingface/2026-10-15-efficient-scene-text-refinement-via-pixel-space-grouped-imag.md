---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227603+05:30
arxiv_id: 2610.18284
url: https://huggingface.co/papers/2610.18284
arxiv_url: https://arxiv.org/abs/2610.18284
date: 2026-10-15
---

# Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation

Generated images often have coherent layouts and visual content, yet local errors in small text and complex characters still limit their readability and practical use. Scene-text refinement requires accuracy, preservation, and efficiency. Existing methods based on variational autoencoders (VAEs) can lose fine strokes during reconstruction, while full-image editing can shift background colors. In this work, we introduce PixText, a model that formulates local text refinement as grouped image generation in pixel space. Conditioned on the original image, PixText generates only the target regions, preserves unedited content, and uses MeanFlow for four-step generation. We further introduce Text Refinement Bench to evaluate text correction and image preservation in generated images. On this benchmark, PixText achieves 83.06% glyph pass and 94.66% exact target-character OCR accuracy, versus 36.77% and 52.31% for the strongest baseline. Its four-step MeanFlow variant retains an 81.84% pass rate with less than one GPU-second of amortized generation cost per image.
