---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.04513
url: https://huggingface.co/papers/2606.04513
arxiv_url: https://arxiv.org/abs/2606.04513
date: 2026-06-04
---

# MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation

Lane-level maps are critical infrastructure for autonomous driving and lane-level navigation, yet constructing and maintaining standardized lane networks for hundreds of cities remains highly labor-intensive. Recent end-to-end vectorized mapping methods can predict lane geometry and topology directly from sensor data, but they typically treat mapping specifications and traffic regulations as implicit, dataset-dependent supervision. Moreover, in complex scenes (e.g., worn or missing markings and occlusions), correct lane configurations are often under-determined by visual evidence alone, making specification violations a major source of human post-editing. We propose MapAgent, an industrial-grade agentic architecture that augments a vectorization backbone for specification-compliant lane-map production. Rather than merely adding an agent loop to map prediction, MapAgent couples backbone perception with explicit specification verification, constraint-aware reasoning, and deterministic map editing under a bounded, verification-driven Judge-Planner-Worker loop. A vision-language Judge diagnoses errors by jointly inspecting visual evidence and draft vectors, while a tool-calling Planner generates minimal corrective edits with post-edit re-validation. To remain scalable for city-scale production, MapAgent is selectively triggered only on tiles with low backbone confidence, adding modest overhead while preserving throughput. Experiments on real-world datasets show consistent gains over strong production baselines, especially in complex and long-tail scenarios. Additionally, MapAgent has been integrated into Baidu Maps, supporting lane-level map generation for over 360 cities nationwide and elevating the overall production automation to over 95%, demonstrating MapAgent's practicality and effectiveness for large-scale lane-level map generation.
