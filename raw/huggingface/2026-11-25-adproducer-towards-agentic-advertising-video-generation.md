---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31466
url: https://huggingface.co/papers/2611.31466
arxiv_url: https://arxiv.org/abs/2611.31466
date: 2026-11-25
---

# AdProducer: Towards Agentic Advertising Video Generation

Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product research and creative design are closely intertwined, as the information gathered about a product determines which features can be faithfully demonstrated and how they should be presented. In this paper, we introduce AdProducer, the first end-to-end agentic framework for advertising video creation, transforming concise creative briefs into finished advertisements. Our multimodal agent autonomously researches products through web and image search and translates its findings into selling-point-driven storyboards that guide a frozen video generator. To achieve this, we develop a dedicated data construction pipeline that yields two training datasets, AdProducer-SFT and AdProducer-RL, and train the agent through supervised fine-tuning followed by reinforcement learning with joint optimization of storyboard- and video-level rewards. We further introduce AdCreation-Bench, comprising 305 advertising briefs across eight domains, with two complementary metrics: PG-Score for product correctness and creative execution, and Ad-Score for overall advertising effectiveness assessed by an independent judge. Experiments demonstrate that AdProducer improves the PG-Score of MiniMax H3 from 17.3 to 51.3 and generalizes to Veo 3.1 without additional training, improving its score from 28.0 to 35.9, with consistent gains in Ad-Score, VideoScore2, and human evaluations. Code, models, and data are released.
