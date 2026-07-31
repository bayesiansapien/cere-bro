---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28595
url: https://huggingface.co/papers/2607.28595
arxiv_url: https://arxiv.org/abs/2607.28595
date: 2026-07-31
---

# Beacon: Knowing When and How to Perform Agentic Visual Reasoning

The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool use: Mode Adaptiveness (MA) and Tool Effect (TE). Mode Adaptiveness characterizes whether an MLLM can recognize when tools are truly necessary and invoke them accordingly, thereby avoiding unnecessary computational overhead while improving performance on challenging problems that require tool assistance. Tool Effect characterizes the actual impact of tool use: tools should extend the model's capabilities on problems unsolvable through text-only reasoning, while avoiding additional errors on problems that the model can already solve without tools. We conduct a comprehensive analysis to quantify these two properties and empirically reveal that existing agentic visual reasoning models exhibit limited Mode Adaptiveness, while the gains produced by tool use on hard examples are largely offset by the harm introduced on easy examples that the models can already solve. Motivated by these observations, we propose Beacon, a novel agentic visual reasoning model that achieves stronger overall performance, improved Mode Adaptiveness, and genuine tool-induced performance gains. At the core of Beacon are the Necessity-Aware Adaptive Reward and the Hint-Guided Capability Expansion mechanism in the reinforcement learning stage, which respectively encourage adaptive tool invocation based on task necessity and strengthen the model's tool-use capability on the most challenging problems. Extensive experiments across diverse benchmarks demonstrate the strong overall performance of Beacon and its substantial improvements in both Mode Adaptiveness and Tool Effect.
