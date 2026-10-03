---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.817714+00:00
arxiv_id: 2609.39027
url: https://huggingface.co/papers/2609.39027
arxiv_url: https://arxiv.org/abs/2609.39027
date: 2026-10-02
---

# A Missing Piece for Trustworthy AI Reviewers: From Benchmarking Rhetorical Robustness to SciCore Review

AI reviewers can assign different judgments to manuscripts that report the same science in different wording, potentially rewarding rhetorical optimization over scientific improvement. We formulate Rhetorical Robustness as the joint requirement of stability across content-preserving rewrites and discrimination across papers. We introduce RobustReview, a controlled full-manuscript benchmark with 1,260 manuscript versions, and evaluate 30 reviewer configurations. The benchmark reveals false robustness, where low rewrite sensitivity coincides with score collapse across papers, and shows that human alignment and rhetorical robustness rank reviewers differently. Moreover, the evaluated content-focused prompting protocol does not consistently improve robustness across backbones. Motivated by these findings, we introduce SciCore, a dual-branch reviewer that averages a full-manuscript judgment with a judgment based on an extracted, structured science core. This design combines manuscript-level assessment with a content-normalized view intended to reduce rhetorical sensitivity. In our primary GPT-5.5 comparison, SciCore achieves a leading joint stability-discrimination profile among the benchmarked reviewers while maintaining competitive human alignment. These results identify rhetorical robustness as a distinct evaluation target and demonstrate the potential of science-core review to improve it.
