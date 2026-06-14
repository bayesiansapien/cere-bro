# Build Small with Modal

**Channel:** Hugging Face  
**Published:** 2026-06-12  
**Source:** https://www.youtube.com/watch?v=8Oz64pGwRk4  

## TL;DR
Modal's Adam Aam discusses the platform's role as the high-performance infrastructure layer for the "Build Small" hackathon, emphasizing serverless GPU optimizations like memory snapshotting and sub-second cold starts. The session covers Modal's four core primitives—Inference, Training, Batch, and Sandboxing—and provides a roadmap for developers to deploy native multimodal models like Gemma 4 within the hackathon's 32B parameter constraint.

## Key Takeaways
- **Serverless GPU Efficiency:** Modal's architecture is built for AI-native workloads, using a custom distributed file system and container snapshotting to achieve sub-second cold starts, even for large model weights.
- **The "Build Small" Constraint:** Projects are limited to ≤ 32B parameters, favoring high-density models like Gemma 4 (12B native multimodal) and Nemotron-3.
- **Agentic Sandboxing:** Sandboxes are treated as "burstable" first-class primitives, allowing for low-latency RL rollouts and stateful agent environments without over-provisioning memory.
- **Compute as Code:** Modal replaces YAML/Docker configuration with pure Python decorators, shipping the local environment state directly to remote GPUs.
- **Inference Specialization:** Support for vLLM and SGLang ensures OpenAI-compatible endpoints can be spun up in minutes.

## Architecture & Optimization Mechanics
- **Memory Snapshotting:** By snapshotting GPU memory states, Modal bypasses the traditional bottleneck of loading weights from disk to VRAM, which is critical for scaling "councils of agents" dynamically.
- **Burstable Sandboxes:** Unlike standard containers, Modal sandboxes allow for memory "bursting" above reservations. For Amit's work in MoE and routing, this means the router can reside in a low-resource state and burst only during high-compute token generation.
- **Distributed File System:** Optimized for the high-concurrency read patterns of model weights, reducing the overhead of shared volumes across large clusters.

## Grounded Context (Web Enrichment)
As of June 13, 2026, the "Build Small" hackathon is in its final 48 hours. The release of **Gemma 4 12B** on June 3, 2026, has shifted the meta toward **encoder-free multimodal** apps, which Modal handles natively through its updated vLLM integration. While the **RTX 5080 (Blackwell)** is the consumer standard for these models, Modal's $250 credits provide access to **H100/A100** clusters and the **RTX 5880 Ada (48GB)**, which is essential for participants attempting LoRA fine-tuning on the 31B Dense Gemma variants.

Recent web data confirms that Modal's "Compute as Code" approach has become the industry standard for **Agentic Workflows**, particularly for companies like Ramp and Lovable, which use Modal's sandboxes to execute untrusted code in real-time. The hackathon's 32B limit reflects a broader 2026 trend: the "death of the giant model" in favor of orchestrated small models that outperform GPT-4 class models through specialized fine-tuning and better routing.

## Real-World Application / Actionable Step
**Optimization Strategy:** Amit should leverage Modal’s **memory snapshotting** for his MoE research. Instead of keeping a full MoE model hot in memory, he can use Modal to snapshot individual experts and "cold-boot" them sub-second as the router calls them. 
**Protocol:**
1.  **Redeem Credits:** Use the `modal.com/credits` link for the $250 H100/A100 pool.
2.  **Benchmark Routing:** Use the **LLM Almanac** (`modal.com/lmalmanac`) to select the optimal GPU/engine (SGLang vs. vLLM) for specific Gemma 4 12B request shapes.
3.  **Deploy MoE:** Implement a "bursty router" in a Modal Sandbox to handle dynamic expert selection without paying for idle VRAM.
