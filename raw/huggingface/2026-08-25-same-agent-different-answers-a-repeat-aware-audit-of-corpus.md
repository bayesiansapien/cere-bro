---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.22856
url: https://huggingface.co/papers/2608.22856
arxiv_url: https://arxiv.org/abs/2608.22856
date: 2026-08-25
upvotes: 2
authors: ["Jingjie Ning", "Xueqi Li"]
---

# Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Churn in Retrieval-Augmented QA

**Upvotes:** 2
**Authors:** Jingjie Ning, Xueqi Li

A retrieval-augmented QA system can return different answers after an index expansion even when its requested model identifier, prompt, retrieval policy, evidence depth, rendering, and exposed generation controls are held fixed. Aggregate accuracy may hide these changes when gains and losses cancel, while ordinary generation variability makes one-shot comparisons overstate update effects. We call the hidden phenomenon accuracy-blind answer churn and introduce the Snapshot Compatibility Audit, which estimates excess answer churn by subtracting same-snapshot repeat disagreement from cross-snapshot disagreement. We instantiate it by expanding one frozen FineWeb prefix from one to seven shards. In a preregistered 400-question Natural Questions study, normalized-exact and blinded-semantic excess churn are 6.44 and 10.25 percentage points while exact-match accuracy changes by only -1.50 points. A post-hoc analysis finds repeat-stable semantic flips on 40/400 questions. A separately preregistered 200-question TriviaQA study yields smaller, directionally consistent excess churn while exact-match accuracy moves in the opposite direction. An outcome-blind post-hoc 100-question subset replication with a second DeepSeek generator and serving configuration finds 8.75 pp of semantic excess churn even as exact match rises by 3.00 percentage points. Answer-level compatibility can therefore fail without a conspicuous or consistently directed utility shift. Retrieval-augmented releases should audit compatibility alongside utility.
