---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.26809
url: https://huggingface.co/papers/2608.26809
arxiv_url: https://arxiv.org/abs/2608.26809
date: 2026-08-28
---

# Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning

While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge. Naive chunking strategies, e.g., fixed-duration segmentation, often lead to entity fragmentation, severe editing hallucinations, and disrupted temporal continuity. To bridge this gap, we introduce the Multi-Instruction Multi-Shot Long-Video Editing (MMLVE) task, which is structured around three core objectives: Cross-Shot Editing Consistency (CSEC), Multi-Instruction Decoupling (MID), and Zero-Destruction on Spatiotemporal Structure (ZDSS). To tackle these three unique challenges, we introduce an agentic editing framework that leverages the synergy of Large Language Models (LLMs) and Vision-Language Models (VLMs) to achieve shot-level video decoupling and precise instruction parsing. Furthermore, to comprehensively evaluate this task, we construct MMLVE-Bench, which is an MMLVE-focused dataset characterized by complex real-world spatiotemporal dynamics, high-density heterogeneous instructions, and sparse, random entity distributions. Three MMLVE-focused evaluation metrics are further exploited to assess the quality of the editing results. Extensive experiments demonstrate that our MMLVE-Agent outperforms existing closed-source SOTA approaches (e.g., Seedance 2.0), successfully eliminating editing hallucinations, preserving cross-shot editing consistency, and attaining seamless spatiotemporal transitions.
