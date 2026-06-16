---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16295
url: https://huggingface.co/papers/2606.16295
arxiv_url: https://arxiv.org/abs/2606.16295
date: 2026-06-16
---

# VisualClaw: A Real-Time, Personalized Agent for the Physical World

Vision language models are serving as general-purpose interfaces for complex multimodal tasks. However, deployment still faces three gaps: VLMs typically incur high latency and cost when processing dense video frames and long prompts, the agent scaffold remains static after deployment, and standard video-QA benchmarks do not test whether agents can use visual evidence inside tool-using workspaces. We present VisualClaw, a self-evolving multimodal agent built around two principles. First, hybrid encoding reduces deployment cost by filtering less informative streaming frames with a cascaded gate and compressing the text skill bank through hot/cold top-k injection. Second, skill evolution lets the agent learn from failures: retrieved memories condition an evolver as direct concatenated context or as guided evidence, producing skill-bank updates that help future questions. Across 4 video-QA benchmarks with 2 VLMs, VisualClaw cuts per-question API cost by an average -98% versus full-frame upload and by -25.9% over the offline uniform 8 frame baseline, while boosting accuracy in most settings, e.g., an average +3.85% and a peak +15.80% on EgoSchema with Gemini 3 Flash. To address the gap, we curate VisualClawArena, a 200-scenario multimodal agentic benchmark built through a strict five-stage pipeline; models must use video evidence, documents, dynamic updates, and executable checks inside a workspace. On VisualClawArena, the same framework with computer-use agent backends improves macro accuracy by +2.9% for Codex (GPT-5.5) and +3.2% for Claude Code (Sonnet 4.6) over no-evolution baselines, with a -9.5% cost reduction compared to the uniform-sampled baseline. These properties make VisualClaw a natural fit for edge applications, where the cascade reduces a 1-hour streaming session from ~3,600 API uploads down to only 5-20 calls and the self-evolution makes it a perfect personalized assistant.
