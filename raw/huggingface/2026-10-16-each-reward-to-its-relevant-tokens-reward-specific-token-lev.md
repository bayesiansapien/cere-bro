---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21439
url: https://huggingface.co/papers/2610.21439
arxiv_url: https://arxiv.org/abs/2610.21439
date: 2026-10-16
---

# Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL

Language models are increasingly trained against several verifiable rewards at once, such as the correctness and the format of a tool call, or the individual constraints of a complex instruction. Reward-decoupled normalization (GDPO) normalizes each reward separately so that different reward combinations keep distinct advantages, but it still spreads every reward's advantage evenly over the whole response, although each verifier checks only a few positions. We propose MRTPO, which assigns the advantage of each reward to the tokens relevant to it, using the information its verifier checks, without auxiliary models or token-level annotations. For each reward, the policy replays its own response with and without that reward's verifier information, and the per-token Jensen-Shannon distance between the two next-token distributions measures each token's relevance and reassigns the advantage. On text-to-SQL, multi-constraint instruction following and tool calling, MRTPO converges faster and achieves better performance than the compared methods.
