---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33169
url: https://huggingface.co/papers/2610.33169
arxiv_url: https://arxiv.org/abs/2610.33169
date: 2026-10-27
---

# World-in-Context: Interactive Video World Modeling with In-Context Conditioning

Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion. Existing methods typically leave view modes implicit in text captions, conflate action with camera motion, and inject controls through fragmented architectural pathways that capture interdependencies only indirectly. In this work, we present World-in-Context, an interactive world modeling framework powered by In-Context Conditioning (ICC). Rather than relying on specialized conditioning pathways, World-in-Context unifies view, action, and camera controls into explicit tokens contextualized directly within a shared self-attention space. Our formulation reveals that (i) explicit view tokens disentangle conflicting dynamics and unlock emergent view switching from single-view data, while (ii) action and camera inputs play complementary roles in governing local responsiveness and global stability. To preserve temporal continuity across execution intervals, we further introduce Interaction-Transport RoPE (IT-RoPE), parameterizing temporal attention with accumulated control transitions. On WBench, World-in-Context-5B achieves navigation performance on par with 22B EchoWM (81.5 vs. 81.6) and attains a 93.8% perspective-switching success rate, substantially outperforming existing 5B baselines (18.8%). Controlled analyses further demonstrate compounding advantages of World-in-Context under richer conditioning mixtures, favorable data efficiency, and natural applicability to causal rollouts.
