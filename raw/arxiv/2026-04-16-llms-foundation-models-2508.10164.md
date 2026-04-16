---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2508.10164
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2508.10164
published: 2026-04-16
authors: Bin Hong, Jiayu Liu, Kai Zhang
---

# Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization

**arXiv:** https://arxiv.org/abs/2508.10164
**Authors:** Bin Hong, Jiayu Liu, Kai Zhang

## Abstract

arXiv:2508.10164v2 Announce Type: replace  Abstract: Recent advances in Large Reasoning Models (LRMs) have demonstrated strong performance on complex tasks through long Chain-of-Thought (CoT) reasoning. However, their lengthy outputs increase computational costs and may lead to overthinking, raising challenges in balancing reasoning effectiveness and efficiency. Current solutions often compromise reasoning quality or require extensive resources. In this paper, we investigate how to reduce the generation length of LRMs with limited tuning. We analyze generation path distributions and filter generated trajectories through difficulty estimation. Subsequently, we analyze the convergence characteristics of various preference optimization objectives under a unified Bradley-Terry loss based framework. Based on the analysis, we propose Length Controlled Preference Optimization (LCPO) that directly balances the implicit reward related to NLL loss. LCPO can effectively learn length preference with limited data and training. Extensive experiments demonstrate that our method significantly reduces the average output length of LRMs by over 50\% across multiple benchmarks while maintaining the reasoning performance. Our work highlights the potential for computationally efficient approaches in guiding LRMs toward efficient reasoning.
