---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.13560
url: https://huggingface.co/papers/2608.13560
arxiv_url: https://arxiv.org/abs/2608.13560
date: 2026-08-14
---

# AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design priors, where a meta-harness optimizer guides a code agent to recursively improve harness based on rollout feedback. To instantiate and evaluate this framework, we focus on the academic paper-to-poster generation task and introduce PosterBench, comprising a 100-paper Main Track spanning five disciplines and PosterBench-mini, a shared 10-paper subset for controlled evaluation. On the PosterBench Main Track, AutoDesign achieves the highest score of 78.32, surpassing the closed-source commercial system Claude Design by 7.45 points. Across seven controlled code-agent-model configurations, integrating the learned DesignHarness consistently improves performance, increasing the average PosterBench Score from 54.99 to 67.39 (+12.4%). In a fully autonomous long-horizon loop, it executes 253 tool calls and 11 editing turns within 40 minutes for under $3, reaching average conference-poster quality in human evaluation. A system-blind human study further demonstrates that AutoDesign achieves the highest human preference among evaluated systems.
