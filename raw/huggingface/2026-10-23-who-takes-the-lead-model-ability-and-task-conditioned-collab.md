---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.886968+00:00
arxiv_id: 2610.27148
url: https://huggingface.co/papers/2610.27148
arxiv_url: https://arxiv.org/abs/2610.27148
date: 2026-10-23
---

# Who Takes the Lead? Model Ability and Task-Conditioned Collaboration with Humans

As language-model agents grow more capable, they can carry more of a task without asking anyone for help. Falling reliance on a human partner is easy to read as a failure of collaboration when it may instead be a correct division of labor, and the rate of human involvement alone cannot tell the two apart. We study this systematically by placing an agent and a person under a shared objective while varying who holds the advantage: the human has a clear advantage, neither does, or the agent does. To obtain this control, we introduce a shared-control maze, in which an agent-controlled and a human-controlled avatar share the objective of reaching a common target in as few team turns as possible. The agent allocates each team turn between acting itself and handing the move to the person, and initial placement sets the human's shortest-path advantage while the task is otherwise unchanged. We evaluate GPT~5.6~Sol, Command~A+, Qwen~3.8~27B, and Command~R, first measuring solo capability with a single avatar and full-map observability, then running co-play with human participants across the three advantage conditions. Across the four models, stronger solo performance is associated with selective, route-conditioned human involvement: the models that solve the maze reliably on their own act for themselves almost without exception when the human holds no advantage, and involve the human on roughly 80% of initial decisions when the human route is shorter. Command R, the model with substantially weaker solo performance, shows no such selectivity.
