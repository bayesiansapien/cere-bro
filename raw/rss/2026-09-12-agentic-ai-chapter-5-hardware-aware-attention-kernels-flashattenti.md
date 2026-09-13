---
source: farmer/rss
feed: agentic-ai
farmed: 2026-09-13T07:27:06.541918+00:00
title: Chapter 5: Hardware-Aware Attention Kernels: FlashAttention-3, FlashDecoding & TPU Pallas
url: https://kenhuangus.substack.com/p/chapter-5-hardware-aware-attention
published: 2026-09-12
author: Ken Huang
---

# Chapter 5: Hardware-Aware Attention Kernels: FlashAttention-3, FlashDecoding & TPU Pallas

<h3><em>SRAM Tiling, Asynchronous Tensor Memory Accelerator (TMA) Pipelines, Warp Specialization, Split-K Sequences, and Custom Pallas DMA Kernels</em></h3><p><em>Technical Analysis &amp; Systems Synthesis by <a href="https://distributedapps.ai">DistributedApps.ai</a> | Synthesizing frontier research from DeepSeek, Moonshot AI, Zhipu AI, Alibaba, NVIDIA, and Google DeepMind into production engineering blueprints.</em>
</p><p>This is Chapter 5 of the 10-part series The Physics &amp; Engineering of Frontier LLM Inference. I announced the full curriculum, including every later chapter, in <a href="https://kenhuangus.substack.com/p/announcing-the-10-part-series-the">Announcing the 10-Part Substack Series</a>.</p><p>Read the earlier parts first: <a href="https://kenhuangus.substack.com/p/the-physics-of-llm-inference-memory">Chapter 1: The Physics of LLM Inference</a>, <a href="https://kenhuangus.substack.com/p/chapter-2-the-kv-cache-frontier-hybrid">Chapter 2: The KV Cache Frontier</a>, <a href="https://kenhuangus.substack.com/p/chapter-3-next-gen-speculative-decoding">Chapter 3: Next-Gen Speculative Decoding</a>, <a href="https://kenhuangus.substack.com/p/chapter-4-extreme-quantization-and">Chapter 4: Extreme Quantization</a>.</p><h2>Executive Summary &amp; Free Preview</h2><h3>Squeezing Maximum MFU from Accelerator SRAM and Tensor Cores</h3><p>Modern deep learning accelerators possess terrifying theoretical compute capacity. An NVIDIA Hopper H100 SXM5 GPU delivers 989.5 TFLOPS of dense FP16/BF16 matrix arithmetic and nearly 2,000 TFLOPS of FP8 Tensor Core throughput. The Blackwell B200 raises this ceiling to 2.25 PFLOPS of FP16 and 4.5 PFLOPS of FP8 compute. Yet, if you execute textbook scaled dot-product attention in PyTorch on an H100 across a 16,000-token sequence, your observed hardware utilization will rarely exceed 15% Model FLOPs Utilization (MFU)&#8212;wasting over 800 TFLOPS of raw compute capacity per GPU.
</p><p>Why does this compute collapse occur?
</p><p>The answer lies in the physics of the memory hierarchy. Attention is not bounded by how fast Tensor Cores can execute matrix multiply-accumulate operations; it is bounded by the speed at which operands can be moved across the silicon. On an H100 GPU, the High-Bandwidth Memory (HBM3) bus delivers 3.35 TB/s of bandwidth with a memory latency of 400 to 800 clock cycles. In stark contrast, the on-chip Static Random-Access Memory (SRAM)&#8212;distributed across 132 Streaming Multiprocessors (SMs) as 228 KB of Shared Memory and L1 cache per SM&#8212;delivers an aggregate bandwidth exceeding 33 TB/s with a latency of just 15 to 30 clock cycles.
</p><p>When standard attention materializes the intermediate N &#215; N attention score matrix in global HBM, it forces the GPU to transfer O(N&#178;) bytes over the narrow 3.35 TB/s bus. Because the arithmetic intensity of memory-bound elementwise operators (softmax scaling, masking, exponentiation, and normalization) is strictly below 1.0 FLOP/byte&#8212;against an H100 hardware saturation roofline of 295.4 FLOPs/byte&#8212;the execution pipeline stalls completely, starving the Tensor Cores.
</p><p>Unlocking 70% to 80%+ MFU across frontier LLM architectures requires complete algorithm-hardware co-design: restructuring attention algorithms so that intermediate matrices never leave ultra-fast on-chip SRAM, and orchestrating asynchronous hardware engines to overlap memory movement directly with Tensor Core arithmetic.
</p><pre><code>========================================================================================
                          THE 2026 HARDWARE-AWARE ATTENTION SUITE
