# MYSTERIOUS Stealth AI Model BEATS GPT-6 Astra & It's COMPLETELY FREE!

**Channel:** WorldofAI
**Published:** 2026-09-28
**Source:** https://www.youtube.com/watch?v=TyhlQ0ufH3Y

## TL;DR
Space Bunny Alpha is an anonymous stealth model on OpenRouter and OpenCode (free during preview) with a 1M-token context, native multimodal input, adjustable reasoning effort and very high decode throughput. On one-shot web-dev tasks at max reasoning it beat GPT-6 Astra (xhigh) on visual detail, at the cost of 3x the wall-clock time. The video's "beats GPT-6" framing rests on a handful of subjective front-end demos, not benchmarks.

## Key Takeaways
- **Specs observed:** ~74 tok/s listed on OpenRouter with ~1.5 s TTFT at default effort; at max reasoning, one run hit ~120 tok/s over a 50K-token output with 7.8 s TTFT.
- **Head-to-head vs GPT-6 Astra (xhigh):** a Three.js voxel Japanese garden took Space Bunny ~45 min (free) vs Astra ~15 min at a reported $424. Space Bunny's output was judged more detailed.
- **vs GPT-6 Sol on a 3D globe:** Sol finished in ~5 min using ~520K tokens; Space Bunny took ~43 min using ~219K tokens. Fewer tokens but far longer wall-clock, implying either heavy queueing on the free tier or long serial tool loops rather than slow decode.
- **Multimodal strength:** recreated a playable HTML game from a video clip (read boss name off the HUD, synthesized Web Audio sounds); turned a floor-plan image into a Blender apartment via tool calls.
- **Agentic breadth:** one-prompt equity research app pulling market data, SEC filings and competitor sets.
- **Weaknesses:** a "Call of Duty clone" used 2D sprites in a 3D scene; macOS clone had UI flashing bugs; several outputs needed ~4 iterations.
- **Checkpoint is moving:** the stealth checkpoint was updated mid-preview and got faster, so any evaluation is a snapshot.

## Architecture & Optimization Mechanics
- **Tokenizer fingerprinting is the real story.** Independent testers matched all 36 input-token counts across 12 fixtures to MiniMax's public M3 tokenizer (M2.7 also matches), while Qwen, GLM, DeepSeek and Llama tokenizers did not. This is a cheap, robust provenance technique: token counts from the billing API leak the vocabulary.
- **Throughput profile fits an efficient sparse MoE.** 1M context plus 120 tok/s on long outputs is consistent with MiniMax's lineage of hybrid/linear-attention MoE designs aimed at long-context cost.
- **Reasoning effort is the dominant latency knob.** The same model swings from "faster than M3.1 Flash" to ~45 min per task. For a router, effort level is a second routing dimension on par with model choice.
- **Cost asymmetry:** Astra at $10/$50 per M tokens burned $424 on a single agentic web build. Free stealth models distort cost comparisons; the useful metric is tokens-to-solution (219K vs 520K), which favors Space Bunny.

## Grounded Context (Web Enrichment)
The video dismisses the MiniMax theory because MiniMax "officially released M3.1 Flash." That reasoning is weak. MiniMax launched only **M3.1-Flash-Preview** on September 27 inside MiniMax Code and its Token Plan, and the full M3.1 release is still pending. The tokenizer evidence points to the MiniMax M3 family, not a specific checkpoint, so Space Bunny could plausibly be a larger or later M3.1 variant. Reports also note Space Bunny briefly entered the global top three on OpenRouter usage.

On pricing context: GPT-6 Astra lists at $10 in / $50 out per million tokens, and OpenAI's GPT-6.1 Sol (launched at DevDay, Sept 29) matches Astra on DeepSWE v1.1 at one-fifth the price. So the "free model beats $424 Astra run" comparison is already dated a day later; Sol is the fairer paid baseline.

Sources: [OpenRouter: Space Bunny Alpha](https://openrouter.ai/stealth/space-bunny-alpha), [CellCog: MiniMax clues](https://cellcog.ai/blog/what-is-space-bunny-alpha/), [The Neuron](https://www.theneuron.ai/blog/who-made-space-bunny-minimax-clue/), [BigGo Finance](https://finance.biggo.com/news/4850a556-d3c5-4eca-bdbe-bd08641565d0), [DataNorth: M3.1-Flash-Preview](https://datanorth.ai/news/minimax-releases-m3-1-flash-preview), [The Next Web: GPT-6.1 Sol](https://thenextweb.com/news/openai-gpt-6-1-sol-price-astra-devday).

## Real-World Application / Actionable Step
- **Routing research:** add Space Bunny (while free) as an extra arm in your router eval set. Log tokens-to-solution and wall-clock separately, since this model decouples them sharply.
- **Treat reasoning effort as a routing action.** Build a small experiment: fixed model, effort in {low, med, max}, measure quality delta vs latency on your coding tasks. Expect a steep knee.
- **Steal the tokenizer-fingerprint trick** for vendor provenance checks when using routed or aggregated APIs.
- **Do not send proprietary code** to an anonymous stealth provider; use public tasks only.
