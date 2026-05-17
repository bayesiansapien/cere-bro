---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14876"
url: "https://huggingface.co/papers/2605.14876"
arxiv_url: "https://arxiv.org/abs/2605.14876"
date: 2026-05-17
---

# Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning

Despite rapid advancements, current text-to-image (T2I) models predominantly rely on a single-step generation paradigm, which struggles with complex semantics and faces diminishing returns from parameter scaling. While recent multi-step reasoning approaches show promise, they are hindered by ungrounded planning hallucinations lacking verification, monolithic post-hoc reflection, long-context optimization instabilities, and prohibitive inference latency. To overcome these bottlenecks, we propose the Closed-Loop Visual Reasoning (CLVR) framework, a comprehensive system that deeply couples visual-language logical planning with pixel-level diffusion generation. CLVR introduces an automated data engine with step-level visual verification to synthesize reliable reasoning trajectories, and proposes Proxy Prompt Reinforcement Learning (PPRL) to resolve long-context optimization instabilities by distilling interleaved multimodal histories into explicit reward signals for accurate causal attribution. Furthermore, to mitigate the severe latency bottleneck caused by iterative denoising, we propose Delta-Space Weight Merge (DSWM), a theoretically grounded method that fuses alignment weights with off-the-shelf distillation priors, reducing the per-step inference cost to just 4 NFEs without requiring expensive re-distillation.
