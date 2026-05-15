---
source: farmer/huggingface
farmed: 2026-05-15T00:00:00Z
arxiv_id: "2605.15182"
url: https://huggingface.co/papers/2605.15182
arxiv_url: https://arxiv.org/abs/2605.15182
date: 2026-05-15
---

# Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video

Camera-controlled video generation has made substantial progress, enabling generated videos to follow prescribed viewpoint trajectories. However, existing methods usually learn camera-specific conditioning through camera encoders, control branches, or attention and positional-encoding modifications, which often require post-training on large-scale camera-annotated videos. Training-free alternatives avoid such post-training, but often shift the cost to test-time optimization or extra denoising-time guidance. We propose Warp-as-History, a simple interface that turns camera-induced warps into camera-warped pseudo-history with target-frame positional alignment and visible-token selection. Given a target camera trajectory, we construct camera-warped pseudo-history from past observations and feed it through the model's visual-history pathway. Crucially, we align its positional encoding with the target frames being denoised and remove warped-history tokens without valid source observations. Without any training, architectural modification, or test-time optimization, this modification reveals a non-trivial zero-shot capability of a frozen video generation model to follow camera trajectories. Moreover, lightweight offline LoRA finetuning on only one camera-annotated video further improves this capability and generalizes to unseen videos, improving camera adherence, visual quality, and motion dynamics without test-time optimization or target-video adaptation. Extensive experiments on diverse datasets confirm the effectiveness of our method.
