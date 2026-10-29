---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993775+05:30
arxiv_id: 2610.36729
url: https://huggingface.co/papers/2610.36729
arxiv_url: https://arxiv.org/abs/2610.36729
date: 2026-10-28
---

# Hy-Nomas: Towards Free-form Interactive World Generation

Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interaction turns. It generates variable-length segments conditioned on current inputs and cached history. Our central design aligns structured video captions with action-aware causal attention: descriptive context remains accessible across segments, while action instructions are restricted to their intended temporal windows. A vision-language Prompt Enhancer (PE) translates user requests and multimodal interaction histories into structured conditions for the next segment. A multi-stage curriculum progressively introduces causal generation, text interaction, camera control, and training on model-generated histories, followed by diffusion distillation. In human evaluation, Hy-Nomas shows superior performance over existing world models. We release model weights, code and benchmarks, together with a lightweight adaptation workflow, to support reproducible research on interactive world generation.
