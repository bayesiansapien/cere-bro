---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38119
url: https://huggingface.co/papers/2609.38119
arxiv_url: https://arxiv.org/abs/2609.38119
date: 2026-09-30
---

# VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents

Long-form video understanding requires multimodal agents to iteratively gather evidence over many reasoning steps. However, most existing agentic methods suffer from semantic thrashing: as append-only working memory grows, attention to key evidence collapses, and the agent loses access to what it has already found. First, we provide a structural argument showing that append-only memory can incorporate newly observed target evidence, but cannot remove accumulated noise or prevent ordered context growth without a rewrite operator. Second, motivated by this analysis, we propose VideoLoop, a multimodal agent with two coupled loops. The outer loop reasons over the video and the inner loop, after each step, retrieves artifacts from an unbounded filesystem of past observations and intermediate analysis, and rewrites a bounded working memory. Extensive experiments demonstrate the effectiveness of VideoLoop, which improves four popular LVLM backbones in a plug-and-play manner, with an average gain of 4.2% points over baseline on VideoMME (long). Further analysis of working memory suggests that VideoLoop mitigates semantic thrashing: on the hardest quarter of VideoMME (long) questions, a blind judge that reads only the agent's context answers 81.1% correctly, versus 60.9% for the append-only agent. With Gemini 3.1 Pro, VideoLoop reaches 88.3% on VideoMME (long), 88.8% on VideoMMMU, and 80.9% on LongVideoBench (long).
