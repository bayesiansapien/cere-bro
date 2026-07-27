---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.22393
url: https://huggingface.co/papers/2607.22393
arxiv_url: https://arxiv.org/abs/2607.22393
date: 2026-07-27
---

# SceneActBench: Can Agents Act on the 3D Scenes They See?

Vision-language model (VLM) agents increasingly use tools to act on 3D scenes rather than only describe them. Existing 3D benchmarks score textual responses or single-object operations, leaving agent action on complete multi-object 3D scenes under evaluated. We present SceneActBench, a benchmark for visually conditioned action across five 3D tasks under a unified agent-environment loop. Given PNG images or sampled video frames and, where applicable, supplied 3D assets, an agent acts on a 3D environment. We evaluate each final output against hidden ground truth with task-specific geometric metrics. SceneActBench comprises five tasks built from 210 source instances, yielding 520 task cases including paired input conditions. Every task runs through one fixed agent loop to keep the comparison fair. Across eleven proprietary VLM configurations, Overall scores span 38.6-50.2, and none performs consistently well across tasks. We further analyse where and how failures manifest.
