---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38172
url: https://huggingface.co/papers/2609.38172
arxiv_url: https://arxiv.org/abs/2609.38172
date: 2026-09-30
---

# Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation

Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse training set. PRISM first generates hundreds of diverse "counterfactual" human-object interaction videos via video-to-video (V2V) generation from a few exemplar real videos. Our contact-anchored real-to-sim pipeline then reconstructs both human and object motions, retargeting this imperfect video data into physically plausible trajectories. The intra-class variability across these counterfactual videos lets us train a single policy that generalizes to unseen objects within each category. We demonstrate the full pipeline by deploying this policy on a real robot without any real-world fine-tuning. Using only onboard depth observations, our humanoid picks up, carries, and drops objects, including boxes, barrels, bins, and balls, across novel instances, sizes, and initial configurations.
