---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28618
url: https://huggingface.co/papers/2607.28618
arxiv_url: https://arxiv.org/abs/2607.28618
date: 2026-07-31
---

# AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis

Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. Over this shared claim store, AskChem exposes complementary structures for search and synthesis: a stabilized faceted taxonomy for hierarchical retrieval and browsing, an evidence graph linking claims through relations, and an exploratory living taxonomy that situates indexed papers under scientific principles. AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs, compared with 88.3% without retrieval, and the highest citation density among five tested systems. AskChem is live at https://askchem.org.
