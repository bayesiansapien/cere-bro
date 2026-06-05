---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.05553
url: https://huggingface.co/papers/2606.05553
arxiv_url: https://arxiv.org/abs/2606.05553
date: 2026-06-05
upvotes: 25
---

# ArcANE: Do Role-Playing Language Agents Stay in Character at the Right Time?

Role-playing language agents (RPLAs) should play characters whose values and behavior evolve as the story progresses, not maintain a fixed persona. Existing benchmarks measure factual recall at a given chapter, not whether responses align with the character's psychological trajectory, especially in scenarios the source text never explores. We introduce ArcANE (Arc-Aware Narrative Evaluation), an automatically constructed benchmark spanning 17 novels and 80 principal characters. A Character Arc segments the narrative into phases along a psychological axis, and each probe poses the same scenario across phases, spanning both situations within the source text and situations beyond it. Across six models and six context modes, conditioning on the Character Arc tops every other context strategy on every model, and the gap is largest on scenarios outside the source text where retrieval has nothing to find. We further fine-tune open-weight models on the same data to obtain ArcANE-8B/32B, which widen the Arc advantage even more on scenarios outside the source text.
