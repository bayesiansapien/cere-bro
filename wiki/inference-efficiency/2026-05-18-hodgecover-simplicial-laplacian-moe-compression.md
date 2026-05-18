# HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse Mixture-of-Experts

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.13997](https://arxiv.org/abs/2605.13997)
**Tier:** 1 (MoE compression, inference efficiency)
**Raw:** [raw/huggingface/2026-05-18-hodgecover-...md](../../raw/huggingface/2026-05-18-hodgecover-higher-order-topological-coverage-drives-compress.md)

## TL;DR

HodgeCover identifies a structural blind spot in every prior learning-free Mixture-of-Experts (MoE) compressor. Existing compressors score experts on pairwise compatibility, so they cannot detect the case where three experts are each pairwise mergeable but form an irreducible cycle when merged together. The paper proves the obstruction is the harmonic kernel of the simplicial Laplacian on a 2-complex whose vertices are experts, whose edges carry the KL merge barriers between expert pairs, and whose faces carry the triplet merge barriers. Hodge decomposition isolates this harmonic kernel exactly. HodgeCover greedily covers the harmonic-critical edges and the harmonic-critical triangles. A hybrid variant pairs the selection with off-the-shelf weight pruning on the survivors. On three open-weight Sparse MoE backbones under aggressive expert reduction, HodgeCover matches state-of-the-art learning-free baselines on the per-expert-axis and leads on the aggressive-compression frontier of the hybrid axis.

## Why it matters

This is the first MoE compression paper in the wiki that names a mathematically precise reason why pairwise expert-scoring methods cap out at moderate compression. Pairwise compatibility is necessary but not sufficient: a triangle of pairwise-compatible experts can be a non-mergeable triple. The paper turns that observation into an actionable selection objective using tools from algebraic topology (simplicial Laplacians, Hodge decomposition) that are unusual in the inference-efficiency literature.

For practitioners running open-weight MoEs (Gemma 4 26B-A4B, DeepSeek V4 Pro 1.6T-A49B and Flash 284B-13B, Kimi K2.6, Qwen3.6 35B-A3B, Laguna XS.2 33B-A3B) under hardware-constrained inference, the relevant claim is the aggressive-compression frontier. At moderate compression every reasonable scoring method works. At aggressive compression the pairwise-blind methods break, and HodgeCover does not.

## Method (mechanism)

The 2-complex construction:

- **Vertices:** the experts in a Sparse MoE layer.
- **Edges:** for each pair of experts (i, j), the edge weight is the KL merge barrier when those two experts are merged. Low barrier means easy to merge.
- **Faces (triangles):** for each triple (i, j, k), the face weight is the triplet merge barrier when those three experts are merged jointly. A triangle whose pairwise edges are all low-barrier but whose face is high-barrier is the obstruction case the paper highlights.

The simplicial Laplacian on this 2-complex has a Hodge decomposition that splits the edge-barrier signal into three orthogonal components: a gradient component (consistent with merging along a hierarchy), a curl component (consistent with cyclic merge orderings), and a harmonic component (the structural obstruction). HodgeCover isolates the harmonic component and treats the edges and triangles that contribute most to its norm as the critical structures to preserve through any compression decision. Greedy coverage of these harmonic-critical edges and triangles gives the selection objective.

The hybrid variant runs HodgeCover selection first, then applies off-the-shelf weight pruning on the surviving experts. The paper reports that the hybrid version dominates on the aggressive-compression axis where standalone weight pruning would also fail.

## Connection to prior wiki context

This sits at the intersection of two threads the wiki has been building.

**Thread 1, MoE compression and routing.** BEAM (2026-05-16, Binary Expert Activation Masking, the paper that replaced fixed top-K MoE routing with a per-token learned binary mask trained end-to-end via straight-through estimator and achieved 98%+ retention at up to 85% FLOP reduction) attacked the FLOP axis of MoE inference cost by deciding per token which experts to activate. HodgeCover attacks the parameter-memory axis by deciding which experts to keep at all, learning-free. The two are orthogonal and compose: BEAM reduces the active-experts-per-token count; HodgeCover reduces the resident-experts-per-layer count. Combined, they target both the FLOP and memory bottlenecks of frontier MoE serving.

**Thread 2, principled scale-stable MoE design.** MoE-muP (2026-05-17, Vankadara et al., the paper that derived the first principled scaling theory for MoEs as the Maximally Scale-Stable Parameterization across the five axes of expert count M, expert width Ne, routing sparsity K, network width N, and depth L) tells you how to pick (M, Ne, K) for a new MoE before training. HodgeCover tells you how to compress (M, Ne, K) for an existing MoE after training without retraining. Both papers operate on the same five-axis MoE design surface; MoE-muP is the forward direction and HodgeCover is the inverse direction.

**Cross-paper composition the wiki has not seen.** A frontier MoE designed under MoE-muP's MSSP recipe, deployed under BEAM's binary mask, then compressed under HodgeCover's harmonic-coverage objective would target all three knobs of MoE efficiency simultaneously: principled pre-training scaling, dynamic per-token activation, and structural post-training compression. None of those three papers makes this composition explicit; this is the natural next experiment.

## Research angle

1. **Empirical falsifier on the open-model wave.** Apply HodgeCover to Gemma 4 26B-A4B, DeepSeek V4 Flash 284B-13B, Kimi K2.6, and Qwen3.6 35B-A3B. The wiki's prediction: HodgeCover wins by 5-15% on the aggressive-compression frontier and ties at moderate compression. If the win at aggressive compression is smaller than 5%, the harmonic obstruction is rarer in practice than the paper suggests. If larger than 15%, the obstruction is systemic and the field has been leaving large memory savings on the table.
2. **Higher-order obstructions.** The paper analyses the 2-complex (triangles). Whether 3-complexes (tetrahedra) and beyond surface additional obstructions for very wide MoE layers (M >= 64) is open. The DMFT machinery in MoE-muP could potentially predict at which M the higher-order obstructions become quantitatively significant.
3. **Hodge-aware routing.** The harmonic kernel identifies expert triples that should not be jointly merged. A natural extension is to make BEAM's routing aware of harmonic structure: prefer per-token activation patterns that avoid harmonic-critical triples even at fixed K.

## Links

- arXiv: <https://arxiv.org/abs/2605.13997>
- Concept page: [Mixture of Experts compression](../inference-efficiency/kv-cache.md) (extension pending)
- Related: [BEAM 2026-05-16](../ai-routing/2026-05-16-beam-binary-expert-activation-masking-moe.md), [MoE-muP 2026-05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
