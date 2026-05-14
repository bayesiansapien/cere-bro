---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.09131
url: https://huggingface.co/papers/2605.09131
arxiv_url: https://arxiv.org/abs/2605.09131
date: 2026-05-13
---

# MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments

The Model Context Protocol (MCP) has unified the interface between Large Language Models (LLMs) and external tools, yet a fundamental gap remains in how agents conceptualize the environments within which they operate. Current paradigms are bifurcated: Task-level planning often ignores execution-time dynamics, while reactive execution lacks long-horizon foresight. We present MCP-Cosmos, a framework that infuses generative World Models (WM) into the MCP ecosystem to enable predictive task automation. By unifying three disparate technologies, namely MCP, World Model, and Agent, we demonstrate that a "Bring Your Own World Model" (BYOWM) strategy allows agents to simulate state transitions and refine plans in a latent space before execution. We conducted experiments using two strategies, namely ReAct and SPIRAL with 2 planning models and 3 representative world models over 20+ MCP-Bench tasks. We observed improvements in Agent's environment interaction KPI such as tool success rate and tool parameter accuracy. The framework also offers new metrics such as Execution Quality to generate new insights about the effectiveness of world models compared to baseline.
