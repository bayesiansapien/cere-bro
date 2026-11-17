---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.997375+00:00
arxiv_id: 2611.12901
url: https://huggingface.co/papers/2611.12901
arxiv_url: https://arxiv.org/abs/2611.12901
date: 2026-11-16
---

# Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding

Recent advancements in multimodal diffusion language models (MDLMs) have exhibited strong global modeling capabilities through iterative refinement. We observe that mask uncertainty follows an overall downward trend during iterative denoising, while a few denoising steps exhibit localized entropy spikes closely associated with hallucinations. We argue that anomalous steps can be identified by measuring the entropy deviation of each denoising step from its neighboring temporal window. We hypothesize that discrete token commitment discards the distributional information at masked positions, limiting the continued interaction between candidate semantics and the context during entropy spikes. With this goal, we present StepRefine, a plug-and-play decoding strategy that leverages semantic context to achieve reliable denoising. The core of our method lies in a step-aware switch between discrete denoising and latent refinement. The model employs probability-weighted embeddings at entropy spike steps to preserve diverse reasoning hypotheses and performs multiple rounds of continuous refinement. Meanwhile, a refinement controller monitors distributional stability to reduce unnecessary loops and switch the model back to standard discrete denoising. Through extensive experiments, StepRefine demonstrates significant hallucination mitigation across different MDLMs on multimodal benchmarks.
