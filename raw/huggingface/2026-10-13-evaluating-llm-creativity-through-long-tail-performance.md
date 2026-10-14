---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.12998
url: https://huggingface.co/papers/2610.12998
arxiv_url: https://arxiv.org/abs/2610.12998
date: 2026-10-13
---

# Evaluating LLM Creativity through Long-Tail Performance

Creativity benchmarks for large language models (LLMs) vary widely in task and metric design. This raises the question of whether they capture a common notion of creativity. We propose that this shared target can be formalized as task-specific performance in the long tail of a reference input-output distribution, which describes how common input-output pairs are relative to a chosen source of text. We ground this proposition in the novelty-quality product formulation and evaluate it empirically across 15 benchmarks and 26 open-weight models, using n-gram absence from the pretraining data as a novelty proxy. Our results show that creativity benchmarks lie further in the tail regions than standard benchmarks. Moreover, on both creativity and standard benchmarks, model rankings from higher-tail subsets of each benchmark align more closely with human creativity judgments in LM-Arena. Building on these findings, we introduce q@Tail(α), a lower-cost creativity diagnostic that measures mean task quality on the tail fraction of an existing benchmark. Applying it to creativity-promoting methods reveals substantial room to improve LLM creativity through stronger tail performance.
