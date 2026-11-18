---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.112854+00:00
arxiv_id: 2611.20385
url: https://huggingface.co/papers/2611.20385
arxiv_url: https://arxiv.org/abs/2611.20385
date: 2026-11-17
---

# DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images

Can a vision-language model look at a picture of a chain reaction and tell what will happen? Recent multimodal models describe scenes fluently and solve textbook physics problems, which suggests they should also predict how a scene of ramps, ledges, pendulums, seesaws and dominoes plays out once a ball is pushed. We tested this claim on 30 models from 10 families and reached a clear conclusion: unaided, no model predicts the outcome reliably. We built DominoBench, a benchmark of still images of 2D rigid-body scenes whose outcome a physics simulator computes. It holds 854 items in 427 minimal pairs, in which a change of one to three grid steps in one quantity decides whether one person survives, and every item comes with a four-rung hint ladder ending in the exact calculation that decides the outcome. Unaided, frontier models from Anthropic, Google and OpenAI are right about the person whose fate flips in at most 72% of items and answer both twins of a pair correctly in at most 34%. Pointing at the deciding step helps little, and exact geometry given as text barely helps, yet once the deciding calculation and the quantities it needs, including speeds that a still image cannot show, are written out, the same models reach 82-92% on the deciding person, while small open-weight models stay near chance. Physical prediction from a still image therefore fails at the quantitative step: the strongest models use the deciding quantity when they are given it, but do not produce it on their own. For models that plan or act in the physical world, a fluent account of a scene is thus no evidence of a correct prediction: such models must find and compute the deciding quantity unprompted, and DominoBench tests whether they do.
