---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933652+00:00
arxiv_id: 2609.34771
url: https://huggingface.co/papers/2609.34771
arxiv_url: https://arxiv.org/abs/2609.34771
date: 2026-09-29
---

# When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety

Reliable AI safeguards require both control mechanisms that reduce unsafe behavior and monitoring mechanisms that detect safety risks during model interactions. Established behavioral safeguards include alignment methods that optimize model outputs and text monitors that assess interaction text. Representation engineering instead reads or modifies internal model states, but the relative strengths of these approaches remain unclear because they are often evaluated under different settings. We present a matched evaluation across two tracks. For safety control, we compare DPO, a behavioral alignment method, with three representation steering methods across robustness, practicality, and granularity. DPO provides the strongest overall control and generally improves with increasing training data, although its safety can degrade after subsequent benign fine-tuning. Representation steering remains competitive primarily in low-data settings, particularly with high-quality contrastive data. For safety monitoring, we compare representation probes with fine-tuned and open-weight text monitors across full-response detection, early detection, and computational cost. Specialized text monitors achieve the strongest overall detection accuracy, while representation probes remain competitive at substantially lower marginal cost. Finally, monitor-guided interventions recover much of the safety lost by DPO after benign fine-tuning, with little additional over-refusal. Overall, representation engineering does not generally replace behavioral safeguards, but offers practical advantages under specific conditions and can provide complementary safety benefits.
