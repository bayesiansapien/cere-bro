---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.531351+00:00
arxiv_id: 2611.12872
url: https://huggingface.co/papers/2611.12872
arxiv_url: https://arxiv.org/abs/2611.12872
date: 2026-11-13
---

# HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents

As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined representations, which may miss relevant memories and overlook heterogeneous evidence needs across queries. We introduce \hivemem, a multimodal memory framework that interleaves \textsc{H}or\textsc{i}zontal Memory Expansion with \textsc{Ve}rtical Evidence Composition. For horizontal memory expansion, \hivemem organizes memory episodes into a relational graph using textual and visual anchors, expanding semantically retrieved seeds with related neighbors to recover complementary information. For vertical evidence composition, each retrieved memory retains multiple evidence forms, including compact summaries, captions, grounded visual views, raw images, and interaction history. A lightweight trainable selector independently composes an evidence subset for each retrieved memory, enabling query-adaptive utilization of heterogeneous multimodal information. This two-dimensional design jointly broadens memory coverage and adapts the evidence contributed by individual memories. Experiments across three multimodal memory benchmarks show that \hivemem consistently improves task performance across base models while reducing token consumption by about 90\% compared with the most efficient competing multimodal baselines.
