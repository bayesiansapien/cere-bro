---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.14383
url: https://huggingface.co/papers/2606.14383
arxiv_url: https://arxiv.org/abs/2606.14383
date: 2026-06-18
---

# IndustryBench-MIPU: Benchmarking Multi-Image Attribute Value Extraction for Industrial Products

Industrial products such as valves and circuit breakers are defined by dense technical specifications that govern procurement, compatibility, and safety across supply chains. These specifications are scattered across multiple heterogeneous product images, including specification tables, nameplates, and technical drawings, yet whether Multimodal Large Language Models (MLLMs) can reliably recover them remains underexplored. To fill this gap, we introduce IndustryBench-MIPU, the first large-scale benchmark for multi-image industrial product understanding, built around structured attribute extraction -- recovering property-value pairs from product images. This task jointly probes text recognition on specification tables and nameplates, visual reasoning over technical drawings, domain knowledge to decode industrial terminology, and cross-image evidence integration to assemble scattered specifications. Concretely, the benchmark comprises 4,559 products across 27,652 images with 103,703 annotations spanning 18 industrial categories, constructed through multi-model consensus and three-tier quality assurance. Evaluating nine MLLMs under both single-image and product-level multi-image settings reveals a stark completeness gap: models achieve high precision (86--94%) but the best recovers only 49.9% of product-level attributes; moving from single-image to multi-image extraction costs 15--34 percentage points of recall. Multi-image completeness, not single-image accuracy, is the core bottleneck. Dataset and code are publicly available.
