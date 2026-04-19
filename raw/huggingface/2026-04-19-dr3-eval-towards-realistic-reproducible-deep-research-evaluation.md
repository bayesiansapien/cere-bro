---
source: farmer/huggingface
farmed: 2026-04-19T00:00:00Z
arxiv_id: 2604.14683
url: https://huggingface.co/papers/2604.14683
arxiv_url: https://arxiv.org/abs/2604.14683
date: 2026-04-19
---

# DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation

Recent advances in large language models have enabled the development of Deep Research Agents (DRAs), which autonomously perform complex, long-horizon research tasks involving planning, iterative information retrieval, multimodal understanding, and synthesis of structured, citation-grounded reports. However, evaluating deep research poses challenges that go beyond short-form reasoning or single-answer tasks. Existing benchmarks face a fundamental tension: those relying on live web access provide high realism but suffer from temporal volatility and irreproducibility, while sandbox-based approaches ensure reproducibility but often simplify research contexts to clean, text-only data, omitting multimodal complexity and confounding noise inherent in authentic research.

To address these limitations, we introduce DR³-Eval, a benchmark designed to reconcile realism, controllability, and reproducibility for deep research evaluation. DR³-Eval targets report-generation tasks grounded in real user needs, constructed from authentic multimodal files (text, images, videos, audio) that users have encountered in practice. Each task is paired with a per-case research sandbox corpus that simulates the open web while remaining fully static and verifiable. A key feature is its reverse-construction methodology: rather than posing open-ended questions with uncertain answerability, each query is derived from verified evidential documents, ensuring every task admits a single, well-defined solution path. This eliminates evaluation ambiguity while preserving the complexity of real research workflows.

To support fine-grained assessment, we propose a multi-dimensional evaluation framework measuring: Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality. We also develop DR³-Agent, a multi-agent research system adapted to the benchmark's closed-world setting. Extensive experiments across state-of-the-art language models reveal that DR³-Eval is highly challenging and exposes failure modes obscured by existing benchmarks. Our work comprises 100 carefully curated tasks spanning three major domains (Technology, Economy, Humanities) with 13 sub-fields, providing a principled testbed for assessing long-horizon research capabilities of LLMs.
