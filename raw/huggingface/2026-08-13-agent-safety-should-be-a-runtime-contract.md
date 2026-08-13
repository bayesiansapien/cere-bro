---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.11274
url: https://huggingface.co/papers/2608.11274
arxiv_url: https://arxiv.org/abs/2608.11274
date: 2026-08-13
---

# Agent Safety Should Be a Runtime Contract

The dominant paradigm treats AI safety as a property to be instilled during model training via RLHF, DPO, or Constitutional AI. We argue this is structurally insufficient for autonomous agents that execute code, mutate files, send messages, and modify databases. Agent safety should be a runtime contract enforced by the harness, and the contract has two complementary faces. The preventive face blocks dangerous actions before they happen via sandboxes, permission gates, output filters, and trajectory monitors. The evidential face requires verifiable proof that good actions actually happened, gating task submission on hard evidence such as test runs, log captures, file diffs, and citation grounding. We ground the position in four lines of public evidence, with row-level protocols and data released in the supplementary JSON files: a survey of 52 documented AI-agent and LLM safety incidents, a false-completion audit with 31 non-contested core cases plus one disputed illustrative case, a trajectory-schema audit of 12 public agent systems and harnesses, and a title-level audit of all 28,560 papers accepted at NeurIPS, ICML, and ICLR 2023-2025 showing a pooled 8-12x imbalance between training-time and deployment-time publication. Two prior communities that needed to enforce safety, computer security and the experimental sciences, converged on runtime contracts with both preventive and evidential elements; agentic AI is now under the same pressure. We formalize an Agent Trajectory Schema and Evidence Chain, state a compositional gating proposition based on standard monitor composition, and outline a research agenda. The right unit of safety in agentic AI is the trajectory-with-checkable-evidence, not the model.
