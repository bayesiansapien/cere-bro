---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.12357
url: https://huggingface.co/papers/2605.12357
arxiv_url: https://arxiv.org/abs/2605.12357
date: 2026-05-13
---

# δ-mem: Efficient Online Memory for Large Language Models

Large language models increasingly need to accumulate and reuse historical information in long-term assistants and agent systems. Simply expanding the context window is costly and often fails to ensure effective context utilization. We propose δ-mem, a lightweight memory mechanism that augments a frozen full-attention backbone with a compact online state of associative memory. δ-mem compresses past information into a fixed-size state matrix updated by delta-rule learning, and uses its readout to generate low-rank corrections to the backbone's attention computation during generation. With only an 8times8 online memory state, δ-mem improves the average score to 1.10times that of the frozen backbone and 1.15times that of the strongest non-δ-mem memory baseline. It achieves larger gains on memory-heavy benchmarks, reaching 1.31times on MemoryAgentBench and 1.20times on LoCoMo, while largely preserving general capabilities. These results show that effective memory can be realized through a compact online state directly coupled with attention computation, without full fine-tuning, backbone replacement, or explicit context extension.
