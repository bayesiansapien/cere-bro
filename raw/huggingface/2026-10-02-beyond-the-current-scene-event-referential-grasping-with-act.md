---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819090+00:00
arxiv_id: 2609.39375
url: https://huggingface.co/papers/2609.39375
arxiv_url: https://arxiv.org/abs/2609.39375
date: 2026-10-02
---

# Beyond the Current Scene: Event-Referential Grasping with Active View Selection

A robot that observes people interacting with objects should be able to carry out later requests that refer back to those interactions. Such requests may specify a grasp target by the role it played in a past event rather than by its name or appearance. Moreover, the target may no longer be visible when the robot is asked to act. We present BeyondSCe, a zero-shot robotic grasping system for this event-referential setting. Given the event history and the current scene, the system identifies the requested object or part and localizes it for grasping. If the target is occluded, it combines an event prior recovered from the history with current scene geometry to select camera viewpoints likely to reveal the target. The system uses pretrained models without additional task-specific training. In real-robot experiments with a single wrist-mounted RGB-D camera, it achieves grasp success rates of 76% and 77% for initially visible and occluded targets, respectively, compared with 40% and 55% for the strongest baseline in each condition. On four additional scenes with heavy occlusion, it increases grasp success rates from 75% to 95% while reducing the mean number of views from 3.35 to 2.20, compared with an active-perception baseline given the target's ground-truth 3D bounding box.
