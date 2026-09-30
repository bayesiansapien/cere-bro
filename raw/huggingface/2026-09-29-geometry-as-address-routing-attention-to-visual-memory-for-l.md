---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935161+00:00
arxiv_id: 2609.34722
url: https://huggingface.co/papers/2609.34722
arxiv_url: https://arxiv.org/abs/2609.34722
date: 2026-09-29
---

# Geometry as Address: Routing Attention to Visual Memory for Long-Horizon Camera-Controlled Video Generation

Long-horizon camera-controlled video generation requires recovering previously observed content from an ever-growing visual history. Existing approaches either search historical context implicitly or reconstruct it into persistent 3D memory, facing inefficient memory access or accumulated geometric errors. Our key insight is that geometry need not explain the scene--it only needs to determine where visual memory should be read from, while attention decides what should be recovered. Based on this insight, we introduce GEAR, a Geometry-Enabled Attention Routing framework that uses geometry as an explicit token-level address for visual memory. Rather than fusing historical observations into a persistent global 3D representation, GEAR retains them as frame latents and uses per-frame geometry only to establish token-level correspondences with target views, thereby avoiding persistent error accumulation from global fusion. Guided by these correspondences, Geometric Correspondence Attention (GCA) selectively injects geometrically matched historical features into noisy target patches during denoising. We further introduce an Invisible Octree to accumulate visibility evidence and reject geometrically plausible but occluded correspondences. Extensive experiments demonstrate that GEAR achieves state-of-the-art visual quality, precise camera control, and revisit consistency, enabling minute-long video generation along challenging trajectories.