========================================================================================

   1. ONLINE SOFTMAX TILING (Milakov-Gimelshein)
      Eliminates O(N&#178;) HBM materialization. Computes exact running row-maxima and 
      normalizers in a single pass entirely inside on-chip SRAM / VMEM registers.
      IO Complexity compressed from O(N&#178;) down to O(N&#178; d&#178; M&#8315;&#185; + Nd).

   2. FLASHATTENTION-3 (Hopper TMA &amp; Warp Specialization)
      Exploits Hopper H100 / Blackwell B200 Tensor Memory Accelerators (TMA) for 
      zero-register global-to-shared transfers. Decouples Producer warps from Consumer 
      warpgroups. Leverages asynchronous WGMMA and FP8 block scaling for 75-80% MFU.

   3. FLASHDECODING &amp; FLASHDECODING++ (Split-K Sequence Parallelism)
      Solves the single-query (Q_len = 1) decode occupancy collapse. Partitions the 
      KV cache across sequence splits (Split-K), saturating all 132 SMs and reducing 
      128k decode latency from 27.2 ms to 3.40 ms (8.0x speedup).

   4. GOOGLE TPU PALLAS KERNELS (TPU v5p &amp; Trillium v6e)
      Bypasses high-level XLA graph compilers with imperative JAX Pallas kernels. 
      Controls 128&#215;128 systolic Matrix Multiply Units (MXUs) and Vector Processing Units 
      (VPUs) via double-buffered DMA BlockSpecs and ping-pong VMEM memory spaces.
========================================================================================
</code></pre><h3>What We Cover in the Paid chapter</h3><p>In this exhaustive 6,300+ word series, we tear open the silicon, mathematics, and low-level kernel code powering modern attention acceleration across NVIDIA Hopper/Blackwell GPUs and Google Cloud TPUs:
</p><ol><li><p><strong>Memory Hierarchy Physics &amp; Attention IO Complexity:</strong> Mathematical derivation of operational intensity, hardware saturation thresholds, and exact HBM traffic equations.
</p></li><li><p><strong>Milakov-Gimelshein Online Normalization:</strong> Inductive mathematical proof of single-pass running softmax rescaling, register accumulator recurrence relations, and backward-pass activation recomputation.
</p></li><li><p><strong>FlashAttention-3 Microarchitecture on Hopper:</strong> Deep dive into hardware TMA descriptors (<code>cp.async.bulk.tensor</code>), Producer-Consumer Warp Specialization, asynchronous WGMMA matrix multiply instructions, interleaved GEMM overlapping, and FP8 E4M3 dynamic tile scaling. Includes a production C++/CUDA/PTX kernel listing.
</p></li><li><p><strong>FlashDecoding &amp; FlashDecoding++:</strong> The mechanics of sequence-parallel Split-K decomposition, partial log-sum-exp workspace management, hierarchical reduction trees, and asynchronous softmax estimation. Includes a production OpenAI Triton kernel listing.
</p></li><li><p><strong>Google TPU Pallas Optimization:</strong> DeepMind's Pallas framework in JAX, 128&#215;128 systolic MXU tile alignment, double-buffered Direct Memory Access (DMA) pipelines, and VMEM scratchpad management on TPU v5p and Trillium (v6e). Includes a complete JAX/Pallas production kernel listing.
</p></li><li><p><strong>Empirical Benchmarks &amp; Decision Matrix:</strong> Real-world throughput (TFLOPS), MFU (%), and latency across H100, H200, B200, TPU v5p, and Trillium across context lengths from 4k to 1,048,576 tokens (1M context), along with an engineering selection flowchart.
</p></li><li><p><strong>2026+ Frontiers:</strong> Microscaling data formats (MXFP4, NVFP4), State-Space hybrid kernel fusion (Mamba-2 / SSD + Attention), and hardware-assisted sparse verification engines.
</p></li><li><p><strong>Academic Citations:</strong> Complete primary lab references and system papers.
</p></li></ol><h2>Free Edition: Comprehensive Chapter Roadmap</h2><p>Below is the complete architectural roadmap covered in this chapter:
</p><ol><li><p><strong>The Arithmetic Intensity Crisis of Scaled Dot-Product Attention:</strong> SRAM block tiling and the Milakov-Gimelshein online softmax normalization theorem.
</p></li><li><p><strong>FlashAttention-3 Microarchitecture:</strong> Tensor Memory Accelerator (TMA) asynchronous global memory loads and hardware warp specialization on Hopper/Blackwell.
</p></li><li><p><strong>FlashDecoding &amp; FlashDecoding++ Split-K Reduction Trees:</strong> Partitioning KV sequences across thread blocks to restore GPU occupancy during autoregressive decoding.
</p></li><li><p><strong>Google TPU v5p &amp; Trillium v6e Pallas Kernel Pipelines:</strong> Matrix Multiply Units (MXUs), Vector Memory (VMEM) double-buffering, and asynchronous DMA execution.
</p></li><li><p><strong>Attention Kernel Benchmark Suite:</strong> Multi-accelerator comparison measuring Model FLOPs Utilization (MFU), latency, and context scaling.
</p></li></ol><h3>&#9889; Subscriber-Only Deep Dive Beyond This Point</h3><p>To access the complete technical treatise, production code repositories, Triton/CUDA kernels, and infrastructure sizing templates for this chapter, upgrade to a paid subscription today.
</p><p>Special Offer: Get 50% OFF the annual subscription to the 2026 Foundation Model Inference Series using the link below:
</p><p>&#128073; <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">Unlock Full Access with 50% Off Annual Pass</a> &#128072;
</p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-5-hardware-aware-attention">
              Read more
          </a>
      </p>
