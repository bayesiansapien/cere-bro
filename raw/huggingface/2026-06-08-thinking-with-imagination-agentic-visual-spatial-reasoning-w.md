---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.06476
url: https://huggingface.co/papers/2606.06476
arxiv_url: https://arxiv.org/abs/2606.06476
date: 2026-06-08
---

# Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators

While Vision-Language Models (VLMs) have shown strong visual reasoning capabilities, their spatial reasoning abilities remain largely constrained to the observed images and text-oriented chain-of-thought. They often struggle to infer unobserved layouts, maintain cross-view consistency, and reason from alternative viewpoints when only limited egocentric observations are available. In this work, we study this problem as thinking with imagination, where a VLM actively acquires imagined visual evidence by interacting with a world simulator during reasoning. We propose Astra, an agentic spatial reasoning framework that empowers VLMs with action-conditioned visual imagination. Specifically, Astra couples Astra-VL, an RL-trained VLM policy, with Astra-WM, a Bagel-based world simulator that generates novel-view observations from context images and natural-language camera motions. To provide reliable imagined evidence, Astra-WM is trained with view consistency tuning to improve pose and content consistency across views. In the RL stage, we propose a world-simulator-in-the-loop two-phase RL curriculum to stabilize tool-use exploration and advance the model's ability to invoke the simulator only when imagined observations improve over direct answering. Experiments demonstrate that both the world simulator and the agentic policy are necessary: Astra-WM improves simulator-augmented Gemini-3-Flash on MMSI-Bench from 45.1 to 49.5, while Astra-VL improves the Qwen3-VL backbone from 29.8 to 38.8 on MMSI-Bench and from 36.8 to 42.7 on MindCube. These results show that imagined observations can provide useful spatial evidence, but effective world-model-augmented reasoning requires learning when, where, and how to imagine.
