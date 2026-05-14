---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2604.27695
url: https://huggingface.co/papers/2604.27695
arxiv_url: https://arxiv.org/abs/2604.27695
date: 2026-05-13
---

# EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory

Long-term conversational memory requires retrieving evidence scattered across multiple sessions, yet single-pass retrieval fails on temporal and multi-hop questions. Existing iterative methods refine queries via generated content or document-level signals, but none explicitly diagnoses the evidence gap, namely what is missing from the accumulated retrieval set, leaving query refinement untargeted. We present EviMem, combining IRIS (Iterative Retrieval via Insufficiency Signals), a closed-loop framework that detects evidence gaps through sufficiency evaluation, diagnoses what is missing, and drives targeted query refinement, with LaceMem (Layered Architecture for Conversational Evidence Memory), a coarse-to-fine memory hierarchy supporting fine-grained gap diagnosis. On LoCoMo, EviMem improves Judge Accuracy over MIRIX on temporal (73.3% to 81.6%) and multi-hop (65.9% to 85.2%) questions at 4.5x lower latency. Code: https://github.com/AIGeeksGroup/EviMem.
