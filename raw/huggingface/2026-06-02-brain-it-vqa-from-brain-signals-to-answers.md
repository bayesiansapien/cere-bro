---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.29588
url: https://huggingface.co/papers/2605.29588
arxiv_url: https://arxiv.org/abs/2605.29588
date: 2026-06-02
---

# Brain-IT-VQA: From Brain Signals to Answers

Decoding visual content from fMRI signals recorded while a person views images, and specifically answering questions about the seen images, is a long-standing challenge. While significant progress has been made in recent years in visual question answering (VQA) from fMRI, performance remains limited. Moreover, although recent models can make increasingly accurate predictions, they have rarely been used as tools for understanding the structure of visual representations in the brain. We present Brain-IT-VQA, a framework for visual question answering from fMRI. Building on the Brain Interaction Transformer (Brain-IT), our method decodes language tokens from brain activity and integrates them with a language model to answer visual questions. Our model substantially outperforms previous fMRI-based captioning and VQA approaches. We further introduce NSD-VQA, a new dataset and benchmark for visual question answering from fMRI. Unlike existing image-fMRI VQA datasets, which typically provide only a few broad and weakly controlled questions per image, NSD-VQA provides on average 20 question-answer pairs per image across 20 controlled question categories that disentangle multiple levels of visual understanding. This enables more reliable and interpretable evaluation despite limited fMRI test data. Together, Brain-IT-VQA and NSD-VQA provide both a strong predictive framework and a tool for studying brain representations. Using this benchmark, we quantify which forms of visual and semantic information can be reliably decoded from fMRI responses to natural images. We further analyze the contributions of different brain regions across question types.
