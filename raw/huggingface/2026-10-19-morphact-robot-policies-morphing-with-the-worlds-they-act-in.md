---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.20019
url: https://huggingface.co/papers/2610.20019
arxiv_url: https://arxiv.org/abs/2610.20019
date: 2026-10-19
---

# MorphAct: Robot Policies Morphing with the Worlds They Act In

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When different operations favor competing parameter adjustments, fitting their mixture can leave individual operations insufficiently adapted. Our atomic-task diagnostics reveal competing update directions in both vision-language and action parameters, with source-improving updates increasing loss on other tasks. This motivates MorphAct, a contextual parameterization framework that dynamically adjusts robot policy parameters as interaction contexts change. Two coupled generators produce context-dependent low-rank updates for the vision-language and action modules. Their coupling follows the policy's computational dependency: vision-language updates shape the representations that condition action-side parameter generation. Both generators are trained jointly through the native action objective, without operation labels or expert-adapter targets. MorphAct improves performance across three VLA backbones on LIBERO and Meta-World, with gains of up to 16.30%. In real-world evaluation, it achieves gains of up to 14% over π_{0.5}. Ablations support the benefits of contextual parameter generation and representation coupling.
