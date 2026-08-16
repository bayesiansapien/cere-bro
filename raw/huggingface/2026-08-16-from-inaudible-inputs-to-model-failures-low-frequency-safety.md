---
source: farmer/huggingface
farmed: 2026-08-16T13:39:51.900697+05:30
arxiv_id: 2608.09158
url: https://huggingface.co/papers/2608.09158
arxiv_url: https://arxiv.org/abs/2608.09158
date: 2026-08-16
---

# From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs

Large audio-language models (LALMs) have demonstrated strong capabilities in understanding diverse audio inputs. This diversity includes low-frequency signals that are inaudible to humans but can still enter the model and influence its generation. However, the practical impact of such low-frequency inputs on LALMs remains largely unexplored. In this paper, we propose Intermittent Low-Frequency Lockout (ILL), an inaudible red teaming method that evaluates this risk using a universal waveform template in a black box setting. ILL uses Sentence Attention Scale Estimation to determine active intervals and Frequency Confusion Transfer to construct a low-frequency waveform with continuous phase from corpus spectral variation. To mitigate this risk, we propose Distributional Requery Guard (DRG) to detect low-frequency distribution shifts and conditionally request a second recording for semantic recovery. Across six LALMs and multiple audio understanding tasks, ILL reduces accuracy by up to 67 percentage points while receiving a mean human audibility rating of 1.33, close to 1.17 for clean audio; DRG raises mean attacked accuracy from 28.5\% to 46.1\% after clean reacquisition. These findings identify a previously overlooked safety risk for LALMs and provide a foundation for future research on robust audio understanding.
