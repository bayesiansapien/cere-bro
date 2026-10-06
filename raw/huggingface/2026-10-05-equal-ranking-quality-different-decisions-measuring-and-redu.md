---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2608.26762
url: https://huggingface.co/papers/2608.26762
arxiv_url: https://arxiv.org/abs/2608.26762
date: 2026-10-05
---

# Equal Ranking Quality, Different Decisions: Measuring and Reducing Order Dependence in LLM Scorers

In passage reranking, response ranking and multi-document question answering, LLMs can score several candidate documents or responses together in one prompt, each still receiving its own score. Such scorers are selected on ranking quality, but their scores determine a decision: what a score threshold retains, a reader answers, or which chosen/rejected pair enters preference training. Because the candidates share that prompt, reordering them changes their scores. The same query over the same candidates should still yield the same decision. However, equal ranking quality does not imply equal decisions: on passage reranking, five trained scorers within 0.010 nDCG@10 retain sets that overlap by only 0.66-0.84 when reordered. No prompt-time change we test resolves that dependence: the only one that improves ranking quality does not measurably improve decision stability. We introduce order-consistency SFT (OC-SFT), which attenuates it in the weights by penalizing disagreement between a candidate's scores across orderings. It holds ranking quality and leads every decision-stability measure among trained scorers on all three tasks. It is also more stable on 12 base models than order-averaged distillation, which trains on labels averaged across permutations. One OC-SFT permutation retains sets that overlap more than ten averaged off-the-shelf permutations. A comparison of such scorers should therefore report what a threshold retains and a reader answers, not ranking quality alone. Code is available at https://github.com/thomsonreuters/presentation-dependence.
