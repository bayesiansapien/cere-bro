---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22127
url: https://huggingface.co/papers/2610.22127
arxiv_url: https://arxiv.org/abs/2610.22127
date: 2026-10-16
---

# Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization

Personalization of Large Language Models (LLMs) is increasingly important for user-centric applications, yet prior methods mainly adapt dense LLMs, whose polysemantic neurons, each encoding multiple unrelated concepts, hinder localizing the components behind personalization, and thus understanding and controlling it. We propose to personalize Mixture-of-Experts (MoE) LLMs, which sparsely route each token to a few specialized experts, reducing polysemanticity and enabling such localization. We adapt three open-weight MoE LLMs on a large-scale personalization dataset and train crosscoders on paired activations of the personalized and non-personalized models to learn interpretable personalized latents, from which we identify the experts encoding distinct personalization features. The personalized MoE LLMs perform competitively with dense LLMs while activating only a fraction of their parameters, exhibit lower polysemanticity than dense LLMs with similar active parameters, and, within the same model family, yield personalized latents that are less shared with the non-personalized model. Causal interventions show that these latents suffice to recover the personalized model's behavior and that boosting their associated experts moves the non-personalized model toward it, revealing distinct routing paths for different personalization features.
