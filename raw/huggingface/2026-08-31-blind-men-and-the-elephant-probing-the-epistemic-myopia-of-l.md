---
source: farmer/huggingface
farmed: 2026-08-31T10:31:04.593371+05:30
arxiv_id: 2608.28478
url: https://huggingface.co/papers/2608.28478
arxiv_url: https://arxiv.org/abs/2608.28478
date: 2026-08-31
---

# Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge

Factual question answering (QA) typically assumes a single canonical answer, obscuring whether large language models (LLMs) retain divergent accounts of long-tail facts. To address this gap, we introduce ElephantBench, a closed-book knowledge probe comprising 1,094 questions generated through an auditable graph-based pipeline. The pipeline retrieves related documents from a low-exposure web corpus, identifies naturally occurring disagreements, and converts them into multi-account QA records. Each answer is verified against the originating documents and authoritative public web sources and is then reviewed by human annotators. Across 32 models, even the strongest model recovers both accounts on only 52.4% of questions, while on nearly all remaining questions it recalls one account but omits the other. Scaling model size and inference-time reasoning improve recall but do not eliminate this incompleteness. Corpus analysis further shows that exposure imbalance favors the dominant account, whereas greater minority-side exposure is associated with more complete recall. These findings establish ElephantBench as a reproducible knowledge probe for diagnosing epistemic myopia in parametric memory. More broadly, our graph-based benchmark construction pipeline provides an efficient and scalable way to turn long-tail corpora into source-traceable knowledge probes, supporting efforts to evaluate and advance the epistemic rigour of next-generation LLMs. Code is available at https://github.com/Tencent/ElephantBench.
