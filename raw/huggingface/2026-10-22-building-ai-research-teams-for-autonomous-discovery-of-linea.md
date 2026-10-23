---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.192019+00:00
arxiv_id: 2610.28887
url: https://huggingface.co/papers/2610.28887
arxiv_url: https://arxiv.org/abs/2610.28887
date: 2026-10-22
---

# Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures

Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When experiments are costly, a team can test only a limited number of ideas, thereby creating the need to balance exploration and exploitation when selecting a subset of researchers to propose and execute new experiments. Furthermore, each result should shape what the team tries next. We therefore ask how AI researchers with different scientific backgrounds can build on one another's findings and sustain progress under a limited experimental budget. To address these challenges, we build a team of persistent AI researchers, each grounded in a different discipline, who keep private research histories, share experimental evidence, and receive research opportunities through adaptive allocation. We demonstrate the effectiveness of this design by deploying the team to search for linear attention architectures, where it outperforms GDN2 at 1.3B scale on language modeling, common-sense reasoning, and synthetic and real-world retrieval tasks. In controlled comparisons, removing any single organizational component from our design yields markedly weaker discoveries: without disciplinary backgrounds, the search plateaus early; without private histories, researchers make less progress despite identical shared evidence; and uniform selection falls short of adaptive allocation within the same budget. These results suggest that sustained autonomous discovery depends not only on stronger agents, but also on who explores, what they remember, and how research effort is allocated.
