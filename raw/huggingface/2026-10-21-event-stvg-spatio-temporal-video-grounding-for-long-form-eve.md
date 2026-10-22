---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642920
arxiv_id: 2610.22444
url: https://huggingface.co/papers/2610.22444
arxiv_url: https://arxiv.org/abs/2610.22444
date: 2026-10-21
---

# Event-STVG: Spatio-Temporal Video Grounding for Long-Form Event Reasoning

Spatio-Temporal Video Grounding (STVG) aims to jointly localize a target in space and time given a natural-language query. Despite continued advances, existing STVG benchmarks remain largely centered on localizing targets through instance-specific descriptions, leaving them largely decoupled from long-form reasoning increasingly emphasized in multimodal large language models (MLLMs). In this paper, we introduce Event-STVG, a task that shifts STVG from locating what is described toward event-level reasoning by unifying long-form context, repeated-event reasoning, event localization, role inference, and multi-target grounding. To facilitate research on Event-STVG, we construct a large-scale benchmark comprising 4,016 annotated event occurrences across soccer and seven additional domains. Experiments with state-of-the-art MLLMs reveal substantial difficulty, with the strongest model achieving only 5.4% m-vIoU at the 10-minute horizon. Across domains, we consistently observe confusion among repeated same-type events, spatial grounding bottlenecks, and rare success in jointly grounding all required roles. Event-STVG establishes a new challenge for visual understanding in MLLMs, calling for future models that can jointly reason about complex events across space and time. Code and annotations are available at https://github.com/THU-KEG/EventSTVG
