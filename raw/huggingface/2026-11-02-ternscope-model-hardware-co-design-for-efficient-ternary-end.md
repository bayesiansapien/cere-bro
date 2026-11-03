---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.501567+05:30
arxiv_id: 2610.29617
url: https://huggingface.co/papers/2610.29617
arxiv_url: https://arxiv.org/abs/2610.29617
date: 2026-11-02
---

# TernScope: Model-Hardware Co-Design for Efficient Ternary Endoscopic Segmentation

Edge medical segmentation must reconcile small model size, high accuracy, and fast inference. TernScope addresses this tradeoff through model--hardware co-design, learning a compact segmentation network whose low-bit operators also simplify hardware execution. Split-channel large-kernel blocks preserve spatial context with limited computation, while branch fusion removes redundant inference paths. Ternary Progressive Quantization-aware Training (TPQ) then adapts the fused network from deep to shallow layers, through the decoder, and finally to the input and prediction layers. All 25 convolutions use ternary weights and 8-bit activations, enabling packed storage and multiplier-free computation. The resulting model uses 0.2483 M parameters and 0.0949 GMACs while retaining competitive segmentation accuracy on in-domain and external datasets. Under the same 45 nm technology, TernScope reduces compute-array area by 88.46% compared with the original Gemmini, a systolic-array accelerator with 8-bit times 8-bit multipliers. These results demonstrate a path from accurate lightweight medical segmentation to compact low-bit hardware.
