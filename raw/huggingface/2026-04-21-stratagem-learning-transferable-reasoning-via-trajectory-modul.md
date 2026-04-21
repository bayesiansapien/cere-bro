---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.17696"
url: https://huggingface.co/papers/2604.17696
arxiv_url: https://arxiv.org/abs/2604.17696
date: 2026-04-21
---

# Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play

Games offer a compelling paradigm for developing general reasoning capabilities in language models, as they naturally demand strategic planning, probabilistic inference, and adaptive decision-making. However, existing self-play approaches rely solely on terminal game outcomes, providing no mechanism to distinguish transferable reasoning patterns from game-specific heuristics. We present Stratagem, which addresses two fundamental barriers to reasoning transfer: domain specificity, where learned patterns remain anchored in game semantics, and contextual stasis, where static game contexts fail to cultivate progressive reasoning. Stratagem selectively reinforces trajectories exhibiting abstract, domain-agnostic reasoning through a Reasoning Transferability Coefficient, while incentivizing adaptive reasoning development via a Reasoning Evolution Reward. Experiments across mathematical reasoning, general reasoning, and code generation benchmarks demonstrate substantial improvements, with particularly strong gains on competition-level mathematics where multi-step reasoning is critical. Ablation studies and human evaluation confirm that both components contribute to transferable reasoning.

**Authors:** Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, Lei Huang, Weitao Ma, Qiming Li, Yuxuan Gu, Bing Qin, Lingpeng Kong (University of Hong Kong; Harbin Institute of Technology)

**Code:** https://github.com/ydyyyy/Stratagem
