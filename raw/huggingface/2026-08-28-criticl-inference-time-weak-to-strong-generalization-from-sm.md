---
source: farmer/huggingface
farmed: 2026-08-29T05:40:38.746243Z
arxiv_id: 2608.27455
url: https://huggingface.co/papers/2608.27455
arxiv_url: https://arxiv.org/abs/2608.27455
date: 2026-08-28
---

# CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes

Recent advances in inference-time scaling have significantly improved the reasoning performance of large language models (LLMs). However, these methods typically rely on repeated generation or external verification. To address this limitation, we introduce CritICL, a novel inference-time framework that improves reasoning while maintaining high efficiency. Our key insight is that LLM failure modes exhibit structured patterns across model scales within the same family. Instead of treating failures as undesirable outputs, CritICL leverages them as a source of guidance. Specifically, we utilize failure modes derived from weaker models and incorporate them into inference through critique-based in-context examples. We propose two variants: CritICL-dynamic, which adaptively predicts input-specific failure modes and retrieves critiques, and CritICL-static, which uses a global failure mode profile to provide stable guidance. Experimental results show that CritICL consistently outperforms standard in-context learning and achieves performance competitive with or superior to test-time scaling methods, while requiring significantly fewer generations and lower token cost. Code available at: https://github.com/umwyf/CRITICL
