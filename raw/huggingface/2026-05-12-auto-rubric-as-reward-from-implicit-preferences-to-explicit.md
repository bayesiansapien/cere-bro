---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.08354
url: https://huggingface.co/papers/2605.08354
arxiv_url: https://arxiv.org/abs/2605.08354
date: 2026-05-12
---

# Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria

Aligning multimodal generative models with human preferences demands reward signals that respect the compositional, multi-dimensional structure of human judgment. Prevailing RLHF approaches reduce this structure to scalar or pairwise labels, collapsing nuanced preferences into opaque parametric proxies and exposing vulnerabilities to reward hacking. While recent Rubrics-as-Reward (RaR) methods attempt to recover this structure through explicit criteria, generating rubrics that are simultaneously reliable, scalable, and data-efficient remains an open problem. We introduce Auto-Rubric as Reward (ARR), a framework that reframes reward modeling from implicit weight optimization to explicit, criteria-based decomposition. Before any pairwise comparison, ARR externalizes a VLM's internalized preference knowledge as prompt-specific rubrics, translating holistic intent into independently verifiable quality dimensions. This conversion of implicit preference structure into inspectable, interpretable constraints substantially suppresses evaluation biases including positional bias, enabling both zero-shot deployment and few-shot conditioning on minimal supervision. To extend these gains into generative training, we propose Rubric Policy Optimization (RPO), which distills ARR's structured multi-dimensional evaluation into a robust binary reward, replacing opaque scalar regression with rubric-conditioned preference decisions that stabilize policy gradients. On text-to-image generation and image editing benchmarks, ARR-RPO outperforms pairwise reward models and VLM judges, demonstrating that explicitly externalizing implicit preference knowledge into structured rubrics achieves more reliable, data-efficient multimodal alignment, revealing that the bottleneck is the absence of a factorized interface, not a deficit of knowledge.
