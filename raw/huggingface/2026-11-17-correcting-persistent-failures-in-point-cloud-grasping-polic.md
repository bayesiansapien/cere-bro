---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.112040+00:00
arxiv_id: 2611.18919
url: https://huggingface.co/papers/2611.18919
arxiv_url: https://arxiv.org/abs/2611.18919
date: 2026-11-17
---

# Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality

Robots in homes, warehouses and farms must pick up objects they have never seen, usually without a 3D model or a category label. A grasping policy that works directly on the point cloud from a depth sensor needs only the geometry the robot observes, so it applies to any new object. Offline grasp generators such as Contact-GraspNet work this way, but they rank grasps by learned plausibility rather than by whether the grasp actually lifts the object. Reinforcement learning (RL) can optimize for that directly and make a point-cloud grasping policy much better on average, yet it leaves specific grasps persistently unsolved. We present a human-in-the-loop failure loop that targets those grasps: situations an RL policy keeps failing are mined automatically, sent to a virtual-reality application where a person picks the object up with their own hands, and returned to training as two grasp points. The person contributes only where to grasp; the robot chooses its own approach. In simulation, RL raises success on unseen objects from 55% with Contact-GraspNet to 83%. Adding 58 human demonstrations nearly doubles success on the hard cases RL kept failing, from 24% to 45%, and recovers performance that RL alone loses on similar cases that were never demonstrated, without reducing success on unseen objects.
