# Quantization

*Concept page. Created 2026-09-11, prompted by a lint gap: this wiki carries twelve dated quantization summary pages and had no page synthesizing them, and by [Why Does Post-Training Quantization Work? (09-11)](2026-09-11-why-post-training-quantization-works.md), the first entry that explains the mechanism rather than exploiting it.*

Quantization is storing and computing a model's numbers at reduced precision: 16-bit weights become 8-bit, 4-bit, sometimes 2-bit or ternary. The saving is not primarily arithmetic. It is **bytes moved**, which is why quantization is the dominant lever on this wiki's cost pages: a decode step is overwhelmingly memory-bound, so halving the bit width roughly halves the time spent waiting on memory.

---

## 2026-09-17: the error budget inside an attention kernel gets measured, and it was on the value side the whole time

**[VC-Attention (09-17)](2026-09-17-vc-attention-low-bit-value-smoothing.md)** (arxiv 2609.15810, MIT / Nunchux AI / CMU / Berkeley / Stanford, with Song Han) does the decomposition that two years of low-bit attention work skipped. Every prior method in this family (INT-FlashAttention, the SageAttention line, FlashAttention-3) attacks outliers in the **query and key** matrices with channel centering, scaling or Hadamard rotation. VC-Attention measures what is left afterwards and finds that on Wan2.2 the **value** term accounts for roughly **82% of the remaining output error**. The field optimized the smaller term.

**The reason it was missed is structural and it is the transferable idea on this page.** Query and key outliers live in a **small number of fixed channels shared across tokens**, which is exactly the shape a channel-wise transform fixes. Value outliers live in **individual tokens**, and the affected channels move between heads, between layers, and between denoising steps. No fixed transform catches a moving target, and in a block quantizer a single large token sets the scale for its whole hardware block and compresses every other token in it into a narrow range of representable values. **V-Smooth's answer is not a transform at all: reorder value tokens by cheap online clustering so that similar-magnitude tokens co-locate in a block, quantize only the residual after subtracting the block mean, and recover the mean from the row sum online softmax already maintains.** Training-free, no calibration data, no extra pass.

**The second half of the paper is a statement about quantized kernels in general and it should be read as one.** Once both matmuls run on low-bit Tensor Cores, the **high-precision FP32 exponential inside softmax becomes the longest pipeline stage** on datacenter GPUs. ExpCast-FP8 deletes it by mapping log-domain scores straight to E4M3 probability codes with one fused multiply-add. **Generalized: when you succeed at making the matrix multiplications cheap, the scalar transcendental you left in the middle becomes the critical path.** Measured across B200, B300, H200, RTX PRO 6000 and RTX 5090: **1.46-1.59x over BF16 FlashAttention-4 on datacenter parts, 2.3-3.6x on workstation parts**, 1.13-1.70x end to end.

**Against [Why Does Post-Training Quantization Work? (09-11)](2026-09-11-why-post-training-quantization-works.md) this produces a cleaner rule than either result alone.** That paper explained why quantized pretrained weights survive: the error a layer newly introduces tends to **oppose** the error it inherits, so the full-precision and quantized passes diverge slowly, and LM-head geometry preferentially preserves the scores of high-ranked tokens. That is error that cancels over depth. VC-Attention's error is created inside one fused kernel by a block-scale decision and has no residual stream to cancel in. **So: quantization error that flows through the residual stream gets attenuated by pretraining; quantization error created by a block quantizer's scale choice does not, and must be fixed where it is made.** [Directional decomposition (09-16)](2026-09-16-directional-decomposition-compression-error.md), which splits compression error into a component along the hidden state and a component across it and found the perpendicular part separates methods best, is the diagnostic that would test this: block-scale error should be overwhelmingly perpendicular, and nobody has checked.

