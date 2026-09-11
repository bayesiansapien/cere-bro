---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.06806
url: https://huggingface.co/papers/2609.06806
arxiv_url: https://arxiv.org/abs/2609.06806
date: 2026-09-10
---

# Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning

Training strategy, namely whether to retrain from scratch or fine-tune from the previous checkpoint, is an overlooked decision variable in active learning. We show that this choice has exploitable structure: retraining is most useful in early rounds, when each batch can substantially reshape the labeled distribution, while fine-tuning becomes safer once the model trajectory stabilizes. We propose HybridAL, an adaptive training schedule that monitors an online stabilization signal and switches from retraining to fine-tuning after sustained stabilization. Two complementary signals, spectral exponent change Δα (weight-based) and accuracy change ΔAcc (validation-based), span different points on the time-calibration trade-off. Across three encoder backbones and six text-classification tasks (five seeds each), HybridAL keeps endpoint macro-F1 non-inferior to retraining and fine-tuning at a 0.010 margin, saves up to 49% of retraining time, and recovers a substantial fraction of retraining's calibration advantage as measured by negative log-likelihood (NLL). Compared with schedules that switch at a pre-committed round, HybridAL obtains lower NLL at moderate additional cost, showing that trajectory-dependent switching provides a stronger time-calibration trade-off than fixed early switching.
