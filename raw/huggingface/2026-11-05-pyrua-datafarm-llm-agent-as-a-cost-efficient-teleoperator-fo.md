---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.299706+00:00
arxiv_id: 2611.05320
url: https://huggingface.co/papers/2611.05320
arxiv_url: https://arxiv.org/abs/2611.05320
date: 2026-11-05
---

# PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data

Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration episode of the robot in the target scene and rebuilds the task in simulation: it writes the scene, an expert controller, and a success judge. The simulator supplies exact actions, and a video model conditioned on real images renders each rollout as photographic video, generating all camera views together consistently. The output is real-ready data: synchronized camera views labelled with the robot's actions, on which a policy can be trained directly and deployed on the real robot. Independent judges certify the expert and every rendered episode before admission. On five real-robot tasks, policies trained only on farm data match policies trained on as many teleoperated episodes (93 vs. 84 successes in 100 trials), and under an unseen tablecloth and coloured light they keep 87 successes where the teleoperation-trained policies fall to 46. Adapting a task is fully automatic and costs \21 of API usage on average, paid once per task, plus 5 for a render contract; every further episode costs \0.80 on average for simulation, rendering, and review, with no robot or operator. One hour of three-view data for a task costs 107 on average, these costs included, slightly below a quote of \117 for teleoperation in China and below 290 in labour alone in North America.
