---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.312240+05:30
arxiv_id: 2609.38466
url: https://huggingface.co/papers/2609.38466
arxiv_url: https://arxiv.org/abs/2609.38466
date: 2026-10-08
---

# PAMI: Part Anchored Motion for Text to Human-Object Interaction Generation

Text-conditioned full-body human-object interaction (HOI) generation requires synthesizing human motion and object trajectories that match the input text while remaining precisely coordinated over time. Most methods represent the human and object as separate trajectories and predict the global human-object couplings. Learning this complex, dynamically changing relationship implicitly, however, often yields object drift, missed contact, and penetration. We introduce PAMI, a Part-Anchored Motion framework for Interaction generation. Inspired by the classic Hough Transform, our key idea is to localize object motion by letting body-part anchors vote for it: we express object motion relative to multiple body-part anchors and use PamiVAE to learn an interaction latent space, decoding frame-wise weights that aggregate these part-specific votes. Building on this representation, PAMI generates interactions in a coarse-to-fine hierarchy. PamiGen first generates a coarse human-object interaction from text in this structured latent space, and PamiRefiner then recursively resolves fine-grained contact geometry using a hybrid surface-sensing representation, combining long-range probes that capture overall body-part influence with short-range sensors that resolve detailed contacts near the object surface. Experiments on InterAct show that PAMI generates more faithful interactions and more accurate human-relative object motion than previous methods, achieving 14.5% higher contact recall than the previous state of the art. Extensive ablations validate the contributions of both the part-anchored voting representation and hybrid surface-sensing refinement.
