# OSP-Next: Sparse Sequence Parallelism, HiF8, and RL for Efficient Video Generation

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28691](https://arxiv.org/abs/2605.28691) · [HuggingFace](https://huggingface.co/papers/2605.28691) · [raw](../../raw/huggingface/2026-05-28-osp-next-efficient-high-quality-video-generation-with-sparse.md)

## TL;DR

OSP-Next is a text-to-video diffusion transformer that stacks four orthogonal efficiency techniques in one model: a hybrid full-plus-sparse attention pattern (Skiparse-2D) that stays compatible with FlashAttention kernels; Sparse Sequence Parallelism (SSP), a new partition strategy that cuts cross-rank communication by 75% relative to Ulysses sequence parallelism; HiF8 quantization for stable joint 8-bit + sparse fine-tuning; and Mix-GRPO post-training to recover quality lost to sparsification. Net result: a VBench score of 83.73% beating the Wan2.1 baseline, with 1.64x single-GPU and 1.52x eight-GPU speedup on H200, and 1.69x to 2.27x on Ascend 950PR with only a 0.4% VBench drop in the HiF8 variant.

```
OSP-Next stack:

   ┌──────────────────────────────────────────────────────┐
   │  Hybrid attention: Full | Skiparse-2D                │  ← native FlashAttention compatible
   ├──────────────────────────────────────────────────────┤
   │  SSP partitioning  (75% less All-to-All than Ulysses) │  ← sparse-aware parallelism
   ├──────────────────────────────────────────────────────┤
   │  HiF8 quantization  (stable 8-bit + sparse joint FT) │  ← 0.4% VBench drop, 2.27x speed
   ├──────────────────────────────────────────────────────┤
   │  Mix-GRPO post-training (RL recovers sparsity loss)  │
   └──────────────────────────────────────────────────────┘
```

## Key findings

- VBench 83.73% beats Wan2.1 baseline.
- 1.64x single-GPU and 1.52x eight-GPU speedup at 5s 720p/768p on H200 over the dense baseline.
- SSP reduces sparse-attention communication volume 75% vs Ulysses SP via single All-to-All pattern switch.
- HiF8 variant gets to 1.69x/2.27x speedups on Ascend 950PR at only 0.4% VBench drop, demonstrating cross-hardware portability.
- Mix-GRPO is the post-training step that recovers quality lost when sparsifying a dense-trained model.

## How this fits prior wiki state

OSP-Next is the most aggressive stack-everything paper in the diffusion-transformer efficiency line. The Skiparse-2D pattern continues the wiki's growing list of fixed-pattern sparse attentions that stay FlashAttention-compatible. The HiF8 result is a useful data point for the broader "quantization-aware sparse fine-tuning" thread alongside [[2026-05-21-mix-quant-phase-aware-quantization]] and [[2026-05-25-bitcpm-cann-158bit-ascend-npu]]. SSP's communication-reduction trick is parallel-aware design rather than a new attention algorithm, which is unusual: most sparse-attention papers stop at the kernel and leave the multi-GPU side to the existing libraries. Treating partitioning as part of the sparse design is a useful frame and connects to longlive-2 (NVFP4 parallel infrastructure for long video).

## Related pages

- [[2026-05-19-longlive-2-nvfp4-parallel-infrastructure-long-video]] — parallel video infrastructure
- [[2026-05-21-mix-quant-phase-aware-quantization]] — quantization phase awareness
- [[2026-05-22-rtpurbo-full-attention-sparse-transfer]] — sparse-from-dense fine-tuning
- [[2026-05-25-bitcpm-cann-158bit-ascend-npu]] — non-NVIDIA quantization on Ascend NPU
- [[gpu-kernels]] — concept page

## Research angle

The 0.4% VBench gap for HiF8 on Ascend is the most interesting result: it implies that an 8-bit sparse-attention diffusion model trained with RL post-training is genuinely deployable on non-NVIDIA hardware at near-parity quality. That weakens the CUDA-only frame for video-generation production. The SSP-vs-Ulysses comparison should generalize to language-side long-context training where Ulysses is the default; an LLM-side SSP variant is the obvious next paper.
