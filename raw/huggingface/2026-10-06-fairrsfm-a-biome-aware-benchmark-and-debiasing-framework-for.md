---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05790
url: https://huggingface.co/papers/2610.05790
arxiv_url: https://arxiv.org/abs/2610.05790
date: 2026-10-06
---

# FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models

Remote sensing foundation models (RSFMs) are commonly evaluated using aggregate metrics, which can hide systematic performance disparities across ecological regions. We introduce FairRSFM, a biome-aware benchmark for evaluating ecological group robustness in RSFMs. FairRSFM maps georeferenced samples from 14 terrestrial biome classes into six ecologically meaningful macro-groups and evaluates models under a unified frozen-backbone evaluation protocol. The benchmark covers four downstream datasets: m-EuroSAT, m-BigEarthNet, m-SA-Crop-Type, and MMEarth20K with Dynamic World label maps. Using Prithvi-EO-2.0, SatMAE, and DOFA across three random seeds, we show that aggregate performance consistently masks biome-dependent disparities across architectures and tasks. For example, Prithvi-EO-2.0 reaches 90.98% overall macro-F1 on m-EuroSAT but a mean worst-group score of only 83.72%, while m-SA-Crop-Type drops from 27.30% overall mIoU to 18.47% in the Xeric and Mineralogical group. We further evaluate Biome-Orthogonal Linear Probing (BOLP), Dynamic Biome Reweighting (DBR), and GroupDRO as complementary mitigation baselines. Their effectiveness is model- and task-dependent; for example, BOLP improves Prithvi-EO-2.0 worst-group F1@opt on m-BigEarthNet from 46.12% to 50.27% without updating the RSFM backbone. FairRSFM provides a reusable protocol for diagnosing and mitigating ecological robustness gaps in remote sensing foundation models. Code and datasets are available at: https://github.com/aminurhossain/FairRSFM.
