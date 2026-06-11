# The Origins of DeepSeek

**Channel:** ColdFusion  
**Published:** 2026-06-09  
**Source:** https://www.youtube.com/watch?v=dUqfSHOUgP0  

## TL;DR
DeepSeek, founded by High-Flyer Capital Management chair Liang Wenfeng, has emerged as a leader in AI efficiency by prioritizing architectural optimizations over raw compute power. Born from a hedge fund's need for high-performance computing, DeepSeek famously bypassed GPU sanctions and high costs through innovations like Multi-Head Latent Attention (MLA) and the "Engram" technique.

## Key Takeaways
- **Hedge Fund Origins:** DeepSeek was spun out of High-Flyer Capital Management, leveraging quantitative trading expertise for AGI development.
- **Architectural Efficiency:** DeepSeek-V3 (671B parameters) achieves frontier performance using only 2.8 million H800 GPU hours, a fraction of the compute used by Llama 3 or GPT-4.
- **MLA Innovation:** Multi-Head Latent Attention compresses Key-Value (KV) cache, significantly reducing memory usage during inference.
- **GPU Resilience:** Liang Wenfeng pivoted to algorithmic efficiency (e.g., auxiliary-loss-free load balancing) to overcome US export restrictions on high-end NVIDIA GPUs.

## Architecture & Optimization Mechanics
For a Senior AI Researcher, DeepSeek's primary value lies in its **Sparse Mixture-of-Experts (MoE)** implementation. 
- **DeepSeek-MoE:** Utilizes a "Fine-Grained Expert" strategy, where experts are smaller and more numerous, allowing for more precise activation and reducing "knowledge overlap" between experts.
- **Engram Technique:** A 2026 proposal by Wenfeng to use "conditional memory" that bypasses standard GPU VRAM limitations, allowing for parameter counts to scale even when hardware is bottlenecked.
- **Training Stability:** Their auxiliary-loss-free load balancing is a critical breakthrough, ensuring all experts are utilized without the performance degradation typically caused by traditional loss-based balancing.

## Grounded Context (Web Enrichment)
As of June 2026, DeepSeek has shifted the industry focus from "Compute is King" to "Architecture is King." DeepSeek-V3's release in late 2024 proved that a model could match or exceed the performance of much larger, more expensive models through extreme optimization. Specifically, their **Multi-Head Latent Attention (MLA)** has been widely adopted in the 2026 "Small Model" movement to keep KV caches manageable for edge inference.

Liang Wenfeng’s recent "Engram" proposal (May 2026) suggests a shift toward models that can dynamically swap parameters from system RAM to VRAM in real-time—a necessity given the ongoing scarcity of H100/H200 equivalents in certain regions.

## Real-World Application / Actionable Step
*Amit, focus on the following for your MoE and routing research:*
- **Implement MLA:** Evaluate Multi-Head Latent Attention in your current inference pipelines to reduce KV cache pressure.
- **Fine-Grained Experts:** Investigate DeepSeek’s MoE expert splitting logic. Instead of 8 large experts, test 64 smaller experts with better routing to minimize activation costs.
- **Load Balancing:** Move away from auxiliary loss for expert balancing; look into DeepSeek's bias-based routing to ensure high utilization without sacrificing quality.
