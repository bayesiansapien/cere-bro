---
source: farmer/huggingface
farmed: 2026-08-08T23:44:03.927649
arxiv_id: 2608.05369
url: https://huggingface.co/papers/2608.05369
arxiv_url: https://arxiv.org/abs/2608.05369
date: 2026-08-08
---

# World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation

Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context. To address this limitation, we present World-to-Wrist VLA (W2-VLA), a VLA model for fine-grained robot manipulation with task-conditioned future wrist modeling. Given current multi-view observations and a task instruction, W2-VLA contextualizes a set of latent modeling tokens as a compact interface between the vision-language model and the wrist predictor. Conditioned on this interface and the observed wrist history, the predictor forecasts future wrist latents, which are transformed into future-aware context for action prediction. In addition, we introduce W2-CoT, a synthesis pipeline that produces structured annotations describing manipulation progress, physical transition cues, and wrist-local evidence. These annotations provide auxiliary supervision that shapes the task-conditioned latent interface. Experiments on LIBERO, RoboTwin 2.0, and real-world manipulation tasks demonstrate improved fine-grained and contact-sensitive manipulation across both single-arm and bimanual settings, while maintaining action-generation rates above 80 Hz.
