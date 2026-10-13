---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.217511+05:30
arxiv_id: 2610.12341
url: https://huggingface.co/papers/2610.12341
arxiv_url: https://arxiv.org/abs/2610.12341
date: 2026-10-12
---

# Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition

Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AAArena, a benchmark comprising 12 authentic adversarial games and 1,920 archived human programs, with an evaluation protocol modeled on real-world game competitions. Agents interpret rules, choose opponents, analyze replays, and revise game agents to achieve their highest ranking within fixed match and evaluation budgets. We evaluate completedmodels model and harness configurations: Opus5.5 with Claude Code earns 6 gold medals, while no evaluated configuration tops the remaining 6 human ladders. Performance is generally weaker in games with more complex rule specifications. Further experiments show that opponent selection and dense feedback support policy improvement, and that agents learn from both on-policy replays of their own matches and off-policy replays of other players' matches. These results highlight HL's potential in adversarial games and identify persistent challenges in game understanding, strategy implementation, and long-horizon policy development.
