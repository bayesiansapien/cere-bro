---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.15142
url: https://huggingface.co/papers/2606.15142
arxiv_url: https://arxiv.org/abs/2606.15142
date: 2026-06-17
---

# MotionVLA: Vision-Language-Action Model for Humanoid Motion

Generating realistic humanoid motion from scene images and text involves both low-frequency pose semantics and high-frequency physical dynamics. However, many existing methods tokenize motion with a single shared codebook, forcing heterogeneous motion signals into the same quantization space. Our frequency-domain analysis of human motion data reveals a clear mismatch between single-codebook quantization and motion statistics: five DCT coefficients capture 93% of joint-position energy but only 37% of joint-velocity energy, which can bias quantization toward pose statistics and under-represent high-frequency velocity components. A second challenge lies in adapting a standard autoregressive model to effectively model high-frequency physical signals in motion sequences. Therefore, we propose DSFT, a dual-stream frequency tokenizer that separates motion into Base and physical streams and compresses them independently with DCT truncation and BPE. Furthermore, we present MotionVLA, a Qwen3.5-based model that arranges Base and physical tokens in a unified sequence, where Phys tokens are predicted after Base tokens. Experiments on HumanML3D and MBench show that, despite using a lightweight 2B backbone, MotionVLA reduces the Diversity gap to real data by over 50% on HumanML3D and improves Motion-Condition Consistency by 3.8% on MBench, supporting frequency-aware dual-stream decoupling as an effective formulation for autoregressive motion generation. Code: https://github.com/AIGeeksGroup/MotionVLA. Website: https://aigeeksgroup.github.io/MotionVLA.
