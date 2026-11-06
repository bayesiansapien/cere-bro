---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.307736+00:00
arxiv_id: 2611.06042
url: https://huggingface.co/papers/2611.06042
arxiv_url: https://arxiv.org/abs/2611.06042
date: 2026-11-05
---

# UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling

Universal image restoration aims to handle diverse degradations within a single model, but a reliable scaling strategy remains underexplored. Increasing backbone depth and width can lead to performance saturation, while degradation-aware specialization depends on accurate degradation estimation and is vulnerable to errors on out-of-distribution and real-world inputs. We propose UniRestorer++, a scalable framework based on multi-granularity degradation modeling. It progressively refines degradation groups and introduces group-specific experts, coupling capacity growth with specialization. Degradation-estimation-based routing selects a root-to-leaf path, while granularity-estimation-based routing chooses a level along that path to balance specialization and robustness. Spatially dense degradation representation maps further enable region-aware routing for spatially non-uniform corruptions. We develop CDD-50, a benchmark covering 50 degradation categories from single to penta-degradation. Experiments show approximately log-linear PSNR trends over the evaluated model-size range and stronger scaling gains on out-of-distribution and real-world data than vanilla MoE scaling. UniRestorer++ achieves state-of-the-art performance across benchmarks and demonstrates zero-shot generalization and few-shot transfer on real-world images. Code: https://github.com/mrluin/UniRestorer_plusplus
