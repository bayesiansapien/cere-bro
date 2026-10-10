---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.413991+00:00
arxiv_id: 2610.06406
url: https://huggingface.co/papers/2610.06406
arxiv_url: https://arxiv.org/abs/2610.06406
date: 2026-10-09
---

# What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents

As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a software-engineering benchmark comprising three subsets that cover two complementary dimensions: alignment between requirements and behavior, and awareness of consequential autonomous decisions for verification. To support these judgments, we propose the Evidence-Grounded Behavior Graph (EBG), a training-free method that groups source-linked evidence into behaviors and organizes their relationships into a graph. EBG presents task-oriented views of this graph to help monitors interpret behavior in context. Experiments across eight models show that EBG improves decision identification and evidence localization in most settings compared with direct access to the original context. Further experiments show that EBG's evidence-localization gains persist across input scales and hyperparameter settings, while real-world applications illustrate its practical value for human oversight.
