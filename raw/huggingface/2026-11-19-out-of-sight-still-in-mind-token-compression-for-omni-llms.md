---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.148807+00:00
arxiv_id: 2607.21179
url: https://huggingface.co/papers/2607.21179
arxiv_url: https://arxiv.org/abs/2607.21179
date: 2026-11-19
---

# Out of Sight, Still in Mind: Token Compression for Omni-LLMs

The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens account for the vast majority of the input, and are highly redundant. In this paper, we propose ReMo, a training-free framework that compresses visual tokens by redistributing their information across modalities: a visual token is kept only if its information appears nowhere else. ReMo achieves this in two ways: (i) it aligns audio and video in a shared space via closed-form calibration, and removes visual tokens already explained by the audio or by other visual tokens; and (ii) it replaces object-level visual tokens, identified by a lightweight object detector, with compact text proxies, short descriptions of each object and its location, conveying the same content in far fewer tokens. On Qwen2.5-Omni at two model scales, ReMo removes 54% of the input tokens with comparable accuracy. It performs comparably to the full-token model, reaching 101.2% and 101.4% of its average accuracy over five audio-visual benchmarks.
