---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2604.14228
url: https://huggingface.co/papers/2604.14228
arxiv_url: https://arxiv.org/abs/2604.14228
date: 2026-04-17
---

# Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems

Claude Code is an agentic coding tool that can run shell commands, edit files, and call external services on behalf of the user. This study describes its comprehensive architecture by analyzing the publicly available TypeScript source code (v2.1.88) and further comparing it with OpenClaw, an independent open-source AI agent system that answers many of the same design questions from a different deployment context. Our analysis identifies five human values, philosophies, and needs that motivate the architecture (human decision authority, safety and security, reliable execution, capability amplification, and contextual adaptability) and traces them through thirteen design principles to specific implementation choices. The core of the system is a simple while-loop that calls the model, runs tools, and repeats. Most of the code, however, lives in the systems around this loop: a permission system with seven modes and an ML-based classifier, a five-layer compaction pipeline for context management, four extensibility mechanisms (MCP, plugins, skills, and hooks), a subagent delegation and orchestration mechanism, and append-oriented session storage. A comparison with OpenClaw shows that the same recurring design questions produce different architectural answers when the deployment context changes. We finally identify six open design directions for future agent systems.
