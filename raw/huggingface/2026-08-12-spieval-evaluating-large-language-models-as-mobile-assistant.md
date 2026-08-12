---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.10692
url: https://huggingface.co/papers/2608.10692
arxiv_url: https://arxiv.org/abs/2608.10692
date: 2026-08-12
---

# SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information

Large language models (LLMs) are increasingly deployed as mobile assistants, where a key challenge is leveraging personal information scattered across multiple applications (apps) to complete user instructions. However, due to the lack of dedicated benchmarks, their capabilities remain poorly understood. To address this gap, we introduce SPIEval, a human-curated benchmark grounded in five cognitive capabilities (i.e., reasoning, disambiguation, integration, preference inference, and multi-intent decomposition). SPIEval comprises 250 tasks spanning 4,335 personal records distributed across 10 apps and supports multi-turn interaction through 21 tools. Analysis shows that the benchmark exhibits diverse scenarios, challenging tasks, scattered information, controllable environments, and verifiable outcomes. We evaluate nine representative LLMs and find substantial room for improvement. The best-performing model, GPT-5.5 (xhigh), achieves only 57.3% accuracy, while the weakest achieves just 16.4%. Further analysis reveals that 79% of failures stem from inaccurate information localization, as LLMs often commit to plausible but incorrect information instead of continuing retrieval for verification. We also find that fewer than 2% of retrieval actions employ advanced search methods and observe substantial variation in search efficiency across models. These findings expose fundamental limitations of current LLM-based mobile assistants and motivate future research in this direction. Data and code are available at https://huggingface.co/datasets/Junjie-Ye/SPIEval.
