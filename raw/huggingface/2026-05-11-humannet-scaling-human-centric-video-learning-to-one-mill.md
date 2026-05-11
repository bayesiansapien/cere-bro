---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.06747
url: https://huggingface.co/papers/2605.06747
arxiv_url: https://arxiv.org/abs/2605.06747
date: 2026-05-11
---

# HumanNet: Scaling Human-centric Video Learning to One Million Hours

Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly annotated human activity data. We present HumanNet, a one-million-hour human-centric video corpus that captures how humans interact with the physical world at scale. HumanNet spans both first-person and third-person perspectives and covers fine-grained activities, human-object interactions, tool use, and long-horizon behaviors across diverse real-world environments. Beyond raw video, the dataset provides interaction-centric annotations, including captions, motion descriptions, and hand and body-related signals, enabling motion-aware and interaction-aware learning. Beyond scale, HumanNet introduces a systematic data curation paradigm for embodied learning, where human-centric filtering, temporal structuring, viewpoint diversity, and annotation enrichment are treated as first-class design principles. This design transforms unstructured internet video into a scalable substrate for representation learning, activity understanding, motion generation, and human-to-robot transfer. We conduct a first-step validation on the value of this design through controlled vision-language-action ablation: under a fixed set of validation data, continued training from the Qwen VLM model with 1,000 hours of egocentric video drawn from HumanNet surpasses the continued training with 100 hours of real-robot data from Magic Cobot, indicating that egocentric human video could be a scalable and cost-effective substitute for robot data.
