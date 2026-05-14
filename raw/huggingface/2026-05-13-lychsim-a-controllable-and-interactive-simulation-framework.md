---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.12449
url: https://huggingface.co/papers/2605.12449
arxiv_url: https://arxiv.org/abs/2605.12449
date: 2026-05-13
---

# LychSim: A Controllable and Interactive Simulation Framework for Vision Research

While self-supervised pretraining has reduced vision systems' reliance on synthetic data, simulation remains an indispensable tool for closed-loop optimization and rigorous out-of-distribution (OOD) evaluation. However, modern simulation platforms often present steep technical barriers, requiring extensive expertise in computer graphics and game development. In this work, we present LychSim, a highly controllable and interactive simulation framework built upon Unreal Engine 5 to bridge this gap. LychSim is built around three key designs: (1) a streamlined Python API that abstracts away underlying engine complexities; (2) a procedural data pipeline capable of generating diverse, high-fidelity environments with varying out-of-distribution (OOD) visual challenges, paired with rich 2D and 3D ground truths; and (3) a native integration of the Model Context Protocol (MCP) that transforms the simulator into a dynamic, closed-loop playground for reasoning agentic LLMs. We further annotate scene-level procedural rules and object-level pose alignments to enable semantically aligned 3D ground truths and automated scene modification. We demonstrate LychSim's capability across multiple downstream applications, including serving as a synthetic data engine, powering reinforcement learning-based adversarial examiners, and facilitating interactive, language-driven scene layout generation. To benefit the broader vision community, LychSim will be made publicly available, including full source code and various data annotations.
