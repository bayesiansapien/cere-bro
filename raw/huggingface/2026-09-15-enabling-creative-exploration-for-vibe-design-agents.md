---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.15078
url: https://huggingface.co/papers/2609.15078
arxiv_url: https://arxiv.org/abs/2609.15078
date: 2026-09-15
---

# Enabling Creative Exploration for Vibe Design Agents

Vibe design agents turn natural-language briefs into rendered interfaces and frontend code. Yet a useful design agent should do more than produce one valid page: it should help users explore coherent alternatives. Increasing token-level temperature is a blunt solution because it varies aesthetic decisions and syntax-sensitive code at the same time. We instead separate exploration from implementation through an inference architecture that makes design direction an explicit intermediate decision. Inspired by Verbalized Sampling, a pre-pass proposes structured design specifications with typicality scores, an external selector samples one, and the downstream generator realizes the selected specification together with the original request under fixed settings. We apply this approach to UI themes and visual-asset prompts. Across 168 prompts, with 1,255 paired comparisons per temperature for each intervention, theme sampling broadens observed selection coverage and screenshot variation, while LLM-judge preferences vary across interventions, prompt complexity, and viewport. In an online experiment with more than 300,000 tasks, the observed code-export increase remains statistically uncertain, while fewer negative feedback events coexist with more correction interactions and modest operational costs. Together, these findings identify structured design specifications as a practical control point for exploring alternative UI concepts while keeping downstream generation settings fixed.
