---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33503
url: https://huggingface.co/papers/2610.33503
arxiv_url: https://arxiv.org/abs/2610.33503
date: 2026-10-27
---

# Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination

Patent examination is a challenging real-world task that requires agents to discover sparse prior art, iteratively refine queries, inspect technical evidence, and produce novelty assessments documented in Office Actions (OAs) across heterogeneous scientific and technical domains. However, existing benchmarks largely focus on static and limited candidate sets, leaving the full search--reasoning--assessment process underexplored. We present PatEx-Gym, the first framework for developing and evaluating agents for patent examination, which integrates three components. First, PatEx-Bench provides 1K realistic examination tasks, two large-scale retrieval corpora containing over 1M patents and 52K scientific papers, and a harness runtime supporting iterative search, document visits, reasoning, and OA generation. Second, we introduce PASS, an annotation-free Prior-Art Agentic Search Trajectory Synthesis framework. Specifically, it exploits document visits as implicit relevance signals and evidence-acquisition anchors to model intra-turn query behavior, inter-turn search progression, and trajectory-level evidence and outcome quality, yielding PatEx-SynData. Third, we train PatEx-Agent at the 4B scale via supervised fine-tuning on the curated trajectories, establishing a lightweight baseline. Extensive experiments show that final decision accuracy alone does not fully reflect examination quality, while prior-art discovery remains difficult even for strong frontier models. Our PatEx-Agent achieves competitive performance against substantially larger general-purpose agents. These results show that training on PatEx-SynData enables a compact 4B model to serve as a competitive baseline for prior-art search and patent examination. We view patent examination as a demanding testbed for agentic search and deep research agents.
