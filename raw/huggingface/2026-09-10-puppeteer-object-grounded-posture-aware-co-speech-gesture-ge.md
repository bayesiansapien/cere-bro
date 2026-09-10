---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.00369
url: https://huggingface.co/papers/2609.00369
arxiv_url: https://arxiv.org/abs/2609.00369
upvotes: 1
date: 2026-09-10
---

# Puppeteer: Object-Grounded Posture-Aware Co-Speech Gesture Generation

Generating co-speech gestures that are temporally coherent, semantically aligned with speech, and grounded with surrounding objects remains challenging. Prior speech-driven gesture models emphasize audio-gesture alignment but do not explicitly account for posture constraints or surrounding objects, failing to capture the inherent correlation between body gestures and the physical space. We present Puppeteer, a posture-aware, object-grounded co-speech gesture diffusion model operating in a causal latent space. We decompose long gestures into structured primitives and learn a causal variational autoencoder that encodes them into temporally ordered latent tokens, each depending only on the past. We then perform conditional diffusion directly in the causal latent space, conditioning on speech signals, motion history, an initial posture reference, and object geometry to synthesize physically consistent gestures. This temporally ordered latent formulation enables explicit temporal control and supports tasks such as gesture in-betweening and gesture completion. To better assess co-speech gesture synthesis beyond existing measures, we introduce new evaluation metrics tailored to this task. We also created SceneGes, the first curated synthetic 3D dataset of embodied co-speech gestures and corresponding 3D objects, enabling object-grounded gesture generation. Experiments show that Puppeteer generates more diverse and temporally synchronized gestures than prior methods, while enabling object-grounded gesture synthesis.
