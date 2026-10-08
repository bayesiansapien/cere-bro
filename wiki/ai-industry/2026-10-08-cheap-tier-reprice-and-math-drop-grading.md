# Cheap-tier reprice, routing to the PC, and the math drop gets graded (2026-10-08)

**Sources:** [Simon Willison on Haiku 5.5](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/), [The Decoder on Haiku 5.5](https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/), [The Decoder on GPT-6 Intelligent UI](https://the-decoder.com/chatgpt-with-gpt-6-ditches-mostly-text-output-for-interactive-ui-with-charts-buttons-and-mini-apps/), [The Information on Microsoft PCs](https://www.theinformation.com/briefings/microsoft-debuts-new-windows-pcs-features-powered-on-device-ai), [The Information: "Where is all the automation?"](https://www.theinformation.com/articles/ais-simmering-question-where-f-automation), [Marcus on AI](https://garymarcus.substack.com/p/complementary-remarks-from-gary-marcus), [Hacker News Digest #320](https://news.ycombinator.com/item?id=49977979), X Following feed.

**TL;DR.** The US Wednesday was a pricing and placement day. Anthropic's Claude Haiku 5.5 matched GPT-6 Luna's $0.10/$0.50 per million tokens up to 100K tokens (5x above that), with a tokenizer that uses ~1.25x more tokens than Haiku 4.5, a big OSWorld jump (15.7% to 72.4%), half-price Sonnet 5.5 cache reads, and monthly API credits for Max and Team subscribers. Microsoft moved routine Copilot coding onto a 3-bit on-device model on Nvidia RTX Spark PCs. OpenAI rolled GPT-6 with "Intelligent UI" to all ChatGPT users and says answers can start while the model is still thinking, cutting waits 44%. The OpenAI math release moved from hype to grading: Gary Marcus says the procedure is undisclosed; the Association for Human Mathematics urged mathematicians to stop working with OpenAI; and a new paper argues Lean verification of auto-formalized proofs does not guarantee the natural-language proof is right.

## Key points

- **Haiku 5.5 economics.** Same list price as Luna under 100K tokens and better benchmarks; above 100K, Luna ($0.20/$0.75 past 272K) is much cheaper. Hidden 1.25x tokenizer cost. Reasoning cannot be disabled; default effort is medium.
- **Microsoft on-device.** MAI-Code-1.1-Flash (137B/6.8B active, 3-bit, 256K) replaces Claude Haiku 4.5 for routine Copilot work, at no inference charge. Microsoft Execution Containers (agent sandbox) GA on Windows 11. DeepSeek V4 Flash shown at 1.6 bits (~60GB) on the same PCs.
- **Automation gap.** TypeSafe's Diogo Almeida: "100% of LLMs today are optimized for assistance with RLHF," so they fail at unattended automation. Anthropic's Cat Wu describes work stuck at "Claude does 80%, I do 20%." Cognition is now valued at $48B.
- **Math drop grading.** "Navier-Stokes lost in translation" ([arXiv 2610.08144](https://arxiv.org/abs/2610.08144)) argues Lean-verified auto-formalization can still mistranslate the statement being proved.

## How this relates to prior wiki pages

- Extends the [10-07 open MoE / cost-switching page](2026-10-07-open-moe-release-day-and-cost-switching.md): price is now the main competitive lever in the cheap tier, and tokenizer changes are a hidden lever inside it.
- Routing and pricing details live in [routing graded (10-08)](../ai-routing/2026-10-08-routing-graded-jev-router-local-routing.md).

## Related

[Compute economics](../hardware/compute-economics.md) · [LLM routing](../ai-routing/llm-routing.md) · [Responsible AI](../responsible-ai/responsible-ai.md)
