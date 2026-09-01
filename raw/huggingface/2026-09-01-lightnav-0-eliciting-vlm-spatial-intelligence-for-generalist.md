---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30935
url: https://huggingface.co/papers/2608.30935
arxiv_url: https://arxiv.org/abs/2608.30935
date: 2026-09-01
---

# LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation

Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, spatial reasoning, and pointing, but these capabilities are rarely elicited directly for robot control. Existing navigation systems instead rely on task- or embodiment-specific components, fragmenting perception, reasoning, and action while offering limited generalization. Here we present LightNav-0, a compact generalist embodied navigation model that elicits the spatial intelligence of a pretrained VLM and aligns it with navigation, without task-specific prediction heads. LightNav-0 represents diverse navigation tasks through a unified token interface: dual-channel pointing expresses task-, scene-, and embodiment-agnostic spatial intent, while a residual vector-quantized action tokenizer maps this intent to precise, embodiment-specific trajectories. Together with temporally aware visual history compression, ER mid-training, supervised fine-tuning, and reinforcement learning, this formulation supports instruction following, open-vocabulary object navigation, and visual tracking within a single model. The navigation training corpus spans 2K+ scenes and 4K+ hours of embodied navigation data. LightNav-ER, the embodied-reasoning checkpoint used to initialize LightNav-0, attains the highest complete-set average across 8 embodied-reasoning benchmarks, while LightNav-0 achieves state-of-the-art monocular success rates across all 10 public navigation simulation settings. Real-world evaluations further demonstrate zero-shot generalization across robot embodiments, diverse scenes, and static and dynamic targets. These results establish compact VLMs as a unified and transferable backbone for generalist embodied navigation.
