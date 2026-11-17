---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.000972+00:00
arxiv_id: 2611.18529
url: https://huggingface.co/papers/2611.18529
arxiv_url: https://arxiv.org/abs/2611.18529
date: 2026-11-16
---

# eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means

Meetings last up to an hour, and nobody knows in advance how many people will speak. Neural diarizers with a fixed number of output slots, such as Streaming Sortformer and Nemotron-3, are accurate and run online, but they cannot name more speakers than they have slots. We remove this limit without retraining. The slot head keeps deciding who is active and when speech overlaps, and speaker embeddings are clustered inside a single slot, with the official e-means algorithm, only after every slot has been used. In the streaming system, re-clustering is confined to a bounded window, labels are revised for a few seconds, and identities are anchored to the slots of the head. The resulting system has no limit on the number of speakers and stays accurate when speakers outnumber the slots, where fixed-slot models break down. On meetings that grow to an hour it stays far more accurate than Streaming Sortformer, which accumulates errors, and its cost per update does not grow with the meeting. The same recipe turns the four-slot Streaming Sortformer into an open-speaker system. Across recordings, e-means makes it affordable to link the speakers of a large archive frame by frame, a task that arises when conversational corpora are prepared, and it reaches the clustering quality of Lloyd's k-means several times faster. The method needs little tuning, and e-means runs with its default recipe from a few hundred to more than a million embeddings.
