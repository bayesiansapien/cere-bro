---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.02897
url: https://huggingface.co/papers/2611.02897
arxiv_url: https://arxiv.org/abs/2611.02897
date: 2026-11-03
---

# PhotoGuider: Composition-Aware Cropping and 360^{circ} View Framing with Explainable Photographic Assessments

Traditional image cropping assumes the photograph already contains the composition worth keeping, and asks only where to crop. A full 360^{circ} scene offers no such guarantee: the viewing direction in a scene has to be discovered before anything can be framed. We present PhotoGuider, a measure-then-frame method that answers both questions with compact learned scorers over one shared set of composition-aware features. The designed features are extracted using foundation and task-specific vision models and structured into four photographic tokens: Subject, Composition, Aesthetics, and Integrity. Our MLLM explainer is fine-tuned to generate composition-related explanations conditioned on images and measured token assessments. To our knowledge, PhotoGuider is the first method to combine explicit composition-based direction selection in 360^{circ} panoramas with refined framing, camera-parameter output for native re-rendering, and measurement-conditioned explanations. On two standard 2D cropping benchmarks, PhotoGuider achieves the highest average mIoU performance against ground-truth crops. In a blind ranking study, 120 participants ranked three cropping methods over 100 panoramic scenes from the public Poly Haven HDRI library, placing our framings first in 53.2% of cases, against 27.3% and 19.5% for two strong alternatives. Project page: https://ntuneillee.github.io/research/photoguider/
