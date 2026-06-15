---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.11599
url: https://huggingface.co/papers/2606.11599
arxiv_url: https://arxiv.org/abs/2606.11599
date: 2026-06-15
---

# When is Your LLM Steerable?

Activation steering offers a lightweight approach to control language models' behavior at inference time, but whether it succeeds or fails heavily depends on the prompt, concept, model, and steering configuration. Finding the regime and boundaries of successful steering typically requires expensive grid searches and post-hoc evaluation of full autoregressive rollouts. In this work, we investigate whether steerability can be predicted from the model's internal states at the beginning of the generation process, e.g., after generating the first few tokens, and how to leverage such a predictor to improve steering success rate. To this end, we first introduce ASTEER, a testbed including 1.4M steered generations, spanning 150 concepts with each steering success/failure labeled. Leveraging this testbed, we analyze the model's early decoding dynamics by extracting features that compare hidden states before and after steering across layers and initial decoding steps. These features help us understand how steering's effects propagate along layers and token positions, which provide key information for steerability prediction. We then train a Gradient Boosting Decision Trees (GBDT) classifier on these features to predict whether an intervention will under-steer, succeed, or over-steer without requiring full rollout. Our predictor achieves around 0.7 macro-F1 score on unseen concepts, demonstrating that early hidden states encode substantial, structured information about eventual steering efficacy. We further leverage this steerability predictor as guidance for steering strength searching, achieving near-optimal performance with a small fraction of decoding cost.
