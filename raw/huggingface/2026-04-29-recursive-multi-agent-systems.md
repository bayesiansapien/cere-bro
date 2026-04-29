---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.25917
url: https://huggingface.co/papers/2604.25917
arxiv_url: https://arxiv.org/abs/2604.25917
date: 2026-04-29
upvotes: 123
---

# Recursive Multi-Agent Systems (RecursiveMAS)

Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. RecursiveMAS extends such scaling principle from a single model to multi-agent systems: Can agent collaboration itself be scaled through recursion?

RecursiveMAS casts the entire multi-agent system as a unified latent-space recursive computation. It connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thought generation and cross-agent latent state transfer. Develops an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Evaluated across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. Stanford/UIUC/NVIDIA/MIT.
