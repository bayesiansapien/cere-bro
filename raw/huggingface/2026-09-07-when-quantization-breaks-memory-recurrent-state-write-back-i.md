---
source: farmer/huggingface
farmed: 2026-09-07T09:18:04.961411
arxiv_id: 2609.04490
url: https://huggingface.co/papers/2609.04490
arxiv_url: https://arxiv.org/abs/2609.04490
date: 2026-09-07
---

# When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference

Quantization is widely used to reduce the computational and memory demands of neural-network inference. In recurrent networks, however, the quantized state is stored and returned at the next time step, so the rule used to store that state can alter subsequent computations. Here, we introduce recurrent-state write-back to denote this rule and isolate its effect in a compact GRU encoder--decoder for fluorescence lifetime imaging, a molecular imaging modality used in quantitative biological imaging. A central task is estimating two lifetime parameters, the short-lived component τ1 and the long-lived component τ2, from high-noise time-resolved fluorescence signals. Holding the trained model fixed, replacing continuous state propagation with deterministic 4-bit state storage increases estimation errors for τ1 and τ2 by approximately 70x and 300x, respectively. Failure occurs when repeated small updates remain below the write threshold, leaving the stored state nearly fixed while the network continues to propose change. Error feedback, residual memory, and direction memory carry information from these suppressed updates across time and recover accuracy without retraining. Precision sweeps show that increasing state precision can worsen a fixed recurrent solution, while matched training shows that compatibility with the state interface can be learned. To test whether this behavior extends beyond the GRU, we repeat the post-training intervention in an independently trained LSTM, where coarse write-back reproduces the failure, error feedback restores accuracy, and state-specific interventions reveal greater sensitivity of the cell state than the hidden state. Our results establish recurrent-state write-back as a key determinant of low-precision recurrent dynamics and identify the state-storage interface as a central design consideration for quantized recurrent inference.
