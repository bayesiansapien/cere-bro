---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.13880"
url: "https://huggingface.co/papers/2605.13880"
arxiv_url: "https://arxiv.org/abs/2605.13880"
date: 2026-05-17
---

# PREPING: Building Agent Memory without Tasks

Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions. However, regardless of how it is built, an agent faces a cold-start gap when first introduced to a new environment without any task-specific experience available. In this paper, we study pre-task memory construction: whether an agent can build procedural memory before observing any target-environment tasks, using only self-generated synthetic practice. Yet, synthetic interaction alone is insufficient, as without controlling what to practice and what to store, synthetic tasks become redundant, infeasible, and ultimately uninformative, and memory further degrades quickly due to unfiltered trajectories. To overcome this, we present Preping, a proposer-guided memory construction framework. At its core is proposer memory, a structured control state that shapes future practice. A Proposer generates synthetic tasks conditioned on this state, a Solver executes them, and a Validator determines which trajectories are eligible for memory insertion while also providing feedback to guide future proposals. Experiments on AppWorld, BFCL v3, and MCP-Universe show that Preping substantially improves over a no-memory baseline and achieves performance competitive with strong playbook-based methods built from offline or online experience, with deployment cost 2.99x lower on AppWorld and 2.23x lower on BFCL v3 than online memory construction.
