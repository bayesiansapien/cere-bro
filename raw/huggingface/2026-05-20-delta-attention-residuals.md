---
source: farmer/huggingface
farmed: 2026-05-20T09:54:55.019281+00:00
arxiv_id: 2605.18855
url: https://huggingface.co/papers/2605.18855
arxiv_url: https://arxiv.org/abs/2605.18855
date: 2026-05-20
---

# Delta Attention Residuals

Attention Residuals replace standard additive residual connections with learned softmax attention over previous layer outputs, enabling selective cross-layer routing. However, standard Attention Residuals still attend over cumulative hidden states in previous layers, which are highly redundant. We show that this redundancy leads to routing collapse in deeper layers: attention weights become low-contrast and closer to uniform (max weight ${\approx}$0.2), limiting the model&#39;s ability to select informative states in previous layers. This raises a key but underexplored design question: what layer-wise representations should be routed in Attention Residuals? To answer this question, we propose Delta Attention Residuals, which attend over deltas -- the change introduced by each sublayer ($\mathbf{v}_i = \mathbf{h}_{i+1} - \mathbf{h}_i$) -- instead of cumulative states. Delta representations are structurally diverse and yield higher-contrast attention distributions (max weight ${\approx}$0.6), enabling more selective and effective routing across layers. This principle applies at both per-sublayer and block granularity. Across all tested scales (220M--7.6B), Delta Attention Residuals consistently outperform both standard residuals and Attention Residuals, with 1.7--8.2\% validation perplexity gains. Delta Attention Residuals also enables converting pretrained checkpoints into Delta Attention Residuals via standard fine-tuning. Code is available at this https URL .
