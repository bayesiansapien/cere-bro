---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.03645
url: https://huggingface.co/papers/2606.03645
arxiv_url: https://arxiv.org/abs/2606.03645
date: 2026-06-07
---

# The Shape of Addition: Geometric Structures of Arithmetic in Large Language Models

Large Language Models exhibit paradoxical fragility in fundamental arithmetic, implying a disconnect between internal computation and discrete output. By analyzing the residual stream geometry during multi-operand addition, we identify the Iso-Raw-Sum Trajectory (IRST), a geometric structure where representations are anchored by semantic digits and modulated by continuous carry fibers. We propose the Noisy Quantization Model to explain this geometry, framing arithmetic errors as Geometric Slippages caused by internal neural noise pushing a continuous, latent Carry Potential across quantization thresholds. This geometric framework further elucidates Probe Versatility, explaining how lightweight probes can disentangle coexisting latent signals (such as ground truth versus hallucination) from a single activation vector. Finally, we validate these insights through a geometric consistency check method that effectively detects and corrects these quantization failures during inference. Our code is available at https://github.com/RL-MIND/Shape-of-Addition.
