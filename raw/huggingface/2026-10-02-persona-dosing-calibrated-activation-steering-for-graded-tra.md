---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820295+00:00
arxiv_id: 2609.36388
url: https://huggingface.co/papers/2609.36388
arxiv_url: https://arxiv.org/abs/2609.36388
date: 2026-10-02
---

# Persona Dosing: Calibrated Activation Steering for Graded Trait Control

An activation-steering coefficient sets intervention strength, but requesting a particular degree of persona expression requires a behavioral scale. We study persona dosing: controlling a language model through a trait description and a requested mean intensity. PersonaDose specializes a shared, description-conditioned FLAS controller on persona responses, then calibrates its flow time against measured trait expression. Training responses are not paired with requested target intensities. Across Llama-3.1-8B, Qwen3-8B, and Gemma-3-4B, PersonaDose raises core-trait expression at the Persona Vectors coherence floor of 75 by 33.2, 18.3, and 17.8 points over contrastive activation addition. Calibration-selected settings retain an expression advantage on held-out questions, although the coherence floor does not hold for every trait there. Across seven trained traits, calibrated requests yield mean targeting errors of 4.7-6.2 points over 14-22 calibration-reachable targets out of 28 per model. These results separate the behavioral range learned by a controller from the accuracy of requests within that range.
