---
source: farmer/huggingface
farmed: 2026-08-07T18:44:38.156257+00:00
arxiv_id: 2608.01481
url: https://huggingface.co/papers/2608.01481
arxiv_url: https://arxiv.org/abs/2608.01481
date: 2026-08-07
---

# Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval

Short segments of perceived speech can be retrieved from non-invasive magnetoencephalographic (MEG) recordings by deep networks trained with a CLIP-style objective against wav2vec 2.0 audio embeddings. Yet their weights do not map onto electrophysiological quantities, and it remains unclear which speech properties drive retrieval.
  We build on a high-performing MEG-to-audio retrieval architecture but redesign both its front end and decoder. Its spatial attention operates on a flattened sensor layout; we replace it with spherical harmonics defined on the three-dimensional MEG helmet geometry. We reduce the subject-specific representation from 270 to 25 branches, add a temporal filter to each branch to match it to a neuronal source in space and time, and make the convolutional decoder shallower. Ocular and cardiac components are removed before training to reduce the risk of stimulus-locked shortcuts.
  On MEG-MASC, the model reaches 39.75 +/- 0.34% Top-1 accuracy among 1005 candidates across six trained solutions, with about 20 times fewer decoder parameters. Its weights map to source space, recovering generators consistent with the speech-perception network, while left-lateralized branches carry higher-frequency rhythmic components not evident on the right. Paired MEG occlusion shows that 15 of 19 stimulus features contribute, with the largest effects for silence, sound intensity, vowels, and acoustic onsets. Random word lists behave oppositely: substituting narrative MEG into them improves retrieval, indicating that activity without narrative structure carries less recoverable information than activity during coherent speech. The wav2vec target can be reduced to about twelve learned feature dimensions without loss of accuracy, whereas strong temporal compression causes a clear loss.
  Together, source mapping and input interventions reveal what drives retrieval.
