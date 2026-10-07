---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02331
url: https://huggingface.co/papers/2610.02331
arxiv_url: https://arxiv.org/abs/2610.02331
date: 2026-10-06
---

# World Editing: Intervening on Executable Worlds at Increasing Depth

Interactive world models are increasingly capable of generating environments and acting within them, yet deliberately editing an existing executable world remains underexplored. We formulate world editing as intervening on an existing world while preserving properties that should remain unchanged, and introduce intervention depth as an axis describing how strongly an edit couples world entities, dynamics, and systems. We instantiate this capability through industry-grade game modding and introduce IGMWorld, together with IGMBench, a benchmark of 110 tasks and over 1.1K executable state and behavioral criteria across Minecraft and Terraria. The tasks span property, entity, dynamics, and system interventions and are evaluated through deterministic executability, behavioral, preservation, and visual checks. Frontier coding agents already exhibit substantial world-editing capability: the strongest configuration solves 78.2% of tasks under a strict task-level criterion, while criterion-level performance reaches 94.8%. Reliability generally decreases with intervention depth, and this pattern persists even among tasks with similar numbers of evaluation criteria. Most failed edits still build and load successfully, suggesting that the main difficulty is making the edited world behave as requested. Visual consistency remains a separate weakness, with all evaluated configurations below 50% joint visual pass rate. These results show that world editing is a distinct capability from world generation and interaction, and that executable games provide a practical testbed for studying it.
