---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11548
url: https://huggingface.co/papers/2609.11548
arxiv_url: https://arxiv.org/abs/2609.11548
date: 2026-09-11
---

# World in World: Explore the World with World Models

Autoregressive video world models enable interactive, long-horizon exploration, but flexible control remains challenging. Exploring a source video from new viewpoints requires the generated rollout to remain synchronised with the recorded event, place observed content in the requested view, plausibly complete newly exposed regions, and recover previously generated appearance on revisits. Existing methods typically address these requirements through task-specific modules or additional training. We present World in World, a training-free inference-time interface that converts heterogeneous control evidence into camera- and time-labelled clean visual states, which are read through the native self attention of a frozen causal video model. The evidence comprises source-video observations, target-view scene projections, geometry renderings that guide completion of newly exposed subject regions, and retrieved generated states beyond the rolling cache. Each evidence source carries token-level support and its own availability schedule. A correspondence router combines persistent point identities with geometry to establish token correspondences, guiding supported queries towards matching source-video tokens. Evidence-wise attention CFG (EWA) then independently regulates each auxiliary channel's additional contribution using attention responses from the same denoising forward pass. The shared interface supports camera-controlled rerendering, long-horizon revisiting, and human-motion transfer with the same frozen backbone. We evaluate World in World on camera-controlled video rerendering under diverse viewpoint changes, assessing perceptual quality, temporal consistency, and camera-following accuracy.
