---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.15715
url: https://huggingface.co/papers/2604.15715
arxiv_url: https://arxiv.org/abs/2604.15715
date: 2026-04-20
---

# GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows

The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at https://github.com/open-compass/GTA.
