---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353736+05:30
arxiv_id: 2609.35922
url: https://huggingface.co/papers/2609.35922
arxiv_url: https://arxiv.org/abs/2609.35922
date: 2026-10-01
---

# Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change

A voice agent can handle almost every call on the words alone and still fail the few its sector's rules were written for. Emergency-call standards, fraud guidance, radio phraseology and vulnerability rules recognise that how a caller sounds, or what else is audible, can change the right action. VoxParity tests whether agents act on it. In 183 scenarios from 14 sectors, one transcript stays fixed while the audio changes (a coaching voice, a medical monitor beeping, a mayday under a radio check, noise over a drug name, a child's voice placing a bet, a frightened whisper), and with it the correct typed tool call. A words-only null test credits a system only if hearing the call moves its actions more than it moves a pipeline that only reads the words. Only 11 of the 23 systems that can also be run on the transcript pass. Descriptively, errors run toward the words: when the audio calls for protection, all 28 systems carry out the routine request more often than they over-react on clean calls (41% against 12% pooled; the words-only pipeline, 58% against 15%). Exploratory analyses place most of the leading systems' misses on cues they heard; systems beat the null almost entirely on items that state the rule; the leading systems overrule heard resignation or confusion far more often than acute alarm; and, in the models tested, describing the voice and stating the rule each recover part of the shortfall, leaving a gap on emotion.
