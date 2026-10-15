---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.502360+00:00
arxiv_id: 2609.38847
url: https://huggingface.co/papers/2609.38847
arxiv_url: https://arxiv.org/abs/2609.38847
date: 2026-10-14
---

# Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics

Rubric-based reinforcement learning (Rubric-RL) trains language models where no verifier exists. A judge checks each criterion of a rubric, and the verdicts are aggregated into a reward, most often by a weighted sum. We show that this additive aggregation is the weak point. Under a sum, criteria compensate for one another: a policy that misses the one decision that matters can buy the points back with advice nobody asked for. On clinical consultation, such a policy scores higher and answers worse. Rubric coverage rises while appropriateness on held-out physician criteria falls below the untrained model. The medical criteria are not to blame. Grouped so that they must hold together, the same criteria, unchanged to the word, recover a third of the loss; shorter answers recover almost none. We therefore propose Protocol-level Rubrics (ProRubric), which keeps what the criteria ask for and changes how they are aggregated. It groups a checklist into a few protocol-level dimensions. A dimension counts only when all of its criteria hold and its failure clause does not fire. The grouping is done once, offline, and leaves the optimizer unchanged. ProRubric raises appropriateness by 10.8 points without losing coverage and has the best seven-benchmark average at both scales. Reward validity is set not only by what a rubric verifies, but by how it aggregates. Code is available at https://github.com/Estrellajer/ProRubric
