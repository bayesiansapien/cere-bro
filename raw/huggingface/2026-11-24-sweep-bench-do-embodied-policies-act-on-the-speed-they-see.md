---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.932581+00:00
arxiv_id: 2611.30637
url: https://huggingface.co/papers/2611.30637
arxiv_url: https://arxiv.org/abs/2611.30637
date: 2026-11-24
---

# SWEEP-Bench: Do Embodied Policies Act on the Speed They See?

Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds. We introduce SWEEP-Bench, a simulation benchmark with 80 conveyor-belt manipulation tasks spanning 16 skill categories, each evaluated at 13 belt speeds (0.10-0.40 m/s). Objects are transported through physical contact with a visibly moving belt. Each task has a static counterpart, and each evaluation episode uses the same randomized scene at all 13 speeds. We fine-tune eight vision-language-action and world-action models on demonstrations spanning the full speed range, comparing observations from the current frame alone with those including two past frames. For six models, the success rate peaks at intermediate speeds, and their failures indicate that they tend to produce actions suited to the average demonstration speed rather than to the actual one. Past frames raise the success rate by 10-40 percentage points for three models, and linear probes show that the belt speed is also most linearly decodable from these three. Adding ground-truth speed input to four of the models improves all of them, and a speed estimated from the images keeps most of this gain. These results show that SWEEP-Bench exposes speed-dependent failures and suggest that past frames help only policies from which the speed is most decodable, such as those pretrained on multiple frames. Project page: https://damin3927.github.io/SWEEP-Bench
