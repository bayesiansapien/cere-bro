---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.594004+00:00
arxiv_id: 2610.37739
url: https://huggingface.co/papers/2610.37739
arxiv_url: https://arxiv.org/abs/2610.37739
date: 2026-11-07
---

# OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery

Large language models (LLMs) have shown increasing promise in research-level problem solving, yet a comprehensive collection of such problems is still missing, and evaluating them on research-level problems remains challenging. We introduce OpenFrontiers, a cross-disciplinary resource that combines a structured corpus of open research problems with a retrospective benchmark of recently resolved problems in mathematics. The corpus records problem statements, context, progress, and other information for 12,151 problems. The benchmark contains 200 problems, 110 resolved in 2026 and 90 still open, each with a Lean~4 statement checked by automated probes and two independent reviews; a subset HQ-50 further filters based on quality score, etc. Our evaluation protocol grades formal proofs with two independent checkers in an isolated sandbox under closed-book, frozen-retrieval, and live-web conditions. Evaluating seven LLM agents on the HQ-50 subset under a standardized budget, we find that closed-book rediscovery is rare, at most 7 of 40 resolved problems, whereas live-web success mostly reflects retrieval of published solutions. By linking a broad research-problem corpus to a formally graded evaluation subset with documented solutions, OpenFrontiers provides a foundation for measuring research-level rediscovery and studying progress toward solving currently open scientific problems. The dataset and benchmark could be found in https://huggingface.co/collections/FlippyDora/openfrontiers.
