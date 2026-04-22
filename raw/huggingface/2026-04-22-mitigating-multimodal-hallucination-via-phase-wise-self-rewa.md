---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.17982
url: https://huggingface.co/papers/2604.17982
arxiv_url: https://arxiv.org/abs/2604.17982
date: 2026-04-22
---

# Mitigating Multimodal Hallucination via Phase-wise Self-reward

Large Vision-Language Models (LVLMs) still struggle with vision hallucination, where generated responses are inconsistent with the visual input. Existing methods either rely on large-scale annotated data for fine-tuning, which incurs massive computational overhead, or employ static post-hoc strategies that overlook the dynamic nature of hallucination emergence. To address these, we introduce a new self-rewarding framework, enabling dynamic hallucination mitigation at inference time without external supervision. On the empirical side, we reveal that visual hallucination exhibits phase-wise dynamic patterns, peaking at the onset of each semantic phase. Drawing on these insights, we propose PSRD (Phase-wise Self-Reward Decoding) for online hallucination correction guided by phase-wise self-reward signals. To reduce the cost of repeated self-evaluation during decoding, we distill the hallucination guidance signal from LVLMs into a lightweight reward model. The proposed PSRD significantly reduces the hallucination rate of LLaVA-1.5-7B by 50.0% and consistently outperforms existing post-hoc methods across five hallucination evaluation benchmarks for four LVLMs.
