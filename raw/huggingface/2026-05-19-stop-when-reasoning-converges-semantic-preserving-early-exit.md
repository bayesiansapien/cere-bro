---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17672
url: https://huggingface.co/papers/2605.17672
arxiv_url: https://arxiv.org/abs/2605.17672
date: 2026-05-19
---

# Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models

Large Reasoning Models (LRMs) achieve strong performance by generating long chains of thought (CoT), but often overthink, continuing to reason after a solution has already stabilized and thereby wasting tokens and increasing latency. Existing inference-time early-exit methods rely primarily on answer-level signals, such as confidence or trial-answer consistency, to decide when to stop. However, these signals mainly reflect answer readiness rather than reasoning convergence: they may trigger before the model has finished exploring or self-correcting, causing premature exits that can degrade final-answer accuracy and leave the retained reasoning chain semantically incomplete. We identify reasoning-level semantic redundancy as a complementary signal for semantic-preserving early exit: when successive steps no longer add novel progress and instead revisit established conclusions, the reasoning trajectory has likely converged. Building on this insight, we propose PUMA, a plug-and-play framework that combines a lightweight Redundancy Detector with answer-level verification. The detector flags semantically redundant candidate exits, while verification confirms whether stopping is safe, allowing PUMA to remove redundant continuation while preserving both answer accuracy and a coherent reasoning prefix. Across five LRMs and five challenging reasoning benchmarks, PUMA achieves 26.2% average token reduction while preserving accuracy and retained CoT quality. Additional experiments on code generation, zero-shot vision-language reasoning, and learned stopping-policy internalization further demonstrate that reasoning-level redundancy is a robust, transferable, and learnable signal for efficient reasoning. Our code is available at https://github.com/giovanni-vaccarino/PUMA.
