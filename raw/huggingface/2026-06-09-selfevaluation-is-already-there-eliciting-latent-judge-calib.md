---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.05122
url: https://huggingface.co/papers/2606.05122
arxiv_url: https://arxiv.org/abs/2606.05122
date: 2026-06-09
---

# Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data

Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output? We find that the ability is largely present before any targeted training: prompted few-shot, a base model already predicts an external judge's multi-attribute quality scores on open-ended responses well above chance across three benchmarks. We introduce Self-Evaluation Elicitation (SEE), a method that surfaces this latent ability through a short cycle comprising a calibration-coupled reinforcement learning phase that improves the answer and predicts the judge, followed by a masked distillation phase that sharpens the prediction while leaving the answer untouched. From 160 unique examples, roughly 31x fewer than a reinforcement learning baseline, SEE improves held-out calibration across three benchmarks while preserving answer quality. The elicited self-evaluation is sharply localized within the model's own token distribution and stable across judges it was never trained against, indicating a transferable notion of quality rather than a single judge's preference. These results reframe judge-aligned self-evaluation as a problem of elicitation rather than acquisition.
