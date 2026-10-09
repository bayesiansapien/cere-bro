---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.304382+05:30
arxiv_id: 2610.08995
url: https://huggingface.co/papers/2610.08995
arxiv_url: https://arxiv.org/abs/2610.08995
date: 2026-10-08
---

# PhysEvo: Astra Can Act, Let It

Astra can act, yet reliable manipulation depends on the system through which it observes and controls the world. We introduce PhysEvo, a framework for physical recursive self-improvement (RSI) around a single frozen model. A task agent executes robot tasks; a meta-agent uses the resulting trajectories to diagnose failures, revise tools and skills, and test corrections. The meta-agent can also improve its own diagnostic tools, so retained revisions support both later action and later self-improvement. This process develops joint-level control, evidence-seeking observation, and reusable manipulation skills without model-weight updates or a separately trained action policy. Across 42 RoboDojo tasks, held-out-layout evaluation of retained task-specific deployment versions yields a five-dimension average score of 68.14/100 and 62.00% success, compared with 47.17% for RoboDawn's one-shot Astra agent, the strongest published reference in our comparison. On eight manipulation tasks challenging direct Astra, PhysEvo achieves 55.00% success, compared with 1.25% for the direct-Astra reference. Deploying the simulation-evolved harness on AgileX PiPER and continuing skill revision yields 90.60/100 average score and 84.00% success across 25 trials on five real-world tasks. PhysEvo turns the consequences of action into persistent, testable changes to how a frozen model acts and improves.
