---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.05056
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.05056
published: 2026-04-16
authors: Alexis Ross, Megha Srivastava, Jeremiah Blanchard
---

# Modeling Student Learning with 3.8 Million Program Traces

**arXiv:** https://arxiv.org/abs/2510.05056
**Authors:** Alexis Ross, Megha Srivastava, Jeremiah Blanchard

## Abstract

arXiv:2510.05056v2 Announce Type: replace  Abstract: As programmers write code, they often edit and retry multiple times, creating rich "interaction traces" that reveal how they approach coding tasks and provide clues about their level of skill development. For novice programmers in particular, these traces reflect the diverse reasoning processes they employ to code, such as exploratory behavior to understand how a programming concept works, re-strategizing in response to bugs, and personalizing stylistic choices. In this work, we explore what can be learned from training language models on such reasoning traces: not just about code, but about coders, and particularly students learning to program. We introduce a dataset of over 3.8 million programming reasoning traces from users of Pencil Code, a free online educational platform used by students to learn simple programming concepts. Compared to models trained only on final programs or synthetically-generated traces, we find that models trained on real traces are stronger at modeling diverse student behavior. Through both behavioral and probing analyses, we also find that many properties of code traces, such as goal backtracking or number of comments, can be predicted from learned representations of the students who write them. Building on this result, we show that we can help students recover from mistakes by steering code generation models to identify a sequence of edits that will results in more correct code while remaining close to the original student's style. Together, our results suggest that many properties of code are properties of individual students and that training on edit traces can lead to models that are more steerable, more predictive of student behavior while programming, and better at generating programs in their final states. Code and data is available at https://github.com/meghabyte/pencilcode-public
