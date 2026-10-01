---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2607.11433
url: https://huggingface.co/papers/2607.11433
arxiv_url: https://arxiv.org/abs/2607.11433
date: 2026-09-30
---

# Omni-Decision: Evidence-Ledger Planning for Omni-Modal Agents

Omni-modal agents must seek evidence across video, audio, web pages, and computation to answer questions. Their main bottleneck is planning: noisy multimodal observations accumulate in conversation history and disrupt later decisions, while multimodal models have limited capacity for multi-step planning. Controlled backend replacements support this diagnosis: replacing the planner causes a much larger performance loss than replacing the perception backend. We present Omni-Decision, an omni-modal agent built on evidence-ledger planning: it replaces the growing dialogue history with an explicit evidence ledger that records what evidence is still missing, what has been confirmed, and where records conflict. A critic reads each noisy observation and passes only the usable content to the ledger, discarding the rest, so the planner works from a compact context throughout the task. Each run records the state, action, and verdict at every step, and supervised fine-tuning and decision-level reinforcement learning on these trajectories further improve the planner. Omni-Decision achieves state-of-the-art accuracy of 81.4% on OmniGAIA at approximately 43% of Gemini-3.1-Pro's cost per question, and 65.0% on WorldSense long-video understanding, level with the strongest end-to-end model.
