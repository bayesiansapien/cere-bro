---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.05979
url: https://huggingface.co/papers/2606.05979
arxiv_url: https://arxiv.org/abs/2606.05979
date: 2026-06-06
---

# World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis

We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions, conjoining the world modeling interface to learn from extensive egocentric videos as in the world-action model (WAM) and the language reasoning capacities to solve complex long-horizon tasks as in vision-language-action (VLA) models. At the core of WLA lies an autoregressive (AR) Transformer backbone, instead of a bidirectional diffusion Transformer as in WAMs, to predict the next state, comprising the semantic-level textual intention and complementary fine-grained physical dynamics. The physical dynamics are supervised by the world modeling objective based on a dedicated World Expert, and are leveraged to ease the characterization of the state-action correlation for the Action Expert. WLA leverages meta-queries to make the world prediction implicitly impact the action generation so that the former can be disabled during inference. The world prediction can also be activated to enable test-time scaling for improved robot control. Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090. Evaluations across simulated and real-world environments demonstrate that WLA-0 achieves state-of-the-art multi-task and long-horizon learning abilities, e.g., 92.94\% success rate on RoboTwin2.0 Clean and 56.5\% success rate on RMBench. WLA-0 also holds the promise to learn novel tasks directly from cross-embodiment robot videos without action annotations.
