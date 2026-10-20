---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21302
url: https://huggingface.co/papers/2610.21302
arxiv_url: https://arxiv.org/abs/2610.21302
date: 2026-10-19
---

# Dusting the Phantom: Gaussian Allocation for Fading Dynamic Content

Dynamic Gaussian representations have made high-quality, real-time volumetric video increasingly practical, yet challenging motion can still break their reconstruction: small fast-moving objects may disappear, and fine textures in highly dynamic regions are often lost. In particular, simply training longer or using more Gaussians may still fail to recover small, fast-moving objects. We argue that the key bottleneck is not representational capacity itself, but where and when Gaussian primitives are allocated. Existing allocation strategies rely on current Gaussian locations and often overlook the spatiotemporal destinations of relocated Gaussians. To address these limitations, we introduce two complementary strategies. First, Seed Injection identifies under-reconstructed dynamic regions using temporal appearance changes and reconstruction errors, and initializes new Gaussians at geometrically plausible 3D locations through multi-view observations, independent of existing Gaussian locations. Second, Temporal Biased Relocation uses time-resolved optimization signals to guide the spatiotemporal placement of relocated Gaussians. Both strategies maintain a fixed Gaussian budget without modifying the underlying representation. Experiments across multiple dynamic-scene datasets demonstrate improved reconstruction quality, particularly in highly dynamic regions, recovering small, rapidly moving objects and fine-grained appearance details.
