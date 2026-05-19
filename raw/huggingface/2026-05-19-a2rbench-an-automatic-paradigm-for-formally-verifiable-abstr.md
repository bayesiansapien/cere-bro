---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17278
url: https://huggingface.co/papers/2605.17278
arxiv_url: https://arxiv.org/abs/2605.17278
date: 2026-05-19
---

# A2RBench: An Automatic Paradigm for Formally Verifiable Abstract Reasoning Benchmark Generation

Abstract reasoning ability reflects the intelligence and generalization capacity of LLMs to extract and apply abstract rules. However, accurately measuring this ability remains challenging: existing benchmarks either rely on expensive manual annotation, limiting their scale, or risk measuring memorization rather than genuine reasoning. To address this, we introduce an automated pipeline named A2RBench, encompassing generation, expansion, evaluation, and analysis. Specifically, in the generation stage, LLMs create diverse tasks demanding genuine reasoning; in the expansion stage, LLMs reuse validated rules and expand new input spaces to generate task variations, achieving scaling. However, such a process may cause hallucinations. To eliminate it, we further establish a theoretical framework and prove that programmatic verification--testing whether the inverse operation perfectly reverses the forward operation (cycle consistency)--guarantees a unique solution. Through extensive evaluations on mainstream LLMs, we find: (1) Current LLMs exhibit fundamental deficiencies in abstract reasoning, with top models significantly underperforming humans on a representative subset (39.8% vs. 68.5%). (2) Current LLMs fall far short of 2D and 1D in the complexity of generated 3D tasks, revealing their lack of understanding of high-dimensional tasks. (3) Counterintuitively, inputs with higher information complexity can simplify the reasoning process.
