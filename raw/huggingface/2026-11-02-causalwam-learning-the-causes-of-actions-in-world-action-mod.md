---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.501777+05:30
arxiv_id: 2610.42096
url: https://huggingface.co/papers/2610.42096
arxiv_url: https://arxiv.org/abs/2610.42096
date: 2026-11-02
---

# CausalWAM: Learning the Causes of Actions in World Action Models

World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant latent variables), as the model could just as well learn to imitate in this way whilst entangling the action-relevant latent variables with the nuisance variables. We therefore separate out what causes action from what prediction depends on. We prove that under a sparsity constraint the latent variables used to generate actions are an invertible function of the action-relevant latent variables alone and the true structure is identified up to a permutation of the latent variables. This requires neither sufficient temporal dependence nor any assumptions on how the unobserved regimes evolve and holds even when the action-relevant latent variables are statistically dependent on the rest. We therefore propose CWAM (Causal WAM), which incorporates the constraint into a pretrained WAM by adding a sparse routing path to its action head, with the world modeling objective remaining unchanged. Experiments on both synthetic data and real-world robots validate the theory as well as showcase the improved efficiency in closed-loop success.
