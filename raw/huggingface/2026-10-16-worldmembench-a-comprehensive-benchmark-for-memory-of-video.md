---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.19063
url: https://huggingface.co/papers/2610.19063
arxiv_url: https://arxiv.org/abs/2610.19063
date: 2026-10-16
---

# WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models

As video models enable longer and more realistic interactive experiences, maintaining a world consistent with its history becomes essential. This requires both preserving previously observed content and ensuring coherent world evolution over time. World memory is a critical capability to evaluate alongside visual fidelity and video duration. We introduce WorldMemBench, a benchmark for systematically evaluating world memory in video world models. Across 260 test cases, it assesses static memory through the retention of human identity and appearance, object appearance and geometry, and environmental content and geometry, and dynamic memory through event progression and state persistence. Using controlled camera departures and multi-revisit trajectories, the benchmark evaluates static content against fixed initial references and dynamic events against expected state transitions. It combines appearance and geometry metrics with event-specific assessments, and reports video quality and camera-following accuracy as complementary diagnostics. Evaluation of nine representative models shows that strong static retention does not imply reliable dynamic state evolution, while repeated revisits reveal memory degradation beyond the first return. Human studies support the alignment between our automatic evaluations and human judgments. WorldMemBench provides a systematic testbed for diagnosing memory failures and guiding the development of persistent, temporally coherent video worlds.
