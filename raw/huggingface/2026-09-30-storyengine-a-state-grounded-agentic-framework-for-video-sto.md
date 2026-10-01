---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33627
url: https://huggingface.co/papers/2609.33627
arxiv_url: https://arxiv.org/abs/2609.33627
date: 2026-09-30
---

# StoryEngine: A State-Grounded Agentic Framework for Video Storytelling

Despite recent progress in agentic multi-shot video generation, producing coherent and consistent long-form stories remains challenging. Existing agentic pipelines typically rely on textual shot plans or previously generated pixels, yet lack an explicit mechanism for propagating the consequences of story events and maintaining the video world state across shots. As a result, missing visual details may be reconstructed inaccurately, while visual drift may propagate across subsequent shots, undermining both narrative coherence and visual consistency. To address these challenges, we propose StoryEngine, a state-grounded agentic framework for video storytelling. StoryEngine establishes a separation between authoritative semantic plans and unreliable visual observations. Specifically, StoryEngine maintains a structured representation of entity placement and story-relevant states, and propagates event-induced changes to define the intended start and end states of each shot. To visually realize these states, StoryEngine constructs canonical references for recurring entities and environments, and compiles state and visual constraints into executable render plans. Meanwhile, to realize these states correctly, a bounded evaluation-guided repair loop further corrects local state inconsistencies. Together, these mechanisms preserve causal story progression and prevent local visual errors from propagating across shots. To comprehensively evaluate long-form storytelling, we construct a benchmark across diverse scenarios and visual styles, with metrics assessing storytelling quality, narrative coherence, and visual consistency. Experimental results demonstrate that StoryEngine consistently outperforms state-of-the-art methods across all evaluation dimensions, validating its effectiveness for coherent and consistent video storytelling.
