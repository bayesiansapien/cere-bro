# Post-Training Ternarization of Qwen3-4B: Capability, Effective Bit Budget, Storage Compression, and Deployment

**Source:** arXiv [2609.01962](https://arxiv.org/abs/2609.01962) · Anirudh Malik, M Sparsh Mehra, Poojith Devan
**Signal:** Kurate cs.AI weekly leaderboard #16, ai_rating 3.5/10. Not on HuggingFace.
**Raw:** `raw/kurate/2026-09-08-cs-ai.md`
**Date ingested:** 2026-09-08

---

## TL;DR

This is a negative result reported honestly, and it is more useful than most positive ones. The authors take an instruction-tuned Qwen 4B model and convert it post-training to ternary weights (each weight is one of three values, the regime usually marketed as "1.58-bit"), using KOTMS rotation, E2M-ATQ ternarization and GPTQ-style error compensation. Then they measure everything a "1.58-bit" label hides. The real cost is **1.641 effective bits per weight** over the **81.62% of parameters** actually targeted, not 1.58 over 100%. Accuracy across ten scored comparisons falls **64.5% → 54.7%**, and the degradation is wildly uneven: BoolQ retains 84.6% of chance-corrected teacher performance while ARC-Challenge retains **43.8%**. Storage genuinely wins, **8.29 GiB → 3.96 GiB** with essentially unchanged perplexity after packing. And then the deployment section: a preliminary Triton GEMV microbenchmark runs **4.6x slower than FP16 cuBLAS**. The authors' conclusion is the sentence the field needs: **"We therefore do not claim that compression alone yields faster inference."**

---

## What it actually measured

This is a measurement paper, not a method paper, so the contribution is the accounting.

**Effective bit accounting.** The "1.58-bit" figure comes from log2(3) and describes an idealized ternary code, not a stored artifact. Real checkpoints carry scales, zero points, rotation matrices and unquantized layers. The honest number here is **1.641 effective bits per quantized linear weight**, and only **81.62% of model parameters were targeted at all**. The remaining 18% sits at higher precision. Anyone comparing "1.58-bit" claims across papers without this accounting is comparing labels.

**Weight-only, activations at 16-bit.** ILA-AMP is omitted, so this is not a fully low-precision pipeline. That is a fair scoping choice and it is stated.

**Capability retention, disaggregated.** The 64.5% → 54.7% average hides the real finding, which is that **the loss is task-dependent in a way an average destroys**. BoolQ, a binary reading-comprehension task, retains 84.6%. ARC-Challenge, multi-step science reasoning, retains 43.8%. Perplexity rises 13.639 → 18.748 on WikiText-2, 24.700 → 31.992 on PTB, 19.831 → 28.966 on C4. **Reasoning-heavy tasks degrade roughly twice as much as recognition-heavy ones**, which is a pattern worth carrying forward.

**Packing is real and separable.** A subsequent packing run preserving the ternary planes and scales reduces reported model size **8.29 GiB → 3.96 GiB with essentially unchanged perplexity.** The storage claim survives. The authors also note a third-party packing attempt was lossy and exclude it from the primary artifact claim, which is the kind of scrupulousness that makes the rest believable.

**Deployment, where it falls over.** The packed artifact **has not been benchmarked end-to-end** for task accuracy or generation throughput, and the one kernel number available is a preliminary Triton GEMV microbenchmark at **4.6x slower than FP16 cuBLAS on one tested shape**.

---

## How this relates to prior wiki pages

**It is the cleanest possible statement of the [pruning and sparsity page](model-pruning-sparsity.md)'s one-line thesis, which is that *sparsity is easy to find and hard to spend.*** That page's entire argument is that headline compression ratios live in patterns the hardware cannot schedule, so the ratio never becomes a speedup. Here the compression is found (a 2.1x storage reduction, verified, with perplexity intact) and demonstrably **cannot be spent**: the only kernel anyone ran is 4.6x slower than the dense baseline it replaced. **This page has been making that argument analytically for a month. This is the first entry that measured it end to end and published the embarrassing number.**

**It is the counterweight to today's two spendable-compression results, and the three should be read together.** [XMerge (09-08)](2026-09-08-xmerge-depth-compression.md) removes whole transformer layers, which preserves a standard serving architecture and lets it quote a break-even at roughly tens of thousands of requests. [ACE (09-08)](2026-09-08-ace-expert-skipping-moe.md) skips MoE expert slots, a granularity where an unrun expert is a matmul block that simply never executes. Both chose granularities the hardware already schedules. **Ternarization chose a granularity that requires a custom kernel to exist, and the custom kernel is not competitive with a decade of cuBLAS tuning.** The lesson is not that ternarization is wrong; it is that **the unit of compression research should be the kernel, not the bit-width**, and a bit-width result without a kernel result is a storage result.

**It complicates the pattern that today's other results support.** The wiki has recorded a run of results in which removing something expensive turns out to be free: [Random Attention (09-04)](2026-09-04-random-attention-kv-eviction.md) deleted the KV cache importance scorer and matched the strongest evictor at 32-43% higher throughput; [Select, Compress, Reinvest (09-05)](2026-09-05-select-compress-reinvest-visual-tokens.md) found a 1990s sparse-approximation algorithm matching purpose-built video frame selectors and, importantly, showed **compression pays nothing on its own** and only earns accuracy when the freed budget is reinvested. **Ternarization is that second finding again, in the harshest form: the freed budget here is storage, and storage was not the binding constraint.** A 4B model was not hard to store. Cutting 4.3 GiB off it bought nothing anyone was short of, while costing 10 accuracy points and a 4.6x kernel regression.

**On [quantization-aware healing (08-26)](2026-08-26-quantization-aware-healing.md)**, which distills from the original pre-compression model to recover post-quantization capability: this result is the strongest case yet for that direction, and specifically for targeting it. The uneven degradation (ARC-Challenge at 43.8%, BoolQ at 84.6%) says healing effort should be **concentrated on multi-step reasoning tasks** rather than distributed uniformly. No healing was applied here, and applying it is the obvious follow-up.

---

## Gaps

- **One model, one size, one family.** Qwen 4B instruction-tuned. Ternarization's economics are entirely different at 70B, where storage and memory bandwidth genuinely bind and where the accuracy floor may be higher because there is more redundancy to spend.
- **One kernel, one shape, preliminary.** The 4.6x figure is a single Triton GEMV microbenchmark. A tuned ternary kernel from a group that specializes in them might be competitive. The paper does not claim otherwise, and the correct reading is "no competitive kernel was demonstrated," not "no competitive kernel can exist."
- **The packed artifact was never benchmarked end to end**, so the headline storage win and the headline accuracy loss were measured on different objects.
- **No healing, no calibration-sensitivity resolution.** Calibration sensitivity is listed as evaluated but no conclusion is quoted in the abstract.
- **Kurate ranked this #16 with ai_rating 3.5/10**, its lowest-rated entry in the top 20, and this week's tournament scores were all at the 1200 TrueSkill default with 0% win rate, so the ranking carries no information. **A 3.5/10 automated rating on the most methodologically honest paper in today's batch is itself a data point about LLM-judged paper ranking**: the rating rewards novelty claims, and this paper's contribution is declining to make one.

---

## Industrial implication

Two things follow. First, **treat any "1.58-bit" or "2-bit" claim as a storage claim until a kernel benchmark appears next to it.** The effective-bit accounting here (1.641 bits over 81.62% of parameters) should be the reporting standard, and most published ultra-low-bit numbers would look worse under it. Second, ultra-low-bit weight-only quantization currently makes sense in exactly one place: **when storage or download size is the binding constraint and latency is not**, such as shipping a model to an edge device over a metered connection, where you pay the 4.6x compute penalty once at low batch. For server inference, where the [memory hierarchy page](../hardware/memory-hierarchy.md) records that roughly 99.66% of a 70B decode step is spent moving bytes, the theory says ternarization should be a large win, and the reason it is not is that nobody has the kernel. **That gap between the roofline prediction and the measured 4.6x regression is the most interesting open number on this page.**

---

## Related pages

- [Model Pruning and Sparsity](model-pruning-sparsity.md)
- [Knowledge Distillation](knowledge-distillation.md)
- [Memory Hierarchy](../hardware/memory-hierarchy.md)
- [XMerge (09-08)](2026-09-08-xmerge-depth-compression.md)
- [ACE (09-08)](2026-09-08-ace-expert-skipping-moe.md)
- [Daily digest 2026-09-08](../daily-digest/2026-09/2026-09-08.md)
