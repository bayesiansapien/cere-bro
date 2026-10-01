---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36071
url: https://huggingface.co/papers/2609.36071
arxiv_url: https://arxiv.org/abs/2609.36071
date: 2026-09-30
---

# LongCat-DeepResearch Technical Report

We present LongCat-DeepResearch, a deep research system that combines an enhanced LongCat model with a multi-agent workflow for producing comprehensive, evidence-grounded reports. The workflow separates global planning from detailed investigation and coordinates revision at the section level. Multiple planning agents first explore external sources and refine an actionable research plan, termed ResearchSpec. Research agents then investigate and draft their assigned sections in parallel, gathering additional evidence in separate contexts as their analyses develop. Once the sections are assembled, global review guides targeted local revisions, reducing reliance on repeated full-report rewriting. This workflow also supports the construction of research tasks and trajectories for the mid-training and post-training of LongCat's general-purpose models. LongCat-DeepResearch achieves 55.25 on DeepResearchBench, 51.35 on DeepResearchBench II, and 79.83 on ResearchRubrics. On an in-house benchmark, it scores 76.04, ranking second among four compared systems. Development-set analyses show benefits from combining planning perspectives, while further planning refinement has mixed effects. Additional editing improves average automatic readability preference across two benchmarks, with different trends on each.
