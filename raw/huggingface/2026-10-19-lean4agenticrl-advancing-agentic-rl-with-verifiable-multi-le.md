---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22448
url: https://huggingface.co/papers/2610.22448
arxiv_url: https://arxiv.org/abs/2610.22448
date: 2026-10-19
---

# Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards

Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome rewards, with minimal consideration of low-level toolcall and mid-level workflow-stage rewards, which makes the training less effective. To overcome this limitation, we propose **Lean4AgenticRL**, which, to the best of our knowledge, is the first framework that grounds multi-level process rewards in the unified Lean4 formalization schema for open-ended agentic RL. **Lean4AgenticRL** first builds a *problem-specific workflow* system that balances the agent's own capability and controllability during execution, laying the foundation for further verification. Subsequently, our workflow formalization and multi-level reward annotation methods enable agent behavior verification within a general harness system. It provides multi-level rewards to support more effective agentic RL with the workflow-stage-normalized GRPO algorithm. Using **Lean4AgenticRL**, we train **LAR-9B/27B**, a family of models with enhanced agentic capability. Extensive experiments indicate that our model outperforms the leading model of similar size. **LAR-27B** achieves **77.3%** on TerminalBench-2.1. On average, our models outperform the base model by **9.89%** and surpass the second-best model of comparable size we know by **5.07%**. These results indicate the potential of integrating formal methods in enhancing open-ended agentic RL.