**The open question this page should now carry.** Every KV-cache quantizer in the wiki assumes outliers are channel-structured, because that is the assumption inherited from weight quantization. If KV outliers are instead **token**-structured, as value outliers are in video DiTs, then reordering rather than transforming is the right fix, and no KV quantizer does it because reordering breaks positional layout. Nobody has published the decomposition for an autoregressive LLM. **The answer decides whether KV-cache quantization has a factor of two sitting unclaimed.**

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

---

## 2026-09-16: compression error gets a direction, not just a magnitude

**[Disentangling Representation Evolution in Transformers through Directional Decomposition (09-16)](2026-09-16-directional-decomposition-compression-error.md) (arXiv 2609.15975) supplies a diagnostic this page has never had.** A transformer layer adds to the hidden state rather than replacing it, and that added update can be split into the component pointing **along** the current state (parallel, which rescales what is already there) and the component pointing **across** it (perpendicular, which rotates the representation toward something new). Applied to compression-induced update error, the finding is that **perpendicular error separates compression methods more clearly than parallel error does.**

**Why this matters here.** Every method on this page reports a scalar: a perplexity delta, a benchmark drop, a reconstruction error. Two methods with identical scalar error can be doing entirely different damage. One got the magnitude wrong; the other rotated the representation. **The second is the one that should fail on a held-out domain, and nothing currently distinguishes them before deployment.**

**It complements rather than duplicates [Why Does Post-Training Quantization Work? (09-11)](2026-09-11-why-post-training-quantization-works.md).** That paper answered why rounding weights after training costs so little, in terms of loss-landscape flatness. This one answers a different question: given that error is introduced, what *kind* is it. Flatness says how much room there is; direction says which way you moved inside it.

**It also offers an unused redundancy criterion for the pruning branch.** [WRP (09-10)](2026-09-10-wrp-forward-free-depth-pruning.md) removes layers judged redundant with each other, and [Sparser, Faster, Lighter Transformers (09-13)](2026-09-13-sparser-faster-lighter-transformers.md) removes structure more broadly. A layer whose update is overwhelmingly **parallel** is rescaling rather than computing, which is a different kind of removable than a layer duplicating its neighbour, and no pruning method here uses it.

**The cheap unrun experiment.** [Drift-Constrained Optimization (09-16)](../llms-foundation-models/2026-09-16-drift-constrained-optimization.md) selects which layers to **update** during fine-tuning and gets a qualitative reversal from a coarse layer-selective probe. WRP selects which layers to **delete**. **Whether the layers worth updating are the complement of the layers worth pruning is one profile, two uses, and nobody has checked.**

**Caveats to carry.** "Separates methods more clearly" is a separability claim, not a predictive one; whether perpendicular error *predicts* downstream degradation better than scalar error is the question a practitioner needs and it is unanswered. The training-time intervention (suppressing the full-aggregate parallel component) is from-scratch only, so it is unavailable to anyone compressing an existing checkpoint, which is nearly everyone.

## 2026-09-18: FP4 ships inside a frontier cache, and ternary weights reach 98.2% at a ninth of the size

**[DeepSeek-V4.1-Flash (09-18)](2026-09-18-deepseek-v41-flash-kv-cache-compression.md) (arXiv 2609.19969) puts FP4 KV caching in a shipped frontier model, composed with two other compression axes rather than used alone.** Its global KV cache is **890 bytes per token, roughly a quarter of DeepSeek-V4-Flash**, achieved by compressing three orthogonal dimensions simultaneously: values per entry (FP4, four bits), entries along the sequence (CSA2 token selection), and layers holding an independent cache (CSA2 cross-layer reuse). **This page's KV-quantization sub-thread has been the one with the most numbers and the least deployment evidence; four bits per value in production at a lab that publishes its serving economics is the strongest data point it has.**

**The caveat is the one that limits what can be carried forward: FP4 is presented as a design choice, not an ablation.** The paper gives one composite 4x figure and does not separate how much came from precision versus token sparsity versus cross-layer reuse. **So this confirms FP4 KV is viable at frontier scale and quality; it does not tell you what FP4 alone buys.** That matters because anyone retrofitting precision onto an existing model gets only the precision axis.

