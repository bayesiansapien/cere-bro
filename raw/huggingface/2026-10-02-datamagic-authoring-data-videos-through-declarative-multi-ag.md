---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821513+00:00
arxiv_id: 2609.33403
url: https://huggingface.co/papers/2609.33403
arxiv_url: https://arxiv.org/abs/2609.33403
date: 2026-10-02
---

# DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration

Data videos communicate data insights through dynamic charts, voice narration, and synchronized animations, and have become a widely adopted form of data storytelling. However, producing them requires expertise in data analysis, narrative design, and video editing. Static visualization tools lack narrative and animation capabilities; authoring tools rely on pre-prepared charts rather than raw data; and pixel-level models generate videos end-to-end but cannot guarantee data accuracy or provenance. End-to-end automatic generation faces two core challenges: how to uniformly represent charts, narration, and animations together with their temporal relationships, and how to efficiently search a vast design space for narrative-coherent compositions. We present DataMagic, which authors data videos from raw tabular data through declarative multi-agent orchestration. First, the declarative specification DVSpec unifies charts, narration, and animations with data-bound references and declarative synchronization, ensuring data provenance and automatic audio-visual alignment. Second, a "Generate-then-Orchestrate" multi-agent strategy generates candidate scenes in parallel and then optimizes narrative coherence through global orchestration. DVSpec provides a shared state for three complementary interaction modes, bridging full automation with fine-grained human control. Evaluations on 109 real-world samples show that even the most advanced LLM (e.g., GPT-5) achieves only 2.13/5 with execution success rates between 48.62% and 86.24%; DataMagic improves quality to 3.89 (+83%) with success rates above 95%, with the most significant gains in animation and narrative dimensions. A user study shows that, compared to a conversational LLM workflow, DataMagic improves creation efficiency (79.7% reduction in task time) and reduces perceived cognitive load. Project page: https://github.com/HKUSTDial/DataMagic.
