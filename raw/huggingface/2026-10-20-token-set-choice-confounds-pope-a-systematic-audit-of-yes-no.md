---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25964
url: https://huggingface.co/papers/2610.25964
arxiv_url: https://arxiv.org/abs/2610.25964
date: 2026-10-20
---

# Token-Set Choice Confounds POPE: A Systematic Audit of Yes/No Extraction in VLM Hallucination Evaluation

We set out to reproduce a recent hallucination-mitigation result on the POPE benchmark. The LLaVA-1.5-7B baseline we measured, 82.21 F1 on the adversarial split, sat 1.21 to 8.67 points above the adversarial baselines we planned to compare against (81.00, 79.30, and 73.54). We looked at the evaluation code and found a readout choice that moves F1 on its own. A two-token logit readout decides yes versus no by comparing two vocabulary IDs, 3582 ("yes") and 1217 ("no"). Across 9,000 greedy-decode questions spanning all three splits, neither ID is generated even once. The model emits " Yes" (token 3869) and " No" (token 1939), because SentencePiece prepends a space byte after the prompt suffix "ASSISTANT:". Read with an eight-token lookup that covers the space-prefixed surface forms, LLaVA-1.5-7B scores F1 0.8221, 0.8498, and 0.8713 on the adversarial, popular, and random splits. That 6.13-point adversarial shift exceeds the adversarial gain reported by five of the six papers we surveyed. None of them states its readout, and our reference ran under 4-bit NF4 quantization, so we cannot say how much of any reported gain a matched evaluation would keep. That comparison stays unresolved until readout and precision are matched. On the fixed baseline we run nine inference-time corrections of our own (none beat it) and dissect why the adversarial split resists logit-level intervention. In a 3,000-question probe, wrong predictions draw more image attention than correct ones (Cohen's d=-0.46, p=1.4times10^{-24}), the opposite of what grounding-based corrections assume. A four-readout audit across four further VLMs from three tokenizer families confirms the confound is protocol-level, not model-specific: porting the LLaVA-1.5 IDs verbatim drops F1 to 0.00 on the two disjoint-vocabulary models, whereas a tokenizer-derived readout holds between 0.80 and 0.92.
