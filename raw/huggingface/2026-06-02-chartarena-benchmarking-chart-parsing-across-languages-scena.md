---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.01348
url: https://huggingface.co/papers/2606.01348
arxiv_url: https://arxiv.org/abs/2606.01348
date: 2026-06-02
---

# ChartArena: Benchmarking Chart Parsing across Languages, Scenarios, and Formats

Charts are a primary medium for conveying quantitative and relational information, yet systematically evaluating chart parsing models remains difficult. Existing benchmarks focus on narrow chart types and leave diagrammatic structures such as flowcharts and mind maps largely unaddressed, while models produce outputs in incompatible formats, and datasets rarely include the printed or hand-drawn images encountered in practice. To address these issues, we introduce ChartArena, a comprehensive bilingual benchmark covering eight chart families spanning both numeric charts and diagrammatic structures, each evaluated across three visual scenarios: digital renderings, printed photos, and hand-drawn photos. The dataset is built via a human-agent collaborative annotation pipeline with multi-stage human verification to ensure annotation reliability. To enable fair cross-model comparison, we further design a format-agnostic evaluation protocol that maps heterogeneous outputs into two canonical semantic spaces, a normalized triple view and a directed graph view, and scores them with structure-aware metrics. Through extensive evaluation of 26 leading MLLMs, we observe three consistent findings: (i) frontier proprietary models such as Gemini 3.1 Pro lead overall, yet the strongest open-source systems are rapidly closing the gap; (ii) document parsing models handle numeric charts reasonably but fall sharply behind on diagrammatic structures; and (iii) expert chart parsers remain limited to narrow chart families. Across all models, radar charts and hand-drawn scenarios stay especially challenging. These findings show that ChartArena exposes clear capability gaps and provides a unified foundation for future progress. ChartArena is publicly available at https://github.com/pspdada/ChartArena.
