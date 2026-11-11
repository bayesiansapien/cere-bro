---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.328280+00:00
arxiv_id: 2611.08969
url: https://huggingface.co/papers/2611.08969
arxiv_url: https://arxiv.org/abs/2611.08969
date: 2026-11-10
---

# PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals

We present PhysioWave-T, a token-efficient wavelet foundation model family for EEG, ECG, and sEMG. Dynamic scale folding recombines J+1 wavelet subbands prior to tokenization, compressing sequence length from (J+1)CS to CS tokens for J levels, C channels, and S temporal patches. Route-specific front ends and learned channel-name embeddings allow one Transformer per modality to handle diverse montages and sampling rates, while unseen setups reuse the backbone via lightweight adapters. We pre-train a 30M-parameter EEG model on over 15M windows (19--128 channels), alongside ECG (30M) and sEMG (12M) encoders. Across four EEG routes, scale folding cuts Transformer latency by 4.0--7.2x and peak memory by 6.8--12.7x over scale expansion without accuracy loss. Our EEG encoder leads 8 of 9 metrics against BENDR, BIOT, LaBraM, and EEGPT, and surpasses LUNA-L on wearable seizure detection with fewer parameters. Reliability-aware latent fusion (RALF) further integrates summary tokens from independently pre-trained encoders via sample-adaptive weights. On SeizeIT2, RALF raises event sensitivity at 11 false alarms/h from 61.4% to 74.4% and window AUPRC from 0.321 to 0.399 over the best unimodal baseline, outperforming weighted-logit and concatenation fusion across all variants. PhysioWave-T also achieves state-of-the-art sEMG accuracies and top macro-F1 on PTB-XL Super and Chapman-Shaoxing. Code and models: https://github.com/ForeverBlue816/PhysioWave.
