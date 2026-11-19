---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.22563
url: https://huggingface.co/papers/2611.22563
arxiv_url: https://arxiv.org/abs/2611.22563
date: 2026-11-18
---

# CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference

CAD practitioners often work with proprietary parts that they are unwilling to share with external services. For individuals and small companies, bringing this work in-house also requires computational resources they can afford. We introduce CADMAGEDDON, an open-source agent that reconstructs editable CAD from meshes and can run locally on single-GPU systems and current-generation laptops. The method decomposes this complex task into a chain of simple visual decisions about what to construct and what to correct. Geometric tools support precise construction, allowing the agent to focus on visual reasoning. Using the mid-sized Qwen3.8-27B model, CADMAGEDDON outperforms prior approaches, including systems based on frontier models, in reconstruction quality on all the main benchmarks. CADMAGEDDON integrates with FreeCAD, bringing its reconstructions into practitioners' existing CAD workflows. Code: https://github.com/kulibinai/cadmageddon
