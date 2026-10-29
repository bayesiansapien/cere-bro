---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996898+05:30
arxiv_id: 2610.36184
url: https://huggingface.co/papers/2610.36184
arxiv_url: https://arxiv.org/abs/2610.36184
date: 2026-10-28
---

# Lipi-Ghor: A Large-Scale, Diarized, Multi-Domain Bengali Speech Corpus and a Scalable Pipeline for Building It

Bengali, spoken by over 230 million people, remains severely under-resourced in spoken language research. Existing open Bengali ASR corpora are confined to short, read or crowd-sourced speech and lack speaker diarization and long-form audio.
  We present Lipi-Ghor, a large-scale weakly-supervised Bengali speech corpus comprising 885 hours of audio sourced from 998 YouTube videos across 596 unique channels, spanning 17 diverse domains including audiobooks, drama, religious sermons, news, and regional dialects. Each recording is annotated in SSTT format (Speaker, Speech, Transcription, Timestamp), which combines automated diarization with Bengali YouTube caption tracks.
  To our knowledge, Lipi-Ghor is the first Bengali speech corpus to pair large-scale coverage with speaker-diarized, long-form audio annotations, both of which are absent from existing open Bengali resources. We also present the construction methodology as a replicable pipeline for any language with a sufficient captioned YouTube presence. Targeted channel curation across a handful of rich domains yields corpus scales that were previously out of reach for low-resource languages.
  We benchmark four widely-used ASR models under zero-shot and fine-tuned conditions. All four degrade consistently on emotive, dialectal, and long-form content. Because caption targets are noisy, we also release a human-annotated gold evaluation split, verified by 17 volunteer annotators over 30 hours of human-in-the-loop correction and stratified across all 17 domains.
  We release our original contributions (video-ID lists, diarization output, pipeline code, and the gold annotations) under CC-BY-4.0, and distribute caption-derived transcripts for research use only; no raw audio is redistributed.
