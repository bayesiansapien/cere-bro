---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.08348
url: https://huggingface.co/papers/2606.08348
arxiv_url: https://arxiv.org/abs/2606.08348
date: 2026-06-09
---

# Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses

LLM agents increasingly rely on external inference conditions: prompts, tools, memory, SOPs, skills, and harness feedback. These assets can improve task execution without changing model weights, but they are often revised by heuristic reflection or by reusing observed successes and failures as if counts alone were reliable belief. We introduce Bayesian-Agent, a native and cross-harness framework that treats reusable skills and SOPs as hypotheses about whether a frozen model will succeed under a particular prompt, context, and harness environment. Bayesian-Agent records verified trajectory evidence, maintains a feature-conditioned categorical posterior over each skill, and maps posterior state into inspectable actions such as patch, split, compress, retire, and explore. Model-facing prompts receive executable guardrails and failure-mode patches, while posterior summaries remain available for audit. With deepseek-v4-flash, incremental repair improves SOP-Bench from 80\% to 95\%, Lifelong AgentBench from 90\% to 100\%, and RealFin-Bench from 45\% to 65\%. We further evaluate Bayesian-Agent's native backend and optional GenericAgent, mini-swe-agent, and Claude Code backends. The results include positive, negative, saturated, and case-study settings, suggesting that agent skill evolution is best viewed as posterior-guided harness optimization rather than uncalibrated prompt accumulation. The source code is available at https://github.com/DataArcTech/Bayesian-Agent.
