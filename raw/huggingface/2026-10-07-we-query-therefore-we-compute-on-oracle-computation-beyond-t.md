---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.09243
url: https://huggingface.co/papers/2610.09243
arxiv_url: https://arxiv.org/abs/2610.09243
date: 2026-10-07
---

# We Query, Therefore We Compute: On Oracle Computation beyond the Machine, with an Application to Agents

Agentic systems use large language models (LLMs) to carry out concrete tasks. Prior work often borrows abstractions such as scheduling, caching or isolation piecemeal from operating systems, so the mechanisms it builds share little common ground, and the shared view of the two forms of agentic system, Workflows and Agents, is limited. We construct an abstract machine that provides both.
  We treat the LLM as an Oracle and extend a two-stack pushdown automaton with one instruction, which hands the Oracle a whole stack as its query and appends the answer to that same stack. The machine thus performs two computations, the Oracle's and a Turing-complete one that we call the Priestess. A stack that the program only appends to grows autoregressively, as an agent's context does. Two symmetry breakings, S in storage and T in transitions, make a Priestess program the operating system of the programs the Oracle runs, and produce the Agent and the Workflow as the two placements of a task's program.
  For internally autoregressive Oracles, the two computations synchronize at the end of every answer under certain conditions, and through that synchronization we model caching and analyse scheduling. No guarantee that holds for every Oracle can fix which content crosses between the two computations, but such a guarantee does fix the boundary itself.
  The construction V fits the machine to a von Neumann computer. To show that it is realizable, we propose ArchNights, an extended RISC-V ISA and a Linux-style operating system implementing the machine by design. ArchNights-SE runs on gem5 as a computer system, becomes an agentic system when it runs an LLM as the Oracle, and will be open source.
  Agentic systems can then be designed as computer systems are. With a foundation built and a unified view, future work can share invariants and bounds, each with its conditions.
