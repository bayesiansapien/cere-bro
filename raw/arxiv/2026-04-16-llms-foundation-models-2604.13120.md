---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13120
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13120
published: 2026-04-16
authors: Rajesh Kumar, Waqar Ali, Junaid Ahmed
---

# AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering

**arXiv:** https://arxiv.org/abs/2604.13120
**Authors:** Rajesh Kumar, Waqar Ali, Junaid Ahmed

## Abstract

arXiv:2604.13120v1 Announce Type: cross  Abstract: Large language models generate plausible code but cannot verify correctness. Existing multi-agent systems simulate execution or leave verification optional. We introduce execution-grounded verification as a first-class principle: every code change must survive sandboxed execution before propagation. We instantiate this principle in AGENTFORGE, a multi-agent framework where Planner, Coder, Tester, Debugger, and Critic agents coordinate through shared memory and a mandatory Docker sandbox. We formalize software engineering with LLMs as an iterative decision process over repository states, where execution feedback provides a stronger supervision signal than next-token likelihood. AGENTFORGE achieves 40.0\% resolution on SWE-BENCH Lite, outperforming single-agent baselines by 26--28 points. Ablations confirm that execution feedback and role decomposition each independently drive performance. The framework is open-source at https://github.com/raja21068/AutoCodeAI.
