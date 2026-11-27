---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.904872+00:00
arxiv_id: 2611.34347
url: https://huggingface.co/papers/2611.34347
arxiv_url: https://arxiv.org/abs/2611.34347
date: 2026-11-26
---

# AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos

Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that formulates social embodied intelligence as a time-anchored chain of Attention, Intention, Reaction, and Interaction (A-I-R-I). AIRIS contains 8,000 expert-curated questions grounded in 357 egocentric clips across 11 context categories and 36 capability dimensions. At each query, models receive only the observation prefix available at that time; decision-aware metrics reward calibrated waiting and complete reactions while penalizing premature commitment. Evaluating 45 proprietary and open-source general-purpose, embodied, streaming-video, and omni-modal models reveals fragmented and temporally miscalibrated competence. General-purpose VLMs excel at passive cue grounding and intent recognition, whereas embodied specialists lead on isolated reaction sub-decisions; yet across all families, models frequently guess intents before sufficient evidence emerges and fail to jointly align intervention timing, action domain, and concrete execution within the same episode. AIRIS thus provides a diagnostic foundation for bridging the gap between passive social perception and reliable embodied interaction.
