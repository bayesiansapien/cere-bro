---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.21556
url: https://huggingface.co/papers/2607.21556
arxiv_url: https://arxiv.org/abs/2607.21556
date: 2026-07-24
---

# Visual Contrastive Self-Distillation

On-policy self-distillation (OPSD) is promising as it removes the external teacher required by on-policy distillation (OPD), yet it still needs asymmetric information between teacher and student to ensure that the self-teacher provides a stronger learning signal than the student. Existing methods create this asymmetry either through privileged answers or visual evidence. We ask whether both can be removed, yielding a simpler form of OPSD driven purely by input conditioning. For this purpose, we propose Visual Contrastive Self-Distillation, namely VCSD, which converts image-content removal into an on-policy self-distillation signal. At each student-generated response prefix, the EMA teacher produces two next-token distributions under the same prompt and prefix -- one conditioned on the original image and the other on a content-erased control. Their token-wise log-probability difference highlights candidates whose likelihood is specifically increased by the instance-level visual content. We use this contrast to sharpen the teacher's original-image distribution within its plausible support, and distill the resulting full-distribution target into the student. Using ViRL39K dataset, VCSD consistently outperforms matched OPSD across Qwen3-VL and Qwen3.5 models. For example, on Qwen3-VL, it improves the seven-benchmark aggregate from 62.27% rightarrow 67.04% at 2B, 71.30% rightarrow 73.16% at 4B, and 72.51% rightarrow 76.26% at 8B. Furthermore, VCSD requires no external teacher, privileged answers, visual evidence signals, reasoning traces, or additional inference-time cost.
