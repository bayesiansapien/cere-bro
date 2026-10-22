---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.641448
arxiv_id: 2511.14102
url: https://huggingface.co/papers/2511.14102
arxiv_url: https://arxiv.org/abs/2511.14102
date: 2026-10-21
---

# Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading

Mixture-of-experts (MoE) models often exceed a single accelerator's memory capacity. Offloading experts to host memory creates a severe PCIe I/O bottleneck because data-dependent routing keeps transfers on the critical path. We present Specter, an inference system that uses quantization to combine speculative decoding with expert offloading. Its lightweight quantized draft model runs efficiently on device while preserving high-fidelity expert activation patterns. This provides accurate multi-step lookahead over future expert usage, allowing the runtime to organize expert movement and execution ahead of verification and improve both communication and execution efficiency. Under single-request inference, Specter achieves an average 1.50x (up to 1.88x) speedup in time per output token (TPOT) over the state-of-the-art system. Specter makes memory-constrained, single-GPU MoE inference more practical on commodity hardware. Our code is available at https://github.com/wwwwwf/specter_asplos.
