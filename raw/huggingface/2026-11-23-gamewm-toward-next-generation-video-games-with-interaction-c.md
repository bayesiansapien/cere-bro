---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.252037+00:00
arxiv_id: 2611.19247
url: https://huggingface.co/papers/2611.19247
arxiv_url: https://arxiv.org/abs/2611.19247
date: 2026-11-23
---

# GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models

For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay. Generative video models (VMs) now bear on all three. Neural networks already draw most of the pixels in shipped games, and recent world models let a lightweight game engine keep the world state while a VM turns the engine's coarse proxy video into final frames. These systems, however, treat the VM as a renderer that only restyles motion the engine has already authored, which leaves most of its generative capacity unused and limits the diversity a game can offer. We present GameWM, a design for next-generation games built on a clear division of labor. The GameWM-engine keeps what must be exact: rules, state, camera, and the layout of the world, which also spares the video model from having to remember it. The GameWM-VM generates what is expensive to author by hand: the look of the world and the detail of the player's interactions. One game mechanic can then be realized in many visually and physically distinct ways, while its outcome stays exactly as the engine computed it. To realize this division of labor, we build GameWM as a complete system: a data engine centered on interactions rather than exploration, an interface through which authored character sheets, scene art, and skill descriptions enter the model, and a model family from 5B to 33B parameters with a real-time causal variant for play. Together they give every player a fresh version of the same game: each player's own character, world, and skills turn the same engine mechanics into a new experience, while every event keeps the timing and outcome the GameWM-engine computed.
