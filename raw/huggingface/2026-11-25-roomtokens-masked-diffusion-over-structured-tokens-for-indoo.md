---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30219
url: https://huggingface.co/papers/2611.30219
arxiv_url: https://arxiv.org/abs/2611.30219
date: 2026-11-25
---

# RoomTokens: Masked Diffusion over Structured Tokens for Indoor Scene Synthesis

Generating 3D indoor scenes requires a representation that captures object semantics, instance identity, height structure, and orientation while respecting room geometry. Methods that model scenes as sequences of object vectors learn spatial constraints implicitly, leaving collisions and boundary violations to losses or post-processing; semantic-map methods make occupancy explicit, but collapse instance and directional structure. We introduce RoomTokens, a sliced structured-token representation in which each token stores semantic class, instance-color identity, and facing field. This representation allows a scene to be generated as a discrete grid while preserving cues for instance grouping, orientation estimation, and 3D extent prediction. To learn the RoomToken distribution, we propose MDIRT (Masked Diffusion over RoomTokens), a masked discrete diffusion model that denoises semantic/instance-color/facing channels jointly with a shared cross-slice backbone. Architectural tokens are clamped as explicit floor- plan constraints, so the model samples furniture layouts that respect room geometry while retaining instance and object-attribute structure. Experiments on 3D-FRONT show that RoomTokens with MDIRT improve layout fidelity and physical consistency over sequence/vector- and map-based methods, suggesting structured spatial tokens as a practical choice for discrete 3D scene synthesis.
