---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.11616
url: https://huggingface.co/papers/2608.11616
arxiv_url: https://arxiv.org/abs/2608.11616
date: 2026-08-13
---

# MBA: Multimodal Benchmark and Agents for Real-World Business Ideation

Agentic systems powered by large language models (LLMs) have opened new opportunities for business ideation. Yet existing approaches remain confined to a text-only paradigm, despite the inherently multimodal nature of real-world contexts. We thus introduce MBA-Bench, the first multimodal benchmark for training and evaluating business ideation agents, comprising 30K samples across six domains, each domain characterized by distinct visual cues not fully conveyed by text alone. Concretely, we automatically caption images and employ GPT-4o to generate five reference ideas for each of three business questions through retrieval query generation, market evidence retrieval, and evidence-augmented synthesis. Following prior work, we evaluate agents across six business-oriented criteria using MLLM-as-a-Judge. To consider settings where criteria are hidden or disclosed, we present MBA-b and MBA-k for blind and known, respectively. We train both with two novel reward objectives---creativity and feasibility---while MBA-k further optimizes the six disclosed criteria for eight in total. Both are trained via LoRA-based supervised fine-tuning followed by group relative policy optimization with these setting-specific rewards. For extensive experiments on MBA-Bench, we set up two baselines accommodating either captions only or multimodal inputs, with the latter nearing closed-source performance on several metrics. MBA-b and MBA-k outperform caption baselines by 63.9% and 77.1%, and multimodal baselines by 25.6% and 35.8%, respectively.
