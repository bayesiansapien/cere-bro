---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13059
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13059
published: 2026-04-16
authors: Zhenhai Pan, Yan Liu, Jia You
---

# A Proactive EMR Assistant for Doctor-Patient Dialogue: Streaming ASR, Belief Stabilization, and Preliminary Controlled Evaluation

**arXiv:** https://arxiv.org/abs/2604.13059
**Authors:** Zhenhai Pan, Yan Liu, Jia You

## Abstract

arXiv:2604.13059v1 Announce Type: cross  Abstract: Most dialogue-based electronic medical record (EMR) systems still behave as passive pipelines: transcribe speech, extract information, and generate the final note after the consultation. That design improves documentation efficiency, but it is insufficient for proactive consultation support because it does not explicitly address streaming speech noise, missing punctuation, unstable diagnostic belief, objectification quality, or measurable next-action gains. We present an end-to-end proactive EMR assistant built around streaming speech recognition, punctuation restoration, stateful extraction, belief stabilization, objectified retrieval, action planning, and replayable report generation. The system is evaluated in a preliminary controlled setting using ten streamed doctor-patient dialogues and a 300-query retrieval benchmark aggregated across dialogues. The full system reaches state-event F1 of 0.84, retrieval Recall@5 of 0.87, and end-to-end pilot scores of 83.3% coverage, 81.4% structural completeness, and 80.0% risk recall. Ablations further suggest that punctuation restoration and belief stabilization may improve downstream extraction, retrieval, and action selection within this pilot. These results were obtained under a controlled simulated pilot setting rather than broad deployment claims, and they should not be read as evidence of clinical deployment readiness, clinical safety, or real-world clinical utility. Instead, they suggest that the proposed online architecture may be technically coherent and directionally supportive under tightly controlled pilot conditions. The present study should be read as a pilot concept demonstration under tightly controlled pilot conditions rather than as evidence of clinical deployment readiness or clinical generalizability.
