---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.386524+00:00
arxiv_id: 2611.21885
url: https://huggingface.co/papers/2611.21885
arxiv_url: https://arxiv.org/abs/2611.21885
date: 2026-11-20
---

# Language Models Can Rewrite Their Own Weights

Language models are trained once, frozen and deployed: improving one again takes another training run, and a prompt, a scaffold or extra computation at inference is gone once the task ends. A frontier model has been shown to edit the weights of a much smaller one. We ask whether a model can rewrite its own weights to make itself better, and find that it can, by its own reasoning, with no gradients and no training; we call this self-rewriting. Given its weights, graded answers and the ability to run itself, a 27B model diagnoses its failure and edits the weights behind it. It surpasses itself: its own edit makes it 6.6 points more accurate on 490 problems it never saw, in a test fixed in advance, and another session's edit also makes it significantly better. It keeps getting better: it submits an edit only when its own tests support it, each edit replacing the last, and over its first eight such sessions its accuracy only rises. Unlike test-time scaling, the gain persists in its weights and adds no cost per answer; unlike training, it needs no pre- or post-training infrastructure, only an open model and hours on one GPU. It repairs a damaged copy of itself: it locates the corrupted matrix and rewrites it with values of its own, never reading the undamaged weights; found on text math problems alone, the repair lifts the copy on six image benchmarks it never saw from 7% to 70% accuracy, 83% of the undamaged model's. And the ability emerges with scale: across four sizes of one family, the 2B model makes no edit and the 4B and 9B models break themselves; only the 27B model works on itself as a human would, comparing its hidden states on answers that finish and on answers that run out of tokens, weakening the direction that separates them. Like a human, a model need not separate training from inference; improving a language model may come to take a conversation rather than a training run.
