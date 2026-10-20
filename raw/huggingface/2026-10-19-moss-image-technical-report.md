---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23374
url: https://huggingface.co/papers/2610.23374
arxiv_url: https://arxiv.org/abs/2610.23374
date: 2026-10-19
---

# MOSS-Image Technical Report

Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system that combines high-fidelity visual synthesis with intent-aware composition. First, we pretrain a 5B single-stream diffusion transformer (DiT) from scratch with a carefully designed recipe, enabling bilingual long-form text rendering and precise layout control. Second, we develop an intention-aware agentic prompt enhancement (PE) module that translates diverse user requests into detailed content and layout specifications. Together, they enable MOSS-Image to generate text-rich and layout-coherent images. We further introduce LongLongTextBench (LLTB) for evaluating long-form English and Chinese text rendering, and RealLayoutArena (RLA) for end-to-end layout-rich generation. MOSS-Image achieves state-of-the-art performance among open-weight models on LLTB, with an average text coverage of 96.3%. On RLA, MOSS-Image ranks second in the end-to-end system comparison, while its backbone ranks first among generators evaluated with shared enhanced prompts. We will release the model, training recipe, and evaluation framework to support further research and promote the text-to-image community.
