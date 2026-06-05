---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.00125
url: https://huggingface.co/papers/2606.00125
arxiv_url: https://arxiv.org/abs/2606.00125
date: 2026-06-05
upvotes: 1
---

# Multimodal Music Recommendation System using LLMs

Music recommendation systems typically treat songs as opaque tokens, relying on collaborative interaction histories which overlooks semantic or acoustic content. Prior work has explored LLM-augmented, multimodal, and text-enhanced approaches to sequential recommendation, and while some methods partially combine semantic, acoustic, or engagement signals, none jointly model all three within a unified LLM-based sequential reasoning framework that grounds recommendations in actual song content. In this work, we propose a multimodal framework for session-based music recommendation that enriches the LastFM-1K dataset with three complementary signals: (1) audio and lyric embeddings extracted using pretrained music and text representation models, (2) LLM-generated semantic metadata using the MGPHot annotation schema, and (3) listening completion ratios. We adopt the E4SRec framework by extending it with multimodal features and different item ID encoder backbones, including SASRec, BERT4Rec, and GRU4Rec. We further extend the LLM backbone option with LLaMa-2-13B, Qwen2.5-7B-Instruct, and LLaMa-3-70B in both zero-shot and fine-tuned settings. Our experiments show that integrating content-based features improves over ID-only baselines up to 95% in terms of Recall and 79% in terms of NDCG. Moreover, our experiments show that naive multimodal fusion does not always yield additive improvements, highlighting challenges in cross-modal integration. We release a large-scale multimodal benchmark for music recommendation.
