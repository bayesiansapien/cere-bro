---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12925
url: https://huggingface.co/papers/2605.12925
arxiv_url: https://arxiv.org/abs/2605.12925
date: 2026-05-14
---

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

Evaluation of software engineering (SWE) agents is dominated by a binary signal: whether the final patch passes the tests. This outcome-only view treats a principled solution and a chaotic trial-and-error process as equivalent. We show that this equivalence is empirically false. We evaluate 2,614 OpenHands trajectories from eight model backends on SWE-bench Verified. Of the 60 tasks in this corpus, 47 have enough passing trajectories to construct task-level process references, yielding a 1,815-trajectory evaluation subset. Among passing trajectories in this subset, 10.7% exhibit behavior we call a Lucky Pass: regression cycles, blind retries, missing verification, or temporally disordered exploration, implementation, and verification. We introduce AgentLens, a framework for process-level assessment of SWE-agent trajectories, and release AgentLens-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points, and 47 task-level Prefix Tree Acceptor (PTA) references. AgentLens combines two components. First, it merges multiple passing solutions for the same task into a PTA reference space of correct behaviors. Second, it uses a context-sensitive intent-stage labeler that assigns actions to Exploration, Implementation, Verification, or Orchestration using trajectory history rather than tool identity alone. On AgentLens-Bench, the composite score separates passing trajectories into Lucky, Solid, and Ideal tiers; decomposes Lucky Passes into five recurring mechanisms; and changes how the eight evaluated model backends are ranked compared with pass rate alone. Across these models, AgentLens classifies between 0.5% and 23.2% of successful trajectories as Lucky, and some models move by as many as five rank positions when ranked by quality score instead of pass rate.
