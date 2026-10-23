---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.196024+00:00
arxiv_id: 2610.09861
url: https://huggingface.co/papers/2610.09861
arxiv_url: https://arxiv.org/abs/2610.09861
date: 2026-10-22
---

# Toward Part-Aware Choral Transcription with singing voice assignment

Single-instrument automatic music transcription (AMT) has advanced substantially, yet choral applications require soprano, alto, tenor, and bass (SATB) to be transcribed as separate parts. Recent note-level choral AMT instead produces a single merged note track, limiting rehearsal, education, and score reconstruction. To address this limitation, we introduce Part-aware Choral Transcription (PawCT), to our knowledge the first end-to-end neural framework that identifies active SATB parts from choral audio and transcribes each into a separate note-level track. PawCT combines part-specific onset, offset, and frame prediction with part-presence estimation, union-level supervision, and structured training targets using a range prior (RP) based on SATB pitch ranges and its ordered-continuity (OC) extension, which adds within-part melodic continuity and cross-part pitch ordering. On YouChorale, PawCT-RP-OC achieves a macro part-aware note F1 of 0.225 at a 50-ms onset tolerance, outperforming an adapted choral baseline (0.165) by 36.4% relative and a two-stage post-hoc assignment pipeline (0.175). Its part-agnostic variant, PagCT, achieves a 50-ms onset F1 of 0.382, compared with 0.237 for the previous state-of-the-art choral AMT model. Cross-dataset evaluations on CSD and Cantoria further assess performance under dataset shift. These results demonstrate the benefit of jointly modeling note transcription and vocal-part assignment. Code and demos are available at https://hanyu-meng.github.io/Paw_Choral_AMT_Demo/.
