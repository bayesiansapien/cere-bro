---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.14232
url: https://huggingface.co/papers/2610.14232
arxiv_url: https://arxiv.org/abs/2610.14232
date: 2026-10-16
---

# Speech event detector: Timestamped detection of non-verbal vocalizations and background sounds for rich speech transcription

Automatic speech recognition produces words but drops the non-verbal content of a recording: the breaths, coughs, sighs and laughter of the speaker, and the horns, music or barking around them. We describe Speech Event Detector, a 5.8-million-parameter convolutional-Transformer model that outputs probabilities every 40 ms for 54 event classes (20 speaker vocalizations and 34 background sounds), together with post-processing that converts these probabilities into timestamped events and a procedure for merging the events into a Whisper transcript. The model is trained on material drawn from seven public datasets whose labels come in incompatible forms: single detected regions, free-text tags with timestamps, temporally strong ontology labels, symbols embedded in transcripts, isolated recordings and environmental recordings. We unify them using rule-based label mapping, recover timestamps for transcript-embedded labels through CTC forced alignment, locating 6,360 of 8,620 sounds, and combine about 168 hours of real annotated training recordings with synthetic mixtures and augmentation using real background noise. Per-class thresholds for two operating profiles are tuned on real held-out recordings, and performance is estimated using two-fold cross-validation. On whole held-out recordings from four datasets, considering the 48 classes with at least ten held-out events, the sensitive profile detects an average of 49 percent of a class's events, covering 67 percent of all 9,367 events, at a macro precision of 0.30. The balanced profile achieves a macro recall of 0.37 at a precision of 0.36, with macro event F1 scores of 0.32 and 0.33, respectively. The detector runs about 39 times faster than real time on eight CPU threads.
