---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.16533
url: https://huggingface.co/papers/2606.16533
arxiv_url: https://arxiv.org/abs/2606.16533
date: 2026-06-18
---

# Kairos: A Native World Model Stack for Physical AI

World models are transitioning from passive visual generators to foundational, operational infrastructure for Physical AI: they must natively acquire world knowledge from heterogeneous experience, maintain persistent states over long horizons, and execute efficiently within real deployment constraints. We introduce Kairos, a native world model stack designed around these requirements. (1) Kairos learns the world by pioneering a Native Pre-training Paradigm governed by a Cross-Embodiment Data Curriculum, which organizes open-world videos, human behavioral data, and robot interactions into a progressive developmental pathway. (2) Kairos maintains the world by unified world understanding, generation, and prediction within a Native Unified Architecture equipped with Hybrid Linear Temporal Attention, where sliding-window attention captures local dynamics, dilated sliding windows capture mid-range dependencies, and gated linear attention maintains persistent global memory. We establish formal theoretical bounds demonstrating that this temporal factorization strictly limits error accumulation, mathematically guaranteeing state propagation across extended horizons. (3) Kairos runs the world by incorporating a Deployment-Aware System Co-Design to support low-latency rollout generation on server and consumer-grade hardware for real-world observation-action-feedback loops. Experiments on embodied world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top level performance while offering a strong efficiency-capability trade-off. Together, these results position Kairos as a cohesive operational foundation for future self-evolving physical intelligence.
