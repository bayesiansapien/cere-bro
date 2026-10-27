---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.802320+00:00
arxiv_id: 2610.27528
url: https://huggingface.co/papers/2610.27528
arxiv_url: https://arxiv.org/abs/2610.27528
date: 2026-10-26
---

# Judging the Justification: Decision Certificate Supervision for Generative Reward Models

Generative reward models (GenRMs) generate natural language rationales to justify preference judgments, yet a correct verdict does not guarantee a sound justification. Existing approaches often rely on reference explanations to supervise rationales, but obtaining such references can be costly and does not necessarily establish whether generated rationales support the resulting verdict. To address these limitations, we propose DeCert, a framework that evaluates the validity and verdict consistency of generated rationales without requiring reference explanations. Crucially, DeCert translates these assessments into preference supervision that accounts for both verdict correctness and justification quality. In particular, when multiple sampled judgments share the same correct verdict, differences in certificate quality enable DeCert to construct rationale preference pairs that distinguish stronger from weaker justifications. Extensive empirical studies across two model families and multiple in- and out-of-distribution benchmarks demonstrate that DeCert consistently outperforms strong generative judge baselines while improving rationale quality. Moreover, DeCert effectively mitigates positional bias, improving position-consistent accuracy by up to 14.8 points. These results highlight the importance of supervising not only which verdict is correct, but also how that verdict is justified.
