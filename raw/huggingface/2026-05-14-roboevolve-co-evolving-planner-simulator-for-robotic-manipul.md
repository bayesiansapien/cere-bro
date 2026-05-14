---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13775
url: https://huggingface.co/papers/2605.13775
arxiv_url: https://arxiv.org/abs/2605.13775
date: 2026-05-14
---

# RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

The scalability of robotic manipulation is fundamentally bottlenecked by the scarcity of task-aligned physical interaction data. While vision-language models (VLMs) and video generation models (VGMs) hold promise for autonomous data synthesis, they suffer from semantic-spatial misalignment and physical hallucinations, respectively. To bridge this gap, we introduce RoboEvolve, a novel framework that couples a VLM planner and a VGM simulator into a mutually reinforcing co-evolutionary loop. Operating purely on unlabeled seed images, RoboEvolve leverages a cognitive-inspired dual-phase mechanism: (i) daytime exploration fosters physically grounded behavioral discovery through a semantic-controlled multi-granular reward, and (ii) nighttime consolidation mines near-miss failures to stabilize policy optimization. Guided by an autonomous progressive curriculum, the system naturally scales from simple atomic actions to complex tasks. Extensive experiments demonstrate that RoboEvolve (I) achieves superior effectiveness, elevating base planners by 30 absolute points and amplifying simulator success by 48% on average; (II) exhibits extreme data efficiency, surpassing fully supervised baselines with merely 500 unlabeled seeds, a 50x reduction; and (III) demonstrates robust continual learning without catastrophic forgetting.
