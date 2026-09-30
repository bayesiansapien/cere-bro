---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935070+00:00
arxiv_id: 2609.35706
url: https://huggingface.co/papers/2609.35706
arxiv_url: https://arxiv.org/abs/2609.35706
date: 2026-09-29
---

# Reinforcing Agentic Creativity in Scientific Ideation with Night Science

Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach models when and how to depart from predictable reasoning. Grounded in cognitive science, we model creativity along three axes: action (what to do and how creatively), process (when to explore versus exploit), and outcome (the novelty and usefulness of the resulting idea). We use these axes to train models with GRPO, exposing them to varying degrees and forms of creativity throughout training. This produces substantially more diverse scientific proposals, expanding the range of research directions by 27.8% and contribution types by 14.9% over the base model. It also improves predicted citation impact by up to 32.0 percentage points and originality by 66.2 points. These gains cannot be reproduced by simply increasing decoding temperature; instead, we find that semantic guidance specifying what kind of creativity to pursue is critical. Overall, our results suggest that creativity is a learnable, multi-level ability that can be shaped to help researchers reach ideas beyond those typically explored by LLMs.
