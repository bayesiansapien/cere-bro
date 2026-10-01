---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34309
url: https://huggingface.co/papers/2609.34309
arxiv_url: https://arxiv.org/abs/2609.34309
date: 2026-09-30
---

# MaLiang-Harness: A Programmable Path to Image and Video Generation

Executable programs offer explicit control over how images and videos are constructed, but generating runnable code is only the beginning of visual creation. A program can execute correctly while violating the requested composition, appearance, or motion. We define this discrepancy as the Program-to-Visual (P2V) gap and introduce MaLiang-Harness, a unified framework for organizing MLLM-driven visual generation into a persistent process of construction, inspection, and revision. Its central design is to make the evolving visual program, its construction history, and its verification share a common revision reference. We define the Persistent Executable Generation (PEG) state as preserving programs and task context. Traceable Generation Process (TGP) connects edits to rendered evidence, and Revision-aware Editing and Verification (REV) supports restoration and checks the current revision before completion. Together, these mechanisms coordinate planning, execution, and visual feedback across rendering backends. We evaluate 11 powerful closed-source MLLMs on MaLiang-IBench and four on MaLiang-VBench, measuring generation success, visual quality, and computational cost. GPT-6-Astra achieves 100% generation success on both benchmarks, with 96.0% of image tasks and 76.9% of video tasks meeting all quality thresholds. The comparison also reveals a mismatch between general capability scores and visual generation performance, with similarly scored models differing substantially in their ability to satisfy visual requirements. MaLiang-Harness provides a systematic basis for studying how MLLMs translate executable code into visual outcomes, exposing both the potential of programmable generation and the limitations of general benchmarks as predictors of this ability. The project is available at https://github.com/gulucaptain/MaLiang-Harness.
