---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.911633+00:00
arxiv_id: 2611.34750
url: https://huggingface.co/papers/2611.34750
arxiv_url: https://arxiv.org/abs/2611.34750
date: 2026-11-26
---

# SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator

LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between them. The agent decides the number and spacing of keyposes for both fast long-range motion and fine-grained manipulation. This granularity matches the sparsity of teleoperated manipulation: most demonstrations in DROID can be compressed into a few keyposes instead of dense actions. SOLVE grounds keyposes with sparse depth queries answered by noisy sources, such as multi-view triangulation, stereo, or monocular depth, and copes with that noise itself. It also improves from execution feedback, reflecting on its own rollouts and distilling a few rules per task. SOLVE reaches state-of-the-art performance of 74.5% on RoboDojo and 84.5% on RoboLab, with only $1.7 per episode on average, 12x less than previous dense-control agent policies. On a real robot, the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks. Our project page is at https://serenos.github.io/solve-website.
