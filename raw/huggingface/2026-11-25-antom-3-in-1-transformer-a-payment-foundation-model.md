---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.25403
url: https://huggingface.co/papers/2611.25403
arxiv_url: https://arxiv.org/abs/2611.25403
date: 2026-11-25
---

# Antom 3-in-1 Transformer: A Payment Foundation Model

We report the development of Antom 3-in-1 Transformer, a payment foundation model that integrates sequence, tabular, and graph representations for payment risk detection. The model contains approximately 7B parameters, with approximately 1.7B activated per task route. Antom 3-in-1 Transformer is pretrained to learn reusable behavioral and relational representations, primarily on Ant International's internal payment data. In a cross-business transfer experiment, pretraining improves the target business metric by 34.5% over the same architecture trained from scratch. With only 25% of the training labels, the pretrained model outperforms the full-label scratch baseline in Average Precision (AP) and Recall@0.5% on different merchant domains. In a four-month online experiment on Ant International's billion-scale payment platform, the model reduced the overall loss rate by 37.88% relative to XGB-Online.
