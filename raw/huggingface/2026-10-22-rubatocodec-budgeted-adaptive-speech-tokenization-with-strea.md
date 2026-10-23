---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.194164+00:00
arxiv_id: 2610.29434
url: https://huggingface.co/papers/2610.29434
arxiv_url: https://arxiv.org/abs/2610.29434
date: 2026-10-22
---

# RubatoCodec: Budgeted Adaptive Speech Tokenization with Streaming Decoding

Neural speech codecs provide discrete tokens for speech generation. Lower frame rates shorten token sequences, but each token must then carry more linguistic and acoustic information. Variable-frame-rate codecs address this trade-off by adapting token allocation to speech content, but threshold-based allocation lets content determine the token count, so the sequence length a speech generator must produce varies across utterances and datasets at a fixed setting. We present RubatoCodec, a variable-frame-rate speech codec built on X-Codec-2 with an exact utterance-level event budget and streaming decoding. Its Adaptive Firing mechanism uses changes in codec features and waveform spectra to divide speech into variable-duration events without a learned boundary predictor. Discrete codes and an explicit duration represent each event, allowing a speech generator to predict and decode one event at a time. Controlled experiments show that adaptive allocation outperforms fixed-rate coding in reconstruction fidelity and intelligibility at low event rates. A model trained on large-scale multilingual speech achieves competitive reconstruction quality across English, Japanese, and Mandarin, with the best intelligibility preservation among the compared codecs on the evaluated English and Japanese benchmarks at comparable bitrates. In a matched text-to-speech comparison, the adaptive representation yields lower WER and higher UTMOS and UTMOSv2 with comparable speaker similarity. The speech generator also learns the codec's utterance-level event budget without an explicit generation-time rate constraint. These results demonstrate that budgeted adaptive speech representations support both high-quality reconstruction and streaming text-to-speech generation. Code and weights are available at https://github.com/third-intelligence/RubatoCodec and https://huggingface.co/third-intelligence/RubatoCodec.
