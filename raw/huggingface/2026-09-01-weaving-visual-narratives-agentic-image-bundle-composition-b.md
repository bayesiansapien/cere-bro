---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.28695
url: https://huggingface.co/papers/2608.28695
arxiv_url: https://arxiv.org/abs/2608.28695
date: 2026-09-01
---

# Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching

Image retrieval has traditionally been formulated as a point-wise matching problem, where each candidate image is scored in isolation. However, this atomic paradigm fails to capture the complexity of human search intent within personal photo collections, where users often seek compact visual stories bound by structural relations rather than isolated snapshots. To address this limitation, we introduce **Image Bundle Composition (IBC)**, a novel paradigm that shifts the objective from ranking individual images to dynamically composing cohesive image bundles from a massive, unstructured photo pool. Since target bundles are not predefined, IBC presents a severe combinatorial explosion challenge and demands modeling non-decomposable joint relevance. To establish this paradigm, we construct **IBCBench**, the first IBC benchmark dataset containing 109,467 images and 667 verified queries, built via a semi-automated verification pipeline. Furthermore, we propose **BundleWeaver**, an agentic framework that reformulates IBC as query-conditioned incremental hyperedge discovery. By employing a Large Language Model to adaptively search for missing relational roles and utilizing a Vision-Language Model for whole-bundle verification, BundleWeaver effectively navigates the combinatorial space. Extensive experiments demonstrate that while state-of-the-art embedding models and static decompose-and-rerank paradigms suffer from relational blindness, BundleWeaver achieves substantial performance gains, highlighting the necessity of shifting from atomic scoring to dynamic relational composition. Our dataset and code are available.
