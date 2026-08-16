---
source: farmer/huggingface
farmed: 2026-08-16T13:39:51.900697+05:30
arxiv_id: 2608.12440
url: https://huggingface.co/papers/2608.12440
arxiv_url: https://arxiv.org/abs/2608.12440
date: 2026-08-16
---

# Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review

This paper reports a single, fully instrumented case study of a large-scale architectural refactoring by an AI coding agent under a specification-first protocol, with no human review of the generated code and no pre-existing oracle to validate the target behaviour. The task, dismantling a central invariant across a large interdependent codebase, was assessed by the author as effectively infeasible through incremental refactoring, the kind of change that conventionally calls for a rewrite instead. Under the protocol described here, the agent completed it successfully.
  The system is a 717,725-line production TypeScript application across 3,648 files. The task required dismantling a core lifetime invariant: the guarantee that a UI panel remains open for the duration of an AI request. The target behaviour was that a streaming generation survives the closing of its panel and can be reattached, on reopening, to the same live stream with no loss or duplication.
  The protocol: formal specification by the agent, 14 refinement cycles auditing that specification against the source code, atomic implementation, a compile/test feedback loop, then 17 verification cycles auditing the code against the frozen specification. Across 31 audit passes, 201 defects were corrected before any human executed the program. The convergence criterion was empirical: two consecutive verification passes returning zero findings.
  The change touched 189 files (31 new); with the extraction phase, the two commits total 288 files, 34,770 insertions, 16,422 deletions. Across the first and roughly thirty later sessions, the software behaved as specified, no bug observed. Elapsed: three days; cost: USD 2,430.
  The full specification and raw session logs, 1,500+ pages in French, are published as evidence, allowing inspection of the process and submission to a language model for consistency checking.
