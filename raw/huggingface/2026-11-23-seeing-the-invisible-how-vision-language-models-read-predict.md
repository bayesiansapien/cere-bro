---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.249873+00:00
arxiv_id: 2611.28123
url: https://huggingface.co/papers/2611.28123
arxiv_url: https://arxiv.org/abs/2611.28123
date: 2026-11-23
---

# Seeing the Invisible: How Vision-Language Models Read, Predict and Trace Radio Fields

Operating in the physical world requires reasoning beyond what cameras directly capture. In a city, radio signals are invisible to the lens, yet their strength is governed by the buildings and streets an image does show. Given only these visible structures, can vision-language models (VLMs) infer the invisible radio field they shape? Probing true physical reasoning requires exact fields in real cities, alongside controlled interventions where a single physical factor changes. We build a label-free engine that turns any coordinate on Earth into a ray-traceable city, simulates matched single-factor counterfactuals, and computes every answer exactly. This yields RadioVISTA, a benchmark and training dataset for visual reasoning about invisible fields. Physically, a radio field is the sum of its propagation paths, yet across six continents we uncover a striking field-path dissociation: frontier VLMs accurately judge where a field is strong, but fail to tell whether a single direct or one-wall path exists. Open models fail even earlier at reading the field itself, and are systematically wrong, scoring below random guessing even when credited for any of four attempts. On unseen cities, fine-tuning brings a 9B open model close to frontier proprietary models on fields, yet neither supervised nor reinforcement fine-tuning improves path tracing. Supervising only final answers teaches models to approximate the field, yet leaves single-path geometry out of reach.
