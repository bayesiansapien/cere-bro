# Quantization

*Concept page. Created 2026-09-11, prompted by a lint gap: this wiki carries twelve dated quantization summary pages and had no page synthesizing them, and by [Why Does Post-Training Quantization Work? (09-11)](2026-09-11-why-post-training-quantization-works.md), the first entry that explains the mechanism rather than exploiting it.*

Quantization is storing and computing a model's numbers at reduced precision: 16-bit weights become 8-bit, 4-bit, sometimes 2-bit or ternary. The saving is not primarily arithmetic. It is **bytes moved**, which is why quantization is the dominant lever on this wiki's cost pages: a decode step is overwhelmingly memory-bound, so halving the bit width roughly halves the time spent waiting on memory.

---

## The mechanism: why it works at all

Until 2026-09-11 this page's prior entries all took the empirical fact for granted. [Why Does Post-Training Quantization Work? (09-11)](2026-09-11-why-post-training-quantization-works.md) (Tsinghua + Bosch, Kurate cs.LG #10, absent from HuggingFace) measures it and names two mechanisms.

1. **Counteracting residual interaction.** Decompose the error at a layer's output into the part inherited from its input and the part its own quantized weights just introduced. In a pretrained model those two components are **anti-correlated**: the fresh error systematically opposes the inherited one, they partly cancel, and the full-precision-versus-quantized gap grows slowly instead of compounding. A randomly initialized model with *comparable weight reconstruction error* does not have this and its hidden states diverge fast. So the robustness is **acquired during pretraining**, not a consequence of the perturbations being small.
2. **LM-head geometry.** Whatever hidden-state error survives is projected through the output head, and that projection preferentially preserves the scores of high-ranked tokens. The error lands in the long tail of the vocabulary, reordering tokens that were never going to be sampled.

The practical consequence, which no method on this page currently uses: **the error budget is not uniform**, so the regions where neither protection applies are the ones worth spending bits on.

---

## The organizing finding: uniform precision is the wrong default

Every result below is an answer to the same question, *along which axis is sensitivity non-uniform*, and the axes keep multiplying.

| Axis | Result | Claim |
|---|---|---|
| Inference phase | [Mix-Quant (05-21)](2026-05-21-mix-quant-phase-aware-quantization.md) | NVFP4 for prefill, BF16 for decode. Prefill is empirically robust; decode error compounds across a long autoregressive trajectory. Up to 3x prefill speedup. |
| Layer sensitivity | [MXSens (07-27)](2026-07-27-mxsens-mixed-precision-quantization.md) | Measure which parts degrade under low precision, spend the bit budget accordingly. |
| Geometric tile of the score matrix | [TileMix (08-25)](2026-08-25-tilemix-tile-centric-mixed-precision-attention.md) | Dispatch each tile group through an FP16 or INT8 path, both updating one shared online-softmax state. Recovers the INT8-KV-cache quality tax. |
| Semantically selected tokens | [HyQuant (09-11)](2026-09-11-hyquant-hybrid-precision-attention.md) | Keep persistently attended "vertical-line" tokens plus a local window in high precision, quantize the rest. One rule covers prefill and decode. |
| Block processing order | [ICBQ (08-12)](2026-08-12-icbq-interleaved-cross-block-quantization.md) | The *schedule* alone separates a usable sub-2-bit model from a broken one. A left-to-right sweep never revisits early error; interleaving block interfaces does. |
| Robot execution state | [VQVLA (08-03)](2026-08-03-vqvla-motion-aware-quantization.md) | Coarse approach motion tolerates aggressive quantization, fine contact-adjacent motion does not. Precision follows the trajectory, not the tensor statistics. |
| Normalization position | [MXAttention (08-01)](2026-08-01-mxattention-mxfp4-attention-quantization.md) | Quantize unnormalised exponentials **before** the softmax row sum, and a single distribution-independent optimum (Qmax = 7.25) removes the calibration set entirely. |

**The pattern statement.** Seven results, seven different non-uniformity axes, and no two of them compose in any published system. The field has converged on "precision should be allocated, not set" and has not yet asked whether the allocations are additive or whether they all cash the same redundancy budget. That is the highest-value open question on this page.

---

## KV cache quantization: the sub-thread with the most numbers

The cache is where quantization pays best because it grows with context and concurrency while the weights do not.

- [TurboQuant (04-22)](2026-04-22-turbo-quant-kv-cache-quantization.md): 6x memory reduction at 2.5 bits/channel, online with no offline calibration. Random rotation shapes the distribution, then per-coordinate optimal scalar quantizers plus a 1-bit QJL residual for unbiased inner products.
- [OScaR (05-21)](2026-05-21-oscar-extreme-kv-cache-quantization.md): identifies **Token Norm Imbalance** as the real failure at extreme bit widths, not channel outliers as the literature assumed. Canalized rotation re-aligns token-level outliers into channels, omni-token scaling absorbs the residual. Near-lossless INT2, 3.0x decode, 5.3x memory, 4.1x throughput against BF16 FlashDecoding-v2.
- [Ken Huang, Chapter 4 (09-10)](2026-09-10-extreme-quantization-blackwell-fp4-native-fp8.md): the production view. Blackwell NVFP4 and OCP MXFP4 on 5th-gen Tensor Cores, DeepSeek-V4's tile-wise FP8 GEMM with E4M3 forward and E5M2 backward reported lossless at 1.6T and 2.8T scale, and KIVI 2-bit streaming caches with a sliding-window residual buffer.
- [HyQuant (09-11)](2026-09-11-hyquant-hybrid-precision-attention.md) fuses KV dequantization into the attention computation, which is the detail that decides whether a compressed cache is actually faster: dequantizing into registers and *then* attending reintroduces the traffic the compression removed.

