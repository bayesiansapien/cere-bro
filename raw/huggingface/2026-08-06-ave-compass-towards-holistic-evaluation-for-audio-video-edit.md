---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2607.24821
url: https://huggingface.co/papers/2607.24821
arxiv_url: https://arxiv.org/abs/2607.24821
date: 2026-08-06
---

# AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities

While instruction-based video editing has advanced rapidly, real-world videos contain tightly coupled audio and visual signals, and editing one modality often requires coordinated changes in the other. Existing benchmarks primarily evaluate visual transformations on silent clips or isolated audio editing, leaving complex audio-visual editing and cross-modal consistency underexplored. We introduce AVE-Compass, a comprehensive benchmark with 145 curated source videos, 196 audio-visually coupled editing instructions, and 2,688 fine-grained checklist items. It evaluates Instruction Following, Fidelity Preserving, Realism, and Editing Intent through checklist-based MLLM judging and a dedicated realism rubric, complemented by automated cross-modal, video, and audio metrics. Extensive evaluation shows that state-of-the-art models still struggle to execute cross-modal instructions while preserving non-target content. We further propose AVE-Agent, a modular agent framework that decomposes complex instructions into dependent subtasks and iteratively improves editing results through self-reflection and evaluator feedback. AVE-Agent improves instruction execution, Fidelity Preserving, and audio-visual alignment in joint editing while maintaining competitive perceptual quality.
