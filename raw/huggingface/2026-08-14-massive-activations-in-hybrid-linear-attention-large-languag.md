---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.12149
url: https://huggingface.co/papers/2608.12149
arxiv_url: https://arxiv.org/abs/2608.12149
date: 2026-08-14
---

# Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus

We present the first systematic study of Massive activations (MAs) in layer-interleaved HLA LLMs and uncover two architecture-aligned morphologies: MAs consistently spike immediately before full attention layers, forming pre-attention spikes (PAS), and can persist through intervening linear attention layers, giving rise to inter-spike plateaus (ISP). As full attention becomes denser, successive PAS become increasingly connected through ISP, ultimately recovering the stable MA morphology of full attention LLMs. We establish the recurrence of this organization across five linear attention architectures, six hybridization configurations, five data domains, and representative open-source hybrid models spanning 1.2B to 397B total parameters. Controlled pretraining of GDN-based hybrids at scales up to 1.3B shows that both morphologies emerge early and respond asymmetrically to output gating: full attention output gating strongly attenuates their absolute magnitudes without eliminating their layerwise organization, whereas removing GDN gates yields comparatively modest amplification. Mechanistically, our systematic-outlier analysis supports a shared lifecycle account governed by the timing of MA cancellation. PAS follows a localized write-sink-cancel process, while the extended persistence of ISP is consistent with delayed cancellation. At the full attention limit, this account recovers the stable MA morphology characteristic of full attention LLMs. Our code is available at https://github.com/StartluxLabs/Massive-Activations-HLA.
