---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.29534
url: https://huggingface.co/papers/2605.29534
arxiv_url: https://arxiv.org/abs/2605.29534
date: 2026-05-29
---

# UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents

Recent advances in mobile GUI agents have shown strong potential for automating mobile tasks, but most effective systems still depend on large vision-language models for screenshot understanding and long-horizon planning. Small GUI agents that can be deployed directly on mobile devices are more attractive for practical use, offering lower inference cost and better protection of sensitive on-device information. However, due to limited model capacity, such lightweight agents remain unreliable when planning and executing GUI tasks end-to-end from screenshots alone. We propose Knowledge-Oriented Behavior Exploration (UI-KOBE), a framework that improves lightweight mobile GUI agents with reusable app-specific graph knowledge. UI-KOBE first autonomously explores a mobile application and constructs an app knowledge graph, where nodes represent distinct UI states and edges represent executable transitions. At runtime, a lightweight GUI agent uses the graph as external guidance: given a user task and the current screenshot, it identifies the current graph node and selects among self-loop actions, neighboring transitions, task completion, or fallback free actions associated with that node. By supporting runtime decisions with app-specific graph guidance, UI-KOBE reduces the burden of end-to-end GUI planning and helps lightweight models perform mobile GUI tasks more effectively, offering a practical step toward efficient, interpretable, and privacy-conscious on-device GUI agents.
