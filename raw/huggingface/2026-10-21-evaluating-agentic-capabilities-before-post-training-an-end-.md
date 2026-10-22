---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.644600
arxiv_id: 2610.19425
url: https://huggingface.co/papers/2610.19425
arxiv_url: https://arxiv.org/abs/2610.19425
date: 2026-10-21
---

# Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach

Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but provide limited visibility into how base models behave in interactive environments. We introduce ASAP (Agent Scaffold Adaptation for Pretraining Evaluation), a lightweight framework for eliciting and evaluating agentic behavior from pretrained base models on end-to-end tasks. Rather than converting base models into chat-style agents, ASAP preserves the completion interface and adapts existing agent scaffolds through structured trajectory continuation, short reference prefixes, and minimal recovery mechanisms. Across software-engineering and deep-research benchmarks, ASAP yields discriminative end-to-end performance across base models and pretraining checkpoints. Beyond aggregate scores, ASAP exposes model-generated execution trajectories, enabling analysis of exploration, editing, testing, recovery, and task completion across training stages. These trajectories provide a behavioral view of how agent-relevant capabilities change during pretraining and how execution patterns differ after post-training. Our results suggest that end-to-end agent evaluation can complement conventional pretraining benchmarks by providing a practical diagnostic of interactive model behavior.
