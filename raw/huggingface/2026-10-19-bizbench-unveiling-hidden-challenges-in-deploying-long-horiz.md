---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.20424
url: https://huggingface.co/papers/2610.20424
arxiv_url: https://arxiv.org/abs/2610.20424
date: 2026-10-19
---

# BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business

Existing long-horizon agent benchmarks often emphasize final task success while providing limited assessment of intermediate execution validity. Yet real-world business operations require agents to navigate extensive, potentially outdated or conflicting policies while satisfying critical constraints throughout execution. These requirements are particularly consequential in high-stakes domains such as payments, where intermediate violations can incur financial losses or regulatory consequences regardless of the final outcome. To bridge this evaluation gap, we introduce BizBench, a multi-turn benchmark grounded in real-world procedures from a leading payments company. Its executable environment integrates 789 knowledge documents and 601 discoverable business tools, with consistent policies, states, and tool behavior. The benchmark comprises 50 tasks involving resource constraints, temporal dependencies, prior commitments, and conflicting or outdated guidance. Each task is validated through reference execution, while deterministic checks assess both goal attainment and execution validity without prescribing a single solution path. Experiments reveal substantial limitations even among frontier models: Claude Opus 5 and GPT-6 Sol achieve strict success rates of only 64.0% and 61.3%, respectively. For Qwen3.8-27B, goal attainment reaches 42.0%, but strict success drops to 32.7%, demonstrating how outcome-based evaluation can mask invalid execution. Beyond success rates, DeepSeek-V4.1-Flash averages 191.3 tool calls per run, approximately 70% more than reference executions, revealing substantial execution overhead. Overall, BizBench establishes a testbed for evaluating and advancing long-horizon agents beyond task completion, toward reliable and constraint-compliant execution in complex business environments.
