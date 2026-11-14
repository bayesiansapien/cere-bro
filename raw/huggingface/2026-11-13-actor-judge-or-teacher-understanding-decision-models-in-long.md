---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.527586+00:00
arxiv_id: 2611.17167
url: https://huggingface.co/papers/2611.17167
arxiv_url: https://arxiv.org/abs/2611.17167
date: 2026-11-13
---

# Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents

Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges on ALFWorld, and use JEV as a teacher on ALFWorld and WebShop. As actors, all six models are pulled away from a subgoal that must come first by an easier one. As judges that see the whole trajectory, the same models credit the steps toward that subgoal, and asking whether each action helped, rather than whether the task will succeed, separates useful from useless actions. As a teacher, JEV raises a Qwen2.5-1.5B policy over GRPO from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop. These results suggest that a poor actor can still teach well, because judging an action after the episode ends reveals the consequences that acting must anticipate. Code is available at https://github.com/ZJU-REAL/decision-agents.
