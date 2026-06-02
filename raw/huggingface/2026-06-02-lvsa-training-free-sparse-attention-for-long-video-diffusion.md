---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.31057
url: https://huggingface.co/papers/2605.31057
arxiv_url: https://arxiv.org/abs/2605.31057
date: 2026-06-02
---

# LVSA: Training-Free Sparse Attention for Long Video Diffusion

Dense self-attention is the compute and quality bottleneck of long-video diffusion inference: cost grows quadratically with the sequence length, and beyond the training horizon the model converges to near-static output, that is, "frozen" repetitive video. State of the art approaches are either too costly, e.g., they require retraining, or fail to satisfy both performance and quality objectives in a scalable manner. To this end, we introduce Long Video Sparse Attention (LVSA), a training-free model-agnostic block-sparse attention for video diffusion transformers that combines a structured window pattern with rotating global anchors, thus removing the fixed-grid bias which causes long-range temporal artifacts. LVSA, combined with a FlashInfer kernel, reduces compute up to 3.17x on Wan 2.1 1.3B at a 6x horizon, 2.98x on Wan 2.1 14B at a 6x horizon, and 3.33x on HunyuanVideo 1.5 at a 1.5x horizon, compared to dense attention. Beyond reducing compute, LVSA enables HunyuanVideo 1.5 generation at a 2x horizon, which is otherwise out-of-memory on a single GPU. Moreover, LVSA provides speedups up to 2.41x compared to RIFLEx and 3.27x compared to UltraViCo on Wan 2.1 1.3B. To demonstrate applicability across diverse platforms, we apply LVSA on NPUs and achieve speedups up to 2.71x on Wan 2.2 A14B and 3.24x on Wan 2.1 1.3B compared to dense attention. To evaluate quality in a fair way, we introduce VQeval, a tool properly scoring loopy video failures, which instead are rewarded in state of the art evaluators like VBench-Long. LVSA is quality-neutral for generation at training horizon length and quality-positive at extended lengths.
