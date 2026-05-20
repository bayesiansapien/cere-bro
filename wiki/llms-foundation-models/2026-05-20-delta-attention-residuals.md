# Delta Attention Residuals

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.18855](https://arxiv.org/abs/2605.18855) · [raw](../../raw/huggingface/2026-05-20-delta-attention-residuals.md)

## TL;DR

Attention Residuals replace standard additive residual connections with learned softmax attention over previous layer outputs, enabling selective cross-layer routing. But standard Attention Residuals attend over cumulative hidden states, which are highly redundant. The paper shows this redundancy causes routing collapse in deeper layers: attention weights become low-contrast and approach uniform (max weight roughly 0.2), so the model cannot pick out informative states in previous layers. Delta Attention Residuals attend over deltas, the change introduced by each sublayer (the new hidden state minus the prior one), instead of cumulative states. Deltas are structurally diverse and yield high-contrast attention distributions (max weight roughly 0.6), enabling selective and effective routing across layers. Across all tested scales (220M to 7.6B), Delta Attention Residuals consistently outperform both standard residuals and Attention Residuals with 1.7-8.2% validation perplexity gains. The construction supports fine-tuning conversion of pretrained checkpoints.

## Why it matters

The residual connection is one of the most load-bearing architectural choices in the Transformer. Most prior architectural work either replaces it (highway networks, gated residuals) or augments it (DenseNet-style aggregation). Attention Residuals already showed that learned routing over layer outputs works. The contribution here is identifying that cumulative states are the wrong substrate to route over, because they have low effective rank relative to the contribution any single layer makes. Deltas (sublayer increments) are the right substrate. The 1.7-8.2% PPL gain at 7.6B scale is a real architectural primitive worth attention.

## Mechanism

For each sublayer i, compute the delta v_i = h_{i+1} - h_i (the change the sublayer introduced). Replace the additive residual with a learned softmax-attention over the deltas of all prior sublayers. The attention picks which sublayer contributions are most useful at the current layer. Because deltas are structurally diverse (each comes from a different sublayer's update), the attention distribution becomes high-contrast (max weight around 0.6) rather than low-contrast (around 0.2 for cumulative states). The principle works at per-sublayer granularity and at coarser block granularity.

## Open questions and gaps

Tested at 220M to 7.6B; whether the gain holds at frontier MoE scale is unknown. The conversion of pretrained checkpoints is shown to work via fine-tuning but the cost of conversion (FLOPs, data) is not quantified. The mechanism naturally raises a question about MoE architectures, where the sublayer is itself a routed mixture, and whether double-routing (route over experts within a sublayer, route over deltas across sublayers) composes or interferes.

## Industrial implication

A 1.7-8.2% PPL gain at architecture-level is large enough to justify integration in the next pretraining run for any lab that controls its training recipe. Conversion of pretrained checkpoints via fine-tuning lowers the bar further. If conversion holds at 30B+ scale, this is the kind of architectural primitive that gets adopted by every open-weight release within a year.

## Connections

- **SNLP (2026-05-19)** opened layer-parallel inference via Newton corrections on the residual structure. Delta Attention Residuals changes what the residual structure is. Whether the two compose, or whether deltas help or hurt Newton convergence, is the obvious next experiment.
- **Lighthouse Attention (2026-05-16)** is a training-only wrapper that gets removed at inference. Delta Attention Residuals is a permanent architectural change. Different parts of the architecture-modification design surface.
