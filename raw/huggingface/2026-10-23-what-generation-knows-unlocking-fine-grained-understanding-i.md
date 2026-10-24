---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.879450+00:00
arxiv_id: 2610.23987
url: https://huggingface.co/papers/2610.23987
arxiv_url: https://arxiv.org/abs/2610.23987
date: 2026-10-23
---

# What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models

Fine-grained visual understanding requires distinguishing subtle differences in local attributes and spatial relations, yet remains challenging for existing vision-language models. Unified multimodal models (UMMs) offer a new opportunity through generation pathways that preserve rich visual information complementary to understanding. However, existing generation-assisted understanding methods mainly rely on generative supervision or explicit generation and have not systematically explored direct use of native generation-side representations. To address this gap, we systematically analyze what generation-side representations offer for fine-grained understanding, finding that they are more sensitive to fine-grained semantic changes, capture task-relevant changes missed by understanding-side representations, and depend on correct spatial organization for this advantage. Guided by these findings, we design GAFU, a post-training framework that unlocks native generation-side information for fine-grained understanding. It compresses generation-side visual representations into compact \(G\) tokens that preserve fine-grained visual details, enabling task-conditioned retrieval by the understanding pathway. Experiments show that GAFU consistently outperforms SFT baselines trained on the same data across diverse visual understanding tasks and UMM architectures, with maximum relative improvements of 20.00\%, 17.94\%, and 8.62\% on VStar-Bench, OmniSpatial, and VSR-Bench, respectively. Overall, GAFU converts complementary information from the generation pathway into gains in fine-grained visual understanding, providing an effective path toward synergy between generation and understanding in UMMs.
