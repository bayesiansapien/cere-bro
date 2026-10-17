---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22186
url: https://huggingface.co/papers/2610.22186
arxiv_url: https://arxiv.org/abs/2610.22186
date: 2026-10-16
---

# EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment

Recent advances in Omni Language Models (OLMs) provide a unified solution for audiovisual video captioning. Nevertheless, existing approaches predominantly treat captioning as an unstructured text generation process, neglecting the inherent semantic structure of videos and leading to suboptimal fine-grained audiovisual alignment. To bridge this gap, we propose EVA-Cap, a novel framework that decomposes captions into atomic audiovisual events and transforms unstructured text supervision into event-centric alignment. We train EVA-Cap via Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) on a self-curated dataset, EVA-Data, which is built with event-centric quality control. During the GRPO phase, the model is explicitly optimized against three event-centric alignment targets: global event completeness, intra-event attribution, and inter-event synchronization. Extensive experiments demonstrate that EVA-Cap significantly outperforms existing methods in event-centric evaluation (e.g., +9.0% average gain on ChronusAV), while achieving competitive performance on general audiovisual captioning benchmarks (e.g., +3.3% on WorldSense).
