---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.20342
url: https://huggingface.co/papers/2605.20342
arxiv_url: https://arxiv.org/abs/2605.20342
date: 2026-05-26
---

# ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning

Training large multimodal models (LMMs) via reinforcement learning (RL) to natively invoke video-processing tools (e.g., cropping) has become a promising route to long-video understanding. However, existing native-RL methods dispatch tool calls sequentially (i.e., one per turn): a single wrong crop propagates errors without peer correction, multi-turn tool calls corrupt context, and inference cost scales linearly with the number of turns. We introduce ParaVT, the first multi-agent end-to-end RL-trained framework for Parallel Video Tool calling, dispatching multiple time-window crops in a single turn for cleaner context and better fault tolerance. Yet applying standard RL to ParaVT reveals an obstacle we term the Tool Prior Paradox: the pretrained tool priors that enable tool exploration also destabilize cold-started structural format and expose the skip-tool reward shortcut under temperature sampling. A cross-model contrast on a weaker-prior LMM supports this claim: format stays stable but RL elicits zero tool calls, indicating that prior strength is the shared driver of both format collapse and tool exploration. We propose PARA-GRPO (Parseability-Anchored and Ratio-gAted GRPO), which augments standard RL with two complementary mechanisms: (i) a targeted format reward applied only at the structural-token positions most prone to collapse, and (ii) a per-prompt frame-budget randomization that creates training prompts where calling the tool yields a measurable reward signal over skipping it. Across six long-video understanding benchmarks, ParaVT improves over the Qwen3-VL baseline by +7.9% on average, with PARA-GRPO lifting training-time format compliance from 0.13 to 0.64. As tool capabilities become increasingly internalized in modern LMMs, RL must cooperate with the resulting priors, and ParaVT offers a general recipe for agentic RL. Code, data, and model weights are publicly available.
