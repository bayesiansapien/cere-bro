---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12913
url: https://huggingface.co/papers/2605.12913
arxiv_url: https://arxiv.org/abs/2605.12913
date: 2026-05-14
---

# Revisiting DAgger in the Era of LLM-Agents

Long-horizon LM agents learn from multi-turn interaction, where a single early mistake can alter the subsequent state distribution and derail the whole trajectory. Existing recipes fall short in complementary ways: supervised fine-tuning provides dense teacher supervision but suffers from covariate shift because it is trained on off-policy teacher trajectories; while reinforcement learning with verifiable rewards avoids this off-policy mismatch by learning from on-policy rollouts but with only sparse outcome feedback. We address this dilemma by revisiting Dataset Aggregation (DAgger) for multi-turn LM agents: the algorithm collects trajectories through a turn-level interpolation of student and teacher policies, and the student is then trained on these trajectories using supervised labels provided by the teacher. By directly interacting with environments, we expose the model to realistic states likely to be encountered during deployment, thereby effectively mitigating covariate shift. Besides, since the student is learned by mimicking the teacher's behavior, it receives rich feedback during learning. To demonstrate DAgger enjoys the benefits of both worlds, we tested the algorithm to train a software-engineering agent with 4B- and 8B-scale student models. On SWE-bench Verified, our DAgger-style training improves over the strongest post-training baseline by +3.9 points at 4B and +3.6 points at 8B. The resulting 4B agent reaches 27.3%, outperforming representative published 8B SWE-agent systems.
