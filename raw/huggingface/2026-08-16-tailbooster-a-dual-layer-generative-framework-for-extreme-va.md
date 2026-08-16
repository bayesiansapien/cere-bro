---
source: farmer/huggingface
farmed: 2026-08-16T13:39:51.900697+05:30
arxiv_id: 2608.11951
url: https://huggingface.co/papers/2608.11951
arxiv_url: https://arxiv.org/abs/2608.11951
date: 2026-08-16
---

# TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation with Operational Validity Enforcement

Extreme events in air transport, such as severe arrival delays and abnormal air times, cause cascading network disruptions with substantial operational, economic, and safety costs. Such events are rare in historical records, leaving insufficient training signal for machine learning models. Synthetic data augmentation offers a principled solution, but conventional generative models under-represent distributional tails and give no guarantee against operationally infeasible instances, such as a short air time paired with a long flight distance. No existing approach addresses both limitations for mixed-type tabular records. We propose TailBooster, a dual-layer generative framework combining generative modelling with two anomaly detection layers. A statistical layer extracts extremes via the interquartile range, supplying tail-concentrated training signal to dedicated generative models, here a Tabular Variational Autoencoder. A deep learning layer then applies autoencoder-based cleaning, discarding synthetic records that violate the operational envelope learned from historical data. The framework was evaluated on US flight records across five dimensions: diversity, statistical similarity, fidelity, operational validity, and utility, the latter two being the primary improvement targets. Data-driven cleaning markedly improved operational validity, while targeted augmentation enhanced utility for extreme-event prediction. Across six regression algorithms, training on the framework's records reduced Mean Absolute Error by 47-49% on extreme air time and 29-57% on extreme arrival delay prediction relative to conventional synthetic data, with comparable gains when real records were enriched with synthetic extremes. Being fully data-driven and model-agnostic, TailBooster extends to domains where extreme-event prediction is critical and domain-specific rules are unavailable.
