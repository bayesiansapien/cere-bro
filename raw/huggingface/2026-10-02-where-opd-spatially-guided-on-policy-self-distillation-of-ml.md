---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820364+00:00
arxiv_id: 2610.02117
url: https://huggingface.co/papers/2610.02117
arxiv_url: https://arxiv.org/abs/2610.02117
date: 2026-10-02
---

# Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes

On-policy self-distillation has recently emerged as an effective approach for improving language-model reasoning by supervising students with a frozen or EMA version of themselves that receives privileged information. Its application to multimodal large language models (MLLMs), however, remains largely unexplored. Recent approaches use privileged visual information, such as image crops corresponding to a question, to improve fine-grained perception, but their gains are confined to tasks that benefit from such visual zooming and require either human-annotated grounding data or external teacher models. We introduce a different form of on-policy self-distillation for MLLMs that provides the teacher with textual, spatially grounded guidance identifying the visual elements relevant to a query. We use procedurally generated scenes with automatically available object identities and spatial coordinates, enabling scalable and annotation-free post-training. The teacher uses this spatial guidance to locate and integrate evidence from multiple relevant image regions, while the student learns to reproduce the resulting behavior from the image and question alone. Our approach consistently improves performance on counting, document and chart understanding benchmarks across multiple models. Importantly, although post-training uses only synthetic scenes, the resulting improvements transfer to real-world perception benchmarks, yielding a 3.23-point gain in average performance across CVBench, V*, ZoomBench, BLINK, HR-Bench, and MME-RealWorld. These results show that spatially grounded privileged information can induce broader perceptual capabilities through on-policy self-distillation, enabling substantial synthetic-to-real transfer beyond the task and data distribution used for post-training. Project page: https://github.com/sirkosophia/Where-OPD
