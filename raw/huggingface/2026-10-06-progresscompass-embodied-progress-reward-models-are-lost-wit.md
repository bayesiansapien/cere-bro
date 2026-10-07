---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.36684
url: https://huggingface.co/papers/2609.36684
arxiv_url: https://arxiv.org/abs/2609.36684
date: 2026-10-06
---

# ProgressCompass: Embodied Progress Reward Models Are Lost Without the Right Context

Embodied agents now take on ever longer tasks. For long tasks, knowing only whether a task finally succeeds or fails says little; the steps along the way matter. Progress Reward Models (PRMs) score how far a task has come at every step, and serve as dense rewards, verifiers and monitors. Yet in long tasks the current frame alone often cannot tell how far the task has come, because progress depends on what happened before. We call this problem context-dependent progress estimation. Existing benchmarks on progress estimation mostly focus on short tasks whose progress can be read from the current observation, and whether PRMs can estimate progress when context is needed remains underexplored. We therefore build ContextProgress-Bench, with 24 manipulation tasks for 120 episodes. The benchmark covers three settings: (i) State Recall, where information needed for progress appeared earlier but is not in the current frame; (ii) Sequence Tracking, where steps follow a fixed order, so progress requires knowing which steps are done and which comes next; and (iii) Recurrence Disambiguation, where look-alike frames sit at very different progress. We then run a paired diagnosis: each PRM keeps the same input format in both runs, and in one run its instruction integrates the right context. Even PRMs that read the entire history get lost in estimating progress, yet with the right context the same five models cut their progress error by 77-82%. Embodied PRMs are thus not incapable of progress estimation, but lost without the right context. We therefore propose ProgressCompass, an autonomous agentic loop that reorients an existing PRM and uses current general-purpose VLMs to supply the context the PRM needs. Wrapped in the loop, the same frozen PRM cuts its progress error by 63% and raises its rank agreement by 76%. With such a compass, PRMs estimate progress far better on longer, more complex tasks.
