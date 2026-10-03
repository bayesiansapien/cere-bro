---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819937+00:00
arxiv_id: 2606.10953
url: https://huggingface.co/papers/2606.10953
arxiv_url: https://arxiv.org/abs/2606.10953
date: 2026-10-02
---

# Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans

Furnished floor plans support real-estate visualization, interior design, and architectural workflows, yet automatic furnishing remains challenged by limited real-world data and the need to satisfy interacting geometric and functional constraints. We ask whether professional furnishing knowledge can be learned from real floor plans using a pretrained model, enabling direct constraint-aware layout generation without relying on costly iterative agentic inference. We introduce AntPlan, a curated dataset of 505 real professional architectural floor plans with dense furniture annotations spanning 92 object classes and ten residential room categories, and Architect-Ant, a framework for generating furniture layouts. Architect-Ant represents layouts with an editable coordinate-based DSL and first learns professional furnishing patterns through supervised fine-tuning. It is then optimized with GRPO using a Layout Rule Score (LRS) that aggregates geometric and functional constraints derived from professional plans, providing outcome-level supervision without prescribed reasoning traces. Experiments against diverse state-of-the-art baselines show that Architect-Ant combines low geometric violation rates with high functional completeness, while qualitative results more closely reflect real-world residential furnishing patterns. The resulting layouts remain object-level editable and can be converted into 3D scenes.
