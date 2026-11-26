---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.25946
url: https://huggingface.co/papers/2611.25946
arxiv_url: https://arxiv.org/abs/2611.25946
date: 2026-11-25
---

# Point Dynamics as Proxy for Robotic World Models

Robotic world models predict future video frames from the current observation and a sequence of robot actions. While recent models follow the given actions closely, manipulated objects often collapse or move inconsistently with the action. We attribute this to the conditioning: an action, or a rendering of the robot, specifies where the robot goes but not how the scene responds, leaving a single video model to infer the interaction dynamics implicitly while also rendering appearance. We therefore separate dynamics prediction from visual rendering, with 3D point dynamics as the proxy between them. Specifically, we lift the first frame into 3D points, simulate how they respond to the robot's motion with a learned point dynamics model, and render the simulated points back into pixel-aligned videos that any video model can read. In controlled experiments on the DROID dataset with two video renderers of different architectures, this point dynamics proxy reduces object motion error by 8.6% and 6.2% without degrading image quality, and by 8.1% on a real bimanual robot. Moreover, the video follows the simulation: more accurate dynamics yield more accurate object motion, and editing the points steers the video. This suggests that advances in dynamics modeling can translate into more faithful robotic world models.
