---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.10366
url: https://huggingface.co/papers/2608.10366
arxiv_url: https://arxiv.org/abs/2608.10366
date: 2026-08-12
---

# DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?

Real-world data science involves long-horizon workflows that span data wrangling, exploration, modeling, visualization, and validation, and require coordinated use of tools such as notebooks, IDEs, terminals, browsers, and databases within real operating environments. Yet existing benchmarks lack real-computer interaction and do not evaluate whether agents can execute complete end-to-end data-science workflows in realistic computing environments, failing to capture the multi-stage, multi-tool nature of data-science practice. We introduce DSAgentBench, the first benchmark to evaluate whether agents can automate full data-science workflows inside real computer environments. DSAgentBench contains 275 diverse tasks covering the entire data-science life-cycle, reflecting the complexity and tool coordination required in practice. Each task requires grounding decisions in intermediate outputs and coordinated tool use, and includes a deterministic evaluator that verifies analytical correctness, visual outputs, and model performance rather than code-only execution. Our extensive experiments with 15 closed- and open-source models show that even the strongest agent, Claude-4.6-Sonnet, achieves only 56.70% task success, while all open-source agents remain below 1%, frequently failing at tool orchestration, OS grounding, and multi-step reasoning. These results reveal a substantial capability gap between current agentic systems and real data-science workflows, positioning DSAgentBench as a foundation for developing grounded, verifiable, autonomous data-science agents. We release DSAgentBench at https://github.com/vis-nlp/DSAgentBench.
