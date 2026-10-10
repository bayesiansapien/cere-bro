# SparseDecoding: calibrate pruning on what the model actually decodes (2026-10-10)

**Sources:** HuggingFace Daily Papers 2026-10-09: SparseDecoding, Westlake/Ant Group ([arXiv 2610.12327](https://arxiv.org/abs/2610.12327), [raw](../../raw/huggingface/2026-10-09-sparsedecoding-decoding-aware-pruning-for-accurate-and-effic.md)); full HTML paper read. No alphaxiv overview yet.

**TL;DR.** Decoding is memory-bound: each new token streams every weight through memory, so fewer nonzero weights means faster tokens. Training-free pruners like SparseGPT and Wanda pick which weights to zero using a Hessian built from calibration text (usually C4), fed with the true next token at every position. But at serving time the model reads its *own* generated tokens. SparseDecoding fixes the mismatch: the dense model generates continuations of task prompts, and only the **decode-position** activations (prefill dropped) feed the unchanged SparseGPT objective. It also ships a Triton **N:M sparse matrix-vector kernel**, because existing 2:4 sparse kernels (cuSPARSELt) actually run decode at 0.85-0.87x of dense speed. Result: big quality recovery at 2:4 (Qwen3-14B WritingBench 1.85 to 4.18; dense 5.97) and 1.34-1.48x faster batch-1 decode on A100.

<div class="dg-title">Prune with the activations you will actually see</div>
<div class="dg-sub">Calibration moves from fixed text to the model's own decode steps; the kernel moves from SpMM to SpMV.</div>

```mermaid
flowchart LR
  P["Task prompts<br/><small>writing, code</small>"] --> D["Dense model<br/><small>generates continuations</small>"]
  D --> A["Decode activations<br/><small>prefill dropped</small>"]
  A --> H["SparseGPT solve<br/><small>same objective, new Hessian</small>"]
  H --> W["N:M weights<br/><small>2:4 to 16:32</small>"]
  W --> K["SpMV kernel<br/><small>bitmask, fixed-step loop</small>"]
  K --> O["Decode<br/><small>1.34-1.48x, batch 1</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class P input
  class D,H core
  class A,K loop
  class W,O exit
```

<div class="dg-legend">Blue is the prompt set, purple the dense model and solver, amber the two new pieces (decode-only calibration and the kernel), green the output.</div>

## Key points

- **Why the gap matters.** The dense-vs-pruned activation gap grows fast in the first decode steps; every layer reaches 90% of its plateau by step 12, then stays flat. Calibrating on teacher-forced text misses that drift. A theory check finds decode-time calibration has the smaller worst-case discrepancy in at least 87% of prunable modules.
- **Kernel design.** One bit per input column, packed into 32-bit words: at 50% sparsity that is 2 bits of metadata per nonzero (16x less than int32 indices). With 50% N:M every aligned word has exactly 16 set bits, so the inner loop has a compile-time fixed length and is fully unrolled; each step takes the lowest set bit as the column index. All N:M patterns run at the same speed because they move the same bytes.
- **Accuracy.** ClassEval Pass@1 at 2:4 for Qwen3-32B goes 9% to 24% (dense 34%). Qwen3-32B 50% unstructured reaches 6.09 vs 6.48 dense on WritingBench. Gains on Llama at 2:4 are small (1.34 to 1.52 on 8B). Self-generated calibration narrowly beats using a bigger sibling's generations.
- **Speed.** Llama-3.1-8B 96.3 to ~136.6 tok/s (1.42x); Llama-3.3-70B 1.38-1.48x; Qwen3-32B 1.45x. A100, GPT-Fast, context 512, batch 1.

## How it relates to the wiki

- **Second "prune for decode" paper in three days.** [SlimWise (10-08)](2026-10-08-slimwise-phase-decoupled-expert-pruning.md) kept the full MoE for prefill and a 50%-expert-pruned MoE for decode (1.81x decode throughput). SparseDecoding does the same phase split for dense weights at the calibration level. The field is treating prefill and decode as two different models to compress, a pattern that started with disaggregated serving and is now reaching weight compression.
- **Fills the wall-clock gap** this page has flagged for weight sparsity since 2025: N:M sparsity saved memory but rarely sped up batch-1 decode because Sparse Tensor Cores target matrix-matrix work. A decode-shaped SpMV kernel is the missing piece. See [Model pruning and sparsity](model-pruning-sparsity.md).
- **Echoes the OPD "train on your own samples" lesson** ([OPD skills not knowledge, 10-10](2026-10-10-opd-skills-not-knowledge.md)): calibration, like distillation, works better on the student's own distribution.

## Gaps

- A100, batch 1, context 512 only. At larger batches decode becomes compute-bound and SpMV gains shrink.
- 2:4 quality is still far from dense; 50% unstructured is the usable setting, and it lacks a fast kernel here.
- Needs task-specific prompts; calibration on writing may not transfer to code or agents. Two benchmarks, judged by DeepSeek-V4-Flash.

## Research angle

Decode-only calibration should compose with quantization (GPTQ uses the same Hessian), so a joint decode-calibrated W4 plus 2:4 recipe is an obvious next test. The deeper question: if the calibration set should be the model's own generations, should it also be *agent* generations (tool calls, long contexts) for models deployed as agents?

## Related

[Model pruning and sparsity](model-pruning-sparsity.md) · [Quantization](quantization.md) · [GPU kernels](../hardware/gpu-kernels.md)
