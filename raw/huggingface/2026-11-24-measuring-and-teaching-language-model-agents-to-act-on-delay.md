---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.928865+00:00
arxiv_id: 2611.28158
url: https://huggingface.co/papers/2611.28158
arxiv_url: https://arxiv.org/abs/2611.28158
date: 2026-11-24
---

# Measuring and Teaching Language Model Agents to Act on Delayed Consequences

Language model agents are increasingly asked to run ongoing multi-day operations rather than finish isolated single-turn tasks. In daily operations, today's choices reshape later observations and cash constraints because empty shelves hide lost walk-in demand, short-shipped customers quietly shrink future orders weeks later, and emergency buying drains working capital. We introduce SMB Bench, a calibrated 90-day wholesale simulator with 18 causally paired tasks and an 859-run frontier trace dataset, to ask what experience and learning signal make an agent better at noticing, attributing, and acting on the delayed consequences of its own decisions in unseen businesses. Across 16 frontier models, only 3 outperform a fixed buying rule; models often record a relevant diagnosis in their notes without changing later purchases in time, showing that diagnosing a problem, changing behavior, and improving a business are separate achievements. To study how experience improves those failures in an open model (Qwen3.8-27B), we used training-business records to identify operational rules and archived frontier quarters as starting states to continue from rather than transcripts to copy. On an unseen test business under identical evaluation instructions, the trained policy followed customer-protection commitments more consistently and reduced severe-loss quarters, while the additional profit benefit remained uncertain. Carrying those commitments through the quarter exposed the cost of fulfilling them, as early-quarter stocking habits left the buyer relying on emergency supply and a deteriorating supplier. The results separate recognizing a delayed effect, acting on it consistently, and coordinating surrounding decisions so that the response improves profit. SMB Bench connects these observations to a learning method by turning archived decisions and their consequences into reusable training experience.
