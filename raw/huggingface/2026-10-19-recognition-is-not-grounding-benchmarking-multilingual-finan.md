---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.19432
url: https://huggingface.co/papers/2610.19432
arxiv_url: https://arxiv.org/abs/2610.19432
date: 2026-10-19
---

# Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction

Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same multilingual evidence. In particular, it remains unclear whether language models can recognize these concepts across languages and exhaustively recover their corresponding numerical evidence from the same contexts. We introduce MULTIFINGROUND, a benchmark designed to investigate this recognition-grounding gap in multilingual financial reports. Constructed from FY2025 disclosures of 90 issuers in English, French, and Greek, MULTIFINGROUND aligns independently authored reports through a shared accounting taxonomy and provides traceable fact-level annotations. The benchmark evaluates financial fact identification, concept recognition, exhaustive fact selection, and concept discrimination without candidate labels. Across 15 evaluated models, eight API and open-weight reference models achieve 97.3-99.4\% concept recognition accuracy, yet miss at least one target fact in 26.6-41.9\% of correctly recognized groups. Further analyses reveal substantial variation in concept discrimination and limited gains from the evaluated finance-specialized models. Our findings demonstrate that strong concept recognition can coexist with incomplete evidence recovery, highlighting the importance of evaluating semantic recognition and evidence completeness together.
