---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15040"
url: "https://huggingface.co/papers/2605.15040"
arxiv_url: "https://arxiv.org/abs/2605.15040"
date: 2026-05-17
---

# Orchard: An Open-Source Agentic Modeling Framework

Agentic modeling aims to transform large language models (LLMs) into autonomous agents that can solve complex tasks through planning, reasoning, tool use, and multi-turn interaction with external environments. Despite substantial investment, open research in this area remains constrained by infrastructure and training gaps. Many high-performing agentic systems rely on proprietary codebases, models, or services, whereas open-source frameworks focus primarily on agent orchestration and harness design rather than improving agentic capabilities of LLMs through scalable model training. We present Orchard, an open-source framework for scalable agentic modeling. At its core is Orchard Env, a thin, Kubernetes-native environment service that provides reusable primitives for sandbox lifecycle management. Orchard Env is designed to operate across task domains, agent harnesses, and pipeline stages. With Qwen3-30B-A3B-Thinking, Orchard-SWE achieves 64.3% on SWE-bench Verified after SFT and 67.5% after SFT+RL, setting a new state of the art among open-source models of comparable size. Orchard-GUI trains a 4B vision-language computer-use agent achieving 68.4% average across WebVoyager, Online-Mind2Web, and DeepShop.
