---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.161517+00:00
arxiv_id: 2610.23656
url: https://huggingface.co/papers/2610.23656
arxiv_url: https://arxiv.org/abs/2610.23656
date: 2026-10-30
---

# ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics

Blockchain forensics is adversarial and open-ended: money launderers split, swap, and bridge funds, cut their trail at mixers or custodial services, and change tactics from one incident to the next. Investigators must keep adapting their tracing in response. Yet the immutability of public ledgers preserves every recorded movement in public view, making much of the investigation independently verifiable. We introduce ABF-Bench, an interactive benchmark that makes evidence-backed fund tracing a verifiable agent task, in which every claimed movement must cite ledger records the agent retrieved. A case-to-task pipeline builds well-posed tasks across ledgers: conservative rules halt tracing wherever the records leave a continuation unresolved, and each task's reference graph is the answer those rules determine. Built from real laundering activity, the tasks combine multi-hop transfers, DeFi exchanges, cross-chain round trips, custodial and mixer deposits, and address poisoning. We also propose the ABF agent harness, built around a working memory, and evaluate it alongside general-purpose agents and fixed-order tracers. The harness reaches 75% edge recall, against 47% for Codex with the same model and 10% for Claude Code, which loses recall to overconfidence: it cites records it left unretrieved. Compared with fixed-order tracers, the harness acquires evidence faster than the best of them early in the budget and recognizes undisclosed custodial services that they walk past (89% vs. 0%), with 98% fidelity. However, agents tend to stop early and lose recall on larger tasks, which holds their final recall below the best tracer. Beyond exposing these gaps, ABF-Bench opens blockchain forensics to LLM agents as a verifiable domain, where the verdicts that score agents also offer potential training signals.
