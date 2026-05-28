---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28721
url: https://huggingface.co/papers/2605.28721
arxiv_url: https://arxiv.org/abs/2605.28721
date: 2026-05-28
---

# LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines when answer-supporting evidence is removed. These results suggest that static search benchmarks can reward memory-backed verification rather than evidence-driven discovery, conflating what agents already know with what they can find. We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage. It contains 335 human-authored questions whose answers depend on facts published within the 90 days preceding benchmark construction, drawn from six updated sources and filtered to exclude globally salient events. On LiveBrowseComp, all evaluated agents fall below 2% closed-book accuracy, search-augmented scores drop by 25-40 points relative to BrowseComp, and prior model rankings no longer reliably predict performance. LiveBrowseComp is available at https://huggingface.co/datasets/Forival/LiveBrowseComp.
