---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14697
url: https://huggingface.co/papers/2606.14697
arxiv_url: https://arxiv.org/abs/2606.14697
date: 2026-06-15
---

# ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning

Building trustworthy medical multimodal large language models (MLLMs) is critical for reliable clinical decision support. Existing medical hallucination benchmarks mainly focus on data collection, but often ignore where hallucinations originate within the reasoning process. We find that hallucination sources vary across samples: errors may arise from visual misrecognition, incorrect medical knowledge recall, or flawed reasoning integration. To enable source-level hallucination diagnosis, we introduce ClinHallu, a benchmark for stage-wise hallucination diagnosis in medical MLLM reasoning. ClinHallu contains 7,031 validated instances, where each instance is augmented with a structured reasoning trace decomposed into Visual Recognition, Knowledge Recall, and Reasoning Integration. We also use stage-replacement interventions to measure how correcting specific stages affects the final answer. Beyond evaluation, we show that trace-supervised fine-tuning reduces stage-wise hallucinations. ClinHallu provides a fine-grained hallucination testbed for diagnosing and mitigating reasoning failures in medical MLLMs. The benchmark is publicly available at https://github.com/alibaba-damo-academy/ClinHallu.
