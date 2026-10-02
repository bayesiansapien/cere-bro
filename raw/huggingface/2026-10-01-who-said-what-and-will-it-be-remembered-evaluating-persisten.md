---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352728+05:30
arxiv_id: 2609.39344
url: https://huggingface.co/papers/2609.39344
arxiv_url: https://arxiv.org/abs/2609.39344
date: 2026-10-01
---

# Who Said What, and Will It Be Remembered? Evaluating Persistent Speaker Attribution Across Meetings

Speech transcripts used as long-term memory must preserve both words and stable speaker identities. Existing meeting-transcription metrics either ignore speakers or remap anonymous speakers independently in each recording, so they cannot measure whether the same person retains one identity across meetings. We evaluate persistent speaker attribution with Speaker Identified cpWER (SI-cpWER), which scores a corpus under one global speaker-ID assignment. The benchmark covers five commercial diarize-then-identify cascades, two open academic baselines, and ThyVoice on the full 129-meeting CHiME-8 NOTSOFAR evaluation set in clean and noiseaugmented form, plus CHiME-6. ThyVoice is our end-to-end reference system; it repairs overlap and gates the evidence used to create and update voiceprints. Requiring persistent identity changes the commercial ranking: ThyVoice records lower SI-cpWER than every evaluated commercial cascade in all three conditions and the lowest mean in the full panel, 47.13 versus 54.75 for the next system. Complementary lexical, diarization, per-recording attribution, and speaker-clustering diagnostics characterize upstream error surfaces in the final attributed record. These results show why persistent attribution must be evaluated directly in systems that reuse conversations across time.
