---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.02218
url: https://huggingface.co/papers/2608.02218
arxiv_url: https://arxiv.org/abs/2608.02218
date: 2026-08-05
---

# PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diversity with Editable Print-Ready Outputs

Scientific poster construction compresses a long multimodal paper into a readable, editable canvas. Existing systems hide request-level failures by scoring only completed outputs; direct image generation is not element-editable, while coding-agent workflows are costly. PosterMELD is a template-conditioned multi-agent pipeline: capacity-aware slots guide writing before rendering, and deterministic gates plus vision-language model (VLM) review route failures to bounded repair. Each accepted request exports editable PowerPoint (PPTX) and Portable Network Graphics (PNG) artifacts; explicit design controls yield same-paper variants. Across 621 papers, Print-Ready Rate (PRR) counts requests passing geometric, readability, asset-integrity, and obvious-factual-error checks, with native editability reported separately. A frozen VLM assigns conditional Craftsmanship-Harmony-Expressiveness (CHE) scores to print-ready outputs. PosterMELD attains 81.3% PRR, 3.4 times P2P's rate and 5.2 times PosterGen's, and the highest conditional CHE among generated methods with multiple print-ready outputs. Native editability and explicit design controls are retained at a mean cost of USD 0.38 per request, 3.5% of Codex+Skill's. Code and resources are available at https://github.com/Shannon4Science/PosterMELD.
