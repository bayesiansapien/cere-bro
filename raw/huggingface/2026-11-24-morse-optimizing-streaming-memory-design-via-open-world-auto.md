---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.927977+00:00
arxiv_id: 2611.30011
url: https://huggingface.co/papers/2611.30011
arxiv_url: https://arxiv.org/abs/2611.30011
date: 2026-11-24
---

# MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research

A streaming video system must decide in a single pass what evidence to retain under bounded frame storage, before it knows which details a future question will require. Recent recursive self-improvement methods automate the design of the harness that stores and retrieves this evidence. They revise the harness in response to failures, but the editor must still devise each repair from its prior knowledge and a predefined set of tools. A failure that recurs across videos, however, may point to a problem that prior work has already addressed. We introduce MORSE (Memory Optimization with Recursive Self-Evolvement), an open-world auto-research framework that uses recurring failures to guide an online search for solutions. Its editor groups failures in training traces by cause, then searches papers, model cards, and code for methods it can adapt or pretrained perception models it can use. When the editor introduces a new perceptual capability, it can also revise how the harness stores and retrieves the resulting evidence for a frozen video-language model. On held-out validation streams, MORSE first selects revisions that improve answer quality, then seeks faster revisions that preserve those gains within a specified tolerance. Across three streaming video benchmarks, MORSE consistently achieves the highest answer accuracy within each frozen-backbone comparison. On OVO-Bench, our Qwen3-VL-8B harness answers queries in 0.30 seconds on average while achieving 75.1% accuracy, 3.1 percentage points ahead of the next-best evaluated harness using the same frozen backbone.
