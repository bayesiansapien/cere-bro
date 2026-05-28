---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.27311
url: https://huggingface.co/papers/2605.27311
arxiv_url: https://arxiv.org/abs/2605.27311
date: 2026-05-28
---

# Chartographer: Counterfactual Chart Generation for Evaluating Vision-Language Models

Chart question-answering (QA) benchmarks aim to pose questions that require visual reasoning to correctly answer, but models can often reach solutions through shortcuts or prior familiarity with a chart based on their own background knowledge. To strictly evaluate visual reasoning, we propose counterfactual charts where the chart-question task remains fixed, but underlying chart and the corresponding answer are varied. We introduce Chartographer, a framework to reverse engineer charts into executable code, validate reconstruction fidelity, generate seed-controlled counterfactual variants, and derive new answers from executable QA logic. We apply this framework to existing chart QA datasets and evaluate proprietary and open-source vision-language models (VLMs), measuring variation sensitivity and generalizability. Counterfactual charts reveal failures hidden by single-chart performance: VLMs often fail to generalize after answering the original chart correctly. We find failures are most prevalent when updated charts require novel visual reasoning pathways.
