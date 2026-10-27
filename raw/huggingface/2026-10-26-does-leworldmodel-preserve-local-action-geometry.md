---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801905+00:00
arxiv_id: 2610.31716
url: https://huggingface.co/papers/2610.31716
arxiv_url: https://arxiv.org/abs/2610.31716
date: 2026-10-26
---

# Does LeWorldModel Preserve Local Action Geometry?

We examine how closely pretrained LeWorldModel (LeWM) reproduces the effects of small action changes. Using matched simulator and model responses, we measure action sensitivity with Gram matrices at three perturbation scales. Across nearly a thousand states from Reacher and OGBench Cube, the most sensitive action directions differ by median angles of about 36^circ and 42^circ, respectively, at the smallest scale. Increasing the perturbation tenfold reduces median normalized Gram discrepancy by roughly 70\% on Reacher and 47\% on Cube. Geometry measured in pixels and embeddings varies more across scales than the chosen physical-state geometry. On held-out directions, environment Grams achieve median embedding response errors of 17\% and 28\%, compared with 26\% and 38\% for an isotropic reference with the same trace. LeWM's errors are higher at this scale. These findings support scale-specific evaluation of action sensitivity; its effect on control remains an open question.
