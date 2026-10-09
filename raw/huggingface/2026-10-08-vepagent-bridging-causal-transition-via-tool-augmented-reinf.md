---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.302704+05:30
arxiv_id: 2610.06293
url: https://huggingface.co/papers/2610.06293
arxiv_url: https://arxiv.org/abs/2610.06293
date: 2026-10-08
---

# VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction

Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented reinforcement learning (RL) for robust VEP. Unlike prior methods that passively project future trajectories from historical dependencies, our approach explicitly models the logical progression from terminal observed states to future events. Specifically, we first construct futurebench-4K, a high-quality chain-of-thought dataset for supervised fine-tuning (SFT) that effectively bridges the causal-logic gap by structuring the deduction of unobserved intermediate states. Subsequently, we develop a diagnostic tool library integrating state tracking, frame retrieval, and region magnification, enabling the agent to dynamically augment reasoning with external tools to recover missing spatio-temporal evidence and resolve visual ambiguities during inference. Moreover, we propose a composite reward mechanism that jointly optimizes prediction accuracy, causal coherence, and reliable prior, compelling the agent to rely on genuine visual grounding rather than superficial textual similarities. Extensive evaluations on FutureBench and NEPBench datasets demonstrate that our method achieves state-of-the-art performance, significantly outperforming larger MLLMs and validating the empirical effectiveness of our agentic, future-oriented reasoning paradigm.
