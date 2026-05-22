---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.20158
url: https://huggingface.co/papers/2605.20158
arxiv_url: https://arxiv.org/abs/2605.20158
date: 2026-05-21
---

# Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models

Large Vision Language Models (LVLMs) show promise in medical applications, but their inability to faithfully ground responses in visual evidence raises serious concerns about clinical trustworthiness. While visual attribution methods are widely used to explain LVLM predictions, whether these explanations actually reflect the visual evidence underlying the model's decision is largely unverified, since ground-truth annotations for internal model reasoning are typically unavailable. We address this question for chest X-ray (CXR) reasoning by developing a causal evaluation framework that retains only CXR-VQA samples for which the expert-annotated region is verified, via counterfactual editing, to be causally responsible for the model's prediction. Using this framework across 11 attribution methods, six open-source LVLMs, and two output modes (direct answer and step-by-step reasoning), we find that existing attribution methods often fail to identify the evidence used by LVLMs. To address this failure, we propose MedFocus, a concept-based attribution method that localizes clinically meaningful anatomical regions via unbalanced optimal transport and measures their causal effect on model outputs through targeted interventions. MedFocus produces spatial, concept-level, and token-level attributions and substantially outperforms prior methods, taking a step toward more trustworthy attribution for medical LVLMs. Our data and code are available at https://github.com/gzxiong/medfocus/.
