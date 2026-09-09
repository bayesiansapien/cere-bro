---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06289
url: https://huggingface.co/papers/2609.06289
arxiv_url: https://arxiv.org/abs/2609.06289
date: 2026-09-09
---

# Steering Geometry: Validating Human Value Geometry in LLM Steering Space

As large language models (LLMs) are increasingly deployed in alignment-sensitive contexts, activation steering has emerged as a lightweight, inference-time alternative to fine-tuning methods (e.g., RLHF, DPO) for behavioral control. However, existing work typically validates steering on isolated behaviors, leaving it unclear whether steering vectors encode coherent semantic structure or merely exploit behavior-specific shortcuts. We investigate whether the latent geometry of LLM steering vectors reflects theory-specified structure in human values and morality. Using Schwartz's Theory of Basic Human Values as our primary fine-grained framework, we introduce a 26K-sample benchmark covering 20 human values and analyze distribution-driven methods (e.g., CAA, SphericalSteer, ODESteer) and behavior-centric approaches (e.g., COLD-Steer, BiPO) across diverse model families and sizes. We find that distribution-driven methods recover human value topologies aligned with theoretical predictions (Spearman ρ up to 0.51, p < 10^{-13}). In contrast, behavior-centric methods achieve comparable steering performance but show little correlation with the expected value geometry. Geometric fidelity improves with model scale but drops after instruction tuning. Finally, better geometric alignment also leads to more human-consistent transfer across values: steering one value correctly lifts compatible values and suppresses opposing ones. Code and data are available at: https://github.com/DeepRCL/Steering_Geometry.
