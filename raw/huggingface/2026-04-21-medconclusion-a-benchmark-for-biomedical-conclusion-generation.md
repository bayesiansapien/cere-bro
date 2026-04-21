---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.06505"
url: https://huggingface.co/papers/2604.06505
arxiv_url: https://arxiv.org/abs/2604.06505
date: 2026-04-21
---

# MedConclusion: A Benchmark for Biomedical Conclusion Generation from Structured Abstracts

Large language models (LLMs) are widely explored for reasoning-intensive research tasks, yet resources for testing whether they can infer scientific conclusions from structured biomedical evidence remain limited. We introduce MedConclusion, a large-scale dataset of 5.7M PubMed structured abstracts for biomedical conclusion generation. Each instance pairs the non-conclusion sections of an abstract with the original author-written conclusion, providing naturally occurring supervision for evidence-to-conclusion reasoning. MedConclusion also includes journal-level metadata such as biomedical category and SJR, enabling subgroup analysis across biomedical domains. As an initial study, we evaluate diverse LLMs under conclusion and summary prompting settings and score outputs with both reference-based metrics and LLM-as-a-judge. We find that conclusion writing is behaviorally distinct from summary writing, strong models remain closely clustered under current automatic metrics, and judge identity can substantially shift absolute scores. MedConclusion provides a reusable data resource for studying scientific evidence-to-conclusion reasoning. Our code and data are available at: https://github.com/Harvard-AI-and-Robotics-Lab/MedConclusion.

**Authors:** Weiyue Li, Ruizhi Qian, Yi Li, Yongce Li, Yunfan Long, Jiahui Cai, Yan Luo, Mengyu Wang (Harvard AI and Robotics Lab, Harvard Medical School; University of Southern California; Carnegie Mellon University; Stanford University; Kempner Institute, Harvard University)

**Code:** https://github.com/Harvard-AI-and-Robotics-Lab/MedConclusion
