---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.18149
url: https://huggingface.co/papers/2607.18149
arxiv_url: https://arxiv.org/abs/2607.18149
date: 2026-07-23
---

# Differentiable Logic Gate Networks for Low-Latency EEG Classification on Edge Devices

Real-time EEG classification on edge devices is bottlenecked by the floating-point arithmetic of conventional neural networks. We investigated Differentiable Logic Gate Networks (Diff-Logic) as a hardware-native alternative that compiles models into pure Boolean circuits executable via bitwise CPU operations. Through rigorous iso-parameter experiments across four EEG datasets spanning two classification tasks, binary dementia detection and 3-class emotion recognition, we compared Diff-Logic against matched-capacity Multi-Layer Perceptron (MLP) and Binarized Neural Network (BNN) baselines at four complexity tiers (50k-500k parameters). On dementia screening, Diff-Logic achieved 80.2% Macro F1, outperforming the MLP baseline by 6.8%. On emotion recognition, the MLP retained a moderate performance advantage but incurred a 2.3times higher latency and 14times larger model size when deployed on a power-constrained (7W) Nvidia Jetson Orin Nano CPU (Single-core). Critically, Diff-Logic inference time remained nearly constant across a 10times increase in model scale, achieving a peak speedup of 2.9times over MLPs at the largest complexity tier. Our results establish logic-based neural architectures as a practical paradigm for resource-constrained brain-computer interfaces, achieving competitive or superior performance while natively satisfying the latency and memory constraints of portable edge deployment. Code is available on GitHub: https://github.com/Shyamal-Dharia/eeg-difflogic
