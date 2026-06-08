---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.07454
url: https://huggingface.co/papers/2606.07454
arxiv_url: https://arxiv.org/abs/2606.07454
date: 2026-06-08
---

# PaperFlow: Profiling, Recommending, and Adapting Across Daily Paper Streams

Scientific paper recommendation is typically evaluated as static ranking over a fixed candidate set, yet real scientific reading unfolds as a daily, longitudinal process in which interests shift and feedback accumulates. We introduce PaperFlow, a framework that organizes it into three coupled stages: Profiling, which constructs and maintains a structured, inspectable scholarly profile from heterogeneous cold-start evidence; Recommending, which ranks each date-specific paper stream through multi-signal aggregation under a fixed display budget; and Adapting, which updates user state from semantically distinct feedback signals and models interest drift across days. We further define a longitudinal user-day benchmark that fixes users, dates, candidate pools, visible inputs, and hidden simulated relevance labels under a shared temporal information boundary. The benchmark contains 24 simulated research users, 50 daily paper streams, 1,200 user-day episodes, 20,727 unique papers, and 497,448 episode-paper records. We additionally specify a blind human-evaluation protocol to validate alignment between automatic metrics and expert judgments. Experiments against five scientific recommendation baselines show that PaperFlow achieves the strongest oracle-based ranking, the highest behavioral alignment with simulated reading selections, and the best blind human-evaluation score.
