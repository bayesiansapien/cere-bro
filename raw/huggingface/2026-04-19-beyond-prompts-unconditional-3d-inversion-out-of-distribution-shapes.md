---
source: farmer/huggingface
farmed: 2026-04-19T00:00:00Z
arxiv_id: 2604.14914
url: https://huggingface.co/papers/2604.14914
arxiv_url: https://arxiv.org/abs/2604.14914
date: 2026-04-19
---

# Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes

Text-driven inversion of generative models is a core paradigm for manipulating 2D or 3D content, unlocking numerous applications such as text-based editing, style transfer, or inverse problems. However, it relies on the assumption that generative models remain sensitive to natural language prompts. We demonstrate that for state-of-the-art native text-to-3D generative models, this assumption often collapses. We identify a critical failure mode where generation trajectories are drawn into latent "sink traps": regions where the model becomes insensitive to prompt modifications. In these regimes, changes to the input text fail to alter internal representations in a way that alters the output geometry. Crucially, we observe that this is not a limitation of the model's geometric expressivity; the same generative models possess the ability to produce a vast diversity of shapes but, as we demonstrate, become insensitive to out-of-distribution text guidance. We investigate this behavior by analyzing the sampling trajectories of the generative model, and find that complex geometries can still be represented and produced by leveraging the model's unconditional generative prior. This leads to a more robust framework for text-based 3D shape editing that bypasses latent sinks by decoupling a model's geometric representation power from its linguistic sensitivity.
