---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.929725+00:00
arxiv_id: 2611.23946
url: https://huggingface.co/papers/2611.23946
arxiv_url: https://arxiv.org/abs/2611.23946
date: 2026-11-24
---

# How Complete Must an Environment Be to Train a Capable GUI Agent?

Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three dimensions: reward coverage, the goal-reaching trajectories the verifier rewards; data coverage, the application data the agent is exposed to beyond what the task reads or writes; and feature coverage, the application features beyond what the task uses. Existing works set each dimension on engineering grounds, but they do not measure its effect on training. How complete must an environment be to train a capable agent, and along which dimensions? In MobileGym, we adjust each dimension separately, train Qwen3-VL-4B-Instruct, and evaluate every policy in the original full environment. A verifier that rewards only one reference path lowers success by 10.53 points, and removing unneeded records also lowers success. Pruning unneeded features instead raises success from 51.61% to 56.13%, entirely on tasks whose environments it left unchanged. The gain reverses when each episode is weighted equally and vanishes when only episodes on the pruned tasks are balanced. Without pruning, length weighting there reinforces long detour successes that erode skills on other tasks. Following these findings, we build MobileGym-Lite, which keeps reward and data coverage complete and prunes unneeded features. It outperforms Full in the full environment (55.48% versus 51.61% success) with lower construction cost.
