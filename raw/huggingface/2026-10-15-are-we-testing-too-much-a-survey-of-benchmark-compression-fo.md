---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227999+05:30
arxiv_id: 2610.18248
url: https://huggingface.co/papers/2610.18248
arxiv_url: https://arxiv.org/abs/2610.18248
date: 2026-10-15
---

# Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models

Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and findings. We review 119 papers to explain how methods choose what to evaluate, recover full-benchmark results, and verify their reliability. From this analysis, we develop a taxonomy covering compression within individual benchmarks, across benchmark suites, and during adaptive evaluation, together with work on redundancy and reliability. We compare their information needs, total costs, reliability checks, and limitations. Methods reduce evaluation costs by selecting representative subsets, using cheaper or reusable information, and testing adaptively, but risk poor coverage, inaccurate estimates, and sequential delays. The resulting taxonomy and practical guide help researchers choose, validate, and deploy methods for more efficient and reliable LLM evaluation.
