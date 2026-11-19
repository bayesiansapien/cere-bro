---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.20992
url: https://huggingface.co/papers/2611.20992
arxiv_url: https://arxiv.org/abs/2611.20992
date: 2026-11-18
---

# MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding

Medical image understanding with vision-language models (VLMs) typically relies on autoregressively generating reasoning and answer tokens. These unnecessary tokens make the inference cost scale with the response length and force the answer to be parsed from free-form text, incurring avoidable latency and decision errors. To this end, we introduce MedJev, a system one vision-language decision model that maps medical images, questions, and candidate answers directly to decisions in a single multimodal forward pass, without any autoregressive generation process. For fast inference, MedJev removes the upper language layers and the generative output pathway, while keeping the full vision pathway and all visual tokens. On this shortened backbone, a decision head scores each candidate by pretrained query--key matching and refines the scores with a lightweight multilayer perceptron (MLP) residual, coupling the pretrained matching structure with task-specific nonlinear discrimination. Built on Qwen3.5-4B, MedJev-4B improves both accuracy and speed over the original model on each of four medical image classification and visual question answering benchmarks, with an absolute accuracy gain of 7.93\% and a 6.04times end-to-end speedup. Further comparison with 20 cutting-edge models shows that MedJev-4B achieves state-of-the-art performance and inference speed among 4B--9B general and medical VLMs, indicating that direct multimodal decision making is an effective route to fast and effective medical image understanding.
