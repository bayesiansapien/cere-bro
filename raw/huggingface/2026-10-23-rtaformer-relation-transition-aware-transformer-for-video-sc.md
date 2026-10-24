---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.883646+00:00
arxiv_id: 2610.20091
url: https://huggingface.co/papers/2610.20091
arxiv_url: https://arxiv.org/abs/2610.20091
date: 2026-10-23
---

# RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation

Video scene graph generation (VidSGG) aims to capture objects and their evolving relationships in videos. This requires accounting for both the persistence of object identities and abrupt changes in relationships. Existing methods aggregate information across frames to exploit temporal context, but an emphasis on consistency can obscure these changes. As a result, a model may retain its previous prediction even after the underlying relation has changed. We refer to this failure mode as relational semantic inertia. To address this issue, we propose Relation-Transition-Aware Transformer (RTAformer), a one-stage framework that separately models entity persistence and relation changes. It injects calibrated differences between adjacent-frame relation queries to guide predicate updates, while cross-frame instance alignment during training helps reduce cross-frame representational drift. Experiments on Action Genome show improvements in recall and mean recall over existing methods, with ablation studies supporting the contributions of the proposed components and comparisons using matched backbones showing larger gains on relation-transition frames than on non-transition frames.
