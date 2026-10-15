---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.501991+00:00
arxiv_id: 2610.12818
url: https://huggingface.co/papers/2610.12818
arxiv_url: https://arxiv.org/abs/2610.12818
date: 2026-10-14
---

# LeWAM: End-to-End World and Action Modeling with JEPAs

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and action-conditioned dynamics before adding a control policy or solver. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic Gaussian constraint on the latent state, enabling a single model to support direct policy execution and efficient planning by evaluating sampled actions with its learned latent dynamics. Compared with prior JEPAs in visual planning, LeWAM improves success rate from 28.6% to 89.7% on contact-rich tasks and from 10.9% to 46.2% on long-horizon tasks, and plans 32.3 times faster. On behavior cloning tasks in simulation and physical robots, LeWAM is also competitive with established methods. Interpretability analyses show that LeWAM learns control-relevant representations and action distributions effectively guiding test-time planning and control.
