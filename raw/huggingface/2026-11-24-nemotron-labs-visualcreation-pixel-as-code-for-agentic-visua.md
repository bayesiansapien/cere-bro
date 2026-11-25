---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.919020+00:00
arxiv_id: 2611.31358
url: https://huggingface.co/papers/2611.31358
arxiv_url: https://arxiv.org/abs/2611.31358
date: 2026-11-24
---

# Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation

Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Raster images are represented by learned discrete visual tokens, while structured artifacts use explicit programs. A shared generation-and-rendering interface connects these representations to visual feedback across images, vector graphics, webpages, and documents. A Nemotron-native harness coordinates planning and raster candidate selection, with targeted repair for editable structured and hybrid artifacts. To support this interface, we develop Nemotron-Labs-Image-Tokenizer, the autoregressive raster generator Nemotron-Labs-Image-30B-A3B, and the structured-code model family Nemotron-Labs-VisionCode. On approximately 178K images spanning six visual domains, our tokenizer improves reconstruction PSNR from 26.08 to 29.57 dB over Emu3.5 IBQ. It also provides 7.13x faster encoding and 10.93x faster decoding at batch size one on A100. In standalone evaluation, one Nemotron-Labs-VisionCode variant surpasses Kimi K3.1 Pro on the aggregate across Chart2Code, MMSVG, Design2Code, and Image2Struct. At the system level, the Nemotron-native configuration raises GenEval2 Soft-TIFA GM from 31.71 to 52.56 using the same raster generator. With our best setting, Nemotron-Labs-VisualCreation achieves performance competitive with GPT Image 2 and Nano Banana Pro across most benchmarks with available comparisons.
