---
source: farmer/huggingface
farmed: 2026-08-31T10:31:04.593371+05:30
arxiv_id: 2608.27529
url: https://huggingface.co/papers/2608.27529
arxiv_url: https://arxiv.org/abs/2608.27529
date: 2026-08-31
---

# Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction

Streaming 3D reconstruction from extremely long videos requires estimating camera motion and scene geometry online under bounded memory and computation. Early streaming models achieve causal, bounded-cost inference using finite context buffers or compact recurrent states, yet their estimates often deteriorate as sequences grow. Recent methods improve long-horizon stability by coupling short-range context with persistent or multi-level long-range memory. We pursue a different route: we keep the learned temporal state strictly local and formulate predictions whose targets remain independent of sequence length. We present ABot-Recon, a simple streaming model that caches KV features from only the preceding 11 frames. It predicts a point map in the current camera coordinate system together with an adjacent-frame relative pose. These predictions remain equivariant under changes of reference frame, and global poses and geometry are recovered through sequential composition. To reduce accumulated drift, a lightweight temporal refiner improves relative rotations using recent visual and motion context, while a composition-aware pose loss supervises multi-step pose composition. Extensive evaluations on challenging long-sequence benchmarks demonstrate the superior long-horizon performance of our local-context approach. On Oxford Spires, ABot-Recon achieves an ATE of 4.35 m and an RPE-R of 0.12^circ, reducing both errors by approximately 40\% relative to the best prior results.
