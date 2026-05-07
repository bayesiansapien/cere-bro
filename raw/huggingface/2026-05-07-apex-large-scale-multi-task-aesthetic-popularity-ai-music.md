---
source: farmer/huggingface
farmed: 2026-05-07T00:00:00Z
arxiv_id: 2605.03395
url: https://huggingface.co/papers/2605.03395
arxiv_url: https://arxiv.org/abs/2605.03395
date: 2026-05-07
---

# APEX: Large-scale Multi-task Aesthetic-Informed Popularity Prediction for AI-Generated Music

Music popularity prediction has attracted growing research interest, with relevance to artists, platforms, and recommendation systems. However, the explosive rise of AI-generated music platforms has created an entirely new and largely unexplored landscape, where a surge of songs is produced and consumed daily without the traditional markers of artist reputation or label backing. Key, yet unexplored in this pursuit is aesthetic quality. We propose APEX, the first large-scale multi-task learning framework for AI-generated music, trained on over 211k songs (10k hours of audio) from Suno and Udio, that jointly predicts engagement-based popularity signals -- streams and likes scores -- alongside five perceptual aesthetic quality dimensions from frozen audio embeddings extracted from MERT, a self-supervised music understanding model. Aesthetic quality and popularity capture complementary aspects of music that together prove valuable: in an out-of-distribution evaluation on the Music Arena dataset, comprising pairwise human preference battles across eleven generative music systems unseen during training, including aesthetic features consistently improves preference prediction, demonstrating strong generalisation of the learned representations across generative architectures.
