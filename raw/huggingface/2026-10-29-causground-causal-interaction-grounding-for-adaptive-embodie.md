---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.926408+05:30
arxiv_id: 2610.29702
url: https://huggingface.co/papers/2610.29702
arxiv_url: https://arxiv.org/abs/2610.29702
date: 2026-10-29
---

# CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

Multimodal large language models (MLLMs) show promising reasoning capabilities, but reliable physical interaction requires planning that accounts for when actions are executable and how they change the world. These preconditions and effects are environment-dependent and often not captured by MLLMs, making adaptation challenging. Yet existing approaches either require costly environment-specific training or rely on unstructured interaction experience that is difficult to reuse. Therefore, we introduce CausGround, a non-parametric causal interaction grounding framework that distills interaction experience into reusable action-centered causal knowledge. CausGround identifies action preconditions and effects and organizes them in a factorized world-state representation capturing object attributes and inter-object relations. At planning time, task-relevant causal dependencies are grounded in current observations to support backward reasoning over preconditions and forward reasoning over effects for action selection and multi-step planning. We evaluate CausGround on simulated high-level planning, interaction reasoning, and real-world robot manipulation. On adapted VirtualHome and RoboCasa benchmarks, CausGround improves vision-based high-level planning across MLLM backbones, increasing average task success from 24.9% to 53.3% on VirtualHome and closed-loop planning success from 43.0% to 57.0% on RoboCasa. On SWITCH, average interaction reasoning accuracy increases from 25.8% to 31.9%, indicating improved action selection, recovery, and verification. Moreover, real-world experiments show that CausGround reasons backward from MLLM-interpreted goals to derive executable high-level action sequences for sequential manipulation. These results demonstrate that reusable action preconditions and effects support long-horizon embodied planning across diverse environments without parameter updates.
