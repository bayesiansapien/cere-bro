---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26752
url: https://huggingface.co/papers/2604.26752
arxiv_url: https://arxiv.org/abs/2604.26752
date: 2026-04-30
---

# GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

**Authors:** GLM-5V-Turbo Team, Z.ai & Tsinghua University

We present GLM-5V-Turbo, a step toward native foundation models for multimodal agents. As foundation models are increasingly deployed in real environments, agentic capability depends not only on language reasoning, but also on the ability to perceive, interpret, and act over heterogeneous contexts such as images, videos, webpages, documents, GUIs. GLM-5V-Turbo is built around this objective: multimodal perception is integrated as a core component of reasoning, planning, tool use, and execution, rather than as an auxiliary interface to a language model. This report summarizes the main improvements behind GLM-5V-Turbo across model design, multimodal training, reinforcement learning, toolchain expansion, and integration with agent frameworks. These developments lead to strong performance in multimodal coding, visual tool use, and framework-based agentic tasks, while preserving competitive text-only coding capability. More importantly, our development process offers practical insights for building multimodal agents, highlighting the central role of multimodal perception, hierarchical optimization, and reliable end-to-end verification.

## Key contributions

- **CogViT vision encoder**: A new parameter-efficient vision encoder using two-stage pretraining (distillation-based masked image modeling, then contrastive image-text pretraining) with dual SigLIP2 + DINOv3 teachers.
- **Multimodal Multi-Token Prediction (MMTP)**: Extension of MTP to multimodal inputs; uses a shared `<|image|>` special token rather than raw visual embeddings at the MTP head, reducing communication overhead while improving training stability.
- **Joint RL over 30+ task categories**: Covers perception, reasoning, and agentic tasks; shows weaker cross-domain interference vs SFT, with transfer of thinking patterns across tasks.
- **Multimodal RL infrastructure**: Full-pipeline decoupling with async rollout inference, fine-grained memory management for ViT/projector, topology-aware partitioning and dynamic load-balancing for variable-length visual inputs.
- **Benchmarks**: 75.7 on AndroidWorld, 62.3 on OSWorld, 94.8 on Design2Code (outperforming Claude Opus 4.6), 87.0/80.7 on PinchBench.
