---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.799739+00:00
arxiv_id: 2610.32002
url: https://huggingface.co/papers/2610.32002
arxiv_url: https://arxiv.org/abs/2610.32002
date: 2026-10-26
---

# DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation

The rapid growth of microdramas has increased demand for high-quality script production. Long-form microdrama script generation with LLMs requires both diverse plot progression and long-range narrative coherence. Our observations reveal that candidate continuations increasingly concentrate on fewer narrative mechanisms as generation progresses, while conventional retrieval may reinforce trope reuse and overlook historical information essential to future plots. To address these challenges, we propose DraMaze, a multi-agent pipeline that explores diverse causal paths through trope memory-guided evolutionary tree search and mutation. It further constructs a Backward Narrative Dependency Tree to organize, retain, and retrieve historical memories based on future narrative goals. We also introduce MiDramaBench, a bilingual benchmark for evaluating script logic and creative quality across different script lengths, together with causal-pattern metrics for narrative repetition and diversity. Experiments show consistent improvements across three backbone LLMs. For 60-episode scripts of up to 60k words, DraMaze reduces causal-pattern repetition by 32.1% and achieves a Logic score of 82.5, outperforming the best-performing baseline by 8.5 points.
