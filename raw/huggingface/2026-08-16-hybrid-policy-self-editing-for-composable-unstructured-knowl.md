---
source: farmer/huggingface
farmed: 2026-08-16T13:39:51.900697+05:30
arxiv_id: 2608.11660
url: https://huggingface.co/papers/2608.11660
arxiv_url: https://arxiv.org/abs/2608.11660
date: 2026-08-16
---

# Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing

Large language models (LLMs) achieve remarkable performance across natural language tasks, yet they are trained on static corpora and their knowledge quickly becomes outdated in a fast-changing world. This motivates knowledge editing (KE), which updates specific knowledge in an LLM without changing unrelated others. Recent works move from structured knowledge triples toward unstructured KE (UKE), where the edit is a free-form passage that may state multiple facts at once. Nonetheless, existing editors inject such a passage yet fail to use it: the edited model can recall the passage, but can neither answer atomic questions about its facts nor compose them into multi-hop reasoning. We attribute this missing property, which we term composability, to editors' passive reliance on the fixed passage as the sole learning source. In response, we cast editing as a proactive self-distillation from a privileged in-context state of the same model, which requires no external supervision. We further reveal that due to the novelty of the injected knowledge, the pre-edited model's own rollouts rarely cover it, which limits the effectiveness of pure on-policy distillation. To close this gap, we propose HPSE, which builds a hybrid rollout that steps in to place missing facts onto the student's own trajectory precisely where its coverage fails, while staying on-policy elsewhere. We theoretically analyze HPSE's advantage over pure on-policy distillation, and empirically establish its plug-and-play improvements across four LLM backbones and two KE editors under various scenarios.
