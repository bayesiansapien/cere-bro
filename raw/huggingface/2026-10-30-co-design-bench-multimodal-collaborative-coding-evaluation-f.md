---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.157766+00:00
arxiv_id: 2610.35138
url: https://huggingface.co/papers/2610.35138
arxiv_url: https://arxiv.org/abs/2610.35138
date: 2026-10-30
---

# Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models

Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real user coding sessions. Its two tracks, Multimodal Editing (ME) and Repository Editing (RE), cover localized edits with optional image, audio, video, or document inputs and coordinated repository revisions. Tasks span three capability dimensions: Grounded Understanding, UI Transformation, and Functional Implementation. The tasks pair normalized requests and runnable pre-edit applications with 2,331 hidden expert-authored acceptance criteria. Our judge-then-refute protocol grades criteria using source and browser evidence, challenges positive verdicts with a separate LLM verifier, and audits visual and interaction claims without gold code or target screenshots. Under a shared agentic harness, the strongest of ten model endpoints passes an average of 69.9% of criteria per task but fully satisfies only 26.4% of tasks. All ten endpoints achieve lower criterion completion on repository edits spanning three or four change types than on those spanning one or two. Co-Design Bench provides a testbed for studying the gap between partial requirement satisfaction and complete task success under agentic execution for real-user application revisions.
