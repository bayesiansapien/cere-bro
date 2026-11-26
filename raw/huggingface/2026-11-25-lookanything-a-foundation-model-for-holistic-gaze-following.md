---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32351
url: https://huggingface.co/papers/2611.32351
arxiv_url: https://arxiv.org/abs/2611.32351
date: 2026-11-25
---

# LookAnything: A Foundation Model for Holistic Gaze Following

Human gaze provides a rich window into attention and intent, making its understanding essential for applications ranging from social signal analysis to human-robot interaction. Existing methods typically employ highly customized architectures relying on auxiliary inputs like head crops or depth maps, causing cascading errors and inference overhead. Trained on single domains and confined to isolated gaze following with heatmap outputs, they lack flexibility and generalization for diverse interactive scenarios. To bridge this gap, we present LookAnything, a foundation model that unifies diverse gaze-centric tasks for holistic gaze following. Benefiting from large-scale multi-task and cross-domain training, LookAnything flexibly adapts to various settings, generating diverse outputs (points, boxes, heatmaps, and language) and supporting broad gaze-centric localization, description, and reasoning. At its core, we introduce learnable gaze-prior queries to promote gaze-aware representation learning, eliminating the need for auxiliary external inputs. To facilitate this paradigm, we construct HoliGaze, a comprehensive corpus and benchmark comprising 311K question-answer pairs across 5 capability dimensions and 9 distinct tasks. Experiments demonstrate that LookAnything consistently outperforms 33 leading vision-language models on holistic gaze following, while remaining highly competitive with dedicated specialists across 5 conventional target detection benchmarks. Evaluation on unseen datasets and deployment on a real robot further validate its strong out-of-domain generalization and flexible adaptation in real-world scenarios.
