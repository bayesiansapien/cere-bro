---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.27180
url: https://huggingface.co/papers/2607.27180
arxiv_url: https://arxiv.org/abs/2607.27180
date: 2026-07-30
---

# HumanCLAW: Can Vision-Language Models Act Through a Body?

Evaluating whether a vision-language model (VLM) can act through a physical body is challenging. The outcome of an action couples the VLM's decision with motor control. When a task fails, it is hard to tell whether the VLM made a bad choice or the motor controller simply failed to execute it, e.g., losing balance and falling. In this work, we introduce HumanCLAW, an evaluation framework that decouples action decision-making from low-level execution. At every step, a harnessed, off-the-shelf VLM issues an atomic skill command, and the command is translated into a sub-second chunk of continuous full-body motion with real physical consequences, including gravity and collisions. The body can therefore act freely in the physical world, while execution-side disturbances, balance and motor errors, are factored out. What remains measurable is the model's action intelligence: its moment-to-moment choice of what the body should execute next. Based on this framework, we build HumanCLAW-Bench: 1,218 long-horizon, egocentric find-navigate-interact episodes across 41 indoor scenes. We test nine state-of-the-art VLMs and find that none solves the benchmark; the best model reaches only a 16.8% success rate. Recognizing the target is not the bottleneck. What current VLMs lack is embodied self-awareness: they lose track of their own body, failing to tell where it is, whether it has reached the goal, or whether it has hit an obstacle.
