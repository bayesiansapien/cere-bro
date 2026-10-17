---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21261
url: https://huggingface.co/papers/2610.21261
arxiv_url: https://arxiv.org/abs/2610.21261
date: 2026-10-16
---

# Behavioral Compositionality of Sparse Autoencoder Representations

Sparse autoencoders (SAEs) represent model activations with sparse, linearly decoded features, but the downstream effects of those features need not compose additively. We introduce SAE Additivity Residuals (SAR), which measure the behavioral variation left unexplained above a chosen interaction order. Under independent feature subset sampling, population SAR is exactly the normalized energy of interactions above that order and bounds coalition ordering error for the optimal low order approximation. To distinguish compositionality associated with the SAE representation from that induced by downstream computation, we compare learned SAE coordinates with sum preserving random rotations of the same selected subspace and find lower first order residuals for the learned coordinates across all 18 model and behavior settings. The coordinates are nevertheless not fully additive: pairwise terms improve held out coalition ordering in every setting and outperform parameter matched models using randomly selected third order terms. In a combined steering experiment, pairwise modeling raises rank fidelity from 0.5874 to 0.7790 and reduces ordering error from 0.1444 to 0.0606. Together, these results show that SAE coordinates support comparatively compositional behavioral descriptions while faithful joint explanations and interventions still require interactions beyond individual feature effects. Code is available at https://github.com/OpenSAE/SAE-Behavioral-Compositionality.
