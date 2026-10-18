---
date: 2026-10-18
type: source-summary
topic: ai-industry
sources:
  - raw/rss/2026-10-17-interconnects-ai-meta-shakes-up-the-frontiers-open-and-closed.md
  - raw/gmail/2026-10-18-newsletters.md
---

# Interconnects: "Meta shakes up the frontiers, open and closed"

**TL;DR.** Nathan Lambert argues that the week of Muse Spark Open (Meta's 816B-total, 42B-active open model), Reflection's Beam and Mistral Large 4 (announced, weights not yet out) roughly **halved the gap between the best American and Chinese open models**. Without Muse Spark Open and Beam there would be 20+ Chinese open models better than the best Western one. He ranks the field **Anthropic > OpenAI > Meta ≈ Gemini > xAI ≈ Chinese open weights > US open weights**, and says the US frontier has narrowed to five labs.

## The argument

- **Muse Spark Open should get adopted.** Western open models get far more adoption than Chinese ones at the same performance-per-size, and demand for open inference is rising as open agents become real. Capability sits above GLM 5.2, near DeepSeek V4.1 Flash, behind GLM 5.3 and Kimi K3.
- **Probably a safety-tuned Muse Spark 1.2, not a broken 1.3.** About a 1-point Artificial Analysis drop for the extra safety post-training.
- **The license is the risk.** "Built with Muse" display, a revenue gate above $20M/month, an acceptable-use policy that also binds outputs and derivatives (so synthetic-data use is legally ambiguous). Lambert calls non-standard open licenses "an unnecessary strategic risk."
- **Organization beats resources.** Meta's flat org (Alexandr Wang has 200+ direct reports) is shipping consistently. Labs fail from management layers; Llama failed from politics over performance.
- **The "tier 3" squeeze.** Mistral, Nemotron, Reflection, Arcee struggle to move either frontier; frontier models now cost billions each. Microsoft could join the top five given its MAI scaling results.
- **Nobody can predict real-world model quality.** Why did Claude go from Fable 5 (hit) to Opus 5 (dud) to Opus 5.5 (hit)? Evaluations are a proxy; the long tail is unknowable.
- **Valuation puzzle.** Meta is valued under $2T, about where Anthropic's IPO is pitched; "one of the two valuations needs to correct massively."

## Relation to prior wiki pages

- Builds on the [10-16 Muse Spark Open coverage](../daily-digest/2026-10/2026-10-16.md), which focused on its shipped serving stack (NVFP4 weights, DFlash2 drafter, MLX build).
- DeepSeek's V4.1-Flash-1017 ([10-18](../llms-foundation-models/2026-10-18-deepseek-v41-flash-1017.md)) landed the next day and moved the Chinese open frontier again, testing the "gap halved" claim within 24 hours.
- The license argument meets AI Weekly's Tech Against Terrorism finding (10-17): stripped copies of open models now appear in under three days on average.

Source: [Interconnects](https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open)
