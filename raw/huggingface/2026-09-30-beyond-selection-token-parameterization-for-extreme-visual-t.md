---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35232
url: https://huggingface.co/papers/2609.35232
arxiv_url: https://arxiv.org/abs/2609.35232
date: 2026-09-30
---

# Beyond Selection: Token Parameterization for Extreme Visual Token Compression

Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) from (ii) coordinate organization (optimization and cross-modal alignment). This view yields two coupled objectives, compressibility and learnability, which we formalize as unified functionals. Guided by these objectives, we design Braco, a lightweight four-step coder that combines transform-basis truncation, input-independent basis-coordinate embeddings, budget-dependent orthogonal re-parameterization, and learned spatial residual tokens from lightweight pooling. Experiments show that Braco forms the favorable empirical accuracy-efficiency frontier under 23times--64times compression and remains competitive at 144times, reaching 95.2% accuracy while reducing prefill FLOPs by 84.2%--86.7% relative to the uncompressed upper bound. Against prior methods, Braco matches or improves accuracy while achieving up to approximately 36% end-to-end speedup and using 16.6times/78.8times lower compressor latency/FLOPs.
