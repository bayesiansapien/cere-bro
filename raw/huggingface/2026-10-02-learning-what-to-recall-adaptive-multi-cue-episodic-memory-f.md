---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822564+00:00
arxiv_id: 2609.34677
url: https://huggingface.co/papers/2609.34677
arxiv_url: https://arxiv.org/abs/2609.34677
date: 2026-10-02
---

# Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models

World models predict future observations from current experience and actions, yet prediction can depend on observations seen far in the past. Episodic memory preserves past observations for later recall; however, as memory accumulates, it raises a fundamental question: which memories are useful for the current prediction, and which available retrieval cues should be trusted to find them? This is challenging because fixed criteria based on recency, pose overlap, or visual similarity can be unreliable across environments and queries. We propose Future-Aware Recall (FAR), a framework that learns episodic recall from future-aware predictive supervision and adaptive multi-cue scoring. During training, FAR measures predictive utility by the conditional log-likelihood of the realized future given recalled context, approximated by negative diffusion prediction loss, and uses it to train a retriever that remains future-blind at inference. The retriever learns cue-specific relevance and automatically determines which available retrieval cues, such as time, pose, vision, and audio, to trust for each query when selecting memories. Across three complementary settings, FAR outperforms hand-designed recall even with the same retrieval cues, automatically adapts which available cues to trust, and recalls the right history as the world changes. Together, these results establish FAR as a flexible, principled approach to episodic memory access in world models.
