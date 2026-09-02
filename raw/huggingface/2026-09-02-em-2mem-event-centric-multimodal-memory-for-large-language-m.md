---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.00551
url: https://huggingface.co/papers/2609.00551
arxiv_url: https://arxiv.org/abs/2609.00551
date: 2026-09-02
---

# EM^2Mem: Event-Centric Multimodal Memory for Large Language Models

Multimodal memory offers a scalable interface for long-video question answering, but existing methods often retrieve captions, frames, transcripts, summaries, or graph facts as isolated fragments. Although searchable, such fragments are not generation-ready: language models must reconstruct cross-modal and temporal alignments at inference time, when context is limited and attribution is difficult. We propose EM^2Mem, an event-centric multimodal memory framework that binds heterogeneous evidence to event anchors during memory construction. Each event-indexed memory cell aligns multimodal records, temporal context, graph-linked relations, semantic facts, and provenance, enabling compact evidence readout over grounded multimodal events rather than modality-specific fragments. Across three long-video QA benchmarks, EM^2Mem improves average accuracy over the strongest memory baseline by 2.0, 2.4, and 3.7 points, improves strict event-level Top-5 evidence recall by 7.0 points, and reduces per-query latency by 4.67 times and total inference tokens by 63.66% (The code will be integrated into https://github.com/zjunlp/LightMem).
