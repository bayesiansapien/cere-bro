---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.910884+00:00
arxiv_id: 2611.32786
url: https://huggingface.co/papers/2611.32786
arxiv_url: https://arxiv.org/abs/2611.32786
date: 2026-11-26
---

# Simulator-as-Proxy World Model for Robot Manipulation

Video world models for robots are increasingly conditioned on a simulated or rendered proxy of the scene, on the assumption that the video will show what the proxy shows. Testing this assumption requires a proxy whose state is explicit and can be perturbed. We present SimPWM (Simulator-as-Proxy World Model): given a calibrated camera, it represents, from the first frame alone, the robot by its 3D model and the objects the gripper may touch as 3D points; a rule-based simulator with no trained parameters moves them under the actions, and a video model renders the result. SimPWM returns the realistic video together with the simulated state. We then freeze the simulated objects while the arm moves as recorded and check whether the video still shows the object lifted. On DROID episodes from unseen setups, the answer differs for the arm and for the objects. With each of three base video models, the arm follows the proxy (robot IoU 0.75-0.78, against at most 0.69 for end-to-end models); rendering the robot alone already gives this. What the simulated objects add is the object state: against a robot-only proxy, they cut missed pick-ups from 54% to 38%, and the video follows them only with some base models: on rigid objects, freezing them lowers the lift rate of MiniMax-H3, fine-tuned on episodes whose simulation agrees with the real video, from 42% to 10%, but that of LTX-2.3, trained on the same episodes, only from 57% to 49%, as if it inferred the grasp from the arm motion; more than half of the remaining lifts of MiniMax-H3 are of cloth and rope, which the simulator carries rigidly. With any base model, the simulated state records what the simulation did; under perturbed actions, a video that disagrees with it reveals that the video ignores the simulated state.
