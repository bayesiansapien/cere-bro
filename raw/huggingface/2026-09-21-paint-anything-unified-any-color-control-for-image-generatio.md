---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.20816
url: https://huggingface.co/papers/2609.20816
arxiv_url: https://arxiv.org/abs/2609.20816
date: 2026-09-21
---

# Paint-Anything: Unified Any-Color Control for Image Generation and Editing

Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-prompt interface for generation and editing through object-level color supervision. We develop a data pipeline that constructs Paint-500K from real images through object grounding, perceptual color labeling, and editing-pair synthesis. Since shadows make real-image labels only approximate colors, we complement this supervision with pure-color anchors whose pixels exactly match their paired hex values. These anchors are used only at high-noise timesteps, leaving low-noise training to natural images. We further introduce Any Color Benchmark (ACBench), comprising ACBench-T2I and ACBench-Edit, to measure object-level hex color fidelity across both tasks. On FLUX.2-4B, Paint-Anything improves ACBench-T2I and ACBench-Edit scores by 85.3% and 28.3%, respectively, relative to the base model, with ablations supporting the training recipe. It also achieves the highest average CompColor score among the compared methods.
