---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.27404
url: https://huggingface.co/papers/2611.27404
arxiv_url: https://arxiv.org/abs/2611.27404
date: 2026-11-25
---

# Degradation of Language Models under Controlled Load: Synchronization, Rule Execution and Misfires on the Background

As the load grows, a language model makes more and more errors, but different processes stand behind this decline in quality. The model may lose the correspondence with the source text, it may keep its place in the text but execute a rule wrongly, or it may change a word that no rule concerns. In this work the degradation of a model under controlled load is separated into these three components: synchronization, rule execution and misfires. The load is set by rules that replace one word with another in a meaningless text, and each kind of load (the text length, the position of a word in the answer, the replacement density, the number of rules and the place of a rule in the list) is set separately. The alignment of the answer with the reference makes it possible to follow the outcome of every word, and a statistical model that takes into account that the spread of difficulty between requests itself depends on the load restores, for each component, the laws of its dependence on every kind of load. These laws make up the passport of a model. The paper presents the method of the separation, the principles of constructing the laws and the passports of seven models built by this method; the separation opens the way to studying the fine structure of the behavior of a neural network.
