---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14702
url: https://huggingface.co/papers/2606.14702
arxiv_url: https://arxiv.org/abs/2606.14702
date: 2026-06-15
---

# OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains

Current automated pipelines for audio-visual Question Answering (QA) generally adopt a ``video-caption-QA'' paradigm. However, these methods typically segment videos into short clips and generate separate descriptions for audio and visual modalities. This decoupled processing severs inherent associations between sounds and their visual sources, while independent clip processing often causes inconsistent descriptions of the same entity across segments. Furthermore, coupling long-text comprehension and QA synthesis into a single step often restricts models to localized events, yielding questions lacking long-term temporal connections and deep cross-modal reasoning. To address these issues, we propose an automated data engine featuring two mechanisms: (1) Entity-Anchored Video Scripting transforms videos into structured scripts, comprising summaries, main entity lists, and segment-wise audio-visual descriptions. The entity list serves as a global prior to ensure cross-segment referential consistency and reconstruct audio-visual associations. (2) Clue-Guided QA Generation prompts models to first mine cross-segment, multimodal clues from the script, and subsequently generate QA pairs based on these high-value clues. Leveraging this pipeline, we construct the instruction-tuning dataset OmniVideo-100K and a human-verified test set, OmniVideo-Test. Fine-tuning VITA-1.5, Qwen2.5-Omni-7B and Qwen3-Omni-30B on OmniVideo-100K yields performance gains of up to 20.59% on OmniVideo-Test, demonstrating strong generalization (up to 12.64% improvements) across established benchmarks like Daily-Omni and JointAVBench.
