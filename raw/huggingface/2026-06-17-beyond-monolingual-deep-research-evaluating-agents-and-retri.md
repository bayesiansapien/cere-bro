---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.15345
url: https://huggingface.co/papers/2606.15345
arxiv_url: https://arxiv.org/abs/2606.15345
date: 2026-06-17
---

# Beyond Monolingual Deep Research: Evaluating Agents and Retrievers with Cross-Lingual BrowseComp-Plus

Deep research agents are increasingly evaluated on their ability to search for evidence, reason over retrieved sources, and produce grounded answers. Existing browsing benchmarks, however, largely assume that the user's query and the supporting evidence are written in the same language, leaving open whether agentic search systems can operate when relevant evidence appears in another language. We introduce XBCP (Cross-lingual BrowseComp-Plus), a controlled benchmark that preserves the English question-and-answer space of BrowseComp-Plus but varies the languages of the supporting documents. XBCP instantiates two complementary settings: in the cross-lingual setting, each query is paired with evidence in a single assigned language. In the multilingual setting, the full evidence corpus is distributed equally and randomly across 12 languages spanning high-resource and low-resource regimes. We evaluate four deep research agents using sparse and dense multilingual retrievers, measuring answer accuracy, evidence recall, search behavior, calibration, citation fidelity, and oracle retrieval. Results reveal substantial degradation when evidence is translated. Even strong, dense retrievers lose evidence recall, and agents become less calibrated and cite evidence less reliably. Notably, accuracy remains lower even when all gold evidence is supplied directly. These findings suggest that cross-lingual deep research exposes both retrieval failures and an independent, agent-side difficulty in integrating language-mismatched evidence.
