---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.902915+00:00
arxiv_id: 2611.34237
url: https://huggingface.co/papers/2611.34237
arxiv_url: https://arxiv.org/abs/2611.34237
date: 2026-11-26
---

# VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation

Code-driven video generation asks a coding agent to write and run rendering programs. This gives exact control over typography, data visualizations, synchronized audio, and multi-shot scenes, and it leaves an editable project behind. A program that exits cleanly can still render overlapping labels, a camera aimed away from its subject, broken object interactions, or narration that drifts out of sync, and none of these raise a runtime error. Feeding rendered frames and audio back into the coding session bloats its long-horizon context, while critiquing only the finished full-resolution render turns early design mistakes into costly rewrites. We introduce VibeVideoAgent, a training-free framework that lets coding agents inspect their drafts throughout production. Multimodal perception runs in short-lived contexts kept apart from the coder and returns compact, grounded Findings. Seven primitives operate on a unified multi-clock representation of assets and drafts: they explore media from coarse to fine, verify quoted requirements with evidence from every required modality, compare a draft with a reference or an earlier revision on separate clocks, and measure stream signals locally. A lightweight staged protocol has the agent test its riskiest decision on a minimal preview first. On all 239 VibeVideoBench tasks, with matched agent runtimes and a fixed perception model, VibeVideoAgent improves holistic audiovisual quality (L3) for Claude Opus 5.5 (4.03 -> 4.43, while L2 rubric compliance rises from 98.87% to 99.35%), GPT-6 Astra (4.03 -> 4.27), and Claude Sonnet 5.5 (3.97 -> 4.10), with the largest gains in audio-visual synchronization (up to +0.56). Controlled ablations show that each component contributes, and trajectory audits show that the granularity of code edits governs the trade-off between rubric adherence and perceptual quality.
