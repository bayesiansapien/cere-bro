---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.158149+00:00
arxiv_id: 2610.38352
url: https://huggingface.co/papers/2610.38352
arxiv_url: https://arxiv.org/abs/2610.38352
date: 2026-10-30
---

# WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video

Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We address this gap with WeVisCut, a long-form script-to-video system that connects tool execution with policy learning. Its agent harness maintains shared production state so that tool feedback informs subsequent decisions and repairs. Because finished videos do not expose these decisions, our four-stage data pipeline combines editing inversion with verified replay to turn recovered editing intent into executable supervision. Applied to 3,750 finished videos, this pipeline yields over 130K training examples. We use this supervision to train a single 9B policy that coordinates production and recovers from failures within the same harness. Moreover, we introduce a 100-task benchmark and five metrics assessing editing quality and delivery reliability. Under a shared tool environment, WeVisCut substantially outperforms its base model and achieves comparable performance to Claude Opus 5 while using nearly 33x fewer generated tokens per successful output minute. It also outperforms task-matched native editors on our proposed metrics.
