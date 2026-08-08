---
source: farmer/huggingface
farmed: 2026-08-08T23:44:03.927649
arxiv_id: 2608.03451
url: https://huggingface.co/papers/2608.03451
arxiv_url: https://arxiv.org/abs/2608.03451
date: 2026-08-08
---

# DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces

Data agents enable natural-language analytics over organizational workspaces, where relevant evidence may be scattered across databases, structured files, long documents, and multimedia. Existing benchmarks largely isolate structured querying, retrieval, or open-ended analysis, leaving heterogeneous evidence discovery, complete tabular outputs, and deterministic evaluation insufficiently unified. We introduce DataSpace, a benchmark in which data agents produce verifiable tabular results from task-local heterogeneous workspaces. It contains 410 cross-language tasks and 7,439 artifacts totaling 15.01 GB across CSV, JSON, SQLite, Markdown, PDF, and video. DataSpace also served as the official evaluation benchmark for the KDD Cup 2026 Data Agents for Complex Data Analysis competition. Each agent receives only a question and workspace and returns the complete requested tabular result. We construct DataSpace with DataSpace-Builder, an execution-grounded framework comprising cross-language transformation, constraint-aware relational sampling, modality routing and artifact rendering, and human review and task repair by 11 domain experts. A deterministic evaluator performs header-invariant column alignment, type- and precision-aware normalization, and order-aware row comparison. Across six recently released frontier multimodal models and five widely used agent harnesses, the best accuracy reaches 66.34%, while harness choice creates a 15.36-point spread with the backbone fixed. Multimodal evidence integration and joins consistently reduce accuracy across all six backbones. These results show that DataSpace remains unsaturated and identify key challenges for improving data-agent reliability.
