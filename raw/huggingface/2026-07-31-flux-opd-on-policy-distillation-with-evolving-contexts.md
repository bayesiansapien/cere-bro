---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28022
url: https://huggingface.co/papers/2607.28022
arxiv_url: https://arxiv.org/abs/2607.28022
date: 2026-07-31
---

# Flux-OPD: On-Policy Distillation with Evolving Contexts

Large language model training in open-ended domains lacks verifiable rewards, making task preferences difficult to formalize as effective supervision. Contexts can convey such preferences, yet provide little additional supervision once distilled into the student, motivating contexts that evolve with student performance. However, directly using evolving contexts as in-training supervision results in an unstable distillation target and conflicting distributions, requiring mechanisms to stabilize target and downweight conflicts. In this paper, we analyze the effect of contexts through a decomposition of the reverse KL objective, revealing two findings: the student is distilled toward the geometric mean of context-conditioned teachers, and the objective contains a conflict term that measures conflicts among these teachers. Based on this decomposition, we propose Flux-OPD, an OPD paradigm that uses evolving contexts as in-training supervision to capture task preferences in open-ended domains. Flux-OPD treats the differences between context-conditioned and context-free teachers as contextual difference signals, injects them as contextual corrections into the context-free teacher anchor, and weights their correction strength using the conflict term as an indicator. Experiments on open-ended tasks show that Flux-OPD outperforms existing OPD paradigms, highlighting the potential to combine teacher supervision with evolving contexts.
