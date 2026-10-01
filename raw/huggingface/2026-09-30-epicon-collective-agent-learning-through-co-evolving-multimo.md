---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37923
url: https://huggingface.co/papers/2609.37923
arxiv_url: https://arxiv.org/abs/2609.37923
date: 2026-09-30
---

# EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory

Agents can learn from past executions, but enabling different agents to reuse and build on one another's experience remains challenging. We introduce EpiCon, a shared multimodal memory framework for agent collective learning without updating host model parameters. EpiCon links question-level memory evolution to a persistent experience bank through two independently trained 2B models: a memory controller and a tree self-organizer. The controller jointly refines textual guidance and visual evidence across attempts and selectively includes visual memory. The self-organizer consolidates lessons hierarchically and retrieves experience and rules for new problems. We evaluate EpiCon on eleven benchmarks spanning four multimodal task domains, using two harnesses and multiple backbones. A frozen bank improves other systems even with a single solving attempt. A second harness raises the original system's macro-average score by 2.6 points across eleven benchmarks. Across four host configurations, EpiCon improves macro-average scores by 1.7 to 4.9 points over No Memory and reduces memory-operation time by 67\% to 74\% relative to backbone-sized memory models.
