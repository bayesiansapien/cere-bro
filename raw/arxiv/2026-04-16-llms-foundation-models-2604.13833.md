---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13833
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13833
published: 2026-04-16
authors: Yunsheng Lu, Zijiang Yang, Licheng Pan
---

# Robust Reward Modeling for Large Language Models via Causal Decomposition

**arXiv:** https://arxiv.org/abs/2604.13833
**Authors:** Yunsheng Lu, Zijiang Yang, Licheng Pan

## Abstract

arXiv:2604.13833v1 Announce Type: new  Abstract: Reward models are central to aligning large language models, yet they often overfit to spurious cues such as response length and overly agreeable tone. Most prior work weakens these cues directly by penalizing or controlling specific artifacts, but it does not explicitly encourage the model to ground preferences in the prompt's intent. We learn a decoder that maps a candidate answer to the latent intent embedding of the input. The reconstruction error is used as a signal to regularize the reward model training. We provide theoretical evidence that this signal emphasizes prompt-dependent information while suppressing prompt-independent shortcuts. Across math, helpfulness, and safety benchmarks, the decoder selects shorter and less sycophantic candidates with 0.877 accuracy. Incorporating this signal into RM training in Gemma-2-2B-it and Gemma-2-9B-it increases RewardBench accuracy from 0.832 to 0.868. For Best-of-N selection, our framework increases length-controlled win rates while producing shorter outputs, and remains robust to lengthening and mild off-topic drift in controlled rewrite tests.
