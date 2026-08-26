---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24735
url: https://huggingface.co/papers/2608.24735
arxiv_url: https://arxiv.org/abs/2608.24735
date: 2026-08-26
upvotes: 1
---

# Meta^n: Recursive Self-Improvement through Emergent Depth

Self-improving LLM agents refine answers, not the process that produces those answers. Systems that add a meta-level hold that level fixed, and those that edit themselves must leave part of their own editing machinery untouched to stay stable, capping the meta-depth they realize at roughly two. We present Meta^n, which keeps the meta-operation fixed and recurses on its input instead. That operation, Ω, is applied repeatedly to its own products, reading the traces of the solver stack below together with the code that produced them, then writing the next layer as a strategic pre-process and a library of callable helpers. Because Ω never changes, it cannot destabilize the system, and because its input strictly grows, each layer reasons from a higher vantage than the last. Depth is set by convergence rather than fixed in advance, and an evolutionary archive searches over layer chains. Across two backbones, Meta^n outperforms prior self-improving agents on all eight benchmark families. The sharpest case is ARC-AGI-2, built to resist skill memorization, where it alone scores above zero. Ablations indicate that most of the gain from recursion comes from the conditioning each layer passes to the next, and distinct layer roles emerge with depth although no prompt prescribes them. Code available at https://github.com/minnesotanlp/meta-n
