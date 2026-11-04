---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.02112
url: https://huggingface.co/papers/2611.02112
arxiv_url: https://arxiv.org/abs/2611.02112
date: 2026-11-03
---

# Order-Only On-Policy Distillation

On-policy distillation (OPD) trains a student on its own generations by matching the teacher's token probabilities. These probabilities entangle two kinds of information: which tokens the teacher prefers, and how confident it is. The latter reflects the teacher's own capacity and calibration, which a smaller student may be unable to reproduce. Because the teacher temperature changes these values without changing the ordering, OPD is also sensitive to the temperature choice. We ask whether the teacher's ordering of candidate tokens is enough, and propose Order-Only On-Policy Distillation (O^{3}PD). At each student-generated prefix, O^{3}PD trains the student to reproduce the order of the teacher's top-K tokens, without fitting their probability values. The objective is therefore invariant to the teacher temperature and needs no temperature tuning. Across six teacher--student pairs, O^{3}PD outperforms OPD on the average over HMMT25, AIME24, and AIME25 in every pair, by up to 2.9 points, with gains of up to 5.6 points on AIME25. Other ranking losses yield similar gains, so the benefit comes from ordinal supervision itself. Analysis shows that O^{3}PD departs further from the teacher's probabilities than OPD, yet reproduces its ranking more faithfully and yields a stronger student. The ranking, not the probability values, thus carries the knowledge that on-policy distillation needs to transfer.
