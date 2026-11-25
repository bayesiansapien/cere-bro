---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.930756+00:00
arxiv_id: 2611.13730
url: https://huggingface.co/papers/2611.13730
arxiv_url: https://arxiv.org/abs/2611.13730
date: 2026-11-24
---

# Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence

Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits. We present tritify, an open-source runtime that executes the forward pass of real models -- decoder-only language models, Mixture-of-Experts decoders, and the Segment Anything 2.1 image/video stack -- with the entire run-time path in exact integer arithmetic; floating point is confined to offline quantization and the float reference used for verification. We make three separate claims and verify each. (1) Cross-hardware reproducibility: the integer path produces bit-identical output run to run, across CPU instruction-set architectures, and across CPU/GPU, carried by a reproducing SHA-256 of the output. (2) Decision fidelity: the integer path reproduces the float reference's decision on the models and inputs tested, with the numeric exceptions measured; per-layer fidelity through sixteen layers of OLMoE-1B-7B and of a 106-billion-parameter MoE shows no fidelity cliff. (3) Location independence: a model's computation can be split across instruction sets, CPU and GPU, and networked machines with zero effect on the output bits. GLM-4.5-Air (106,852,251,264 parameters, 427 GB of integer codes) generated its answer across three machines, none of which can hold its integer codes in RAM, bit-identically to a single-host reference. The consequence is verifiable distributed inference: an untrusted server or a fleet of devices runs the model while an open scalar oracle re-derives the exact bytes; a guarantee against a dishonest server is future work. We do not claim a per-device speed-up, bit-equality of floating-valued intermediates, or confidentiality. Code: https://github.com/pelloran-inc/tritify
