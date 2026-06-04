---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.03220
url: https://huggingface.co/papers/2606.03220
arxiv_url: https://arxiv.org/abs/2606.03220
date: 2026-06-04
---

# WebRISE: Requirement-Induced State Evaluation for MLLM-Generated Web Artifacts

Existing benchmarks for MLLM-generated web artifacts assess interaction through local evidence and miss the requirement-induced states and transitions that determine whether a page works. We introduce WebRISE, which compiles task requirements into Interaction Contract Graphs (ICGs) of observable states, user-intent transitions, and DOM/visual assertions for implementation-agnostic browser execution. WebRISE spans 442 tasks across five input modalities (Text, Markdown, Sketch, Image, Video), with 5,495 transitions and 5,271 requirement checks that separate user-stated functions from implicit product-level constraints. Across 14 MLLMs, even the strongest model reaches only 65.6% transition validity and 66.3% requirement coverage, and visual quality is no proxy for behavior (Qwen3.6-35B-A3B on Markdown: V=80.8 yet T=15.5). Video gives the strongest interaction signal (+10.6 pp implicit coverage over Text), while implicit constraints persist; defect injection shows ICG-based scoring detects state errors at 2-16x the rate of checkpoint-style evaluation.
