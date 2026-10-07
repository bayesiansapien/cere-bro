---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06425
url: https://huggingface.co/papers/2610.06425
arxiv_url: https://arxiv.org/abs/2610.06425
date: 2026-10-06
---

# SoK: Semantic Decision Engines in Network Control Loops

A semantic decision engine such as Jev can return a valid answer and still miss a network deadline, select an infeasible action or leave the service unverified. We systematize 139 paper families by decision interface, execution path and check ownership. Fifty families claim that their engine fits a control loop or time budget, but only four support the claim with matched measurement. Across all 139, four report deadline attainment. The gap concentrates where the decision has no deterministic computation step. Those 72 families make 22 of the claims, none supported, and name a coverage owner in only two. Bounded tests under one event model show that each gap can reverse an admission verdict. A decision that meets a 10 s budget for every isolated request meets it for none once decisions queue ahead of replayed execution times. The same engine passes one coverage check and fails another. We derive a minimum reporting record, design rules and a research agenda for admitting decision engines to control loops.
