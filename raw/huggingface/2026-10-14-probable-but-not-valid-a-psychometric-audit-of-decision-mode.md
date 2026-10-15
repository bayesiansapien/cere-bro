---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.513293+00:00
arxiv_id: 2610.14912
url: https://huggingface.co/papers/2610.14912
arxiv_url: https://arxiv.org/abs/2610.14912
date: 2026-10-14
---

# Probable but Not Valid: A Psychometric Audit of Decision Models as Synthetic Survey Respondents

Language models are increasingly used to create synthetic survey samples, also called silicon samples. Decision models are a new class of language models that return a probability for each point of a rating scale instead of text. We ask whether these models, or the newest generative LLMs, can stand in for human respondents on a psychometric survey. We test fourteen decision models from eleven providers and 47 generative LLMs on an open Lithuanian organisational-psychology survey (n=263, 68 items), with 100 real respondent profiles, the Psychometric Similarity Score (PSS) and statistical baselines. The best generative model, MiniMax M3, reaches PSS 0.813. This is level with a Gaussian copula fit only on other respondents (0.824) and below a copula fit in sample (0.927). A second sample of 100 real people scores below the best models, so at this size PSS cannot rank them against real respondents. In 5 of 10 product lines the newest generative release scores below an earlier release of the same line beyond resampling noise, and none gains beyond it. With the default rounded readout, 13 of 14 decision models score below the generative reference gpt-5.4-mini. Of the 47 generative models, 33 reproduce the pattern of item correlations better than any decision model. Averaged over respondents, the probability vectors are much closer to the human item marginals than rounded answers. They also rank respondents about as well as a profile regression fit on 163 real people. As forecasts of each person's own answers, however, every decision model is worse than the answer frequencies of other respondents, mainly because its average vector differs from them. The profile regression improves on these frequencies by only 1.0%, so the profile fields say little about how a person answers. Synthetic respondents built on such profiles should therefore aim at sample-level fidelity.
