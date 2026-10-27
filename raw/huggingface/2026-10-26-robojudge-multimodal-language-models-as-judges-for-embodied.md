---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801003+00:00
arxiv_id: 2610.27782
url: https://huggingface.co/papers/2610.27782
arxiv_url: https://arxiv.org/abs/2610.27782
date: 2026-10-26
---

# RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation

Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark measures two fundamental dimensions, Physical Adherence and Instruction Alignment, across 800 human-annotated videos from 8 source corpora and 10 video generators, spanning grippers, human hands, and dexterous hands. Experiments reveal uneven alignment between existing judges and human ratings: general-purpose MLLMs show lower agreement on physical adherence, while specialized video judges designed for general-domain physical reasoning do not consistently transfer to embodied scenarios. Motivated by these findings, we construct RoboJudge-Train, comprising 12K videos annotated with 25K human-verified scores and model-assisted rationales for Physical Adherence and Instruction Alignment. We fine-tune a 9B MLLM on this dataset with supervised learning followed by reinforcement learning, yielding RoboJudge-9B. Among the model judges evaluated on RoboJudge-Bench, RoboJudge-9B achieves the highest overall agreement, reaching a Pearson correlation of 0.719 with a statistically significant 0.089 gain over Gemini-3.7-Flash, the best-performing proprietary baseline in our evaluation. Training on RoboJudge-Train also yields gains on external benchmarks, including VideoPhy2 and Physion-Eval. We further use RoboJudge-9B as a downstream evaluator to benchmark video generation models according to Physical Adherence and Instruction Alignment.
