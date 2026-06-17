---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.17321
url: https://huggingface.co/papers/2606.17321
arxiv_url: https://arxiv.org/abs/2606.17321
date: 2026-06-17
---

# ProCUA-SFT Technical Report

Training computer-use agents (CUAs) -- models that interact with graphical desktops through screenshots and keyboard/mouse actions -- requires large-scale, diverse trajectory data collected in full desktop environments. The largest public resource, AgentNet (22.5K human trajectories), leads to negative transfer when used for supervised fine-tuning (SFT): continuing training UI-TARS 7B on AgentNet causes OSWorld success rate to fall from 26.3% to 8-10%. We present ProCUA-SFT, a dataset of 3.1M step-level SFT samples distilled from 93K synthetic trajectories across 2,484 application combinations. The dataset is produced by a fully automated pipeline that (i) synthesizes grounded tasks on live desktops seeded with real-world content -- 912 spreadsheets from SpreadsheetBench, approximately 10K permissively-licensed presentations from Zenodo10K, and multi-application OSWorld configs -- and (ii) verifies each task's feasibility through binary precondition checking before rollout. A single VLM (Kimi-K2.5) serves as goal generator, precondition judge, and trajectory executor, eliminating planner-actor capability gaps. Each trajectory is expanded into step-prefix samples that exactly reproduce the context layout seen at inference time. Fine-tuning UI-TARS 7B on ProCUA-SFT for one epoch yields 45.0% on OSWorld -- an 18.7 percentage-point improvement over the base model and over 35% above AgentNet-trained counterparts. A subset of ProCUA was incorporated into the training data for the Nemotron 3 Nano Omni model, contributing to its computer-use capabilities.
