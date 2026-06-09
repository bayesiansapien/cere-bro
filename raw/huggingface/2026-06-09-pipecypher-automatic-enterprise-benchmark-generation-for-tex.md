---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.08481
url: https://huggingface.co/papers/2606.08481
arxiv_url: https://arxiv.org/abs/2606.08481
date: 2026-06-09
---

# PIPE-Cypher: Automatic Enterprise Benchmark Generation for Text-to-Cypher Systems

Enterprise property graphs vary widely in schema structure, internal terminology, domain assumptions, governance constraints, and user interaction patterns. A deployment-relevant Text2Cypher benchmark therefore reflects the questions users and agents actually ask of that graph. Creating such a benchmark is difficult because schemas and values are unique, and graph structure changes over time. Each NL-query pair must also be executable, use real graph entities, preserve diversity, and remain balanced across query types and difficulty levels. We present PIPE-Cypher, a local benchmark-generation pipeline that turns a live property graph and optional seed queries from customer questions, analyst logs, or agent tool calls into balanced NL-to-Cypher benchmarks. PIPE-Cypher combines schema profiling, reverse-query grounding, constrained generation, deterministic Cypher governance, execution validation, redaction, diversity controls, and a calibrated local LLM judge. Using local Qwen3.5-9B generation and judging, PIPE-Cypher exports 3,000 accepted FinBench/SNB examples, completes three audited ablation suites, calibrates judge behavior with human labels, and evaluates 11 local downstream models. The resulting benchmark is deliberately discriminative: zero-shot transfer is weak, while a few-shot control shows that schema-specific example banks can help compatible model families. Together, PIPE-Cypher makes Text2Cypher benchmarking a repeatable process that evolves with the graph, its users, and its target workloads.
