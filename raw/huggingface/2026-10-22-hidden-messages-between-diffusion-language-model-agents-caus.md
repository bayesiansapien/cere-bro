---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.195218+00:00
arxiv_id: 2610.28905
url: https://huggingface.co/papers/2610.28905
arxiv_url: https://arxiv.org/abs/2610.28905
date: 2026-10-22
---

# Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication

Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden message into another and, crucially, whether the receiver uses what that message means. In Hidden Messages, a sender compresses its denoising state into four signed dense vectors; the receiver consumes them while retaining its own context, canvas, and trajectory. Removing a message tests whether the channel matters; replacing it with a message from another example tests whether its content matters. Across controlled tasks, derangement removes a +63.6-point advantage on Tiny-A2D and a +100.0-point advantage on Dream-7B, while targeted substitutions steer the receiver toward the substituted fact. On QASC with the two supporting facts split across agents, matched communication reaches 80.8%, but a wrong-example message lowers accuracy to 46.8%, a content effect of +34.0 points. The surprising result is temporal: one late transfer reaches 87.8%, exceeding four recurrent exchanges by +7.0 points. These experiments provide causal evidence for continuous hidden communication between diffusion-LM agents and show that when information is transferred can matter more than how many times agents exchange it.
