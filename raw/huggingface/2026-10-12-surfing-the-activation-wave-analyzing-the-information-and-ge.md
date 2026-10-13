---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.220822+05:30
arxiv_id: 2610.12939
url: https://huggingface.co/papers/2610.12939
arxiv_url: https://arxiv.org/abs/2610.12939
date: 2026-10-12
---

# Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In this work, we present a principled framework for multi-layer hidden-state selection for speculative decoding based on two complementary criteria: informativeness, measured through matrix-entropy analysis, and diversity, quantified using centered kernel alignment (CKA). We investigate layer-wise Shannon entropy, aggregate entropy under hidden-state concatenation, and pairwise CKA dynamics across depth, revealing distinct geometric and informational compartments within decoder representations. Motivated by these findings, we propose entropy and CKA-based layer selection algorithms that favor hidden-state sets that are both highly informative and minimally redundant. As part of this framework, we introduce token-entropy filtering, which removes hidden states associated with low predictive-entropy tokens, thereby improving the quality of layer-selection statistics. In EAGLE3-style speculative decoding, our selected sets outperform fixed baseline choices, including the default [2, N//2, N-3] rule, while providing a clearer explanation of why some defaults can remain competitive. Our results provide a practical recipe for multi-layer hidden-state selection for speculative decoding, insights into the geometry and information in LLM decoder states, and a foundation for extending similar analysis to related applications.
