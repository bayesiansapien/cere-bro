---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15301
url: https://huggingface.co/papers/2605.15301
arxiv_url: https://arxiv.org/abs/2605.15301
date: 2026-05-18
---

# Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution

Large language models (LLMs) still struggle with the rigorous reasoning demands of hard competitive programming. While recent multi-agent frameworks attempt to bridge this reliability gap, they remain fundamentally stateless: they rely on static retrieval and discard the valuable problem-solving and debugging experience gained from previous tasks. To address this, we present Solvita, an agentic evolution framework that enables continuous learning without requiring weight updates to the underlying LLM. Solvita reorganizes problem-solving into a closed-loop system of strategy selection, program synthesis, certified supervision, and targeted hacking, executed by four specialized agents (Planner, Solver, Oracle, and Hacker). Crucially, each agent is paired with a trainable, graph-structured knowledge network. As the system operates, outcome signals such as pass/fail verdicts, test certification quality, and adversarial vulnerabilities discovered by the Hacker are recast as reinforcement learning updates to these network weights. This allows the agents to dynamically route future queries based on past successes and failures, effectively accumulating transferable reasoning experience over time. Evaluated across CodeContests, APPS, AetherCode, and live Codeforces rounds, Solvita establishes a new state-of-the-art among code-generation agents, outperforming existing multi-agent pipelines and nearly doubling the accuracy of single-pass baselines.
