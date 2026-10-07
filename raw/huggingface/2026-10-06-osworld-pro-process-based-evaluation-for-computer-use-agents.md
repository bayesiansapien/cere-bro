---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.24890
url: https://huggingface.co/papers/2609.24890
arxiv_url: https://arxiv.org/abs/2609.24890
date: 2026-10-06
---

# OSWorld-Pro: Process-based Evaluation for Computer Use Agents

Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely provide click-based inputs on the graphical UI. We introduce OSWorld-Pro: a set of over 300 tasks containing over 2800 subgoals to enable the procedural evaluation of CUAs grounded in over 67,000 human annotations. We use robust human-aligned LLM-Judges to evaluate the fulfillment of OSWorld-Pro subgoals and thereby reveal the progress that models make throughout a series of sequentially dependent subgoals. Our findings reveal that OSWorld-Pro is challenging even for state-of-the-art LLMs, with top performers like Claude Opus 5 achieving only 75.7% vs. 83.4% on OSWorld. Furthermore, we identify critical process-focused failure modes of various models (e.g. subgoal-irrelevant actions and click-based mistakes) to provide insights to improve performance and efficiency of CUAs.
