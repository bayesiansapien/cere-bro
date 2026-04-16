---
source: farmer/huggingface
farmed: 2026-04-16T00:00:00Z
arxiv_id: 2604.13822
url: https://huggingface.co/papers/2604.13822
arxiv_url: https://arxiv.org/abs/2604.13822
date: 2026-04-16
authors: Zhengxi Lu, Fei Tang, Guangyi Liu
---

# UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization

**Authors:** Zhengxi Lu, Fei Tang, Guangyi Liu
**arXiv:** [2604.13822](https://arxiv.org/abs/2604.13822)
**HuggingFace:** [hf.co/papers/2604.13822](https://huggingface.co/papers/2604.13822)

## Abstract

MLLM-based GUI agents have demonstrated strong capabilities in complex user interface interaction tasks. However, long-horizon scenarios remain challenging, as these agents are burdened with tasks beyond their intrinsic capabilities, suffering from memory degradation, progress confusion, and math hallucination. To address these challenges, we present UI-Copilot, a collaborative framework where the GUI agent focuses on task execution while a lightweight copilot provides on-demand assistance for memory retrieval and numerical computation. We introduce memory decoupling to separate persistent observations from transient execution context, and train the policy agent to selectively invoke the copilot as Retriever or Calculator based on task demands. To enable effective tool invocation learning, we propose Tool-Integrated Policy Optimization (TIPO), which separately optimizes tool selection through single-turn prediction and task execution through on-policy multi-turn rollouts. Experimental results show that UI-Copilot-7B achieves state-of-the-art performance on challenging MemGUI-Bench, outperforming strong 7B-scale GUI agents such as GUI-Owl-7B and UI-TARS-1.5-7B. Moreover, UI-Copilot-7B delivers a 17.1% absolute improvement on AndroidWorld over the base Qwen model, highlighting UI-Copilot's strong generalization to real-world GUI tasks.
