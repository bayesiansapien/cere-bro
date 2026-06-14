---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.13672
url: https://huggingface.co/papers/2606.13672
arxiv_url: https://arxiv.org/abs/2606.13672
date: 2026-06-14
---

# WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation

The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction. To unlock these downstream capabilities, a WM needs to jointly satisfy three desiderata: (i) fidelity (i.e., producing simulated trajectories that correlate with reality), (ii) consistency (i.e., producing simulated trajectories that are coherent over long horizons), and (iii) efficiency (i.e., producing simulated trajectories quickly). We propose WEAVER (World Estimation Across Views for Embodied Reasoning): a WM architecture that simultaneously achieves all three desiderata, providing state-of-the-art results on robotic manipulation tasks. WEAVER is a multi-view WM trained to predict future latents and reward values via a flow-matching loss. We distill the key design decisions across model architecture, memory, and prediction objectives required to unlock the kinds of long-horizon dynamic manipulation tasks that have confounded prior world modeling approaches. We apply WEAVER in robotic hardware, demonstrating its effectiveness at policy evaluation (ρ=0.870 correlation with real-world success rate), policy improvement (real-world success rate improvement of 38% on top of the π_{0.5} robot foundation model), and test-time planning (real-world success rate improvement of 14% with a 5-10times speedup over prior WMs). WEAVER also demonstrates better performance than prior WMs when evaluated on out-of-distribution scenarios. Code, models, and videos at: https://arnavkj1995.github.io/WEAVER/ .
