---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05739
url: https://huggingface.co/papers/2610.05739
arxiv_url: https://arxiv.org/abs/2610.05739
date: 2026-10-06
---

# HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models

Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts. Softmax attention retains the full generation history through a growing KV cache, whereas recurrent linear attention compresses history into fixed-size states with substantially lower memory cost. However, we identify severe long-range forgetting in Gated DeltaNet (GDN), where information from distant but relevant scenes is progressively attenuated by subsequent state updates. To address this limitation, we propose HLA-WM, a training-free hybrid linear-attention framework that combines coarse-grained geometry-guided retrieval with fine-grained recurrent linear-state computation. HLA-WM exploits the affine structure of GDN to cache compact chunk-wise transition summaries, retrieve scene-relevant historical chunks using camera geometry, and recompose them into query-specific recurrent states. On the 60-second SANA-WM-Bench, HLA-WM improves all six aggregate revisit-consistency and camera-control metrics of the base autoregressive generator without additional training, including a 0.74 dB PSNR gain and a 28.5% reduction in rotation error. The improvements persist after downstream refinement and generalize to MBench-A, where HLA-WM consistently improves all three revisit-consistency metrics across all four subsets and all evaluated inference modes over 547 samples. At a 60-second context, HLA-WM reduces historical-state memory by 12times relative to full KV caching while incurring at most a 1.6% reduction in inference throughput. These results demonstrate that selectively addressable recurrent memory can improve long-range scene recall while preserving the efficiency advantages of GDN. Project page: https://caesarhhh.github.io/hla-wm/
