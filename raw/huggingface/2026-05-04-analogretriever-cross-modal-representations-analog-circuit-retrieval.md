---
source: farmer/huggingface
farmed: 2026-05-04T00:00:00Z
arxiv_id: 2604.23195
url: https://huggingface.co/papers/2604.23195
arxiv_url: https://arxiv.org/abs/2604.23195
date: 2026-05-04
---

# AnalogRetriever: Learning Cross-Modal Representations for Analog Circuit Retrieval

Analog circuit design relies heavily on reusing existing intellectual property (IP), yet searching across heterogeneous representations such as SPICE netlists, schematics, and functional descriptions remains challenging. Existing methods are largely limited to exact matching within a single modality, failing to capture cross-modal semantic relationships. To bridge this gap, we present AnalogRetriever, a unified tri-modal retrieval framework for analog circuit search. We first build a high-quality dataset on top of Masala-CHAI through a two-stage repair pipeline that raises the netlist compile rate from 22% to 100%. Built on this foundation, AnalogRetriever encodes schematics and descriptions with a vision-language model and netlists with a port-aware relational graph convolutional network, mapping all three modalities into a shared embedding space via curriculum contrastive learning. Experiments show that AnalogRetriever achieves an average Recall@1 of 75.2% across all six cross-modal retrieval directions, significantly outperforming existing baselines. When integrated into the AnalogCoder agentic framework as a retrieval-augmented generation module, it consistently improves analog circuit design performance.
