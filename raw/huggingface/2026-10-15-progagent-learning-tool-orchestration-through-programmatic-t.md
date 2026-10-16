---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.226879+05:30
arxiv_id: 2610.14774
url: https://huggingface.co/papers/2610.14774
arxiv_url: https://arxiv.org/abs/2610.14774
date: 2026-10-15
---

# ProgAgent: Learning Tool Orchestration through Programmatic Training

Large language models (LLMs) are increasingly expected to orchestrate diverse tools over long-horizon tasks. Existing agents typically use Direct Tool Calling (DTC), where the model invokes tools sequentially, and tool responses accumulate in the model context, which can lead to context rot and orchestration breakdown. In contrast, Programmatic Tool Calling (PTC) invokes tools through executable code and stores intermediate results in runtime variables rather than appending them to the context. Prior work has explored PTC mainly as an inference-time optimization, but its benefits for agentic training remain unclear, and suitable verifiable training tasks are scarce. In this work, we introduce ProgAgent, a full PTC training stack, comprising a pipeline for synthesizing verifiable long-horizon tasks, a lightweight PTC runtime, and a two-stage training recipe. Using only 215 tasks instantiated at four environment scales, ProgAgent yields higher pass rates than the evaluated baselines of comparable size across four benchmarks. On LOCA-bench, ProgAgent-14B achieves a 30.7% pass rate at a 64k-token environment state, where these baselines score zero. Cross-harness experiments show that PTC-trained models outperform DTC-trained models under both evaluation interfaces, suggesting that the benefits of PTC training extend beyond the interface.
