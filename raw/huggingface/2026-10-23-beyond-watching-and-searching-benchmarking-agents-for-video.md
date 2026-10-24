---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.882701+00:00
arxiv_id: 2610.31158
url: https://huggingface.co/papers/2610.31158
arxiv_url: https://arxiv.org/abs/2610.31158
date: 2026-10-23
---

# Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports

Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, retrieves external multimodal evidence, and produces an interactive report linked to relevant video moments. This task has direct practical value because it helps users locate relevant moments, verify claims, reproduce demonstrated procedures, and make informed decisions from video content. We present a skill-based workflow and OmniDR-Bench for this task. For evaluation, we propose Omni Atomic Rubric Trees (Omni-ARTs). Each tree contains three dimensions, 23 shared directions, and task-specific atomic binary criteria. The directions test audiovisual grounding, multimodal evidence use, and interactive presentation. Audited Rubric Construction (ARC) builds these trees through independent evidence collection, automated checks, behavioral calibration, and iterative human review. OmniDR-Bench contains 50 Chinese and English tasks across 19 realworld subcategories. It includes 6,414 criteria. Across 18 agent configurations, the best system scores 63.3 out of 100. Current agents still need broader content coverage, stronger causal and logical analysis across modalities, and more accurate citation support. We further analyze models, harnesses, skill configurations, video categories, and research trajectories. The code and data are released at https://github.com/marinero4972/OmniDR-Bench.
