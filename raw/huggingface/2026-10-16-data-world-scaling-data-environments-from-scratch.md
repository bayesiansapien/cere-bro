---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21656
url: https://huggingface.co/papers/2610.21656
arxiv_url: https://arxiv.org/abs/2610.21656
date: 2026-10-16
---

# Data World: Scaling Data Environments from Scratch

Data agents use code to process heterogeneous files and derive analytical insights. Scaling their training faces costly environment curation, privacy and intellectual-property restrictions, and difficulty verifying open-ended findings without known generative truth. Our core insight is to specify the world behind the files before generating the files themselves. We introduce Data World, a multi-agent engine that synthesizes environments, tasks, and rubrics from explicit mechanisms. Independent audits check target recoverability from observed files; rubrics support evaluation and RL rewards. Human preference-based curation for question realism selects 100 tasks across 50 held-out worlds and 16 domains for DataWorld-Bench. The engine also yields 2,135 training tasks from 1,037 disjoint worlds. Evaluation of ten frontier models shows that the benchmark remains challenging, particularly for insight discovery, with a consistent computation-insight gap. RL-zero training on the synthesized tasks produces DataWorld-35B-A3B from Qwen3.6-35B-A3B without trajectory distillation. Under matched evaluation, it improves over its base by 7.06 points on DataWorld-Bench, 14.28 on DAComp, 20.90 on DABstep-Hard, and 12.13 on JobBench, a broader occupational benchmark.
