---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.23863
url: https://huggingface.co/papers/2609.23863
arxiv_url: https://arxiv.org/abs/2609.23863
date: 2026-09-22
---

# Grounded Action Model: 3D Grounding as a Foundation for Robotics

Manipulation policies must know which objects matter and where they are, yet the pretrained backbones that current robot foundation models build on, from language in vision-language-action models (VLAs) to video generation in world-action models (WAMs), do not directly require this metric grounding, leaving it to be learned implicitly from robot demonstrations. We propose Grounded Action Models (GAMs), a new paradigm of robot foundation models built with 3D grounding. GAM can be conditioned using language, points, or box prompts, which are first transformed into a shared object-centric representation of the selected objects. This representation captures target-focused visual features and metric object geometry, which is mixed with robot state history through a multi-stream transformer to predict action chunks. Although GAMs can be run autonomously, they can also serve as a low-level controller that a high-level planner controls using its various input modalities, allowing for long-horizon and memory-dependent manipulation. On RoboTwin 2.0, GAM achieves an average success rate of 55.3% across 50 tasks (vs. 52.0% for Spatial Forcing), including 47.6% under scene randomization (vs. 30.4% for Abot-M0), with its action policy trained only on clean-scene demonstrations. On LIBERO-PRO, it achieves a state-of-the-art average success rate of 61% (vs. 53% for π_{0.5}) across 16 perturbation settings, with the largest gains when targets are relocated or newly designated. On two real robots, GAM retains 17/20 successes under visual shift on a bimanual YAM versus 4/20 for π_{0.5}, while its composition with a Molmo2 planner on a Franka achieves 64.7% ID and 49.8% OOD step completion on long-horizon and memory-dependent tasks.
