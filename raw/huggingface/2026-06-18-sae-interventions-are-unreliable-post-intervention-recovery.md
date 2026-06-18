---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.18322
url: https://huggingface.co/papers/2606.18322
arxiv_url: https://arxiv.org/abs/2606.18322
date: 2026-06-18
---

# SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior

Sparse Autoencoders (SAEs) decompose residual-stream activations into interpretable features. Recent latent-space defenses increasingly rely on these decompositions, assuming that identified "unsafe" SAE features serve as actionable handles for monitoring and intervention. In this paradigm, clamping a specific harmful feature is expected to reliably prevent model misbehavior. However, we show that this success may hide a recoverable failure mode: the clamp may block one visible route to a behavior without eliminating the behavior itself. We formulate this vulnerability as post-intervention recovery, a constrained residual-space optimization problem. Starting from the post-intervention residual state, we optimize residual perturbations to recover the pre-intervention behavior while preserving the post-intervention values of the targeted SAE features. Even under a strong threat model where the intervention remains active throughout optimization and generation, recovery remains possible. To rule out that recovery simply undoes the intervention, we use encoder-orthogonal updates for single-layer interventions and the corresponding feature-map Jacobian in the cross-layer setting. Across TPP, unlearning, IOI, and refusal steering experiments, this stress test reveals recoverable behavior despite successful feature-level intervention. Especially in the safety-critical refusal-steering setting, we achieve a 95.8% recovery rate on valid samples while keeping defended-feature relative drift to 0.131, substantially below suffix-based baselines. A recovery-path attribution analysis further localizes this recovery to the SAE reconstruction residual, the component left unexplained by the SAE. These results expose a gap between feature-level control and behavioral completeness: SAE features can support causal intervention, but controlling them does not guarantee control over the underlying behavior.
