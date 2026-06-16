---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.14667
url: https://huggingface.co/papers/2606.14667
arxiv_url: https://arxiv.org/abs/2606.14667
date: 2026-06-16
---

# Memento: Reconstruct to Remember for Consistent Long Video Generation

Long-form video generation requires recurring subjects to remain consistent across various shots, viewpoints, motions, and scene transitions. Existing temporal decomposition methods improve scalability by generating videos shot by shot. However, they mainly focus on optimizing plausible next-shot continuations without verifying whether the historical memory preserves identity-critical subject evidence. Consequently, as generation proceeds, recurring subjects may be diluted, overwritten, or forgotten. In this paper, we propose Memento, a subject-reconstruction-guided framework that treats subject preservation as an explicit identity grounding problem, based on the premise that a memory bank faithfully preserving a subject should support reconstructing that subject from memory alone. Specifically, Memento jointly trains autoregressive next-shot generation with memory-based subject reconstruction, recovering target appearances using historical memory and global story captions. To disentangle long-range subject evidence from short-range cues, Memento introduces a dual-query memory mechanism, where one query retrieves identity-relevant memory and the other selects short-context keyframes for coherent continuation. Additionally, a subject-aware cinematic data pipeline provides precise reconstruction supervision via consistent, pronoun-free subject descriptions. Experiments demonstrate that Memento achieves state-of-the-art performance in long-term subject consistency, cross-shot coherence, and visual quality.
