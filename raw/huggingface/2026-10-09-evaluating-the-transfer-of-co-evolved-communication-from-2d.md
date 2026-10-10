---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.420914+00:00
arxiv_id: 2610.09280
url: https://huggingface.co/papers/2610.09280
arxiv_url: https://arxiv.org/abs/2610.09280
date: 2026-10-09
---

# Evaluating the Transfer of Co-Evolved Communication from 2D to 3D Simulation

This work examines the transfer of a co-evolved communication mechanism between two robotic agents from a discrete two-dimensional (2D) simulator to a three-dimensional simulator with real physics (3D). The study focuses on whether a communication mechanism co-evolved in a 2D environment retains its functional role after transfer to a 3D physics-based simulator. To support this analysis, the effects of the episode time budget, the social cue, and the asymmetry between the two co-evolved roles were examined. The results indicate that the success rate increased approximately linearly with the evaluated time budgets, with no evidence of a plateau between 2,000 and 6,000 physics steps, suggesting that evaluations based on shorter episodes may underestimate the performance of the trained controllers. In both simulators, the social cue functioned primarily as a jam- assistance mechanism rather than as a navigation guide, although with a more pronounced effect in 2D. Analysis of eight independent evolutionary runs revealed a consistent direction of asymmetry, although its magnitude varied across runs. Controlling the processing order between agents allowed us to rule out an artifact of the physics engine. Finally, the results are discussed in terms of the factors that may contribute to the remaining performance gap observed after transfer.