**The ternary result is the day's other compression number and it arrives from the open-weight side.** PrismML released **Bonsai 2 27B**, a ternary-weight compression of Qwen3.8 27B (weights constrained to -1, 0 and +1) that reports **98.2% of the FP16 parent's benchmark performance at 5.95 GB against roughly 54 GB**, about a ninth of the size, Apache 2.0, with 262k context, vision, tool use and agentic capability retained, running at **55 tokens per second with WebGPU on an M5 Max** and demonstrated driving a coding agent and computer-use on a single RTX 5090. The generational detail is the informative one: **against the first Bonsai 27B two months ago the size barely moved, but retention rose from about 95% to 98.2%**, with the base model swapped from Qwen3.6 to Qwen3.8. **The compression ratio is saturating and the quality retention is still improving**, which is the signature of a method whose remaining headroom is in the recipe rather than the bit budget.

**Vendor self-report, single benchmark suite, no independent reproduction, and "98.2% of benchmarks" is an average that can hide a bad tail.** The claim that math and code scores are "very close" to the parent is the one to verify first, since those are where quantization damage usually concentrates.

**Read against [the 09-16 entry](#2026-09-16-compression-error-gets-a-direction-not-just-a-magnitude), both of today's results point the same way.** That entry recorded compression error acquiring a direction rather than only a magnitude. FP4-inside-a-three-axis-scheme and ternary-at-98.2% are both cases where the naive expectation from bit count alone would predict much worse, and the gap between predicted and actual damage is exactly what a directional error model is for. **Neither of today's results reports error direction, so they enlarge the phenomenon the 09-16 entry named without advancing the explanation.**

**Hardware read-through.** [SemiAnalysis reported the same day](../hardware/2026-09-18-semianalysis-engram-dram-ssd-offloading.md) that NVIDIA despec'd Rubin Ultra from 1024 GB to roughly 200 GB of HBM per chip. **Every result on this page is an argument about how to spend a memory budget that just shrank five-fold on the flagship roadmap.** A 27B model that fits in 5.95 GB and a frontier cache at 890 bytes per token are the two ends of the same response.

---

## 2026-09-19: the bit budget gets a minimax objective, and the unit of non-uniformity becomes a sub-network

**[Colla-Q (09-19)](2026-09-19-colla-q-moe-quantization-minimax.md) (arXiv 2609.18131, Ajou University) is the eleventh result on this page supporting the organising finding that uniform precision is the wrong default, and the first where the thing being treated non-uniformly is a routed sub-network rather than a tensor.** Every prior axis catalogued here is a property of numbers in a matrix: per-layer, per-channel, per-tile ([TileMix, 08-25](2026-08-25-tilemix-tile-centric-mixed-precision-attention.md), FP16 or INT8 chosen per matrix tile), per-token, key-versus-value ([09-17](2026-09-17-vc-attention-low-bit-value-smoothing.md), which found the attention error budget sits on the value side), and direction-versus-magnitude ([09-16](2026-09-16-directional-decomposition-compression-error.md)). Colla-Q's axis is **which expert in a mixture-of-experts layer is currently worst**, and its argument requires treating the layer as an ensemble.

**The allocation rule inverts the default and the inversion is the contribution.** PMQ, MxMoE and QuantMoE-Bench all spend bits where the routing traffic is. Colla-Q spends them on the weakest expert, iteratively, on an ensemble argument: if expert errors are roughly uncorrelated and routing weights roughly uniform, minimising the **sum of squared** expert errors drives you to equal error across experts, because a sum of squares punishes outliers. Translated: a rarely-fired expert crushed by 2-bit quantization is a worse defect than a heavily-fired expert that is slightly degraded, because the cost is not paid at allocation time, it is paid the moment the neglected expert fires. **Mixtral 8x7B at 2.54 average bits: 68.5% across eight benchmarks, against PMQ 67.5%, MxMoE 65.1%, uniform GPTQ 42.9%.** At 1.57 bits the margin collapses to 54.5% against 53.6%, which is inside the noise band for an eight-benchmark average with no variance reported.

**The calibration-robustness result is the one to carry forward, because it attacks a failure mode this page has never named.** Routing frequency is a property of the calibration corpus, not of the model: calibrate on math and the numerically-specialised experts look important, then ship that allocation and it underperforms on general text. Colla-Q's activation-entropy metric needs no labels and holds **cosine similarity above 0.98 across C4, math, French and QA calibration sets, where PMQ's routing metric moves at 0.72 to 0.86.** **Every mixed-precision method on this page inherits a calibration set, and none of the others report what happens when the calibration domain does not match the serving domain.** That is now a standing gap for the whole page, not just for MoE.

**What it does not report is throughput, and for a mixed-precision method that omission is disqualifying until filled.** Heterogeneous per-expert bit-widths are exactly the case where kernels get slow, and a one-point accuracy gain is worth nothing at a 20% throughput cost.

**Hardware read-through, continuing the 09-18 entry's.** With Rubin Ultra cut from 1024 GB to roughly 200 GB of HBM per chip, MoE expert parameters are the largest object that must be either shrunk or paged out. **Colla-Q and [Engram-style offloading](../hardware/2026-09-18-semianalysis-engram-dram-ssd-offloading.md) are substitutes competing for the same decision, not complements**, and nobody has priced them against each other. The same week's [MoE decode-fragmentation analysis](../hardware/2026-09-19-moe-decode-batch-fragmentation.md) adds the reason the comparison is not obvious: offloading buys batch size, and batch size is what makes expert matrix multiplies wide enough to be worth doing at all.

## 2026-09-23: precision becomes a per-component allocation problem, in two places at once

**Two papers on the same Kurate cs.LG board this week make the same architectural argument in different parts of the transformer: uniform precision is a bug, and the fix is a per-component allocator.** Neither cites the other.

**[KV-COBRA](2026-09-23-kv-cobra-bit-rank-allocation.md) allocates across attention heads, and adds a second currency.** Its framing is that KV compression has two knobs, rank truncation and bit-width, that trade off differently per head because heads differ in singular-spectrum decay and per-channel outlier structure. Co-optimizing the two per head, using only standard low-rank projection and scalar quantization, **dominates uniform allocation from 0.5 to 4 bits per dimension, with the largest gains at the lowest bit-rates and no per-token overhead.** Two supporting mechanisms are worth noting for this page: a **fused Hadamard rotation** equalizes per-channel variance before quantization, which is the same outlier-taming trick weight quantization has used for two years, and **reordering the SVD basis by attention-KL importance** rather than by singular value makes the allocator query-aware. **The Hadamard reuse is evidence that KV quantization and weight quantization are converging on one toolkit rather than remaining separate literatures.**

**[Colla-Q](2026-09-19-colla-q-moe-quantization-minimax.md) allocates across mixture-of-experts experts, and it reappears on this week's board at #20.** Its minimax objective hands the next bit to the *weakest* expert rather than the busiest, using an activation-entropy statistic that needs no labels. On Mixtral 8x7B at **2.54 bits per weight it reaches 68.5% average accuracy across eight benchmarks, against 67.5% for PMQ, 65.1% for MxMoE and 42.9% for uniform GPTQ.** The under-discussed result is reduced sensitivity to the calibration set, which is operationally worth more than the accuracy delta because calibration sets are usually chosen by convenience.

**Why these belong together.** The averaging objective that both papers reject is the right objective for a dense network, where every parameter contributes to every forward pass. It is wrong for any architecture with routed or heterogeneous components, for two reasons: a rarely-used component contributes little to the average and catastrophically to the inputs it does serve, and degrading components unevenly silently changes the effective routing distribution, because the router was trained against full-precision components and nothing in the loss notices. **Precision is becoming a routed resource allocated per component, not a global hyperparameter.** That claim now has support from the cache side and the weight side simultaneously, and it extends the 09-11 kv-cache entry ("precision becomes the second thing you route inside the cache") out of the cache and into the weights.

**Tooling caught up on the same day.** HuggingFace shipped [Transformers running llama.cpp quants](https://huggingface.co/blog/transformers-llama-cpp-quants) directly, which collapses the long-standing split between the research quantization stack and the practitioner GGUF stack. If per-component allocation lands anywhere, it lands as an allocation pass inside toolchains like this rather than as a new file format.


---

## 2026-09-24: allocation by inference phase

**[Disaggregated Quantization](2026-09-24-disaggregated-quantization-prefill-decode.md) (Panferov, Alistarh et al.) adds a new allocation axis: the inference phase.** Prefill is compute-bound and wants low-precision arithmetic (NVFP4 weights and activations); decode is bandwidth-bound and wants compact weights with unquantized activations. Separate checkpoints per phase: removing activation quantization on decode alone improves decode-heavy accuracy at no cost, and an NVFP4 prefiller lifts a **1-bit** Qwen3.8-27B GGUF decoder by **32.5 points on MMLU-Pro and 35.3 on MMMU-Pro**. The prefiller streams from SSD (ODP) for **1.78x TTFT** at 8K prompts in llama.cpp; shared-weight format disaggregation is validated up to 2.8T parameters.

This extends the page's organizing claim, "precision should be allocated, not set," from spatial axes (per head, per expert, per layer, per token) to a temporal one. It lands the day after [KV-COBRA](2026-09-23-kv-cobra-bit-rank-allocation.md) and [Colla-Q](2026-09-19-colla-q-moe-quantization-minimax.md) made the same allocation argument across heads and experts. Still no published system composes two allocation axes.

Practitioner side, same day: Mirai's codec puts **Qwen3.8-27B at 2.4 bits per weight in 8.45 GB**, running on stock vLLM with a plugin (86-141 tok/s on an RTX 3090) and on Apple silicon ([model card](https://huggingface.co/trymirai/Qwen3.8-27B-S-experimental)).


## 2026-09-25: the quantization pass itself gets 15x to 30x cheaper

[LLM Compressor v0.14.0](2026-09-25-llm-compressor-v0-14-triton-gptq.md) ships a Triton GPTQ kernel (about 15x end to end), batches same-shape layers (up to 30x on MoE), drops Hessian offloading, and widens the MSE/iMatrix observer grid search, which finds better NVFP4 scales and beats GPTQ for NVFP4 on internal benchmarks. Model-free PTQ adds KV-cache quantization. Red Hat's GLM-5.3-NVFP4 recovers 95%+ and is served with an 8-token speculator on Blackwell, so a bandwidth saving and a sequential-step saving stack. **Why it matters for this page:** [Disaggregated Quantization (09-24)](2026-09-24-disaggregated-quantization-prefill-decode.md) needs a separate prefill checkpoint per model. Cheap requantization removes most of the cost of that idea, and makes per-workload checkpoints an operational choice rather than a research project.


---

## 2026-09-26: perplexity is not a safety metric

[Alignment Collapse Under KV Cache Quantization](2026-09-26-kv-quantization-alignment-collapse.md) (NeurIPS 2026) shows low-bit KV quantization can strip refusals with near-unchanged perplexity (Mistral-7B: 15.2% of refusals lost at 1.03x perplexity), with model-specific phase transitions and no universal safe bit-width. The mechanism is outlier-driven scale factors crushing the non-outlier channels where safety lives, or safety overlapping the outliers themselves, or safety diluted across layers. The fix differs per mode, and a 20-prompt probe (PCR) predicts which. **For this page: the 09-25 LLM Compressor release made re-quantizing cheap; this paper says each re-quantization now needs a refusal check next to perplexity.** Whether weight quantization (NVFP4, GPTQ) has the same fragility is untested here.
