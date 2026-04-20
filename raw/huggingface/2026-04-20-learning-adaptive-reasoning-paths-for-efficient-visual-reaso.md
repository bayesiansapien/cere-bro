---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.14568
url: https://huggingface.co/papers/2604.14568
arxiv_url: https://arxiv.org/abs/2604.14568
date: 2026-04-20
---

# Learning Adaptive Reasoning Paths for Efficient Visual Reasoning

Visual reasoning models (VRMs) have recently shown strong cross-modal reasoning capabilities by integrating visual perception with language reasoning. However, they often suffer from overthinking, producing unnecessarily long reasoning chains for any tasks. We attribute this issue to Reasoning Path Redundancy in visual reasoning: many visual questions do not require the full reasoning process. To address this, we propose AVR, an adaptive visual reasoning framework that decomposes visual reasoning into three cognitive functions: visual perception, logical reasoning, and answer application. It further enables models to dynamically choose among three response formats: Full Format, Perception-Only Format, and Direct Answer. AVR is trained with FS-GRPO, an adaptation of Group Relative Policy Optimization that encourages the model to select the most efficient reasoning format while preserving correctness. Experiments on multiple vision-language benchmarks show that AVR reduces token usage by 50-90% while maintaining overall accuracy, especially in perception-intensive tasks. These results demonstrate that adaptive visual reasoning can effectively mitigate overthinking in VRMs. Code and data are available at: https://github.com/RunRiotComeOn/AVR.
