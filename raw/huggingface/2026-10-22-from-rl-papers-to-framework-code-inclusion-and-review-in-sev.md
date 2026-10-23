---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.193862+00:00
arxiv_id: 2610.28027
url: https://huggingface.co/papers/2610.28027
arxiv_url: https://arxiv.org/abs/2610.28027
date: 2026-10-22
---

# From RL Papers to Framework Code: Inclusion and Review in Seven Open-Source Training Frameworks

Practitioners use reinforcement learning methods for language models through training frameworks, so a method that a framework includes is one configuration change away for its users. We measure how often this happens. We trace seven open-source frameworks for RL post-training through their commit histories and link them to 6,939 screened arXiv papers from January 2025 to June 2026. Of 1,598 papers that propose a general RL training method, 37 reached at least one framework. Across five quarterly cohorts of papers, the number included within 180 days stayed between 5 and 7 while the cohorts grew from 72 to 386 papers. Compared with papers from the same quarters, included papers more often trained policies of 30B parameters or more, at 41 against 10 percent, and more often changed a coefficient, clip, mask or weight in the existing loss, at 29 against 9 percent. Both gaps hold without papers from the companies that maintain the frameworks, while code release was equally common in both groups. The frameworks' issues and pull requests show that few methods are turned away in public. More than nine in ten of the general methods no framework included have no thread there that cites or names them, and many proposals that do appear stay open without a reply. Two further records, the frameworks' issues and the technical reports of 13 large open-weight models, show that users rarely report training failures in public and that the reports state 8 of the 13 widely included methods. We release the data as a tracker that links training failures to framework implementations and lists each framework's contribution rules and earlier proposals.
