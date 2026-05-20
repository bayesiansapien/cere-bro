---
source: farmer/huggingface
farmed: 2026-05-20T09:54:54.180017+00:00
arxiv_id: 2605.18827
url: https://huggingface.co/papers/2605.18827
arxiv_url: https://arxiv.org/abs/2605.18827
date: 2026-05-20
---

# Code-Guided Reasoning for Small Language Models: Evaluating Executable MCQA Scaffolds

Multiple-choice QA benchmarks usually evaluate small language models (SLMs) as direct answerers, but deployed language-model systems increasingly rely on external scaffolds such as tools, code, and repeated model calls. We introduce Code-Guided Reasoning (CGR), an evaluation protocol and generated-program resource for measuring when executable reasoning scaffolds improve SLM performance on MCQA tasks. CGR standardizes six components: a normalized item interface, a direct solver prompt, a generator prompt, a Python scaffold, solver-call and extraction helpers, and a three-channel result record. On 20,498 retained result rows from a locally prepared MCQA bundle and six metadata-registered solver models, the observed non-zero-baseline partition shows 66.21% macro assisted accuracy versus 38.11% direct accuracy, a +28.10 percentage-point difference with a pair-bootstrap interval of [20.32, 36.43]. Under a stricter Ab &gt; 30% direct-signal gate, the macro difference is +14.11 points. These estimates are descriptive. Assisted inference uses a larger solver-call budget, answer extraction is brittle, Time-MQA contains the observed regressions, and some generated programs violate the no-hard-coding instruction. CGR provides the trace package needed to interpret these results, including direct, assisted, and generator-side answers, partition definitions, generated programs, response metadata, and audits.
