---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.325085+00:00
arxiv_id: 2611.02810
url: https://huggingface.co/papers/2611.02810
arxiv_url: https://arxiv.org/abs/2611.02810
date: 2026-11-10
---

# TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation

This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our TRIO is to equip three well-designed agents with an iterative refinement paradigm by aligning their individual optimization objectives. Specifically, we first expand ambiguous queries with a query extension agent and quantify the reward based on the improved answer quality, which can be utilized to refine our agent for higher expansion efficiency. To enhance the retrieval quality, we include a unanimity voting to annotate the expanded query as insufficient or sufficient, and their generative outcomes are utilized as ground truth to optimize the judge agent. To further improve evidence utilization and answer accuracy, an answer agent is optimized with dynamic matching-based rewards with curriculum learning for final outputs. Extensive experiments across multiple benchmark datasets validate the effectiveness of the proposed TRIO in comparison with state-of-the-art approaches. Our code is available at https://github.com/yingtaoren/TRIO.
