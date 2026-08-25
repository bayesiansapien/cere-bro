---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.19741
url: https://huggingface.co/papers/2608.19741
arxiv_url: https://arxiv.org/abs/2608.19741
date: 2026-08-25
upvotes: 5
authors: ["Zhuochun Li", "Youngmin Ko", "Ali Keramati", "Nicola Ferri", "Susana Palmaz Lopez Pelaez", "Liang-Chun Tsai", "Calvin Wang", "Mirco Milletari", "Tuhin Kundu", "Vadim Smolyakov", "Kjartan Olafsson", "Tommy Guy"]
---

# One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows

**Upvotes:** 5
**Authors:** Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, Calvin Wang, Mirco Milletari, Tuhin Kundu, Vadim Smolyakov, Kjartan Olafsson, Tommy Guy

Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, a sandbox for tool-agent-user interaction that provides isolated MCP-compatible tool sessions, complete execution traces, and outcome evaluation over terminal backend state. Built on this sandbox, Thinkingbox-bench contains 507 policy-conditioned workflows across numerous scenarios, including retail, hospitality, auto insurance, neobank internal IT, and consulting IT/HR support. Each attempt is evaluated by task-specific executable checks that accept valid trajectories while rejecting wrong, missing, or extra effects; designated tasks additionally check required properties of the final response. Across proprietary and open-weight models, the strongest achieves 65.36% pass@1, but only 25.25% pass^20. Moreover, many failed trials show clean termination and valid state-changing actions, showing that response or tool-call-level signals are not clear proxies for end-to-end task completion. Thinkingbox-bench reveals a large gap between occasionally finding a successful trajectory and reliably completing stateful business tasks. We release both Thinkingbox and Thinkingbox-Bench: https://github.com/microsoft/thinkingbox
