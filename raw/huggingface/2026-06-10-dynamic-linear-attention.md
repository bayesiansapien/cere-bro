---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10650
url: https://huggingface.co/papers/2606.10650
arxiv_url: https://arxiv.org/abs/2606.10650
date: 2026-06-10
---

# Dynamic Linear Attention

The scalability of Large Language Models (LLMs) to long contexts is fundamentally constrained by the quadratic complexity of standard attention, motivating the adoption of linear attention mechanisms with sub-quadratic cost. To improve representation capacity under long contexts, recent approaches organize memory in a multi-state manner. However, existing multi-state linear attention methods rely on fixed state merging policies that cannot adapt to dynamically varying token importance, irreversibly obscuring critical tokens and causing severe error accumulation over long sequences. To address this limitation, we propose DLA, a dynamic memory modeling framework for multi-state linear attention. DLA introduces (i) Information-Aware Dynamic State Merging, which adaptively determines state boundaries based on token-level information variation, preserving high-resolution representations around semantic transitions while aggressively summarizing stable regions, and (ii) Capacity-Bounded Memory Modeling, which maintains a fixed-size, chronologically ordered state cache by selectively merging adjacent low-information states to control memory growth with minimal information loss. We pre-train DLA on two different linear attention models and evaluate on 16 datasets across three categories. Experimental results demonstrate the superiority of DLA over state-of-the-art.
