---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.599952+00:00
arxiv_id: 2609.30837
url: https://huggingface.co/papers/2609.30837
arxiv_url: https://arxiv.org/abs/2609.30837
date: 2026-09-28
---

# MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation

Multi-teacher on-policy distillation (MOPD) integrates specialized capabilities into a single student, but existing practice typically hard-routes each prompt to a domain-matched teacher for the entire rollout. This dependence on prompt-level domain labels restricts using unlabeled training mixtures and leaves complementary signals from other teachers unused. We introduce MOPD-Router, a framework that routes supervision over the full teacher pool at each token, without domain labels or training a separate routing model. Its plug-in interface supports different metrics for selecting and weighting teacher-specific OPD signals. Within this interface, we propose ExpertAlign, which scores each teacher by whether its correction to the student at the current token expresses the specialization that teacher acquired during post-training, and compare it against two reference metrics built on teacher confidence (Entropy) and teacher-student discrepancy (Novelty). Experiments on unlabeled and domain-labeled training mixtures under strong-to-weak and same-size distillation scenarios show that ExpertAlign achieves the strongest overall performance in all four settings. On unlabeled data, it improves the overall score by 5.88 (+12.3%) points over Mean aggregation; on domain-labeled data, it outperforms standard MOPD by 3.95 (+7.8%) points without using available domain labels. These results demonstrate token-level routing can exploit cross-domain complementary supervision, and reduce exclusive reliance on prompt-level domain assignment. Code is available at: https://github.com/TURLEing/MOPD-Router.
