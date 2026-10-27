---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.799069+00:00
arxiv_id: 2610.27103
url: https://huggingface.co/papers/2610.27103
arxiv_url: https://arxiv.org/abs/2610.27103
date: 2026-10-26
---

# Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs

Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fused representations. To address this issue, we propose Omni-Woodpecker (OWP), a training-free framework that shifts hallucination mitigation from output-level manipulation to conflict-conditioned representation rebalancing. Specifically, OWP first identifies cross-modal conflicts from complementary modality-specific views. It then employs orthogonal decomposition to separate grounding evidence from competing priors within the hidden states. Finally, OWP adaptively rebalances fused representations by suppressing misleading priors and restoring ignored evidence before decoding. Extensive experiments demonstrate the effectiveness and strong cross-architecture generalization of OWP. Using Qwen2.5-Omni-7B as the backbone, OWP improves performance by 12.9 and 8.6 points on CMM and AVHBench, respectively, while consistently achieving gains of 0.67-2.25 points across four general OLLM reasoning benchmarks. Furthermore, OWP generalizes effectively to VideoLLaMA2-AV, improving performance by 4.6 and 3.9 points on the same benchmarks. Code is publicly available at https://github.com/ZiiJianLiu/Omni-Woodpecker
