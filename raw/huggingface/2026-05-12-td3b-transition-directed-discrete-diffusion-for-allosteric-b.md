---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09810
url: https://huggingface.co/papers/2605.09810
arxiv_url: https://arxiv.org/abs/2605.09810
date: 2026-05-12
---

# TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation

Protein function is often controlled by ligands that bias the direction of state transitions, such as agonists and antagonists, rather than stabilizing a single conformation. This is especially important for clinically relevant G protein-coupled receptors (GPCRs), where therapeutic efficacy depends on functional directionality. Structure-based design methods optimize binding to static conformations and cannot represent non-reversible, directional effects or systematically distinguish agonist from antagonist behavior. To address this gap, we introduce Transition-Directed Discrete Diffusion for Allosteric Binder Design (TD3B), a sequence-based generative framework that designs binders with specified agonist or antagonist behavior via a directional transition control objective. TD3B combines a target-aware Direction Oracle, a soft binding-affinity gate, and amortized fine-tuning of a pre-trained discrete diffusion model, enabling targeted agonist and antagonist generation decoupled from binding affinity and unattainable by equilibrium-based or inference-only guidance baselines.
