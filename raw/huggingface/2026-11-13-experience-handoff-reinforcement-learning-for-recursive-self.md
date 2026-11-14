---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.532783+00:00
arxiv_id: 2611.16409
url: https://huggingface.co/papers/2611.16409
arxiv_url: https://arxiv.org/abs/2611.16409
date: 2026-11-13
---

# Experience-Handoff Reinforcement Learning for Recursive Self-Improvement

It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this rich information, recent works wrap the agent in a harness that refines its own inputs through reflection or compaction and hands past experience to future rollouts, but the construction of the handed-off artifacts (e.g., a playbook) is itself not learned. We want the best of both worlds: gradient updates from a scalar reward, while also utilizing environment information to hand off experience. As a concrete testbed, we fix the Agentic Context Engineering () harness and train one model to act, reflect, and curate task-local playbooks. Our method, , evaluates candidate experience-handoff artifacts by their downstream effect on future actor rollouts, and co-optimizes the role-specific behaviors (action generator, insight reflector, and playbook curator) under a fixed scaffold. Across agentic benchmarks,  achieves higher held-out performance than baseline methods. The results suggest that agent training should optimize not only the actions in the current rollout, but also the model-written experience that future rollouts inherit.
