---
source: farmer/huggingface
farmed: 2026-05-20T09:54:52.691938+00:00
arxiv_id: 2605.18748
url: https://huggingface.co/papers/2605.18748
arxiv_url: https://arxiv.org/abs/2605.18748
date: 2026-05-20
---

# Aurora: Unified Video Editing with a Tool-Using Agent

Recent video editing models have converged on a unified conditioning design: a single diffusion transformer jointly consumes text, source video, and reference images, and one set of weights covers replacement, removal, style transfer, and reference-driven insertion. The design is flexible, but it assumes that the user already provides model-ready text, reference images, and spatial grounding for local edits, which real requests often omit. We present Aurora, an agentic video editing framework that pairs a tool-augmented vision-language model (VLM) agent with a unified video diffusion transformer. The VLM agent maps a raw user request to a structured edit plan aligned with the transformer&#39;s conditioning channels, thereby resolving textual and visual underspecification before generation. We train the VLM agent with supervised data for complete edit planning and reference-image selection, together with preference pairs for robust tool use and instruction refinement. We introduce AgentEdit-Bench to evaluate agent-enhanced video editing under textual and visual underspecification. Experiments on AgentEdit-Bench and two existing video editing benchmarks show that Aurora improves over instruction-only baselines and that the VLM agent transfers to compatible frozen video editing models. Project page: this https URL
