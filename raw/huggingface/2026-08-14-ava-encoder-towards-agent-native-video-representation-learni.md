---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.12313
url: https://huggingface.co/papers/2608.12313
arxiv_url: https://arxiv.org/abs/2608.12313
date: 2026-08-14
---

# AVA-Encoder: Towards Agent-Native Video Representation Learning

Creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos. A key challenge is the absence of a structured video representation that is both faithful to film content and directly usable for agentic reasoning and manipulation. To address the challenge, we propose the Agentic Video Auto-Encoder (AVA-Encoder), a framework for learning agent-native video representations via agentic auto-encoding.
  AVA-Encoder transforms a video into a knowledge graph (KG) representation and then reconstructs it back into video. Its hierarchy and state nodes store structured text, while a linked asset layer holds generated images, audio, and video. Typed edges preserve the relations between these text descriptions and assets in a form that agents can easily understand, query, and edit. The video reconstruction differences drive a textual-gradient optimization framework, which expresses evaluation feedback as natural-language update directions for Data-Independent Encoding Policy Pseudo-Training in the outer loop and optional Data-Dependent KG Representation Refinement in the test-time inner loop.
  Extensive experiments show that AVA-Encoder improves by 20.7 percentage points over the strongest external baseline. In the controlled policy-only setting, its pseudo-trained shot-level Agentic Video Encoder policy also outperforms a carefully human-tuned policy while using 74.3% fewer system-prompt tokens. We release the complete AVA-Encoder framework, a reliable agentic video reconstruction benchmark, and the first dataset of high-quality film KG representations.
