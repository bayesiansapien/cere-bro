---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.531524+00:00
arxiv_id: 2611.08219
url: https://huggingface.co/papers/2611.08219
arxiv_url: https://arxiv.org/abs/2611.08219
date: 2026-11-13
---

# Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis

Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A key bottleneck is the lack of scalable post-training data that reflects real work intent, authentic file environments, and deliverable-level evaluation. To close this gap, we introduce Agent-R^2, a real-source data synthesis framework that scales training data for realistic productivity work. Instead of relying on manually specified workflows or LLM-generated files, Agent-R^2 grounds synthesis throughout the pipeline in real occupational seeds, corpus-derived workflow evidence, and authentic web-sourced files. From 10k web-corpus candidates, Agent-R^2 distills 4k task instances that pair real multi-format attachments with fine-grained, deliverable-level rubrics. On this data, we train Agent-R^2-4B via supervised fine-tuning and rubric-based reinforcement learning, improving both end-to-end productivity performance and file-grounded reasoning. Trained on only 4k instances, Agent-R^2-4B surpasses Qwen3-235B-A22B-Thinking-2507 on both GDPval (51.0% vs. 48.0%) and OfficeQA (14.8% vs. 13.8%). Further analysis shows that Agent-R^2 mitigates shortcut behavior, where agents produce superficially plausible deliverables before sufficiently grounding, constructing, or verifying them, while promoting sustained exploration.
