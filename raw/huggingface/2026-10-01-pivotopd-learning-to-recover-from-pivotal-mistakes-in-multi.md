---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348559+05:30
arxiv_id: 2609.40285
url: https://huggingface.co/papers/2609.40285
arxiv_url: https://arxiv.org/abs/2609.40285
date: 2026-10-01
---

# PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents

On-policy distillation (OPD) is a promising approach for training language agents, providing dense teacher supervision on student-generated trajectories. However, in multi-turn interaction, an incorrect action changes the states the student encounters later, so errors compound across turns. In preliminary experiments across three Qwen3 models (8B to 235B), we find that more than half of the failed rollouts contain a pivotal mistake, an action that moves the agent farther from completing the task, and this mistake typically occurs early. These pivotal mistakes often remain recoverable: guiding the model for only a few turns after the pivotal turn can restore task success. We therefore propose PivotOPD, an on-policy distillation framework that jointly trains the student to prevent pivotal mistakes and to recover from the states they create. At each pivotal mistake, a teacher model provides a gold action and then names a recovery action at each of the next few turns. Preventive distillation uses the gold action with reverse KL to steer the student away from the pivotal mistake, while recovery distillation uses the recovery actions with forward KL to transfer recovery behaviors that the student rarely samples. Against 13 baselines on ALFWorld, WebShop, and Search-based QA, PivotOPD achieves the strongest average performance for both Qwen3-1.7B and Qwen3-8B students, improving over the strongest baseline on ALFWorld by +5.5% with the 1.7B student. The gains also transfer to another model family on the software engineering domain, where PivotOPD raises the resolve rate of a Nemotron-3.5 student on SWE-Bench Verified by +3.2%. Project page: https://research.nvidia.com/labs/lpr/pivotopd/
