---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.21938
url: https://huggingface.co/papers/2611.21938
arxiv_url: https://arxiv.org/abs/2611.21938
date: 2026-11-18
---

# HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning

Robot policies trained by imitation generalize poorly outside the environments and objects seen in training. Published data-scaling studies find that generalization grows with the diversity of training environments and objects rather than with more demonstrations per environment. Robot data is costly to collect across many environments, whereas egocentric human video can be recorded in the wild at scale; existing egocentric video, however, mostly shows daily-life activity and contains little skilled work in real workplaces. We present HubEgo-100K, a dataset built for diversity. This version of the paper covers the first release, v1.0: 10,124 hours of 1080p egocentric video with synchronized 100 Hz inertial (IMU) data from one head-mounted phone camera. In v1.0, 12,227 contributors record their own unscripted work in 15,548 environments (each one contributor's own setting of one type, such as their kitchen or workshop) across 11 setting types, 30 work categories, 56 task types and 35 action families, with 83% of hours in workplace settings. The release comprises 72,754 episodes with machine-generated action and language annotations, in LeRobot and MCAP formats under CC BY 4.0. We measure diversity along each axis, show that inside v1.0, with episodes in random order, new contributors and words keep appearing, and relate the measurements to published evidence on six data properties tied to policy performance, including hand visibility and inertial sensing. We also document collection, curation, privacy measures and data format, and provide a datasheet. Later versions of this paper will add benchmarks and cover further releases toward 100,000 hours.
