---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06361
url: https://huggingface.co/papers/2610.06361
arxiv_url: https://arxiv.org/abs/2610.06361
date: 2026-10-06
---

# Capability-Driven Self-Evolution of Agent Memory

Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions. Existing approaches typically adopt holistic evolution, deriving revision directions from mixed feedback and judging progress by overall performance. This can obscure optimization directions and hide capability-specific gains offset by regressions elsewhere, leaving promising directions underexplored. We introduce capability-driven evolution, which extends search guidance from overall performance to individual capability dimensions, preserving promising revisions and expanding exploration beyond the boundaries of holistic evolution. We propose PrisMem, which uses dependency-aware capability selection to prioritize targets with potential cross-capability benefits and history-guided diagnosis to refine capability specialists. Trace-guided integration compares evaluated programs on paired differential cases, using their behavioral differences to consolidate complementary gains into a unified memory program. Experiments show that PrisMem outperforms the strongest baselines by 10.54 and 7.83 percentage points on BEAM-1M and LongMemEval-M, respectively, demonstrating its effectiveness on million-token histories.
