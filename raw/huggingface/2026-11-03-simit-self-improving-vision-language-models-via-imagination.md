---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.00053
url: https://huggingface.co/papers/2611.00053
arxiv_url: https://arxiv.org/abs/2611.00053
date: 2026-11-03
---

# SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time

We introduce SIMIT, a test-time self-improvement framework in which a vision-language model creates its own query-specific training data before answering an unlabeled test query. Our goal is to improve performance on a given target test set without annotations or external models. To pursue this goal, some test-time methods improve answers through longer reasoning or repeated sampling but leave the model unchanged. Others update the model using rewards based on majority agreement among multiple candidate answers or the model's own judgments of correctness, but such rewards can reinforce existing mistakes. SIMIT instead imagines similar problems whose solutions it controls: a model need not correctly solve the target query to construct useful practice examples. It synthesizes diverse (question, answer, image) triplets by specifying each answer before realizing its image. To support diverse multimodal tasks, SIMIT combines native image generation with an extensible skill library for structured visuals, including documents, charts, and diagrams. Within this pipeline, multi-stage verification checks that images support their assigned answers, while difficulty filtering retains informative examples. Adaptive budgeting further targets this practice by allocating more samples to queries the model is less confident in answering. The resulting data can improve the model in-context (SIMIT-ICL) or in-weight (SIMIT-FT). Across 17 diverse benchmarks, SIMIT outperforms existing self-improvement methods. Its best configuration achieves a +7.20% mean relative gain over BAGEL-7B, while training-free SIMIT-ICL achieves +6.98%.
