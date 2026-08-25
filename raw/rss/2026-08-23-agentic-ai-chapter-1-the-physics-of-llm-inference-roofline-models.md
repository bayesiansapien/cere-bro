---
source: farmer/rss
feed: agentic-ai
farmed: 2026-08-25T08:53:53.402445+00:00
title: Chapter 1: The Physics of LLM Inference: Roofline Models, Memory Walls & The Prefill-Decode Dichotomy
url: https://kenhuangus.substack.com/p/chapter-1-the-physics-of-llm-inference
published: 2026-08-23
author: Ken Huang
---

# Chapter 1: The Physics of LLM Inference: Roofline Models, Memory Walls & The Prefill-Decode Dichotomy

<h3><em>Arithmetic Intensity, Hardware Ceilings, Iteration-Level Continuous Batching, and the 2026 Production Serving Blueprint</em></h3><p><em>Technical Analysis &amp; Systems Synthesis by <a href="https://distributedapps.ai">DistributedApps.ai</a> | Synthesizing frontier research from DeepSeek, Moonshot AI, Zhipu AI, Alibaba, NVIDIA, and Google DeepMind into production engineering blueprints.</em>
</p><h2>Free Edition: Comprehensive Chapter Roadmap</h2><p>Below is the complete architectural roadmap covered in this chapter:
</p><ol><li><p><strong>Foundational Physics: Breaking the Memory Wall &amp; Arithmetic Intensity:</strong> Microarchitectural roofline modeling across NVIDIA Hopper H100 and Blackwell B200 accelerators.
</p></li><li><p><strong>The Memory Allocation Hierarchy &amp; VRAM Capacity Bottleneck:</strong> Exact memory accounting for model weights, dynamic KV activations, and CUDA workspaces.
</p></li><li><p><strong>The Prefill-Decode Dichotomy &amp; Streaming Multiprocessor Contention:</strong> Why high-arithmetic-intensity prompt prefill and memory-bound autoregressive decoding create execution bubbles when co-located.
</p></li><li><p><strong>Evolution of Batching Systems: Static, Continuous &amp; PagedAttention:</strong> From early static batching waste to Orca iteration-level continuous scheduling and vLLM virtual memory paging.
</p></li><li><p><strong>Production SRE &amp; Cluster Telemetry:</strong> Measuring TTFT, Inter-Token Latency (ITL) P99 SLOs, and memory fragmentation in mission-critical deployments.
</p></li><li><p><strong>Discrete-Event Simulation &amp; Capacity Planning:</strong> Python simulator modeling queue delays, scheduling policies, and multi-tenant goodput.
</p></li></ol><h3>&#9889; Subscriber-Only Deep Dive Beyond This Point</h3><p>To access the complete technical treatise, production code repositories, Triton/CUDA kernels, and infrastructure sizing templates for this chapter, upgrade to a paid subscription today.
</p><p>Special Offer: Get 50% OFF the annual subscription to the 2026 Foundation Model Inference Series using the link below:
</p><p>&#128073; <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">Unlock Full Access with 50% Off Annual Pass</a> &#128072;
</p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-1-the-physics-of-llm-inference">
              Read more
          </a>
      </p>
