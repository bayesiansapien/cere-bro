---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.17117
url: https://huggingface.co/papers/2610.17117
arxiv_url: https://arxiv.org/abs/2610.17117
date: 2026-10-27
---

# Gluing Local Contexts into Global Meaning: A Sheaf-Theoretic Decomposition of Transformer Representations

Existing interpretability tools do not test whether a representation keeps the same content when only the phrasing changes. We treat each paraphrase pair as a local witness that two activations should agree and build a cellular sheaf over the paraphrase graph; its Laplacian L_F answers the question on a frozen model with no training. The kernel H^0 is a content subspace: at 20 dimensions it beats the preserved subspace of the concept eraser LEACE on held-out CounterFact fact retrieval across eight architectures by a mean +17.1\,pp, and constraining all paraphrases of a fact jointly adds a further +6.5\,pp. The spectral complement concentrates causal influence: ablating the most paraphrase-variable coordinates, a coordinate-wise proxy for it, changes model outputs 5.6 to 26.5times more than ablating coordinates of matched per-coordinate variability, across nine models from 124M to 13B parameters. Stacking layers into a grid creates b_1 = N(L-1) algebraic 1-cycles, and the resulting model-derived harmonic mass varies by nearly three orders of magnitude across six architectures and ranks them as their steering fragility does (Spearman ρ= 0.90, exact one-sided permutation p = 0.014). The same paraphrase graph yields the content subspace, the influence directions, and the fragility measure. Project page: https://cwru-aism.github.io/gluing-lc-page/
