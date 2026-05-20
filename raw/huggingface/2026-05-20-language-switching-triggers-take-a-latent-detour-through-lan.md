---
source: farmer/huggingface
farmed: 2026-05-20T09:54:49.933309+00:00
arxiv_id: 2605.18646
url: https://huggingface.co/papers/2605.18646
arxiv_url: https://arxiv.org/abs/2605.18646
date: 2026-05-20
---

# Language-Switching Triggers Take a Latent Detour Through Language Models

Backdoor attacks on language models pose a growing security concern, yet the internal mechanisms by which a trigger sequence hijacks model computations remain poorly understood. We identify a circuit underlying a language-switching backdoor in an 8B-parameter autoregressive language model, where a three-word Latin trigger (nine tokens) redirects English output to French. We decompose the circuit into three phases: (1) distributed attention heads at early layers compose the trigger tokens into the last sequence position; (2) the resulting signal propagates through mid-layers in a subspace orthogonal to the model&#39;s natural language-identity direction; (3) the MLP at the final layer converts this latent signal into French logits. The entire circuit flows through a serial bottleneck at a single position: corrupting that position at any layer entirely mitigate the trigger but also hinder the model&#39;s capabilities. The orthogonal latent encoding suggests that defenses that search for language-like signals in intermediate representations would miss this trigger entirely.
