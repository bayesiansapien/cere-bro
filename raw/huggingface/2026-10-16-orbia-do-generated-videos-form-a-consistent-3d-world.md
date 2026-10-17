---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.20693
url: https://huggingface.co/papers/2610.20693
arxiv_url: https://arxiv.org/abs/2610.20693
date: 2026-10-16
---

# Orbia: Do Generated Videos Form a Consistent 3D World?

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world. Existing benchmarks assess selected geometric properties or use vision-language models to judge memory and consistency, leaving systematic 3D evaluation underexplored. We introduce Orbia, the first benchmark dedicated to a systematic and comprehensive evaluation of 3D consistency in interactive world models. Through controlled exploration and revisit, we organize the evaluation into three dimensions: input preservation, generated-content persistence, and 3D self-consistency. For input preservation, registered RGB-D references and annotated anchors support appearance, geometry, and spatial stability measurements. For generated-content persistence, we compare revisits to regions absent from the input image with their first generated observations to test whether models preserve what they create. For 3D self-consistency, cross-view depth and feature correspondence, regional scale agreement, and held-out Gaussian rendering test whether generated views describe the same 3D scene. Minute-long exploration and revisits further test long-term consistency. Our construction and annotation pipeline brings together public datasets, self-captured scenes, and simulation, yielding 720 instances across indoor and outdoor environments and six exploration-and-revisit protocols. Evaluation spans 27 text-, action-, and camera-conditioned models through native-interface adapters. Our Orbia benchmark provides a systematic basis for diagnosing 3D inconsistency and developing more persistent video world models.
