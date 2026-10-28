---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33413
url: https://huggingface.co/papers/2610.33413
arxiv_url: https://arxiv.org/abs/2610.33413
date: 2026-10-27
---

# AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos

Localized AI manipulations in long-form videos often affect brief events within otherwise authentic content, making video-level classification insufficient for forensic analysis. Existing audio-visual deepfake benchmarks largely focus on short talking-head clips, while long-form temporal forensics remains predominantly visual. We introduce AV-FABLE, a dual-timeline benchmark for sparse manipulations in open-scene long-form audio-visual videos. AV-FABLE contains 16,650 pristine--manipulated twin pairs (998 hours) created with 27 editing configurations, with separate audio and visual timelines that enable modality-specific temporal localization and expose errors hidden by joint-timeline evaluation. On AV-FABLE, zero-shot prompting of audio-visual large language models (AV-LLMs) yields near-chance detection and poor temporal localization. In contrast, supervised readouts of their frozen perception features recover strong forensic signals, suggesting manipulation evidence is encoded in these representations but not effectively exposed through language outputs. Motivated by this observation, we propose NFSR(Native Forensics via Separated Readouts), which reads frozen AV-LLM features with separate audio and visual temporal decoders. NFSR achieves the best audio-visual localization performance in-domain and across all three out-of-distribution settings, including transfer to held-out videos from an external long-video forensic benchmark. AV-FABLE, code, and model weights will be publicly released.
