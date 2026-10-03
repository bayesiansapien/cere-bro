---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821783+00:00
arxiv_id: 2610.00544
url: https://huggingface.co/papers/2610.00544
arxiv_url: https://arxiv.org/abs/2610.00544
date: 2026-10-02
---

# Memorizon: Training World Models Beyond Their Context Window

Streaming world models should render a place consistently across repeated visits. Directly supervising such revisits requires training samples that capture both visits, often spanning minutes. Yet dense attention over the full span incurs quadratic costs, making long-span supervision expensive. Memorizon breaks this coupling: long spans are needed for supervision, but not for attention, since the two visits can share a forward pass without including every intervening frame. A training sample covers a span of any length but is scored only on its last k chunks. Instead of tokenizing the history before them, each scored chunk retrieves its own top-K latents by camera co-visibility, and the union of these requests forms a shared bank. The bank is bounded by kK, so the sequence stays bounded however long the span; at the shortest span the recipe is exactly conventional training. Adding the bank raises the cost of a step once; beyond that, a longer span costs little, and going from 100 to 400 s adds 12% to the step time. Against a sliding-window baseline, retrieval raises revisit consistency on every split, and a span long enough to reach the first visit of each return adds a further 24% to 30%, at some cost in image quality; beyond that span, more length no longer helps. Filling the bank from another episode lowers revisit correlation by 83%, so the model uses what it retrieves. Project page: https://tingtingliao.github.io/memorizon
