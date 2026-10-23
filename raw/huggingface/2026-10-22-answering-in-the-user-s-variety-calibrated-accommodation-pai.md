---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.194698+00:00
arxiv_id: 2610.28474
url: https://huggingface.co/papers/2610.28474
arxiv_url: https://arxiv.org/abs/2610.28474
date: 2026-10-22
---

# Answering in the User's Variety: Calibrated Accommodation Pairs for Post-Training

People adapt how they talk to the person in front of them. However, chat models tend to respond in Standard English regardless of the dialect used by the user. A uniform answer can hide whether training treats these users alike, and output audits cannot tell as well. We trace how each post-training stage, from supervised fine-tuning (SFT) to preference optimization (DPO) and reinforcement learning, changes a model's tendency to match the user, and read what each update prefers from two content-matched replies, one matching the user and one not. Across 10 open model lineages, post-training standardizes replies to every informal cue, yet after adjusting for how likely each reply already was, the DPO update still favours matching British and Australian spelling over AAE and Singlish on 10 lineages, and models still produce AAE features when asked. We then introduce calibrated accommodation pairs (CAP), preference data that reward matching users' dialect density while preserving Standard English for Standard-English users. On a fully open model, CAP raises convergence on features it was not trained on without a detectable increase in dialect for Standard-English users or a cost in instruction following. In contrast, one-sided pairs reach a similar gain only by overshooting the user and imposing dialect. Our findings show that uniform replies can hide selective updates and audits should read the update as well as the output. Code: https://github.com/kouzhizhuo/cap-accommodation.
