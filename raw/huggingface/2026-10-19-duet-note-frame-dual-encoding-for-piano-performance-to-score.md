---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21467
url: https://huggingface.co/papers/2610.21467
arxiv_url: https://arxiv.org/abs/2610.21467
date: 2026-10-19
---

# DuET: Note-Frame Dual Encoding for Piano Performance-to-Score Transcription

Transcribing expressive piano performances into scores requires interpreting individual note timings within an underlying metrical structure. However, score attributes are associated with notes, whereas beats may occur without coincident note onsets. We introduce DuET, a Dual-Encoder Transformer that jointly learns note-level performance MIDI-to-score (PM2S) transcription and frame-level beat and downbeat tracking. Bidirectional cross-attention connects note and frame encoders, while an autoregressive decoder alternates between their representations to predict structured score attributes. We further introduce TimeRoPE and Time-Pitch Rotary Positional Encoding (TPRoPE) to establish a shared performance-time reference and explicitly encode relative temporal and pitch relationships. Evaluations on ASAP, a classical piano dataset, and our curated Gangqinpu dataset, which spans multiple genres with a focus on popular piano music, demonstrate improvements in score timing and notated duration. Compared with the strongest baseline on each dataset, DuET reduces MUSTER mean error from 6.56% to 3.64% on Gangqinpu and from 11.30% to 11.22% on ASAP. Ablations support the benefits of frame-level context, time-based positional encoding, and decoder-history masking. Code, weights, and demos are available at https://github.com/wei-zeng98/DuET.
