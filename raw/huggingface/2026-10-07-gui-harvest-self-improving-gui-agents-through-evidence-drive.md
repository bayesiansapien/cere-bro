---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.00948
url: https://huggingface.co/papers/2610.00948
arxiv_url: https://arxiv.org/abs/2610.00948
date: 2026-10-07
---

# GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution

The executable harness surrounding a GUI model determines how observations are assembled, actions are executed, and verification, recovery, and termination are controlled. Compared with harness optimization for non-GUI agents, automatically optimizing this harness poses three coupled challenges: reconciling model intent with observed visual effects, diagnosing failures under variable execution outcomes, and identifying recurrent failure patterns across tasks and translating them into reusable runtime changes. We introduce GUI-HARVEST, an automatic harness optimizer that enables self-improving GUI agents with frozen backbone models. First, to ground diagnosis in observed action effects, it aligns model outputs and executed actions with before-and-after screenshots, tying findings to specific interface transitions. Second, to account for execution variability, it treats repeated runs of the same task as a joint evidence unit, using within-task comparisons to locate outcome-relevant behavioral differences. Third, it consolidates verified findings across tasks into recurring failure patterns, maps them to bounded source-code edits with predictions recorded before evaluation, and checks the predicted behavioral effects alongside task performance through repeated execution. Experiments on OSWorld-Verified show consistent held-out gains across six general-purpose open, GUI-specialized open, and proprietary backbone models; Qwen3-VL-32B-Instruct gains 12.33 points on the full suite. Frozen-harness transfer improves GPT-5 by 13.87 percentage points on WindowsAgentArena at 50 steps without further optimization. With the same backbone and initial harness, GUI-HARVEST outperforms Self-Harness and Meta-Harness, suggesting that GUI-specific diagnosis and validation help harness improvements generalize to unseen tasks. The code is available at https://github.com/GaryYang12345/GUI-HARVEST.
