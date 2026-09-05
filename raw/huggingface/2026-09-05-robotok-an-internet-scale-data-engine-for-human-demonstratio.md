---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2609.03199
url: https://huggingface.co/papers/2609.03199
arxiv_url: https://arxiv.org/abs/2609.03199
date: 2026-09-05
---

# RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning

Robot learning increasingly depends on broad and diverse demonstrations, yet collecting robot data remains expensive and poorly suited to covering the long tail of real-world tasks. To address this bottleneck, we introduce RoboTok, an internet-scale data engine that, given a query human manipulation video, retrieves manipulation-relevant human demonstrations from web videos for training dexterous robot policies. Specifically, we learn a latent motion space from 3D hand trajectories expressed in estimated actor-centered reference frames. This representation enables manipulation behaviors to be compared across variations in camera viewpoint, scene appearance, and actor occlusions, while remaining compact enough for efficient search and continual indexing over internet-scale video collections. We evaluate RoboTok against existing robot-data retrieval approaches on retrieval benchmarks and downstream robot policy performance. Our results show that RoboTok retrieves more relevant manipulation demonstrations and improves downstream task success, establishing hand-pose trajectory-aware retrieval as a way to make web video a scalable and continuously growing source of supervision for robot learning.
