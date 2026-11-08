---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.593417+00:00
arxiv_id: 2611.02660
url: https://huggingface.co/papers/2611.02660
arxiv_url: https://arxiv.org/abs/2611.02660
date: 2026-11-07
---

# HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation

Recent advances in Vision-Language-Action (VLA) models have enabled fine manipulation capabilities, yet performing tasks that require working memory remains a key challenge. Most existing VLA architectures operate under a Markovian assumption, mapping only the current observation to an action, which leads to failure in non-Markovian environments. Inspired by the human 'inner monologue', we propose Hierarchical Explicit Language Memory (HeLM), a hierarchical VLA framework that maintains task-relevant history in explicit language through factorized event detection and event-triggered memory updates. We evaluate HeLM across 10 non-Markovian real-world tasks with 56 variants, including five newly formulated inter-episode tasks that require persistent context across task boundaries. HeLM improves intra-episode success by 12.8 percentage points over the strongest baseline and achieves 78% subtask success on compositional generalization tasks, while using up to 4.5x less memory and running 2.5x faster than the keyframe baseline at long horizons.
