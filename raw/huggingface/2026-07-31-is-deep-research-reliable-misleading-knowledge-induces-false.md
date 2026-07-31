---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.20891
url: https://huggingface.co/papers/2607.20891
arxiv_url: https://arxiv.org/abs/2607.20891
date: 2026-07-31
---

# Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions

Deep Research agents extend LLM-based assistants into long-horizon workflows involving planning, retrieval, evidence synthesis, and report generation, yet their reliability in open information environments remains underexplored. A key concern is whether apparently credible but factually misleading knowledge encountered in such environments can propagate through these workflows and be adopted as false conclusions in final reports. To study this failure mode, we introduce MisKnow-Agent, a framework for constructing and validating misleading knowledge for Deep Research tasks. MisKnow-Agent generates misleading instances with controllable authority levels and styles, yielding 5,933 quality-controlled instances built on DeepResearch Benchmark tasks. Extensive experiments across open-source and closed-source Deep Research agents show that even limited exposure to misleading knowledge can induce false-conclusion adoption in final reports, revealing a broad reliability vulnerability in current Deep Research agents. Although search-enabled verifier models consistently identify the retained instances as misleading during focused corpus validation, the same instances can still be adopted during long-horizon research, revealing a disconnect between focused verification and workflow-level evidence use. Finally, we evaluate pre- and post-research defenses, both individually and in combination, finding that all three configurations mitigate but do not fully prevent false-conclusion adoption. Our findings suggest that reliable Deep Research requires evidence verification and correction capabilities at both the model and framework levels, beyond improvements in planning, retrieval, evidence integration, or report-generation abilities.
