---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351871+05:30
arxiv_id: 2609.34970
url: https://huggingface.co/papers/2609.34970
arxiv_url: https://arxiv.org/abs/2609.34970
date: 2026-10-01
---

# See it, Say it, Sorted: Mechanistic Diagnosis and Parameter-Space Mitigation of Emergent Misalignment in LLMs

Safety-aligned LLMs can exhibit emergent misalignment (EM): narrow domain adaptation unexpectedly triggers catastrophic safety failures across unrelated domains. Prior static analyses leave training dynamics unmapped, while existing defenses rely on heuristics that degrade utility. We present a dynamic, second-order geometric study of EM. Tracking training trajectories reveals that directional Hessian curvature concentrates sharply on semantic pivot tokens. Grassmannian projections show that, in most settings, harmful-safe gap widens mainly because safe-gradient overlap declines. Leveraging these insights, we introduce a parameter-level Geometric Mitigation Framework that orthogonally projects empirical harmful gradient subspace out of parameter updates. On Qwen2.5-14B-IT, our defense suppresses free-generation EM by up to 80.0%; across the other three of four open-weight instruction-based model families (3B--20B), where single-layer behavioral EM is already near zero, teacher-forced evaluation shows same harmful subspace controls the conditional support of frozen EM responses. Crucially, these diagnostics unmask the illusion of behavioral safety: the same subspace remains measurable and steerable in models where behavioral EM is near zero. Code: https://github.com/WeiqiaoQUE/mechanistic-emergent-misalignment.
