---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.158863+00:00
arxiv_id: 2610.37786
url: https://huggingface.co/papers/2610.37786
arxiv_url: https://arxiv.org/abs/2610.37786
date: 2026-10-30
---

# WebAnything: From the Wild Web to Scalable Agent Environments

Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities.
  We present WebAnything, a fully automated framework that reconstructs source-grounded, reusable Web environments from real URLs without per-site manual implementation or repair after initial setup and authorization. An Explorer-Builder collects browser-observable structures, resources, and interaction outcomes; an independent verifier checks frozen candidates and guides local repair or targeted source recapture.
  We construct 244 website artifacts across 14 application domains and 53 categories, supporting 12,984 executed and accepted tasks. Compared with human-assisted WebHarbor, WebAnything achieves higher aggregate scores on three fidelity metrics, with 12 wins, two ties, and no losses in a blind audit. Fine-tuning Qwen3.5-9B on 5,856 interaction trajectories improves REAL success by 9.9 percentage points, Odysseys-Easy Rubric Avg and Task Avg by 6.25 and 6.32 percentage points, and WebArena-Verified Overall success by 13.33 percentage points under the fixed harness. Code: https://github.com/china-qijizhifeng/Web-Anything
