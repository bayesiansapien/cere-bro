---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15963
url: https://huggingface.co/papers/2605.15963
arxiv_url: https://arxiv.org/abs/2605.15963
date: 2026-05-18
---

# PAGER: Bridging the Semantic-Execution Gap in Point-Precise Geometric GUI Control

Large vision-language models have significantly advanced GUI agents, enabling executable interaction across web, mobile, and desktop interfaces. Yet these gains largely rely on a forgiving region-tolerant paradigm, where many nearby pixels inside the same component remain valid. Precise geometric construction breaks this assumption: actions must land on points in continuous canvas space rather than tolerant regions. Because geometric primitives carry ontological dependencies, a local coordinate error can induce cascading topological failures that distort downstream objects and invalidate the final construction. We identify this regime as precision-sensitive GUI tasks, requiring point-level accuracy, geometry-aware verification, and robustness to dependency-driven error propagation. To benchmark it, we introduce PAGE Bench, with 4,906 problems and over 224K process-supervised, pixel-level GUI actions. We further propose PAGER, a topology-aware agent that decomposes construction into dependency-structured planning and pixel-level execution. Pixel-grounded supervised tuning establishes executable action grammar, while precision-aligned reinforcement learning mitigates rollout-induced exposure bias through state-conditioned geometric feedback. Experiments reveal a pronounced Semantic-Execution Gap: general multimodal models can exceed 88% action type accuracy yet remain below 6% task success. PAGER closes this gap, delivering 4.1x higher task success than the strongest evaluated general baseline and raising step success rate from below 9% for GUI-specialized agents to over 62%.
