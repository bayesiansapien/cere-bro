---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.147099+00:00
arxiv_id: 2611.24681
url: https://huggingface.co/papers/2611.24681
arxiv_url: https://arxiv.org/abs/2611.24681
date: 2026-11-19
---

# DrawScore: Evaluating Generated CAD Models against Engineering Drawings

Automatic CAD generation is commonly evaluated with volumetric IoU, Chamfer Distance, and surface F-score, which barely penalize local errors that occupy only a small fraction of a part's volume or surface area, such as a misplaced hole or a slot on the wrong face, even though such errors are critical to manufacturing. We formalize these metrics in a unified integral form and show that the weight of a local error decays as the (k+q)-th power of its size, where k is the dimension of the integration domain and q is determined by the penalty function. Guided by this analysis, we propose DrawScore, which projects both models into three orthographic views with visible and hidden lines, as in engineering drawings, and applies a saturating penalty along the projected curves, so that the weight of a local error decays only linearly. Controlled experiments confirm the predicted decay orders, and on outputs of existing CAD generation agents, DrawScore exposes errors in outputs that IoU rates as nearly perfect. DrawScore further improves generation as a reinforcement learning reward and, for CAD generation from engineering drawings, serves as a test-time verifier without 3D ground truth or an additional reward model. Our code is available at https://github.com/UESTC-Simon/DrawScore.
