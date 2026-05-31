---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.30010
url: https://huggingface.co/papers/2605.30010
arxiv_url: https://arxiv.org/abs/2605.30010
date: 2026-05-31
---

# EarlyTom: Early Token Compression Completes Fast Video Understanding

Video large language models (Video-LLMs) have demonstrated strong capabilities in video understanding tasks. However, their practical deployment is still hindered by the inefficiency introduced by processing massive amounts of visual tokens. Although recent approaches achieve extremely low token retention ratios while maintaining accuracy comparable to full-token baselines, most of them perform compression only at the late stage of prefilling, leaving the efficiency of the vision encoder unoptimized. In this paper, we first show that vision encoding contributes a large portion to the time-to-first-token (TTFT). Therefore, instead of compressing visual tokens only after the vision encoder, performing compression inside the encoder still leaves substantial room for exploration. Based on this insight, we propose EarlyTom, a training-free token compression framework that performs early-stage visual token compression inside the vision encoder, enabling significantly better TTFT reduction and higher throughput. In addition, we introduce a decoupled spatial token selection strategy that improves the overall compression effectiveness. EarlyTom reduces TTFT by up to 2.65x and FLOPs by up to 61% on a single NVIDIA A100 GPU for the LLaVA-OneVision-7B model, while maintaining accuracy comparable to the full-token baseline. These improvements substantially enhance the practicality of deploying Video-LLMs in real-world production scenarios.
