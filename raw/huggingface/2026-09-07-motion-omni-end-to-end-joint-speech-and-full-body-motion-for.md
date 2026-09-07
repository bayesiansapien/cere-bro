---
source: farmer/huggingface
farmed: 2026-09-07T09:18:04.961411
arxiv_id: 2609.04250
url: https://huggingface.co/papers/2609.04250
arxiv_url: https://arxiv.org/abs/2609.04250
date: 2026-09-07
---

# Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue

An avatar that holds a conversation should decide what to say and to move while saying it, yet these abilities live in separate model families: spoken dialogue models produce speech without motion, and co-speech motion models produce motion only from audio handed to them. The standard remedy is a cascade that first generates the spoken response and then runs a motion model over the finished audio, which requires a second full inference pass and precludes any joint optimisation between the two. We present Motion-Omni, an end-to-end framework in which a spoken dialogue model natively outputs explicit facial expression together with hand, upper-body and lower-body motion, generated directly from the hidden states that produce the speech. Joint training is not optional here: with the speech pathway frozen, motion remains misaligned with the audio, and co-adapting the LLM, Speech Generator and Motion Generator under both objectives is what recovers alignment while retaining spoken-dialogue ability. Supervision comes from a scalable, model-agnostic pipeline that pseudo-labels consistent-voice speech responses with a replaceable motion teacher, yielding 422,856 quality-ranked pairs (1,402 hours). We further release SwDA-500 and, to our knowledge, the first public evaluation protocol for stochastic open-ended full-body spoken dialogue, matching audio across motion systems while unifying rendering, automatic metrics, human evaluation, and latency measurement. Instantiated with a Qwen2.5-7B-Instruct backbone, Motion-Omni-Q7 matches the same-audio teacher cascade to within 2% on reference-free motion metrics while responding 5.4 x faster (RTF=0.78, faster than real time), surpasses all non-teacher cascades on beat correlation and diversity, and reaches a 2.62% word error rate, the lowest among the omni-modal systems compared.
