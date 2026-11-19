---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.19559
url: https://huggingface.co/papers/2611.19559
arxiv_url: https://arxiv.org/abs/2611.19559
date: 2026-11-18
---

# ResWAM: Learning What Changes, Not What Stays, for World-Action Models

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world. Existing WAMs supervise complete future observations. However, observations typically change little over an action chunk, so the future loss is dominated by copying static background content rather than learning task-relevant robot and object motion, limiting policy learning. Moreover, existing WAMs rely on large video generation models or separate world models, incurring heavy training and inference compute that hinders closed-loop deployment. To improve policy performance, we propose visual residual learning, supervising only the feature change from the current frame to the future frame in a frozen DINOv3 space. Compared with complete future features, this residual learning target yields a higher feature rank with richer and more diverse representations of scene changes, and spatially concentrates on the robot arm and manipulated objects rather than the background. To further improve computational efficiency, we present ResWAM, a residual world-action model with 2.3B parameters in total, including a lightweight 0.5B dual-branch DiT that jointly trains an action branch and a residual branch via conditional flow matching. Without robot pretraining (i.e., pretraining on external robot action trajectories beyond the benchmark demonstrations), ResWAM achieves top average success rates on LIBERO-Plus (81.1%), RoboTwin 2.0 (93.8%), and RoboDojo (9.40% success, 13.41 score) at the lowest training (2.7-4.0 TFLOPs) and inference compute (1.0-1.4 TFLOPs), and leads real-robot Open, Put, and Stack (80.0% average, +10.0% over π_{0.5}) at 92.7 ms latency.
