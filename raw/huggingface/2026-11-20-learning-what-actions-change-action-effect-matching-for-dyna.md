---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.385443+00:00
arxiv_id: 2611.25980
url: https://huggingface.co/papers/2611.25980
arxiv_url: https://arxiv.org/abs/2611.25980
date: 2026-11-20
---

# Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. Yet despite producing increasingly realistic videos, current world models often fail to capture how small action changes affect future observations. This limits their use in tasks such as robotic policy evaluation and model-based planning, where nearly identical actions can lead to qualitatively different outcomes. To address this, we propose AFFECT, an auxiliary training objective for learning the distribution of visual changes induced by action perturbations. Specifically, we inject temporally correlated noise into the actions of a policy trained on task-agnostic human teleoperation. We then train the world model so that its generated videos respond to this noise as the recorded videos do, without requiring repeated executions from the same initial state. Across OGBench simulation and real-world DROID and ALOHA-2 setups, AFFECT makes world-model rollouts more faithful to real outcomes. On DROID, the Pearson correlation between policy success rates in the world model and on the real robot rises from 0.47 to 0.79, alongside up to 23% lower FVD. These gains carry over to planning, where selecting actions with AFFECT-trained world models improves task success by up to 8.3%.
