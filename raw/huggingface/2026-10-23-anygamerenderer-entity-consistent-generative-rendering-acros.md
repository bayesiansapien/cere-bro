---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.884553+00:00
arxiv_id: 2610.31466
url: https://huggingface.co/papers/2610.31466
arxiv_url: https://arxiv.org/abs/2610.31466
date: 2026-10-23
---

# AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark

AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact.
  Our AnyGameRenderer generalizes across a wide range of genres that agents build, such as tower defense, auto-battlers, top-down survivors, turn-based battles, kart racing, and crowd runners.
  AnyGameRenderer takes plain video as its game-state input, with no complex representations such as engine G-buffers, per-object class labels, or low-poly proxies. Gray blockouts, colored primitives, semantic maps, and wireframes all work as input.
  It also preserves entity correspondence: group counts stay correct, and entities appear and disappear on the right frame.
  We implement AnyGameRenderer by LoRA fine-tuning MiniMax-H3 ref2va, a 33B reference-video-conditioned video generation model. Training uses sim10k paired clips from three sources: (i) multi-stream rendering data from 38 agent-made games exported from GEAR, an AI game-creation tool; (ii) two-stream rendering data from Unreal Engine, with programmatically controlled crowds, count changes, and entity scales; and (iii) real gameplay recordings, with pairs reconstructed via 3D-box detection.
  To evaluate the entity correspondence, we propose an entity-level benchmark of 59 held-out cases with 753 entities, scored against ground-truth boxes. Compared with the base model, AnyGameRenderer better preserves entity correspondence: temporal match rises from 50.9\% to 62.9\%, missed count changes fall from 34.7\% to 21.3\%, and fewer entities are hallucinated or left unrendered.
