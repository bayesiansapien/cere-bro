---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.08639
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2512.08639
published: 2026-04-16
authors: Huilin Xu, Zhuoyang Liu, Yixiang Luomei
---

# Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning

**arXiv:** https://arxiv.org/abs/2512.08639
**Authors:** Huilin Xu, Zhuoyang Liu, Yixiang Luomei

## Abstract

arXiv:2512.08639v3 Announce Type: replace-cross  Abstract: Aerial Vision-and-Language Navigation (VLN) aims to enable unmanned aerial vehicles (UAVs) to interpret natural language instructions and navigate complex urban environments using onboard visual observation. This task holds promise for real-world applications such as low-altitude inspection, search-and-rescue, and autonomous aerial delivery. Existing methods often rely on panoramic images, depth inputs, or odometry to support spatial reasoning and action planning. These requirements increase system cost and integration complexity, thus hindering practical deployment for lightweight UAVs. We present a unified aerial VLN framework that operates solely on egocentric monocular RGB observations and natural language instructions. The model formulates navigation as a next-token prediction problem, jointly optimizing spatial perception, trajectory reasoning, and action prediction through prompt-guided multi-task learning. Moreover, we propose a keyframe selection strategy to reduce visual redundancy by retaining semantically informative frames, along with an action merging and label reweighting mechanism that mitigates long-tailed supervision imbalance and facilitates stable multi-task co-training. Extensive experiments on the AerialVLN and OpenFly benchmark validate the effectiveness of our method. Under the challenging monocular RGB-only setting, our model achieves strong results across both seen and unseen environments. It significantly outperforms existing RGB-only baselines and narrows the performance gap with state-of-the-art panoramic RGB-D counterparts. Comprehensive ablation studies further demonstrate the contribution of our task design and architectural choices. Our code is publicly available at https://github.com/return-sleep/AeroAct.
