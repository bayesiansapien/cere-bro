---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16838
url: https://huggingface.co/papers/2606.16838
arxiv_url: https://arxiv.org/abs/2606.16838
date: 2026-06-16
---

# OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation

Multi-task learning (MTL) is essential in recommender systems to enable complementary learning among diverse user feedback. While modern industrial practices have shifted from DNNs to Transformer-centric architectures to strengthen sequence modeling and scaling capacity, they still decouple feature encoding from multi-task prediction, treating the Transformer as a task-agnostic encoder. This design fundamentally limits the performance and scalability by (1) creating an information bottleneck under heterogeneous task objectives, (2) inducing gradient interference that leads to the seesaw phenomenon, and (3) forcing a dataflow transition in which attention-based, context-adaptive representation learning is converted to static feed-forward task prediction with incompatible information read-write dynamics. We propose OneRank, a Transformer-native multi-task ranking framework that eliminates encoder-predictor separation and introduces task-private channels for forward representation learning and backward optimization, enabling task-specialized learning while reducing inter-task interference. In the forward pass, OneRank learns task-specific representations bottom-up through task-conditioned information selection, candidate-aware contextualization, and controlled cross-task interaction. In the backward pass, cross-task gradient detachment isolates task-private parameter updates from shared knowledge extraction modules, preventing negative transfer. We further replace static task-specific MLP scorers with dynamic matching-based scoring for context-aware personalized ranking. By internalizing multi-task reasoning within the Transformer stack, OneRank establishes a unified and scalable architectural paradigm. Offline and online experiments on large-scale industrial datasets show that OneRank significantly outperforms state-of-the-art baselines while maintaining computational efficiency.
