---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13667
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13667
published: 2026-04-16
authors: Cihan Ruan, Lebin Zhou, Bingqing Zhao
---

# From Pixels to Nucleotides: End-to-End Token-Based Video Compression for DNA Storage

**arXiv:** https://arxiv.org/abs/2604.13667
**Authors:** Cihan Ruan, Lebin Zhou, Bingqing Zhao

## Abstract

arXiv:2604.13667v1 Announce Type: new  Abstract: DNA-based storage has emerged as a promising approach to the global data crisis, offering molecular-scale density and millennial-scale stability at low maintenance cost. Over the past decade, substantial progress has been made in storing text, images, and files in DNA -- yet video remains an open challenge. The difficulty is not merely technical: effective video DNA storage requires co-designing compression and molecular encoding from the ground up, a challenge that sits at the intersection of two fields that have largely evolved independently. In this work, we present HELIX, the first end-to-end neural network jointly optimizing video compression and DNA encoding -- prior approaches treat the two stages independently, leaving biochemical constraints and compression objectives fundamentally misaligned. Our key insight: token-based representations naturally align with DNA's quaternary alphabet -- discrete semantic units map directly to ATCG bases. We introduce TK-SCONE (Token-Kronecker Structured Constraint-Optimized Neural Encoding), which achieves 1.91 bits per nucleotide through Kronecker-structured mixing that breaks spatial correlations and FSM-based mapping that guarantees biochemical constraints. Unlike two-stage approaches, HELIX learns token distributions simultaneously optimized for visual quality, prediction under masking, and DNA synthesis efficiency. This work demonstrates for the first time that learned compression and molecular storage converge naturally at token representations -- suggesting a new paradigm where neural video codecs are designed for biological substrates from the ground up.
