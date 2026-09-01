---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30147
url: https://huggingface.co/papers/2608.30147
arxiv_url: https://arxiv.org/abs/2608.30147
date: 2026-09-01
---

# CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents

Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be intercepted before execution. Such failures may not appear in every single run, but can emerge across repeated trials, making reliability across steps and trials critical. However, ensuring agentic reliability is challenging: even frontier LLMs struggle to explain why an action may be wrong, especially in long, intertwined trajectories governed by domain-specific policies. Much recent work relies on prompt-based critique agents, while optimization-based methods lack a systematic way to produce rich verification rationales for training. We address this gap with CAST, a critique-aware training framework that converts sparse task outcomes into action-level supervision for critique learning and policy optimization. CAST analyzes agent trajectories to synthesize structured rationales explaining action validity under partial observability. The resulting critique model is used to construct critique-aware training data for optimizing the policy model. Fine-tuning Qwen3-family models on dynamic tool-calling benchmarks, CAST improves reliability across domains, outperforming GPT-OSS-120B by over 10% pass^4 on Retail tasks and yielding an additional 9% improvement on Telehealth in an out-of-domain setting. These results demonstrate that critique-aware training improves the robustness of LLM agents in realistic dynamic environments.
