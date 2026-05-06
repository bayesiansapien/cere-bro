---
date: 2026-04-16
source: huggingface
arxiv: 2604.13822
---

# UI-Copilot: Long-Horizon GUI Automation via Tool-Integrated Policy Optimization

**TL;DR:** UI-Copilot splits the GUI agent into two roles — a policy agent that executes tasks and a lightweight copilot that provides memory retrieval and numerical computation on demand. This separation breaks long-horizon GUI tasks into manageable pieces, achieving 17.1% absolute improvement on AndroidWorld over the base Qwen model.

## Key Findings

- **Memory decoupling** separates persistent observations (what happened before) from transient execution context (what's happening now), reducing memory degradation in long sessions.
- **Tool-Integrated Policy Optimization (TIPO)** trains tool selection and task execution separately — single-turn prediction for routing, on-policy multi-turn rollouts for execution quality.
- Outperforms GUI-Owl-7B and UI-TARS-1.5-7B on MemGUI-Bench at 7B scale.
- Key failure modes in long-horizon GUI: memory degradation, progress confusion, math hallucination — all addressed by offloading to the copilot.

## Related Pages

- [GUI Agents](gui-agents.md)
- [Tool Use & Function Calling](tool-calling.md)

**Raw source:** [../../raw/huggingface/2026-04-16-ui-copilot-advancing-long-horizon-gui-automation-via-tool-in.md](../../raw/huggingface/2026-04-16-ui-copilot-advancing-long-horizon-gui-automation-via-tool-in.md)
