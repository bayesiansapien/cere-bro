---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.00730
url: https://huggingface.co/papers/2608.00730
arxiv_url: https://arxiv.org/abs/2608.00730
date: 2026-08-05
---

# Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains and Surfaces with Segmented Pushing Trajectories

Viscous stains, characterized by high viscosity and complex rheological properties, remain a major challenge for robotic surface cleaning. Conventional wiping often spreads the stain, while scrubbing provides stronger friction but risks damaging the surface. In this paper, we propose Push-Wiper, a framework that reformulates viscous stain cleaning as an aggregation problem. Push-Wiper employs a sponge to progressively gather stains through segmented pushing trajectories, followed by a post-processing phase that detaches the aggregated material and enables sponge self-cleaning. We adopt a stepwise strategy for stain gathering and leverage Diffusion Policy to generate adaptive pushing action sequences. These sequences are executed through our Arbitrary Surface Pose Interpolator (ASPI) and a hybrid force-position controller, allowing the method to generalize to stains with diverse spatial distributions. Push-Wiper achieves a cleaning score (CS), defined as the percentage of stain area removed, up to 130% higher than baseline methods. Without additional training, Push-Wiper also transfers in a zero-shot manner to solid residues, liquid spills, unseen viscous stains, and curved surfaces with varying geometries. Our experiments demonstrate the cleaning effectiveness of Push-Wiper and its strong generalization ability. The project website is available at https://push-wiper.github.io/.
