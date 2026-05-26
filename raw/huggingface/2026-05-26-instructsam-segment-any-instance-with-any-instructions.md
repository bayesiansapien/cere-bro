---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26102
url: https://huggingface.co/papers/2605.26102
arxiv_url: https://arxiv.org/abs/2605.26102
date: 2026-05-26
---

# InstructSAM: Segment Any Instance with Any Instructions

In this paper, we introduce InstructSAM, a unified and streamlined framework designed for multi-instance segmentation under arbitrary instructions. We formulates instruction-driven instance segmentation as a set-structured query prediction problem and propose an explicit reasoning-to-instance query interface that elegantly bridges a vision-language model (VLM) and SAM3. Specifically, a bank of learnable instance queries is injected into the VLM and contextualized with instruction and visual information, enabling each query to serve as an instance-aware slot. A hybrid-attention mechanism further promotes interaction among these queries, visual tokens, and instruction tokens, improving instance enumeration and reducing duplicate predictions. The resulting LLM-conditioned queries are projected into SAM3's detector query space to drive accurate multi-instance segmentation in a single forward pass. This design equips SAM3 with high-level instruction understanding, compositional reasoning, and instance-level set prediction without modifying its core architecture. To support training and evaluation, we further construct Inst2Seg, a high-quality and large-scale instruction-based instance segmentation dataset and benchmark that couples free-form instructions with instance-level masks. Extensive experiments show that only 2B-scale InstructSAM achieves strong results across complex instruction-driven and phrase-level referring segmentation benchmarks, outperforming prior end-to-end methods and SAM3's agentic pipeline while enabling efficient single-pass multi-instance prediction.
