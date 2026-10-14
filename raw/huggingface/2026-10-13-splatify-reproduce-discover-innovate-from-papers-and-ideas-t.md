---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.09116
url: https://huggingface.co/papers/2610.09116
arxiv_url: https://arxiv.org/abs/2610.09116
date: 2026-10-13
---

# SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code

The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable gsplat-based implementations, where generic paper-to-code methods and frontier models fail. SPLATIFY achieves this through five innovations: (1) A context-free grammar for gsplat over a modular method template with extension points for losses, densification, rendering, and optimization, constraining synthesis so generated code satisfies gsplat's architectural invariants by construction. (2) Architectural elements for faithful reproduction: fork-aware citation recovery retrieving component-level code at function-level granularity, Graph-of-Thought synthesis in topological dependency order, RAG-guided in-context example selection from over 20 verified implementations, and visual feedback combining PSNR-guided regeneration, Gaussian-level structural checks, and VLM-driven patching. (3) Knowledge-driven compositional improvement that autonomously finds weaknesses and composes complementary regularizers, losses, and densification strategies to improve upon original results. (4) Interdisciplinary method discovery where agents retrieve physical priors from outside the 3DGS literature and compose them with rendering knowledge to produce methods for previously unaddressed scene types. (5) SPLATIFY-Bench, an evaluation framework across 30 diverse 3DGS papers. On papers without public code, SPLATIFY matches expert implementations while reducing development time from weeks to minutes, and through compositional discovery further improves PSNR by up to 2.4 dB. We additionally demonstrate novel methods for volumetric nebula rendering and other scientific domains, synthesized entirely by SPLATIFY.
