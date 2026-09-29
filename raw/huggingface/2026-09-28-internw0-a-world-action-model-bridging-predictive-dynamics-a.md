---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.594544+00:00
arxiv_id: 2609.31394
url: https://huggingface.co/papers/2609.31394
arxiv_url: https://arxiv.org/abs/2609.31394
date: 2026-09-28
---

# InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data

World Action Models (WAMs) jointly model visual dynamics and action generation for generalist robot manipulation. A central challenge is to integrate priors from large-scale pretrained models---including visual dynamics, scene semantics, geometry, and motion---into a unified framework for robot action generation. We introduce InternW0-Δ, a unified WAM pretrained on a heterogeneous corpus that outperforms prior methods across simulation benchmarks and real-robot platforms.
  InternW0-Δ combines pretrained visual dynamics, scene-level semantics, 4D geometric and motion priors, and action generation within a Mixture-of-Transformers (MoT) framework. A pretrained video expert and an action expert interact under semantic guidance from a frozen VLM, while a pretrained 4D foundation model injects geometric and motion priors through training-only distillation. We further introduce Causal Imprint, which learns future-relevant scene changes from training-only future supervision and provides predictive representations directly to the action expert without future-video rollout at inference.
  For large-scale joint training, we construct a heterogeneous corpus of robot demonstrations, UMI data, egocentric human demonstrations, and Ego2Robot data, curated and aligned under a common state-action representation. The resulting corpus contains over 20K hours of processed training data, to our knowledge the largest open-source corpus of its kind. We pretrain InternW0-Δ on this corpus and demonstrate strong performance across simulation benchmarks and real-robot platforms. We will open source the training code, model weights, infrastructure, data-processing pipeline, and processed data where licenses permit. Project page: https://internrobotics.github.io/InternW0-Delta/
