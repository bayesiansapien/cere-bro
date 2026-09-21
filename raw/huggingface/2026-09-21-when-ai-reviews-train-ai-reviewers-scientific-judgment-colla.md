---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.20942
url: https://huggingface.co/papers/2609.20942
arxiv_url: https://arxiv.org/abs/2609.20942
date: 2026-09-21
---

# When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation

Large language models (LLMs) increasingly participate in scientific evaluation, both as automated reviewers and as assistants to human reviewers. As model-generated reviews enter public data and future training corpora, AI peer review can become recursive: later reviewers learn from judgments produced by earlier models. We study one step of this feedback loop in a controlled setting. Starting from Llama 3.1 8B, we first fine-tune a reviewer on official ICLR reviews from 2018--2023 and then train four successor models on ICLR 2024 data with systematically varied mixtures of official and model-generated reviews. Our study shows that introducing synthetic reviews compresses rating distributions and reduces both same-paper and corpus-level semantic diversity. We call this pattern scientific-judgment collapse.
  To mitigate this failure mode, we introduce TrustReviewer, an open-source LLM-based system for generating peer reviews of AI and machine learning papers. TrustReviewer intervenes at two complementary stages. For training-time prevention, we train the core reviewer in a single stage on a curated corpus designed to reduce low-quality and semantically degenerate supervision. For test-time correction, paired activation steering aims to further mitigate residual tendencies toward collapsed judgments without further training or additional expert annotation. Together, these results characterize a concrete risk of recursive reviewer training and provide practical interventions for preserving judgment diversity and improving recommendation alignment in AI-assisted scientific evaluation.
