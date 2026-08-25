---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.23035
url: https://huggingface.co/papers/2608.23035
arxiv_url: https://arxiv.org/abs/2608.23035
date: 2026-08-25
upvotes: 31
authors: ["Yi Zhu", "Xiongwei Wu", "Qiyi Wang", "Tingyu Qu", "Jiajun Liu", "Sihan Cao", "Long Chen", "Weigao Sun", "Feida Zhu", "Yiran Zhong", "Steven Hoi"]
---

# MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

**Upvotes:** 31
**Authors:** Yi Zhu, Xiongwei Wu, Qiyi Wang, Tingyu Qu, Jiajun Liu, Sihan Cao, Long Chen, Weigao Sun, Feida Zhu, Yiran Zhong, Steven Hoi

As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints. To close this gap, we present MobilePA-Bench, an interactive, stateful, and tool-centric benchmark for evaluating the tool-calling and planning abilities of mobile planning agents. MobilePA-Bench runs on an executable sandbox that maintains live application databases and returns structured feedback, spanning 13 functional domains and 212 realistic mobile tools. Beyond basic tool use, it evaluates a central planning agent along three advanced dimensions: (1)~Sub-agent Collaboration---decomposing a complex task and delegating specialized work to capable sub-agents; (2)~Memory Usage---recalling stored memories, user profiles, and past preferences to resolve implicit requests; and (3)~Skill Usage---invoking pre-packaged composite skills instead of planning every step from scratch. Extensive experiments show that current frontier LLMs remain unreliable in mobile settings: performance drops sharply under strict tool ordering, permission limits, and unexpected runtime errors. By pairing an interactive function-calling sandbox with evidence-based verification, MobilePA-Bench serves as both a practical diagnostic benchmark and an interactive foundation for agentic reinforcement learning---accelerating the development of dependable mobile agents.
