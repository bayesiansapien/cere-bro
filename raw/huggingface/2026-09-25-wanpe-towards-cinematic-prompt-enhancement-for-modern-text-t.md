---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.30221
url: https://huggingface.co/papers/2609.30221
arxiv_url: https://arxiv.org/abs/2609.30221
date: 2026-09-25
upvotes: 24
---

# WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation

Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions, the textual prompt largely directs the production, planning how actions, camera trajectories, lighting, and sound unfold across multi-shot sequences. In this paper, we present WanPE, a 397B-parameter prompt enhancement model trained on 1.05M real-world videos to master director-level cinematic planning. WanPE formulates shot-level cinematic plans via video-grounded reverse construction and employs Semantic-Consistency GRPO (SC-GRPO) to faithfully preserve user requirements across shots and over time. To benchmark this capability, we curate WanPEval, a human-annotated testbed covering durations from 5 to 30 seconds across varying intent granularities, supported by approximately 11K blind pairwise assessments. When powering Wan3.0's video generator, WanPE-397B boosts human preference over raw user prompts by 10.66-18.84 points at 5-15 seconds and by a dramatic 50.86 points in the 30-second arena. Ablation studies show that reverse construction demonstrates clear superiority over forward rewriting, while SC-GRPO robustly preserves semantic fidelity across model scales. Ultimately, WanPE leads all evaluated commercial offerings at 5-15 seconds and remains competitive with Seedance 2.5 at 30 seconds.