---

## Where quantization breaks

- **Recurrent and state-space layers.** [When Quantization Breaks Memory (09-07)](2026-09-07-quantization-breaks-recurrent-state.md): a quantized recurrent state is written down and read back as the next timestep's input, so the storage rule *changes the computation* rather than approximating it. Repeated small updates fall below the write threshold and are silently discarded while the network keeps proposing them. Holding a trained GRU fixed and switching to deterministic 4-bit state storage increased estimation error roughly 70x on one target and 300x on another. Error feedback and residual/direction memory recover accuracy with no retraining. **Read against the 09-11 mechanism paper this is not a coincidence:** counteracting residual interaction requires a residual highway that inherited and injected error can cancel across, and a multiplicatively-carried recurrent state has no such decomposition. The protection simply does not exist in that geometry.
- **After a repair step.** [Quantization-Aware Healing (08-26)](2026-08-26-quantization-aware-healing.md) found that distilling from a degraded recovered checkpoint caps the student, and fixed it by pointing the teacher back at the original pre-compression model. Under the mechanism account, a recovery fine-tune is exactly the thing that could disturb the anti-correlation, which predicts healing procedures should be scored on whether they *restore* it, not only on downstream accuracy. Nobody measures that.
- **Stacked with depth pruning, untested.** [X-AuT (09-11)](2026-09-11-x-aut-audio-encoder-compression.md) and [WRP (09-10)](2026-09-10-wrp-forward-free-depth-pruning.md) both remove transformer depth. Removing layers removes cancellation opportunities, so a depth-pruned model should be *more* fragile to quantization at the same bit width. Falsifiable, cheap, unpublished.

---

## Open problems

1. **Are the seven non-uniformity axes additive or redundant?** Run HyQuant's token selection and TileMix's tile dispatch in one kernel. If the recovered accuracy is roughly the max rather than the sum, the field has been describing one redundancy from seven angles.
2. **Calibrate by anti-correlation.** GPTQ, AWQ and descendants select calibration data by activation statistics. If robustness comes from a residual anti-correlation that is weaker in some layers than others, the calibration budget belongs in the weak layers, and the 09-11 paper's instrumentation already measures which those are.
3. **When during pretraining does quantizability appear?** If the anti-correlation emerges at a particular token count or loss level, quantizability becomes a checkpoint property you can select for, which would be the first training-time lever on a serving-time cost.
4. **Activation and cache quantization have no mechanism account.** The 09-11 analysis is weight-only, and most of this page's practical results are not.

---

## Related Pages

- [KV Cache](kv-cache.md)
- [Model pruning and sparsity](model-pruning-sparsity.md)
- [Knowledge distillation](knowledge-distillation.md)
- [LLM Routing](../ai-routing/llm-routing.md) (precision routing is the lowest level of the same allocation problem)
- [Memory hierarchy for AI](../hardware/memory-hierarchy.md)

---

## 2026-09-12: an eighth non-uniformity axis, and it is not about bits

**[FastE (09-12)](2026-09-12-faste-readout-triggered-token-compression.md)** (arXiv 2609.08407, Zhejiang + Ant Group, Kurate cs.AI #12, absent from HuggingFace) is not a quantization paper, and it belongs on this page anyway, because it makes this page's organizing claim on a new axis. It measures **depth-dependent prefix redundancy** in final-readout LLM embedding models: removing prefix states is substantially damaging in shallow layers and nearly free at depth, because the prefix and the readout state co-propagate until the readout has absorbed what it needs. It then compresses, training-free, triggered by a fixed threshold on batch-mean **readout-prefix alignment**, retaining prefix states ranked by **the attention they receive from the readout position**. On NarrativeQA with Qwen3-Embedding-0.6B: **40.11% fewer decoder-backbone FLOPs at 99.53% of full-forward nDCG@10**, with the tradeoff exposed as one knob (maximum removal ratio) and no retraining.

**The axis is depth crossed with position, and none of the seven rows above carry it.** Mix-Quant splits by inference phase, MXSens by layer sensitivity, TileMix by geometric tile, HyQuant by semantically selected tokens, ICBQ by block processing order, VQVLA by robot execution state, MXAttention by normalization position. **FastE says the compressibility of a token's state is a function of how deep you are**, which is a different object from how sensitive a layer is to low precision. The generalization of this page's pattern statement follows directly: **it is not that precision should be allocated rather than set, it is that compute should be allocated rather than set**, and bit width is one instrument among several. The open question stands and gets larger: eight axes, no two composed in any published system, and nobody has asked whether they are additive or all cashing one redundancy budget.

**It also pairs with a non-quantization result from two days earlier in a way worth naming.** [WRP (09-10)](2026-09-10-wrp-forward-free-depth-pruning.md) removes whole transformer blocks by estimating inter-layer redundancy from checkpoint weights with no forward pass. WRP says the deep layers are redundant with each other; FastE says the deep layers stop needing the input. **Both are claims that the back half of an LLM does less independent work than its parameter count implies, arrived at independently and from opposite evidence.** The composition (prune with WRP, then re-measure FastE's depth-redundancy curve on the shortened stack) would settle whether they are additive, and it is cheap.
