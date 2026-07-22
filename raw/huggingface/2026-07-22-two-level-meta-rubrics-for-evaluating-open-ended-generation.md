---
source: farmer/huggingface
farmed: 2026-07-22T05:46:30Z
arxiv_id: 2607.19322
url: https://huggingface.co/papers/2607.19322
arxiv_url: https://arxiv.org/abs/2607.19322
date: 2026-07-22
---

# Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness

Evaluating the factuality of long-form generations has focused predominantly on precision, measuring whether the claims a model makes are correct. The dominant decompose-search-verify pipeline catches incorrect claims well but says little about whether a response contains all the information it should. Measuring factual completeness, the missing half of factuality, is harder: it requires enumerating the full set of facts a complete answer should contain, and these facts rarely form a flat list. They often involve open-ended sets where coverage is what matters, ordered processes, and relationships among facts that a list of independent boolean checks fails to capture. We introduce a two-level meta-rubric framework for evaluating open-ended generation, and instantiate it as Gamut (Grounded Assessment of Multimodal Factuality), a benchmark for factual completeness in long-form generation. The framework rests on a two-level rubric representation: a structured meta-rubric captures the organization and importance of the required content, which is then mechanically compiled into a flat checklist of binary, machine-gradable rubrics that an LLM judge scores reliably. We construct 1,813 questions grounded in real wearable imagery across 10 diverse domains, each paired with an evidence-backed rubric verified by expert human annotators. Because the framework is modality-agnostic, we also release a text-only variant. Evaluating 14 frontier and open-weight models, we find the benchmark genuinely challenging (best score 58.7% from Gemini 3.1 Pro), highly discriminative, and robust to the choice of judge.
