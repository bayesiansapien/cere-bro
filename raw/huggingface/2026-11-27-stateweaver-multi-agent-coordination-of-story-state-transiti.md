---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34290
url: https://huggingface.co/papers/2611.34290
arxiv_url: https://arxiv.org/abs/2611.34290
date: 2026-11-27
---

# StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation

Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context, while reference updates remain limited. We introduce StateWeaver, which combines Active States and Hierarchical Collaboration to connect review-driven visual reference updates with cross-shot state inheritance. Active States translate state discrepancies identified during review into concrete visual asset requirements that guide reference construction, validation, and regeneration, preserving identity and already-correct content while repairing target attributes. Confirmed generation results are linked to the corresponding asset states, story time, and reference versions for verification and reuse by subsequent shots. Hierarchical Collaboration isolates execution contexts by task, clip, and repair round, and uses hierarchical memory to organize this process across multiple sets. Across multiple benchmarks, StateWeaver outperforms existing methods and produces long videos with sustained cross-shot consistency under predefined and autonomously planned storyboards.
