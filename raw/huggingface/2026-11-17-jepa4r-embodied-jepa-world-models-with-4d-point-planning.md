---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.113564+00:00
arxiv_id: 2611.19771
url: https://huggingface.co/papers/2611.19771
arxiv_url: https://arxiv.org/abs/2611.19771
date: 2026-11-17
---

# JEPA4R: Embodied JEPA World Models with 4D Point Planning

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that observes single-depth-camera point clouds, predicts and plans in their latent space, and acts through a policy head on its frozen latents; we call this 4D point planning. A decoder on the frozen world model shows what it imagines as 4D point clouds, with a mean point error within 1.1 cm over 200 steps. Under the policy-learning protocols of OGBench and CortexBench, JEPA4R leads pixel JEPA models on OGBench Cube-Single, Cube-Double, Cube-Triple and Scene, and ranks first on MetaWorld and Adroit Relocate with 98.4% and 88.0%, above the runner-up, R3M, at 96.0% and 65.3%. Trained only in a digital twin, JEPA4R and its policy heads run zero-shot on the real arm with both a gripper and a dexterous hand.
