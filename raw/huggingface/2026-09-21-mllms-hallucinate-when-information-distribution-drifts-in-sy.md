---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.09206
url: https://huggingface.co/papers/2609.09206
arxiv_url: https://arxiv.org/abs/2609.09206
date: 2026-09-21
---

# MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads

Multimodal Large Language Models (MLLMs) often struggle with hallucinations, thus hindering their reliable practical applications. Existing attention-based mitigation methods mainly rely on indirect signals (e.g., attention weights) that fail to accurately reflect the actual information shift underlying hallucination generation. In this paper, we propose HEAL, Head-lEvel information disentAnglement and caLibration for identifying and mitigating hallucinations. HEAL first employs causal noise intervention on multi-head outputs to filter out causally redundant heads. Subsequently, it disentangles information distribution within the remaining heads via the counterfactual Difference-in-Differences, categorizing heads into four types. Through analysis, we observe: hallucinations happen when information distribution drifts away from a healthy equilibrium in synergy heads, not strongly correlated with the quantity or strength of modality-specific heads. Motivated by this insight, HEAL injects dynamic information calibration factors into the value vectors of synergy heads, and actively regulates visual-language dependencies, steering the output distribution towards factual evidence. Extensive experiments demonstrate that HEAL effectively reduces hallucinations across multiple MLLMs, offering a simple and interpretable pathway to enhance model trustworthiness.
