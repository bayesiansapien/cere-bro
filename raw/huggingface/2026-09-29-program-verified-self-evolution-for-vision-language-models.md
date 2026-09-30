---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.931699+00:00
arxiv_id: 2609.33855
url: https://huggingface.co/papers/2609.33855
arxiv_url: https://arxiv.org/abs/2609.33855
date: 2026-09-29
---

# Program-Verified Self-Evolution for Vision-Language Models

Self-evolving vision-language models train on questions they generate from unlabeled images. Since these questions have no gold answers, prior methods label them by majority vote over sampled answers or by a model judge. In a human evaluation, we find that 24\% of majority-vote labels and 18\% of model-judge labels produced during self-evolution are wrong. To address this problem, we present Verifiable QA Generation for Self-Evolving Models (VQS), which changes how the model judges answers. Instead of voting on an answer, the model parses each image into a structured record, such as a scene graph, a chart table, or a diagram graph. Fixed programs then write a question from the record and compute its answer. The model still acts as a visual checker, but it only confirms the individual facts the program reads, one short claim at a time. These claim-level checks select the parser's training targets, so the parser also improves without labels. Human raters find 94\% of VQS answers correct, against 76\% for majority voting. Across ten benchmarks, VQS improves Qwen3-VL by up to 3.18 points at the 2B, 4B, and 8B scales and outperforms the strongest self-evolving baseline at each. Gains keep growing over three training rounds, reaching 3.84 points at 2B. Code is released at https://github.com/ahmedheakl/VQS
