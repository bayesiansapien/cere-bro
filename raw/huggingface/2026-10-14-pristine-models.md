---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.507180+00:00
arxiv_id: 2610.14091
url: https://huggingface.co/papers/2610.14091
arxiv_url: https://arxiv.org/abs/2610.14091
date: 2026-10-14
---

# Pristine Models

Training on broad, unfiltered data enables high-quality image generation, but can also teach models concepts that should not be generated; restricting the training data ensures safety, but reduces quality because examples containing unsafe concepts also provide useful knowledge that is not itself unsafe. Existing approaches largely address this trade-off post hoc through concept unlearning, which can lead to catastrophic forgetting as the number of concepts to remove grows. We instead ask whether unsafe concept knowledge can be compartmentalized during pretraining so that access to it can be disabled at inference. We introduce Pristine Models, a novel text-to-image generation architecture with an attention mechanism that encourages the separation of safe and unsafe knowledge into independently parameterized branches. The branch-specific parameters are learned during training, while the unsafe branch can be detached at inference. On ImageNet, Pristine Models enable safer generation while retaining much of the utility of full-data pretraining, achieving higher image quality and better text alignment than training only on safe data or applying post-hoc concept removal. We further scale our approach to CC12M, demonstrating that it remains effective in a substantially larger and more diverse open-world pretraining setting.
