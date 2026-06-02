---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.00828
url: https://huggingface.co/papers/2606.00828
arxiv_url: https://arxiv.org/abs/2606.00828
date: 2026-06-02
---

# RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes

Vision-Language Models (VLMs) have shown strong visual understanding and are increasingly deployed in embodied AI systems, where reliable perception under real conditions is essential. However, existing benchmarks assess VLMs using clean images or isolated perturbations rather than stresses caused by physical scene formation. This design has two limitations: it covers only a narrow subset of everyday visual stresses, and some perturbations rarely appear in realistic embodied scenes. This gap raises a fundamental question: how can we define visual stress in a principled way that captures the diverse factors encountered in physical environments? To address this question, we formulate visual perception from an inverse graphics perspective and introduce RoboStressBench, a benchmark for evaluating VLM robustness to physical visual stress in embodied scenes. Inspired by the physical rendering equation, RoboStressBench decomposes visual stress into four physically grounded dimensions: Material (M), Viewpoint (V), Lighting (L), and Geometry (G). This design enables RoboStressBench to cover a broad range of visual stresses in real-world environments, while allowing controlled analysis of their effects on VLM capabilities such as visual recognition, reasoning, and planning. Through comprehensive evaluations of state-of-the-art VLMs, we identify stress-specific failure modes and reveal that different physical factors degrade different embodied capabilities, which are often obscured by aggregate accuracy. We further introduce a stress-aware agentic solver that detects visual stressors and invokes visual-editing skills before reasoning, improving robustness in high-stress scenarios. Overall, RoboStressBench provides a principled evaluation framework for diagnosing and improving VLM perception under real-world physical stress, supporting the development of more reliable embodied AI systems.
