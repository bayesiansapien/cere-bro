---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.232050+05:30
arxiv_id: 2610.16338
url: https://huggingface.co/papers/2610.16338
arxiv_url: https://arxiv.org/abs/2610.16338
date: 2026-10-15
---

# SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation

Recent years have witnessed rapid progress in joint audio--visual generation. However, audio--visual synchronization remains a challenge, as generated speech and sound often temporally misalign with visual events. A key bottleneck is the lack of human-annotated data, reliable evaluation benchmarks, and synchronization-aware evaluation models for generated audio--visual outputs. To address these limitations, we conduct a comprehensive study spanning data, benchmarking, and reward modeling. We first introduce SyncReward-Data-80K, a dataset containing 80K professional synchronization ratings for clips from eight audio--visual generators. A taxonomy-guided construction pipeline covers four sound-event families: Speech, Onset, Instrument, and Ambient. We further construct SyncReward-Bench, a held-out benchmark of 1K clips, each independently rated by multiple professionals. Using this benchmark, we systematically evaluate specialized synchronization metrics and omni-modal models, revealing their substantial misalignment with human judgments. Finally, we develop SyncReward, a reward model that combines semantic--temporal contrastive pretraining on real clips with human supervision on generated clips. As an evaluation metric, SyncReward achieves the strongest agreement with human ratings among the evaluated methods. As a reward, it improves synchronization through inference-time best-of-N selection and reinforcement learning based post-training. We will release the data, benchmark, model, and code at https://github.com/WeChatCV/SyncReward.
