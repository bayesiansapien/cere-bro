---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21025
url: https://huggingface.co/papers/2610.21025
arxiv_url: https://arxiv.org/abs/2610.21025
date: 2026-10-16
---

# Learning to Read Out: Unembedding Dynamics in Language Model Pretraining

When does a language model acquire a capability? Developmental studies usually answer this by tracking when models start producing the correct token. But that prediction passes through the unembedding matrix, or readout, which is itself still being learned during pretraining. We show that a model's hidden states can encode task information before its own readout expresses it, so timelines read from outputs conflate what the model encodes with what its readout expresses. To track the readout directly, we introduce parameter-trajectory crosscoding, which fits one sparse dictionary to every token's readout row at every checkpoint. Unlike crosscoders on activations, it needs only checkpoint weights. We use it to locate a narrow early window, 0.4-1.1% of the way through Pythia's pretraining, in which the readout reorganizes and WordNet word categories become decodable from its rows. By then, linear probes on the hidden states already decode task information that the model's own outputs do not yet show. To test whether such gaps depend on how fast the readout learns, we pretrain small models from scratch that differ only in the readout's learning rate. We find that raising it makes the readout develop earlier and the gap close sooner, with little effect on final loss. Together, these results imply that early in training, where many developmental transitions are dated, a behavioral date can reflect when the readout learns to express task information and not when the model learns it.
