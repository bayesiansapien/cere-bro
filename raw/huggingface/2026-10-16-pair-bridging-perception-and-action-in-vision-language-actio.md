---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.09016
url: https://huggingface.co/papers/2610.09016
arxiv_url: https://arxiv.org/abs/2610.09016
date: 2026-10-16
---

# PAIR: Bridging Perception and Action in Vision-Language-Action Models

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Latent Tokens. A Bridge Module extracts task-relevant features from the current visual-language representations. PAIR aligns these features with the Action Latent Tokens to form Bridge Tokens that preserve task information and capture the structure of expert actions. The Bridge Tokens are then projected into the action-token space and injected into the initial Action Tokens, providing an action-ready starting point for Action Expert refinement. At inference, the autoencoder is removed, and the Bridge Tokens are generated only from the current observation and instruction. Experiments on LIBERO, LIBERO-Plus, and CALVIN ABC-D show gains for the evaluated OpenVLA-OFT and VLA-Adapter models. On LIBERO-Plus, PAIR raises VLA-Adapter's success rate from 59.1% to 64.2%. On CALVIN, it increases VLA-Adapter's average completed sequence length from 4.42 to 4.53. Across seven real-world tasks, PAIR raises OpenVLA-OFT's success rate from 51.4% to 65.0%. Representation analyses show that Bridge Tokens retain task information while making continuous-action information accessible before Action Expert refinement. These results support a shared intermediate representation as a useful interface between perception and action in continuous-action VLAs.
