---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.252501+00:00
arxiv_id: 2611.27490
url: https://huggingface.co/papers/2611.27490
arxiv_url: https://arxiv.org/abs/2611.27490
date: 2026-11-23
---

# Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval

Most established instance-retrieval benchmarks emphasise landmarks; small sculptures from visually similar series offer a complementary challenge. We introduce Doppeldwarf-306: 1,691 openly licensed photographs of 306 bronze dwarf statues in Wrocław, Poland, many made in themed series that share one style, with the photographer of each image recorded. With no training, nearest-neighbour search over frozen DINOv2 features names the right statue first for 93.1% of leave-one-out queries, and the best of thirteen backbones from seven pretraining paradigms reaches 94.7%. Accuracy falls slowly as candidates are added: for DINOv2, by about 0.8 points each time their number doubles. A natural design for a phone guide compares a photograph only with statues near the user. In simulation this helps, but less than an equal number of randomly chosen statues does, so random subsampling overstates its value; a permutation test ties the penalty to the real layout (p = 0.005). Used as a weight instead of a filter, location raises DINOv2 from 93.4% to 98.7% for a simulated user 25 m from the statue. With the query's photographer withheld, learned local-feature matching raises DINOv2 accuracy from 81.8% to 85.5% and also improves DINOv3. Comparing the two best candidates cuts DINOv2's false acceptance of unknown statues from 38.3% to 19.6% at 90% known acceptance.
