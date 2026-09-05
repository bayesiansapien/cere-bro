---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2609.03820
url: https://huggingface.co/papers/2609.03820
arxiv_url: https://arxiv.org/abs/2609.03820
date: 2026-09-05
---

# Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation in Long-Video MLLMs

Long-video language models cannot look at every frame: an hour sampled once per second is 3,600 images, and a system keeps only a small fixed slice of that pool. Which frames survive that slice is usually treated as a preprocessing detail; we test whether it should be. Published selectors make the comparison hard because they change the frame scorer, the prompt boundary, the resolution policy, and the answering model all at once. We hold each fixed and vary one decision at a time: selection, spatial compression, and reinvestment of the savings, across six training-free selection rules, three long-video benchmarks, and two answering models. Selection is the largest single lever: on LongVideoBench's hour-long bin, eight query-selected frames beat sixteen uniformly spaced ones by 6.9 points, and Orthogonal Matching Pursuit, an unmodified decades-old sparse-approximation algorithm, matches or comes within a point of every purpose-built selector we compare it against, across all three benchmarks. Compression is close to free: halving each frame's spatial budget at fixed timestamps costs at most 0.44 points. Reinvestment is where that budget turns back into accuracy: spending the freed tokens on twice as many compressed frames, at a measured cost no higher than the original eight, returns a further two to three points; compression only pays off once its savings are spent this way. Along the way, an implementation bug in our own AKS baseline and a 0.07 to 3.74 point gap between two harnesses running the same published rules at the same budget show why these comparisons need to happen inside one controlled harness rather than across papers.
