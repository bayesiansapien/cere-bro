---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2609.03153
url: https://huggingface.co/papers/2609.03153
arxiv_url: https://arxiv.org/abs/2609.03153
date: 2026-09-05
---

# VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement

Visual fluency in generated video does not imply physical reliability, and a scalar quality score alone is incapable of indicating the obligation a clip violates or the moment it fails. We present VeriPhy, an auditable physical-verification system in which a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed. During execution, observations gate and scope only declared calls to frozen low-level experts (e.g., segmentation and tracking, counting, eleven typed physical measurements over the resulting tracks, depth, OCR, and audio-event detection). Each action returns a provenance-carrying evidence record whose payload, when usable, is either a typed measurement or an explicitly tagged learned state. Typed resolvers and fixed composition map usable records to a three-valued state (supported, contradicted, or unknown, surfaced as plausible, implausible, or abstain) with full provenance, so that every verdict is traceable to the evidence that produced it. We anchor evaluation in a 1,500-clip corpus of human-annotated flaw records that localize real generation failures in prompt reference, space, and time. On a 149-clip core carrying 304 such records, VeriPhy accounts for 228, against 164 for a published question-decomposition evaluator given the same clips and the same claims. Recall alone does not separate it from prompting the same backbone monolithically, which reaches 222; what separates them is that each decision retains its evidence record and provenance, making the traces auditable one verdict at a time and usable as the interface through which a critic verdict could be written back into generation.
