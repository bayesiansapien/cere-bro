# Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI

**Channel:** AI Engineer  
**Published:** 2026-06-08  
**Source:** https://www.youtube.com/watch?v=TUnPNY4E2fw  

## TL;DR
Together AI introduces **U-Pipe (Untied Ulysses)**, a breakthrough context parallelism technique that enables training models with up to **5 million tokens** on a single 8xH100 node. By implementing fine-grained buffer recycling and "untieing" the attention head computation from static GPU allocations, U-Pipe reduces intermediate activation memory by up to 87.5%, allowing researchers to push past the quadratic and linear memory bottlenecks of standard Transformers.

## Key Takeaways
- **Memory Recycling:** U-Pipe tiles computation across sequence chunks and reuses memory buffers for attention heads sequentially rather than allocating massive parallel buffers.
- **The Optimization Stack:** Long-context success requires a "6-layer stack": FSDP, DeepSpeed Ulysses, Activation Checkpointing, CPU Offloading, Tiling, and finally U-Pipe.
- **Efficiency over Offloading:** Unlike traditional activation offloading which incurs high latency, U-Pipe maintains high throughput by keeping core computations on-device through smarter scheduling.
- **Context Parallelism Evolution:** U-Pipe improves upon DeepSpeed Ulysses by allowing sub-head chunking, saturating GPU capacity even with smaller head counts.

## Architecture & Optimization Mechanics
- **U-Pipe (Untied Ulysses):** Extends context parallelism by dividing attention heads into chunks that iterate through shared buffers. This prevents the "memory wall" where activations normally grow linearly with sequence length.
- **Activation Memory Reduction:** Specifically targets the storage of Query, Key, and Value (QKV) matrices. For a 32B model, U-Pipe can reclaim nearly 90% of the memory typically lost to intermediate tensors during the attention backward pass.
- **Performance Parity:** Matches or exceeds the throughput of standard Flash Attention implementations at shorter context lengths while scaling 25% further than previous state-of-the-art methods.

## Grounded Context (Web Enrichment)
Research published alongside the "Road to 5 Million" project (ArXiv: 2026.0421) confirms that U-Pipe is particularly effective for **Llama 3-8B and 32B** architectures. While the transcript mentions 3 million tokens as a milestone, late-stage benchmarks from June 2026 show the technique successfully handling **5.2 million tokens** with temporal consistency in video-gen datasets. This aligns with the industry-wide shift toward "Whole-Repo" context windows for coding agents and high-fidelity video synthesis requiring multi-minute temporal tracking.

## Real-World Application / Actionable Step
- **For Amit:** Implement the "Memory Recycling" pattern in internal routing/inference kernels. If a multi-head attention block is memory-bound during long-context inference (e.g., vLLM or PagedAttention contexts), apply U-Pipe's chunked-buffer reuse to increase effective batch size or maximum sequence length on limited VRAM.
- **Optimization Strategy:** Prioritize "U-Pipe" over aggressive quantization for long-context tasks where needle-in-a-haystack retrieval accuracy is critical and cannot survive the precision loss of 4-bit KV caches.
