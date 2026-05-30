---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.16363
url: https://huggingface.co/papers/2605.16363
arxiv_url: https://arxiv.org/abs/2605.16363
date: 2026-05-30
---

# ORACLE: Anticipating Scams from Partial Trajectories in Streaming App Usage

Smartphone scams are increasingly prevalent and typically manifest as multi-stage, cross-application processes with gradually emerging intent. Effective intervention thus requires anticipating scams before the intent becomes explicit. This is inherently challenging, as decisions must rely on partial trajectories with temporally distributed evidence. In this paper, we propose ORACLE Online Reasoning for Anticipating Cross-temporal Latent thrEats, the first agentic framework for early scam anticipation from streaming app-usage trajectories. To support this setting, we curate a real-world long-horizon benchmark of streaming app-usage trajectories, covering 12 scam types, spanning extended periods (15 days on average), involving diverse applications (95 apps), and interleaving normal and scam behaviors. To address fragmented evidence, we introduce a self-evolving context manager that adaptively consolidates entity-centric interactions over time, enabling more effective reconstruction of cross-temporal evidence from partial observations. To enhance sensitivity to latent early-stage signals, we propose an on-policy self-distillation scheme in which a teacher model, conditioned on summarized anti-scam reflections and clues by skills, supervises a student model without access to such reflections. This scheme thereby distills evidence-informed knowledge and improves recognition of emerging fraud patterns from partial trajectories. Experiments show that  consistently improves early scam anticipation, yielding timely warnings while reducing false alerts in realistic streaming scenarios.
