---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.927386+05:30
arxiv_id: 2610.36095
url: https://huggingface.co/papers/2610.36095
arxiv_url: https://arxiv.org/abs/2610.36095
date: 2026-10-29
---

# Instruction Capacity: Behavior and Degradation of Language Models under Controlled Load

The quality with which language models follow instructions falls as the load grows, yet there is still no quantity that expresses the limit of a model in units of load with an uncertainty. We propose an instrument in which the load consists of rules that replace single-token words in a text without meaning: such an instruction is atomic, the rules are independent by the construction of the task, and the outcome of every application of a rule is determined by a computable reference answer. Every occurrence of a word to be replaced becomes a Bernoulli trial with a known position in the answer and a known rule number. The statistical model first measures the shape of the dependence of the probability of a right replacement on the text length, the word position, the replacement density, the number of rules and the rule number, then describes it by smooth laws and restores a reference level that does not depend on the choice of the coding. The model yields the instruction capacity - the number of rules held at a given share of right replacements - with an uncertainty. A measurement of GPT-4o mini (2958 requests, 642,430 trials) gave regular laws for every load factor and for the collapse of the answer; the instruction capacity was about 37-38 rules at a share of right replacements of 0.95, and about 18-19 rules at the full replacement density. The code of the instrument, the measurement data and the passport are open, and every number of the passport is recomputed from the published points. The passport of a model serves as the calibration of a future meter of the instruction load of prompts.
