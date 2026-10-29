---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994635+05:30
arxiv_id: 2610.35962
url: https://huggingface.co/papers/2610.35962
arxiv_url: https://arxiv.org/abs/2610.35962
date: 2026-10-28
---

# h1: A Taste of the Bitter Lesson in Automated Theorem Proving

While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orchestrating specialized provers. This raises a bitter-lesson question: can a simple agentic loop that scales test-time compute match these workflows? The answer matters as formal verification must scale to keep up with frontier models producing research mathematics, yet new workflows rarely settle it, as their gains are often confounded with stronger models or more compute. We study this question with h1, a simple harness that gives a model an efficient interface to Lean 4 and keeps it working through verifier feedback and self-reflection, without imposing a decomposition or search structure. h1 reaches state-of-the-art results on PutnamBench, FATE-X, and FormalConjectures100-Solved, settles eight open problems in FormalConjectures, and, at matched models, matches or outperforms specialized workflows such as Goedel-Architect and AlphaProof Nexus, surprisingly showing that a single attempt (pass@1) can often scale to solve open problems. Through ablations and matched-model comparisons with Claude Code and AxProverBase, we find that simplicity alone is not enough: an efficient Lean interface largely determines cost and solve rate. We thus recommend that future work evaluate frontier models with efficient execution feedback before prescribing workflows, at the risk of bitter lessons.
