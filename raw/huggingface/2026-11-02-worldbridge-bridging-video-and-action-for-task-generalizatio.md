---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.497474+05:30
arxiv_id: 2610.40748
url: https://huggingface.co/papers/2610.40748
arxiv_url: https://arxiv.org/abs/2610.40748
date: 2026-11-02
---

# WorldBridge: Bridging Video and Action for Task Generalization in World Action Models

Achieving the broad task generalization of embodied models in physical environments remains a central challenge in robot learning. We study this challenge in World Action Models (WAMs) through two complementary capabilities: video generalization, which predicts the visual evolution of new tasks, and action generalization, which translates these predictions into executable behavior through a video-to-action bridge. By varying video and action supervision for tasks outside an initial training set, we examine their respective contributions to task transfer. On RoboTwin 2.0, using only in-distribution video-action supervision yields a 25.07% success rate on out-of-distribution tasks. Introducing videos of these tasks without their action labels raises success to 55.90%, while adding just one action-labeled demonstration per task further improves it to 70.70%. These findings suggest that broader video coverage enables task transfer by leveraging existing inverse-dynamics capabilities, while even sparse action supervision further strengthens those capabilities. Guided by this perspective, we introduce WorldBridge, a WAM with separate video and action experts connected through structured attention and trained with joint flow matching. WorldBridge incorporates visual memory at two temporal scales and action forcing, alongside a unified data processing pipeline that standardizes and filters heterogeneous robot trajectories and egocentric hand-derived supervision. Across multiple manipulation benchmarks, WorldBridge achieves state-of-the-art performance among the compared methods, including 96.23% on RoboTwin 2.0 full data setting and 80.9% on clean to random setting, 82.8% on RoboCasa GR1 TableTop, and 57.6% on DOMINO Level-1. Our study highlights the complementary roles of video prediction and action grounding in developing robots that generalize across tasks.
