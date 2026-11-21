---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.389542+00:00
arxiv_id: 2611.26239
url: https://huggingface.co/papers/2611.26239
arxiv_url: https://arxiv.org/abs/2611.26239
date: 2026-11-20
---

# Teaching Vision-Language-Action Models to Stop Safely

Vision-language-action (VLA) models enable robots to perform diverse tasks from visual observations and language instructions. While prior work has explored task suppression and refusal, stopping prohibited behavior once execution is underway and controlling the resulting physical response remain challenging. Our evaluation reveals that policies which suppress a task from its initial state can still complete it when taking over partway through execution. Even when the task remains unfinished, the robot may drop a held object, making non-completion an incomplete measure of safety. To address these challenges, we introduce State-Aware Fallback Imitation (SAFI) for tasks where holding provides an appropriate alternative response. SAFI comprises two stages, (1) fallback target construction, which assigns stationary arm commands and consistent gripper targets throughout prohibited-task demonstrations, and (2) joint policy adaptation, which learns these targets alongside the original actions of retained tasks. This supervision teaches an explicit alternative response at intermediate execution states while maintaining the robot's other skills. Extensive experiments with OpenVLA-OFT across LIBERO and BadLIBERO tasks evaluate prohibited completion, physical incidents, and retained-task performance. On the evaluated LIBERO tasks, SAFI reduces aggregate target success after takeover to 1.3\%, with no recorded physical incidents or action saturation, while preserving high retained-task success.
