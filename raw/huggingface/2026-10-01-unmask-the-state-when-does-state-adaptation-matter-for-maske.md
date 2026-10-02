---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.346005+05:30
arxiv_id: 2609.33355
url: https://huggingface.co/papers/2609.33355
arxiv_url: https://arxiv.org/abs/2609.33355
date: 2026-10-01
---

# Unmask the State: When Does State Adaptation Matter for Masked Diffusion Language Models

Masked diffusion language models (MDMs) admit flexible generation orders, making the unmasking strategy an inference decision. Existing methods vary in how they prioritize positions, control parallelism, restrict selection regions, revise predictions, or plan future denoising, yet it remains unclear when these choices should change during generation. We study this question through strategy reversals, where an alternative action becomes preferable to a fixed choice. We organize MDM inference into five axes--score, cardinality, region, commitment, and planning--and define adaptation opportunity as the one-step utility advantage of the best candidate action over a validation-selected fixed action. This view shows that adaptation value depends on both the frequency and magnitude of such reversals. Across three MDMs and ten tasks, adaptation opportunities are highly heterogeneous, with some regimes exhibiting concentrated and predictable one-step gains. This motivates selective adaptation: lightweight detectors calibrated on validation prompts identify high-opportunity states, capturing, for example, 56.9 percent of the candidate-set oracle opportunity by adapting only the top 10 percent of states on LLaDA-8B constrained JSON filling. Our transition-level results suggest that state adaptation is most useful when applied selectively rather than uniformly.
