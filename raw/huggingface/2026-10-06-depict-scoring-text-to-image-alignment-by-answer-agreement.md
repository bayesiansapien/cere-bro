---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.03617
url: https://huggingface.co/papers/2610.03617
arxiv_url: https://arxiv.org/abs/2610.03617
date: 2026-10-06
---

# DEPICT: Scoring Text-to-Image Alignment by Answer Agreement

Image-text alignment is a core problem in computer vision with applications in caption evaluation, hallucination detection, data curation, and the benchmarking of text-to-image (T2I) generators. As T2I models improve, benchmarking has become demanding, requiring metrics capable of finding a series of issues like missing objects, swapped attributes, miscounts, and ignored negations. Recent work addresses this by fine-tuning evaluators on preference data or by prompting a vision-language model, either holistically with the caption or with decomposed verification questions. However, existing approaches fall short: fine-tuned metrics remain bound to one backbone and training distribution; holistic metrics miss fine-grained details; and decomposed metrics rely on a fixed-YES assumption that penalizes faithful images whenever that assumption fails. In contrast, we propose DEPICT, a training-free metric that replaces fixed reference answers with expected agreement between image-based and caption-only answers, weighting questions by how decisively the caption determines them. By replacing fixed references, our agreement rule increases negation accuracy from 19% to 88%. To recover the context lost during decomposition, DEPICT merges this agreement score with a holistic score. We evaluate DEPICT on five benchmarks and eleven backbones from three model families and find that it surpasses all training-free metrics and exceeds fine-tuned evaluators on two out of three human-correlation benchmarks.
