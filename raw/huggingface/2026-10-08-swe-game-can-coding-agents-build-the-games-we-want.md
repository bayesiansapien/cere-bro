---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.304893+05:30
arxiv_id: 2609.33678
url: https://huggingface.co/papers/2609.33678
arxiv_url: https://arxiv.org/abs/2609.33678
date: 2026-10-08
---

# SWE-Game: Can Coding Agents Build the Games We Want?

We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D. Five task types cover development from a brief, implementation from a game design document, skeleton completion, repair of 83 injected-fault cases, and Godot-to-Unity porting. Reference materials specify the intended gameplay, while a shared instrumentation interface lets evaluator-owned drivers and probes execute actions and observe independently implemented games. Evaluation combines engine-state checks, certified reference-input replay, and agent-authored feature demonstrations to assess mechanic correctness, demonstrated playability, and behavioral restoration and preservation after repairs. Game-specific vision-language rubrics separately assess presentation. Across six models, Opus5 achieves the highest overall score in all five task types. Best overall scores remain below 60 out of 100 across the three construction tasks, with Brief-to-Game reaching 50.38. Analysis of reviewed submissions identifies requirement omissions and gameplay logic errors as predominant implementation problems. On human-labeled behaviors from 100 agent-built games, executable checks achieve 92.59% balanced accuracy, compared with 78.41% for a video-based VLM judge. Rubric-based visual scores reach a Spearman correlation of 0.829 with human ratings of 200 gameplay clips. Together, these results characterize current agent capabilities across game-development activities and support combining runtime evidence with visual assessment.
