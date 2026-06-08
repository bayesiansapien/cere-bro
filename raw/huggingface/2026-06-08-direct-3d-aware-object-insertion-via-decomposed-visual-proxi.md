---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.06601
url: https://huggingface.co/papers/2606.06601
arxiv_url: https://arxiv.org/abs/2606.06601
date: 2026-06-08
---

# Direct 3D-Aware Object Insertion via Decomposed Visual Proxies

Object insertion aims to seamlessly composite a reference object into a specified region of a background image. Recent diffusion-based methods achieve high visual quality but formulate insertion as a simple 2D inpainting task, providing no explicit control over the object's 3D pose and limiting their practical applicability. We propose DIRECT (Decomposed Injection for Reference Composition and Target-integration), a novel framework that integrates interactive pose manipulation with high-fidelity 2D image synthesis to enable pose-controllable object insertion. Our method decomposes the insertion conditions into three complementary components: appearance guidance capturing visual details from the reference object, geometry guidance derived from the user-adjusted 3D proxy, and context guidance from the target background. By injecting them through separate pathways, DIRECT avoids feature entanglement and simultaneously preserves reference appearance, follows the user-specified pose, and adapts the object to the target scene. We also introduce an automated data construction pipeline to improve the diversity and quality of training data. Experiments show that DIRECT outperforms previous methods in both geometric controllability and visual quality.
