---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36380
url: https://huggingface.co/papers/2609.36380
arxiv_url: https://arxiv.org/abs/2609.36380
date: 2026-09-30
---

# LEGO-Anything: Coding Agents for 3D Scene Reconstruction

A 3D scene reconstructed from a single image is most useful when represented not as a rendering or a fixed 3D output, but as an explicit scene program whose execution yields a scene that can be inspected, edited, and queried. We present LEGO-Anything, an Image-to-Code framework in which a coding agent iteratively writes and executes Blender code, inspects scenes and renderings, and revises the program. To evaluate end-to-end scene recovery, we introduce LEGO-Bench, a simulator-grounded benchmark with 208 images from 104 diverse indoor and outdoor scenes. LEGO-Bench separately scores artifact validity, visible-surface geometry, and rendered appearance. Its simulator-grounded design enables extensibility and precise automatic evaluation. Among evaluated agents, GPT-6-astra achieves the strongest overall results, with 53.4% indoor and 39.6% outdoor scores, yet substantial gaps remain between delivering valid scene artifacts and faithfully recovering scene geometry and appearance. Analysis of agent construction trajectories reveals three recurring issues: weak scene initialization, regressive edits during iteration, and unreliable self-evaluation. These findings motivate LEGO-Plugin, a training-free harness plugin for more controlled iterative scene construction, which improves all six evaluated models, with relative gains of up to 62.7% in overall score. Finally, we test whether reconstructed scenes can represent natural images and support vision tasks. In LEGO-World, we derive object detections, instance masks, and relative depth as deterministic queries on scenes reconstructed by GPT-6-astra. These readouts show non-trivial performance across all three tasks but fall well short of specialized vision models, suggesting that program-constructed scenes from current coding agents are a promising but not yet sufficiently precise representation of natural images.
