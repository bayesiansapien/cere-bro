---
source: farmer/huggingface
farmed: 2026-07-29T08:14:21.288961+00:00
arxiv_id: 2607.24957
url: https://huggingface.co/papers/2607.24957
arxiv_url: https://arxiv.org/abs/2607.24957
date: 2026-07-29
---

# PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models

We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs). Existing benchmarks often fail to isolate perception: holistic evaluations conflate perceptual errors with failures in reasoning or domain knowledge, while application-driven benchmarks only cover narrow, fragmented domains shaped by heuristic designs. To address these limitations, PerceptionBench adopts a bottom-up approach: by diagnosing the earliest failure points in the responses of frontier MLLMs across 42 existing benchmarks, we construct an error taxonomy whose perception branch defines ten atomic perceptual capabilities. Guided by this taxonomy, we construct 3,000 verified questions with short, unambiguous answers, each isolating a single capability, with difficulty stemming from perception rather than reasoning or knowledge. Benchmark results across sixteen frontier MLLMs reveal that atomic perception remains largely unsolved---no model reaches 60\% accuracy, perception-related hallucination is the weakest capability on average, and similar overall scores conceal sharply divergent capability profiles. PerceptionBench thus provides a capability-level standard for measuring and diagnosing the visual perception boundaries of MLLMs.
