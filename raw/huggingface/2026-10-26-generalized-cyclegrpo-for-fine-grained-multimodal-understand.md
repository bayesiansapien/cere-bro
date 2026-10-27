---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800648+00:00
arxiv_id: 2610.29552
url: https://huggingface.co/papers/2610.29552
arxiv_url: https://arxiv.org/abs/2610.29552
date: 2026-10-26
---

# Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding

Fine-grained multimodal intelligence requires models to both understand a designated region and localize it from language. Existing methods learn these directions with separate objectives and task-specific annotations. We present Generalized CycleGRPO, the first unified reinforcement learning framework coupling region understanding and localization across spatial, temporal, and spatio-temporal domains. Given a region, a multimodal large language model generates candidate descriptions and then localizes each description to reconstruct the input region. Reconstruction overlap provides a verifiable reward for captioning, while individual localization rewards improve the inverse mapping. A common region-space formulation extends this cycle from image masks and boxes to video intervals and timestamped spatial evidence, without reference captions or an external language-model judge during reinforcement learning. In videos, the cycle encourages descriptions that distinguish a target event from similar recurrences. We introduce DOVE (Distinctive Occurrence-level Video-caption Evaluation), a human-verified contrastive benchmark for this temporal distinctiveness. CycleGRPO improves SAMTok's overall gIoU from 57.5% to 68.2% on GroundingSuite and average gIoU from 71.2% to 78.7% on GRES. For temporal tasks, it achieves 51.9% tIoU on Charades and 33.3% Temporal Evidence Coverage on DOVE, compared with 45.6% and 14.8% for the Qwen3-VL initialization. These results establish region-text cycle consistency as a general self-evaluation principle for multimodal understanding and localization. Models, code, and DOVE are available at https://devinxzhang.github.io/Generalized-CycleGRPO-Page/.
