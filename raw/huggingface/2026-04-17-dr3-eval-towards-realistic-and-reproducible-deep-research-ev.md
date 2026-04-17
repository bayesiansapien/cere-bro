---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2604.14683
url: https://huggingface.co/papers/2604.14683
arxiv_url: https://arxiv.org/abs/2604.14683
date: 2026-04-17
---

# DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation

Recent advances in large language models have enabled the development of Deep Research Agents (DRAs), which autonomously perform complex, long-horizon research tasks involving planning, iterative information retrieval, multimodal understanding, and synthesis of structured, citation-grounded reports. However, evaluating deep research poses challenges that go beyond short-form reasoning or single-answer tasks. Existing benchmarks reveal a fundamental tension between realism, controllability, and evaluability: those relying on live web access provide ecological validity but suffer from temporal volatility and irreproducibility, while sandbox-based approaches ensure stability but often simplify research contexts to clean, text-only data and omit the multimodal complexity and confounding noise inherent in authentic research. To address these limitations, we introduce DR3-Eval, a benchmark designed to reconcile realism, controllability, and reproducibility for deep research evaluation. DR3-Eval targets report-generation tasks grounded in real user needs, constructed from authentic multimodal files that users have encountered in practice. Following a controlled sandbox paradigm, each task is paired with a per-case research sandbox corpus that simulates the open web while remaining fully static and verifiable. A key feature is its reverse-construction methodology: queries are derived from verified evidential documents, ensuring that every task admits a single, well-defined solution path, eliminating evaluation ambiguity while preserving real research complexity. We further develop DR3-Agent, a multi-agent research system adapted to the benchmark's closed-world setting. The benchmark comprises 100 independently curated tasks covering three major domains (Technology, Economy, Humanities) subdivided into 13 atomic sub-fields, with 68% multimodal tasks and an average of 2.24 user files per task.
