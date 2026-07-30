---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.24117
url: https://huggingface.co/papers/2607.24117
arxiv_url: https://arxiv.org/abs/2607.24117
date: 2026-07-30
---

# Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems

Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). What is missing is an operational framework that attaches graded, per-domain transmitter reliability to claim-level transmission chains, with completeness semantics, transformation-typed aggregation, decoupled content criticism, and serve/review/quarantine routing.
  Classical Islamic hadith science confronted a structurally similar problem: deciding whether knowledge transmitted through chains of human narrators should be accepted. Over centuries it developed a rigorous methodology - isnad (a complete transmission chain attached to every claim), rijal (systematic grading of each narrator's integrity and precision), weakest-link chain evaluation, corroboration through independent chains, and matn criticism (content evaluated independently of chain quality). This paper transfers that methodology to AI system design.
  We contribute a formal mapping from hadith-science concepts to multi-agent pipelines, a relational schema implementing claim chains and a graded narrator registry, a decision matrix combining chain grade with content criticism, and an evaluation on 20,000 claims from real physics textbooks. The evaluation validates weakest-link quarantine and independent-chain corroboration; reports a partial failure of the grade-recovery loop, which missed the highest-fault narrator; and reports two analyses as inconclusive, including a matched-coverage comparison the framework could not reach with the reference content critic. The paper is explicit throughout about which claims the evidence does and does not yet support.
