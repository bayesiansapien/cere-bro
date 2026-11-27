---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.907754+00:00
arxiv_id: 2611.30460
url: https://huggingface.co/papers/2611.30460
arxiv_url: https://arxiv.org/abs/2611.30460
date: 2026-11-26
---

# CONCOR: Benchmarking Contrastive Decoding for Visual Hallucination Mitigation Beyond Final-Output Performance

Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token scores. However, existing generative and discriminative benchmarks primarily measure final task scores, which can be confounded by candidate filtering, changes in generation trajectories, and response biases, making it difficult to isolate the effects of the underlying contrastive adjustments. To address these limitations while complementing existing evaluations, we introduce CONCOR (Contrastive Correction Evaluation), a controlled benchmark that directly evaluates the competition between ground-truth and different types of hallucinated candidates using the Contrastive Grounding Margin (CGM). CGM also enables analysis of directional consistency, composition, and reliability of contrastive corrections. Our evaluation reveals that existing CD methods exhibit distinct correction behaviors: some consistently favor ground-truth candidates, whereas others produce strong corrections but also introduce more errors. Crucially, these differences help explain their contrasting responses to increased contrast strength, which improves some methods while degrading others. These findings highlight the importance of evaluating the contrastive correction itself, rather than relying solely on final-output performance, and CONCOR provides a controlled and interpretable framework for understanding and improving CD methods for hallucination mitigation.
