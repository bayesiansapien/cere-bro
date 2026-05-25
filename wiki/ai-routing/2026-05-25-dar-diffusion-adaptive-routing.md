# DAR: Diffusion-Adaptive Routing for cross-layer information flow in DiTs

**arxiv:** [2605.20708](https://arxiv.org/abs/2605.20708) · **HF:** [papers/2605.20708](https://huggingface.co/papers/2605.20708) · **Raw:** [farmed](../../raw/huggingface/2026-05-25-rethinking-cross-layer-information-routing-in-diffusion-tran.md)
**Authors:** Alibaba Group, Nanjing University, Zhejiang University, CityU HK.

## TL;DR

Diffusion Transformers (DiTs) inherited the residual stream from the original Transformer without revisiting it. The authors diagnose three concrete pathologies in this inherited stack: monotonic forward magnitude inflation, sharp backward gradient decay, and pronounced block-wise redundancy. They propose DAR, a drop-in residual replacement that performs learnable, timestep-adaptive, non-incremental aggregation over the history of sublayer outputs. On ImageNet 256, DAR improves SiT-XL/2 by 2.11 FID (7.56 vs 9.67) and matches converged baseline quality with 8.75x fewer training iterations. Stacked on REPA it doubles early-stage training speed.

## Why this matters

DAR reframes cross-layer information flow as a routing problem. Instead of every layer reading whatever the residual stream happens to carry forward, DAR learns *which prior sublayer outputs to mix at this layer, at this denoising timestep*. That is routing in the AI-routing sense, not just "skip connections done better." The denoising timestep is the conditioning variable. Early denoising steps want coarse global structure; late steps want high-frequency detail; the same residual schedule for both is the wrong inductive bias. DAR makes the schedule learnable per timestep.

Three pathologies the paper diagnoses, with consequences:
- **Forward magnitude inflation.** Residuals accumulate monotonically, so deep layers operate in a regime far from the LayerNorm scale they were optimized for. Symptom: late layers contribute less than they could.
- **Backward gradient decay.** Pre-norm residual stacks shrink gradient signal sharply with depth. Symptom: deep DiT layers are undertrained.
- **Block-wise redundancy.** Adjacent blocks compute correlated updates. Symptom: capacity is wasted on duplicated representations.

DAR is orthogonal to REPA (the representation-alignment objective). Stacking gives 2x training acceleration in the early stage on top of REPA's own gains, suggesting cross-layer routing and representation alignment hit different axes.

## Where this fits

This is the first paper in the wiki that applies *routing* directly to diffusion architectures, rather than to LLM expert selection or agent trajectory orchestration. The MoE muP paper from 2026-05-17 ([moe-mup-maximally-scale-stable-parameterization.md](2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), which derived a scale-stable parameterization for MoE so width and expert count compose without retuning) gave routing a clean scaling theory in the LLM/MoE world. DAR extends the routing frame to the depth axis of diffusion. The KVServe paper from 2026-05-24 ([2026-05-24-kvserve-service-aware-kv-compression.md](../inference-efficiency/2026-05-24-kvserve-service-aware-kv-compression.md), which made KV compression a runtime control surface rather than a static hyperparameter) made the same move in transport. The pattern is the design surface that was treated as a fixed schedule is now a learned controller.

## Open research angles

- Does the same diagnosis hold for autoregressive video diffusion models, where the temporal axis adds a second timestep dimension? WorldKV (2026-05-24) treats those KV chunks as retrievable memory; DAR-style timestep routing on top would be interesting.
- The paper does not test DAR with linear attention substrates (Gated DeltaNet-2). If the cross-layer routing fix and the linear-attention substrate fix compose, the combined system would address two distinct pathologies at once.
- DAR's 8.75x training speedup is on ImageNet 256, an established benchmark. The next question is whether the same gain shows up at megapixel scale on T2I pretraining where the per-step cost dominates.

## Related wiki pages

- [llm-routing.md](llm-routing.md) — concept page for routing across the stack
- [2026-05-17-moe-mup-maximally-scale-stable-parameterization.md](2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) — scale-stable MoE routing
- [2026-05-24-kvserve-service-aware-kv-compression.md](../inference-efficiency/2026-05-24-kvserve-service-aware-kv-compression.md) — runtime control surface for transport
