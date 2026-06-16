---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.06302
url: https://huggingface.co/papers/2606.06302
arxiv_url: https://arxiv.org/abs/2606.06302
date: 2026-06-16
---

# Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving

Multi-turn LLM serving accumulates dialogue history whose Key-Value (KV) cache grows with every turn and every user, quickly exceeding the model weights themselves and making memory -- not compute -- the binding constraint on throughput. Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths across heads, so heterogeneity traps freed memory as page fragmentation, spends up to 25% of prefill time reclaiming scattered pages, and skews GPU workloads that inflate decode latency by up to 1.7x or burn 15-20% of each decode step on re-planning. We observe that this heterogeneity need not be discovered at runtime: head-wise retention follows a two-level structural regularity -- an input-invariant head ranking with narrowly bounded per-head ratios -- that can be calibrated offline from as few as 50 samples. Building on this insight, we present Tangram, a serving framework that statically resolves what prior systems handle dynamically: Budget Reservation fixes each head's post-compression footprint at scheduling time, eliminating page reclamation; Ragged Paging clusters similar-budget heads into independent page tables, turning fragmentation into reclaimable memory; and Ahead-of-Time Load Balancing precomputes balanced GPU partitions with zero runtime planning. Implemented on vLLM, Tangram serves as a drop-in substrate for existing non-uniform compression methods, matching their accuracy while improving end-to-end throughput by up to 2.6x over the full-KV baseline. Our implementation is publicly available at https://github.com/aiha-lab/TANGRAM.
