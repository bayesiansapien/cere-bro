---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36130
url: https://huggingface.co/papers/2609.36130
arxiv_url: https://arxiv.org/abs/2609.36130
date: 2026-09-30
---

# Memory Is a Derivation: The Distributed-Evidence Paradox in Long-Term Agents

Long-running LLM agents compress past interactions into persistent memories that may be reused as premises for later tasks. This creates a distinct derivation problem: whether the memory actually follows from what the interaction history supports. Relevant evidence may be scattered across earlier interactions, while compression can introduce relations or event status that the history never established. A valid memory may therefore appear unsupported because its citations omit relevant evidence, while individually supported facts may be composed into a stronger statement the history never established. We characterize this problem through three coupled requirements: (1) Evidence scope; (2) Compositional validity; (3) Admission reliability. We therefore ask whether the interaction history available at write time supports what enters persistent memory. We introduce DerivAudit, a framework for auditing whether a memory is actually supported by the history available when it was written. The audit separates three questions: whether supporting evidence lies beyond writer-provided citations, whether the composed memory introduces unsupported meaning, and how write-time admission decisions affect later memory use. Across two natural memory corpora, audits using broader pre-write history recover support for nearly 60% of memories that appear unsupported from citations alone, while 17-21% remain unsupported after expansion. Yet broader evidence does not by itself make admission reliable: unsupported memories are still frequently admitted across verification models, and evidence expansion alone worsens it on two backbones.
