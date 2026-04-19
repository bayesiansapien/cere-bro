---
source: farmer/huggingface
farmed: 2026-04-19T00:00:00Z
arxiv_id: 2604.14430
url: https://huggingface.co/papers/2604.14430
arxiv_url: https://arxiv.org/abs/2604.14430
date: 2026-04-19
---

# Three-Phase Transformer

We present Three-Phase Transformer (3PT), a residual-stream structural prior for decoder-only Transformers built on a standard SwiGLU + RMSNorm + RoPE + GQA backbone. The model-dimension hidden vector is partitioned into N equally-sized cyclic channels, each maintained by a small number of phase-respecting operations scattered through every block: a per-channel RMSNorm, a 2D Givens rotation inserted between attention and FFN that rotates each channel by θ + i·(2π/N), and a head-count constraint that aligns GQA heads with the partition. The architecture is a self-stabilizing equilibrium between scrambling and re-imposition, not a bolted-on module. The cyclic partition geometrically carves out a one-dimensional DC subspace orthogonal to the channels, into which we inject a fixed Gabriel's horn profile r(p) = 1/(p+1) as an absolute-position side-channel that composes orthogonally with RoPE's relative-position rotation in attention. The canonical instantiation N=3 borrows its geometric metaphor from a balanced three-phase AC system in which three sinusoids 120° apart sum to zero with no anti-correlated pair. At 123M parameters on WikiText-103, 3PT achieves a 7.20% perplexity reduction (−2.62% bits-per-byte) over a matched RoPE-Only baseline at +1,536 trainable parameters (0.00124% of total), with a 1.93× step-count convergence speedup (1.64× wall-clock, after a 17% per-step overhead).
