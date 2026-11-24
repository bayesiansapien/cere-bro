---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.252771+00:00
arxiv_id: 2611.22495
url: https://huggingface.co/papers/2611.22495
arxiv_url: https://arxiv.org/abs/2611.22495
date: 2026-11-23
---

# Motion-Aware Reward Modeling for Instruction-Guided Video Editing

Reward models for instruction-guided video editing can favor temporal consistency at the expense of motion. We study this failure, termed motion collapse, using controlled motion-suppression variants of real edits. On VE-Bench, the evaluated composite reward prefers a motion-suppressed candidate in 97% of cases. Learned video rewards and a VLM judge also struggle with mild suppression, while latent optimization and reward-guided fine-tuning exploit this weakness to increase reward as motion declines. A linear probe of our base reward backbone performs near chance on mild suppression, motivating an explicit inter-frame dynamics input. We propose a motion-aware reward model that combines an RGB frame-difference stream with preference training against motion-suppressed and fabricated-motion negatives. A distillation anchor preserves alignment with human quality judgments. On the VE-Bench motion ladder, our model reduces the rate of selecting motion-suppressed candidates to 0% while achieving a Spearman correlation of 0.57 with human quality ratings. It also detects unseen suppression variants and preserves motion during reward-guided fine-tuning on two editing pipelines. These results support explicitly modeling motion in rewards for video editing.
