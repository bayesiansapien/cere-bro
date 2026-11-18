---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.114759+00:00
arxiv_id: 2611.04395
url: https://huggingface.co/papers/2611.04395
arxiv_url: https://arxiv.org/abs/2611.04395
date: 2026-11-17
---

# Correct Labels Are Not Enough: Reliable Metadata Can Silently Control Model Behavior

Fine-tuning data can include metadata that predicts the correct answer, such as a reward-model score or a quality label. We ask whether a model learns to rely on this metadata even when every training label is correct. We fine-tune 7-9B open-weight models from three families on multiple-choice questions in which (Reward: 5) always marks the correct option; when this annotation is moved to a wrong option at test time, models select that option on 97-100% of CommonsenseQA items. Removing it leaves most answers correct, so evaluation without it misses the dependence. Cue-following rises sharply with training-time reliability and develops even with neutral or nonsense annotation words, although test-time wording affects its strength. A Qwen3 experiment also finds cue dependence in option-letter scores after direct preference optimization. Audits can test for this dependence by moving or removing visible annotations while holding the task and correct answer fixed.
