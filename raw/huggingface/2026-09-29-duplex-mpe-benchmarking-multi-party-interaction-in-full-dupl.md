---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928529+00:00
arxiv_id: 2609.31948
url: https://huggingface.co/papers/2609.31948
arxiv_url: https://arxiv.org/abs/2609.31948
date: 2026-09-29
---

# Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue

Real-time full-duplex speech models can listen while speaking, enabling natural interaction without rigid turn boundaries. Existing benchmarks evaluate turn-taking, interruption handling and multi-round dialogue, but largely centre on a designated user rather than an assistant participating in a shared conversation among several people. We introduce Duplex-MPE to evaluate when such an assistant should answer, remain silent or stop speaking. The benchmark contains 2,000 scenarios with three or four human speakers and one assistant, each paired across explicit and implicit addressing of the same request. Models receive continuous conversation audio without transcripts or supplied turn boundaries. Four scores measure fresh response initiation, answer accuracy, silence preservation and stopping when a human resolves a request. We evaluate five open-weight speech systems: MiniCPM-o 4.5, Moshi, FLM-Audio, Voila and Freeze-Omni. MiniCPM-o 4.5 leads on three scored capabilities, while frequent speech from other systems can coexist with inaccurate answers or failures to remain silent. A transcript-based Gemini 3.1 Pro reference responds 64.3 percentage points more often to explicit than implicit requests; paired tests detect no significant response-rate difference for the speech systems.
