---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.11052
url: https://huggingface.co/papers/2606.11052
arxiv_url: https://arxiv.org/abs/2606.11052
date: 2026-06-10
---

# Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It

Chain-of-thought (CoT) supervised fine-tuning (SFT) is widely adopted to improve reasoning ability, yet we find that it systematically degrades long-context recall in hybrid linear-attention models. Across architectures including HypeNet and Jet-Nemotron, retrieval performance on Needle-In-A-Haystack (NIAH) deteriorates substantially after CoT-SFT, and the degradation becomes more severe under harder retrieval settings and longer context windows. For example, HypeNet-9B on NIAH-S2@256K decreases from 67.2% to 9.4%. We attribute this to CoT-SFT biasing attention gradients toward short-range patterns, disrupting query-key projections (W_Q, W_K) that are responsible for long-range routing. Motivated by this observation, we propose QK-Restore, a training-free method that restores only W_Q and W_K from the pre-SFT checkpoint while preserving all other post-SFT parameters. We further introduce a Procrustes variant to balance routing preservation and reasoning adaptation. Across architectures, QK-Restore consistently restores long-context capability at zero training cost while preserving reasoning performance; for instance, on HypeNet-5B it improves S3@256K from 65.4% to 76.4% while maintaining strong reasoning performance.
