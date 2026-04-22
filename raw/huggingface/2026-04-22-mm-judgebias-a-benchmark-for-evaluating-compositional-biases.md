---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.18164
url: https://huggingface.co/papers/2604.18164
arxiv_url: https://arxiv.org/abs/2604.18164
date: 2026-04-22
---

# MM-JudgeBias: A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge

Multimodal Large Language Models (MLLMs) have been increasingly used as automatic evaluators—a paradigm known as MLLM-as-a-Judge. However, their reliability and vulnerabilities to biases remain underexplored. We find that many MLLM judges fail to reliably integrate key visual or textual cues, yielding unreliable evaluations when evidence is missing or mismatched, and exhibiting instability under semantically irrelevant perturbations. To address this, we systematically define Compositional Bias in MLLM-as-a-Judge systems and introduce MM-JudgeBias, a benchmark for evaluating it. MM-JudgeBias introduces controlled perturbations across Query, Image, and Response, and evaluates model behavior via two complementary metrics: Bias-Deviation (BD) for sensitivity and Bias-Conformity (BC) for stability. Our dataset of over 1,800 curated and refined multimodal samples, drawn from 29 source benchmarks, enables a fine-grained diagnosis of nine bias types across diverse tasks and domains. Experiments on 26 state-of-the-art MLLMs reveal systematic modality neglect and asymmetric evaluation tendencies, underscoring the need for more reliable judges.
