# GUI Agents

Agents that interact with graphical user interfaces — clicking, typing, navigating apps — using vision-language models to perceive the screen and take actions.

## Current State (as of 2026-04-16)

GUI agents are one of the fastest-moving areas of applied agentic AI. MLLMs now power agents that can operate desktop and web UIs, but **long-horizon tasks remain the core challenge** — memory degrades, math fails, and progress tracking breaks down over extended sessions.

## Key Papers

**UI-Copilot (2026-04-16)** — Splits the agent into an executor (policy) and a copilot (memory+compute). Introduces memory decoupling and TIPO (Tool-Integrated Policy Optimization). 17.1% improvement on AndroidWorld at 7B scale. → [summary](2026-04-16-ui-copilot.md)

**UI-Zoomer (2026-04-16)** — Uncertainty-driven zoom-in for GUI grounding. Triggers zoom only when the model is uncertain, using a two-axis confidence gate. Gains of up to +13.4% on ScreenSpot-Pro with no training. → see raw: `../../raw/huggingface/2026-04-16-ui-zoomer-uncertainty-driven-adaptive-zoom-in-for-gui-ground.md`

**GameWorld (2026-04-16)** — Benchmark of 34 browser games and 170 tasks for MLLM game agents. Best agents still far below human performance. → [summary](../multimodal/2026-04-16-gameworld-multimodal-game-agents.md)

## Open Problems

- Long-horizon memory management
- Math and numerical reasoning during execution
- Action validity and irreversibility in real environments
- Evaluation standardization across different UI paradigms

## Related Pages

- [Tool Use & Function Calling](tool-calling.md)
- [Agent Evaluation & Benchmarks](agent-benchmarks.md)
- [Multi-Agent Systems](multi-agent-systems.md)
