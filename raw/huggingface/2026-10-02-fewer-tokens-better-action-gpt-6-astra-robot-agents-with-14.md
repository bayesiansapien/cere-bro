---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819159+00:00
arxiv_id: 2610.01939
url: https://huggingface.co/papers/2610.01939
arxiv_url: https://arxiv.org/abs/2610.01939
date: 2026-10-02
---

# Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead. We introduce PyRUA-Lean, an interactive code-execution framework that couples feedback-driven primitive composition with selective observation: the agent composes classical robot primitives and learned vision-language-action (VLA) policies into Python cells that perform conditional checks and local retries, returning only explicitly requested images and state feedback for replanning. Across 700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365, we compare PyRUA-Lean with a tool-calling baseline using the same GPT-6 Astra planner and underlying robot primitives. Under equal LLM-call budgets, PyRUA-Lean increases overall success from 63.1% to 71.7%. On instances solved by both agents, it uses 49% fewer LLM calls and 65% fewer input tokens.
