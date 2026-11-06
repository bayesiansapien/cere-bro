---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.305723+00:00
arxiv_id: 2611.04634
url: https://huggingface.co/papers/2611.04634
arxiv_url: https://arxiv.org/abs/2611.04634
date: 2026-11-05
---

# VeriSpoof: Beyond Real or Fake with One Audio LLM

A speech deepfake detector estimates whether a recording is synthetic, but a forensic analyst also asks which system produced it, whether recordings share a source, and what evidence supports each conclusion. We present VeriSpoof, an audio language model that unifies five tasks with shared weights: deepfake detection, generator attribution (generator, acoustic model and vocoder), recording-condition analysis, synthesized-span localisation, and source verification. Each decision is supported by grounded rationales whose statements can be independently verified. Answers are scored by sentence likelihood, allowing detection and source verification to be thresholded without separate heads. Rationale statements can be checked against waveform measurements, span labels, or generator metadata. Counterfactual examples train decisions to follow the stated evidence. Across the 14 Speech-DF-Arena test sets, VeriSpoof-Plus achieves 2.14% pooled EER, ranking third of 28 systems and first among open-weight systems. VeriSpoof-Base, trained only on official training splits of eight corpora, achieves 4.43% EER, less than half that of the next open-weight detector. With the same weights, VeriSpoof-Plus verifies whether recordings from generators unseen in training share a source at 6.2% EER. Controlled studies show that the audio representation governs detection, the LLM governs recording comparison, and source supervision is necessary for neural-codec fakes. Statement-checkable rationales catch partial fakes missed by one-step answers (99.6% vs. 78.4% on PartialEdit) and determine decisions under edits unseen in training (99.5%). Training updates only 29.7M of 2.85B parameters, fitting a single 24 GB GPU with gradient checkpointing. We release both models, inference code, a demo, and VeriSpoof-Bench, the evaluation suite covering these questions.
