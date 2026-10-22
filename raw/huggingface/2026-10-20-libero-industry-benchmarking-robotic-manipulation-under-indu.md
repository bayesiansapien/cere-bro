---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.16782
url: https://huggingface.co/papers/2610.16782
arxiv_url: https://arxiv.org/abs/2610.16782
date: 2026-10-20
---

# LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap, we introduce LIBERO-Industry, a novel benchmark built on the widely used robot learning benchmark LIBERO, that translates the aforementioned industrial constraints into controllable task conditions and measurable success criteria. Specifically, LIBERO-Industry comprises three classic task scenarios: Static-to-Dynamic (S2D) loading, Dynamic-to-Static (D2S) unloading, and Dynamic-to-Dynamic (D2D) transfer. The suites contain 216 tasks in total that systematically vary object geometry, conveyor speed, interaction-window duration, and geometric acceptance region size. Extensive experiments across five generalist robot policies (including vision-language-action models and world-action models) show that performance progressively degrades as industrial constraints are introduced and combined. Under a shared fine-tuning and evaluation protocol, the LIBERO-Industry co-training condition achieved higher observed target-transfer completion than the original-LIBERO condition.
