---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349194+05:30
arxiv_id: 2609.40333
url: https://huggingface.co/papers/2609.40333
arxiv_url: https://arxiv.org/abs/2609.40333
date: 2026-10-01
---

# I Have a Stream: Making Self-Supervised Learning Work on Continuous Video

Self-supervised learning draws inspiration from infant visual development, yet standard training pipelines bear little resemblance to it: images are independently sampled and globally shuffled across epochs. We study self-supervised learning from continuous video streams, where frames are consumed in temporal order using strict sliding-window batches, without global reshuffling or multi-epoch replay. To this end, we construct WT++, a 95-hour urban walking-tour video dataset for streaming pretraining. Combined with a comprehensive evaluation suite we find that contrastive and distillation-based methods struggle in this setting, while MAE is more robust but still falls short of standard i.i.d. pretraining. We find that high inter-batch similarity, caused by sliding-window consumption across consecutive batches, does not explain this gap. The main challenge is high intra-batch similarity, where frames within each batch are near-duplicates. To mitigate this, we propose StreamMAE, which preserves the core MAE reconstruction objective while adapting the input pipeline with stream-aware regularization and motion-biased crop selection. StreamMAE outperforms streaming baselines, matches i.i.d. MAE trained on the same video data, remains competitive with ImageNet-pretrained MAE, and scales positively as the pretraining stream grows from 12 to 95 hours.
