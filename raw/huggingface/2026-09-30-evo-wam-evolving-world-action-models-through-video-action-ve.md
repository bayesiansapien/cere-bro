---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38057
url: https://huggingface.co/papers/2609.38057
arxiv_url: https://arxiv.org/abs/2609.38057
date: 2026-09-30
---

# EVO-WAM: Evolving World Action Models through Video-Action Verification

Improving robot policies on new tasks without collecting additional expert demonstrations remains a central challenge in robot learning. World action models (WAMs) use broad video priors to jointly predict future videos and actions, offering a potential source of supervision for adapting to new tasks. However, generated videos may fail to depict task completion, and even visually successful videos may be paired with inconsistent actions that lead to execution failure. We propose EVO-WAM, a framework that adapts WAMs to unseen tasks by learning from their own generated video-action trajectories, without executing candidate actions in an external environment. First, we augment WAM training with state prediction and anchored multi-frame context to enable complete autoregressive rollouts without external execution feedback. Second, we identify reliable training experience by selecting task-completing prefixes with a vision-language model and verifying their video-action consistency with an inverse dynamics model. Third, we iteratively train the WAM on verified prefixes and generate new rollouts with the updated model. On seven unseen RoboTwin 2.0 tasks, EVO-WAM increases average success rates from 26.9% to 68.0% for Cosmos3 and from 28.5% to 46.4% for DreamZero, reaching approximately 2.5times and 1.6times their initial success rates. On three unseen long-horizon composite tasks in the real world, it improves Cosmos3's average success rate from 20.0% to 76.7%, a gain of 56.7 percentage points. Project Page: https://evo-wam.github.io/.
