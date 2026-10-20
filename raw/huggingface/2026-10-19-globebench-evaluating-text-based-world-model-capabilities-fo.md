---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22708
url: https://huggingface.co/papers/2610.22708
arxiv_url: https://arxiv.org/abs/2610.22708
date: 2026-10-19
---

# GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check whether models can predict the environment's response to a specific action given the full agent trajectory by understanding earlier state changes, following environment rules, and predicting the effects of actions on both related and unrelated objects. We compare the predicted environment response with an execution-derived reference, using a hybrid architecture with both deterministic gates and a semantic judge. Among 20 general-purpose LLMs and specialized text world models, GPT-6 Astra achieves the highest task success rate at 49.57%. We find that model accuracy decreases as actions affect a larger portion of the environment. Specifically, when the agent's changes must propagate to dependent objects, task success drops to an average of 5.1% across all 20 models. Although model strengths differ across tasks, 631 tasks remain unsolved by any model, suggesting a significant gap in general LLM capabilities as a world model.
