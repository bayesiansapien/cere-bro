---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.09155
url: https://huggingface.co/papers/2609.09155
arxiv_url: https://arxiv.org/abs/2609.09155
upvotes: 5
date: 2026-09-10
---

# SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.
