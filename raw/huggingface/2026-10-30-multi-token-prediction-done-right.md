---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.158520+00:00
arxiv_id: 2610.38331
url: https://huggingface.co/papers/2610.38331
arxiv_url: https://arxiv.org/abs/2610.38331
date: 2026-10-30
---

# Multi-Token Prediction Done Right

Multi-Token Prediction (MTP) is now a common ingredient in language-model pre-training, as it improves downstream performance and enables faster inference through speculative decoding. We identify a flaw in standard MTP training, in which a residual component of the MTP gradient interferes with both next-token and multi-token learning, increasingly so with scale. Specifically, the MTP cross-entropy gradient can be decomposed exactly into a KL self-distillation term that pulls each MTP head toward the model's own next-token prediction (NTP) distribution and improves speculative decoding, and a residual that has a low signal-to-noise ratio and buries the useful KL signal. We introduce the KL gradient-recovery trick: when two distributions share a linear output head, the gradient of their KL divergence can be recovered exactly by combining their cross-entropy gradients through straight-through gradient routing. Unlike minimizing the KL directly, this trick requires no vocabulary-sized logit matrices and is compatible with standard fused cross-entropy kernels. This enables Soft Multi-Token Prediction (Soft-MTP), a one-line code change to MTP that removes the noisy residual and backpropagates only the KL self-distillation signal by reusing the existing NTP and MTP cross-entropy computations. Soft-MTP supports both DeepSeek- and Meta-style MTP, adds no parameters, and incurs no measurable overhead. From 167M to 1.2B parameters, Soft-MTP improves over standard MTP with lower NTP perplexity, faster speculative decoding and higher zero-shot accuracy at every scale, lower MTP perplexity from 689M onward, and stronger math and code reasoning after fine-tuning at 1.2B. Soft-MTP also matches, if not exceeds, direct KL divergence minimization on most metrics. Soft-MTP is, in effect, a free lunch for MTP optimization. Our code can be found at https://github.com/JaydenTeoh/Soft-MTP.
