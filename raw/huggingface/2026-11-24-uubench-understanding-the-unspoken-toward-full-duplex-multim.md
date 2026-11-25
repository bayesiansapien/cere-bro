---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.922250+00:00
arxiv_id: 2611.30157
url: https://huggingface.co/papers/2611.30157
arxiv_url: https://arxiv.org/abs/2611.30157
date: 2026-11-24
---

# UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction

Effective real-time, full-duplex multimodal interaction requires systems to understand not only what users say, but also the communicative needs conveyed through prosody, facial expressions, gestures, and context, and to generate audiovisual responses that appropriately address those needs. Existing evaluations offer limited insight into whether systems translate an understanding of such unspoken needs into effective responses. We introduce UUBench, a benchmark for assessing how well multimodal interactive systems Understand the Unspoken intent and address users' implicit communicative needs. The inherent subjectivity of implicit intent inference poses a key challenge for evaluation. To address this, we introduce Process-Oriented Scoring, which grounds the assessment of intent fulfillment in observable auditory and visual cues, such as prosody and gestures. Rather than relying solely on a single overall score, it evaluates how well a response addresses the communicative needs conveyed by each applicable primitive dimension. We aggregate the dimension-level scores according to each dimension's relevance to the annotated evidence. Beyond intent fulfillment, Outcome-Oriented Scoring evaluates the naturalness, appropriateness, and human-likeness of the reply itself under audio-only, visual-only, and audiovisual conditions. To make these judgments traceable to observable evidence, we propose a Fact-Grounded Scoring JEV module, which uses structured, timestamped audiovisual observations of the user and the digital human's reply to assess one dimension or criterion at a time. UUBench provides a foundation for assessing whether multimodal interactive systems respond effectively to meaning beyond literal wording, supporting progress toward context-aware, real-time, full-duplex interaction.
