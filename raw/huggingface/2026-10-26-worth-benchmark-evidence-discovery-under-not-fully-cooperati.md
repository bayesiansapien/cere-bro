---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.802161+00:00
arxiv_id: 2610.27597
url: https://huggingface.co/papers/2610.27597
arxiv_url: https://arxiv.org/abs/2610.27597
date: 2026-10-26
---

# WORTH Benchmark: Evidence Discovery under Not-Fully-Cooperative Information -- A Two-Episode Pilot

Existing reasoning evaluations typically provide task-relevant information to models as available premises, rarely examining concurrently how models discover evidence autonomously and how information presentation within narratives guides or obscures judgment. This paper proposes the WORTH Benchmark: models read original mystery narratives without clue annotations, autonomously select key clue sentences, identify case participants, and explain their reasoning process. The narrative materials are designed by professional authors such that evidence facilitating reasoning coexists with narrative arrangements that delay the revelation of truth. We report a pilot experiment under full-story conditions across two episodes, conducting a total of 70 formal runs on models, of which 67 runs are content-scorable. Scoring separately records hits on author-designated key clue sentences and participant selections; natural language explanations are used for case diagnosis and are not scored independently. The results show that clue hits and participant judgments are not synchronized; across 37 content-scorable runs in Episode 02, 31 runs simultaneously selected the same set of incorrect participants, while adjacent suspicion-oriented and exoneration-oriented sentences were selected 25 times and 0 times, respectively. These phenomena illustrate the diagnostic value of component-wise analysis and suggest that not-fully-cooperative informational relationships may influence evidence selection and judgment. This study only implements full-story conditions for two episodes, and does not establish stable model rankings or infer general mechanisms on this basis; human player records have not yet been cleaned, and this version does not report human-model comparisons.
