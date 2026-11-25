---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.928702+00:00
arxiv_id: 2611.28167
url: https://huggingface.co/papers/2611.28167
arxiv_url: https://arxiv.org/abs/2611.28167
date: 2026-11-24
---

# VideoJSON: A Minimal Harness Beats Purpose-Built Memory for Ultra-Long Video Understanding

Answering questions over days or weeks of video requires searching for scattered clues across long timelines. Existing video agents rely on complex memory graphs and fixed retrieval pipelines, which restrict how the agent can search. We propose VideoJSON, a minimal harness for ultra-long video understanding that keeps the memory simple and lets a coding agent write its own search programs. During indexing, a vision-language model turns each minute of video into a single JSON record containing a dense caption and structured fields such as events, entities, places, and speech transcripts. At query time, the agent writes Python or Bash programs in a sandboxed container to filter, link, and read these records over multiple steps, without task-specific training or raw video access. On four ultra-long video benchmarks, VideoJSON with DeepSeek V4.1 Flash outperforms MAGIC-Video by 7.0, 20.0, and 24.75 points on EgoLifeQA, Ego-R1-Bench, and MM-Lifelong Week, and beats the best prior EgoMemReason score by 12.6 points. Across four policy models of increasing capability, VideoJSON's average score rises by up to 11.58 points over the weakest model, compared with at most 5.50 points for MAGIC-Video. Ablations show that both agentic code search and the structured JSON records drive these gains, while adding hourly summaries, extra tools, or video access changes the average score by less than 1.5 points. In addition, fine-tuning Qwen-3.5-Flash on 64 VideoJSON trajectories from an unrelated 100-hour livestream improves its MM-Lifelong scores by up to 8.25 points. Code will be open-sourced after publication.
