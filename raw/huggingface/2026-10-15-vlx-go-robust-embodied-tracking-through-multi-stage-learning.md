---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234547+05:30
arxiv_id: 2610.19361
url: https://huggingface.co/papers/2610.19361
arxiv_url: https://arxiv.org/abs/2610.19361
date: 2026-10-15
---

# VLX-Go: Robust Embodied Tracking through Multi-Stage Learning and On-Policy Refinement

Embodied visual tracking requires a robot to identify a designated target from visual observations and control its own motion to follow that target through an environment. Following an isolated person is a comparatively simple demonstration of embodied visual tracking, but following the intended person among distractors remains challenging. Existing methods exhibit a substantial drop in success from single-target to distractor tracking, motivating a focus on the shared spaces that person-following robots must navigate. We present , a vision--language waypoint policy built around the hypothesis that visual and language representations should be aligned before tracking-specific motion is learned. The policy combines complementary frozen visual encoders, multiscale temporal context, a transformer backbone, and a lightweight head for robot-centric waypoint prediction. Its training progresses through vision--language alignment, multimodal reasoning mid-training, and tracking specialization on 19,532 oracle episodes. Compared with 41.54\% distractor-tracking success for our earlier OmTrackVLA model, the complete multi-stage recipe achieves 55.80\%. We then explore on-policy refinement using filtered oracle labels for states visited by the policy. This preliminary study adds 2.42 percentage points of distractor-tracking success, reaching 58.22\%, while reducing collision rate by 1.99 pts. The final policy records the highest distractor- and ambiguous-tracking success rates among the compared methods. These results support staged multimodal learning as a promising direction for tracking among distractors and motivate further study of on-policy refinement for person following in shared spaces.
