---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935850+00:00
arxiv_id: 2609.30247
url: https://huggingface.co/papers/2609.30247
arxiv_url: https://arxiv.org/abs/2609.30247
date: 2026-09-29
---

# Rolling-WAM: World Action Models with Rolling Imagination

World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a rolling noise schedule fully denoises the imminent action chunk for execution, while partially refining farther-future chunks. As the window advances with new camera observations, the retained future chunks continue their denoising process. This distributes the computational cost over time while carrying an evolving visual-action context across chunk boundaries. Evaluations on LIBERO, RoboTwin, and a real-world Unitree G1 humanoid show that Rolling-WAM achieves competitive manipulation performance. By removing the need to denoise the entire prediction horizon from scratch, it delivers a 4.5x steady-state replanning speedup over standard joint WAMs.
