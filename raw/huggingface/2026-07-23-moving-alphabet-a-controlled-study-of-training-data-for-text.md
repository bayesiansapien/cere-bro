---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.18789
url: https://huggingface.co/papers/2607.18789
arxiv_url: https://arxiv.org/abs/2607.18789
date: 2026-07-23
---

# Moving Alphabet: A Controlled Study of Training Data for Text-to-Video Generation

Text-to-video generation has advanced significantly over the past five years through scaling of model size, data, and compute. Unlike model architecture, training data is often underexplored. Real-world data curation is complex and non-trivial, involving clip selection from raw videos and captioning to create video-text pairs for learning text-to-video mappings. We study how data distribution and caption quality impact text-to-video models. To enable controlled experiments, we introduce Moving Alphabet, a procedural testbed that renders letters with varying fonts, colors, sizes, and positions, moving in different directions and speeds against a black background. This design allows precise control over data distribution and caption quality by corrupting ground-truth metadata. Our experiments yield three findings: a) a diverse and balanced distribution of video content and duration is critical for generalization; b) caption quality significantly affects both model performance and training efficiency, suggesting that text-to-video models are bounded by video understanding capabilities; and c) classifier-free guidance and fine-tuning on high-quality data provide partial recovery from models trained on corrupted captions, but cannot fully compensate for poor pre-training data. We believe these insights can inform the development of large-scale text-to-video models, and we advocate for greater attention to the science of pre-training data.
