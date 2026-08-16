---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.07193
url: https://huggingface.co/papers/2608.07193
arxiv_url: https://arxiv.org/abs/2608.07193
date: 2026-08-14
---

# An AI4AI Framework for Visual Token Pruning

Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating the expanding design space becomes increasingly difficult. This paper aims to build an AI4AI framework for visual-token pruning by addressing a natural question: Can large language models automatically design effective visual-token reduction algorithms? Although LLMs possess broad algorithmic knowledge and strong reasoning capabilities, translating such general knowledge into effective solutions for a specialized task remains nontrivial. We argue that the key lies in designing an appropriate search-state representation that connects the internal knowledge of LLMs with the structural requirements and constraints of visual-token pruning. Based on this insight, we propose AutoPrune, a training-free framework for LLM-driven visual-token pruning policy design. At its core, AutoPrune introduces a Token Pruning Domain-Specific Language (TPDSL) comprising 131 reusable atoms for budget control, token scoring, selection constraints, and token reassembly. A key property of TPDSL is that it represents each search state as a residual modification of a strong base policy. This residual formulation narrows the search space and directs the LLM's attention toward the policy components that are most consequential for performance. Experiments on 14 multimodal benchmarks and three MLLM backbones demonstrate the effectiveness, efficiency, and transferability of AutoPrune. Even when removing 94.4% of visual tokens, AutoPrune preserves more than 99% of full-token performance while reducing FLOPs by 9.9x and prefill latency by 6.4x.
