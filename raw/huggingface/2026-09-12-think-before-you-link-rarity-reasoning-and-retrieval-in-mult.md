---
source: farmer/huggingface
farmed: 2026-09-12T06:06:40.318302+00:00
arxiv_id: 2609.10745
url: https://huggingface.co/papers/2609.10745
arxiv_url: https://arxiv.org/abs/2609.10745
date: 2026-09-12
---

# Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking

Multimodal entity linking grounds entity mentions in text and images to knowledge-base entries. These systems degrade on rare entities, but prior work measures rarity primarily through popularity-based metrics such as pageviews. We broaden this view using knowledge-graph structural metrics that capture how well an entity is documented and connected. These metrics identify many rare entities that popularity metrics miss. Across the resulting rare-entity slices, state-of-the-art accuracy drops by 15.4-39.9%, showing that different rarity definitions expose different failure modes. To address these failures, we introduce a simple, training-free framework in which a reasoning-capable vision-language model iteratively searches and reasons over Wikipedia, gathering evidence dynamically. Controlled experiments show that reasoning and retrieval are complementary. Reasoning alone does not significantly improve accuracy on rare entities. Retrieval without reasoning improves rare-entity accuracy but can hurt overall accuracy. Their combination performs best. On MERLIN, a multilingual multimodal entity linking benchmark over five languages (Hindi, Indonesian, Japanese, Tamil, Vietnamese), our best system improves over the state of the art by 6.9% overall and by up to 23.3% on rare-entity slices. We release MERLIN-Rare, rare-entity test slices for targeted evaluation, with our framework.
