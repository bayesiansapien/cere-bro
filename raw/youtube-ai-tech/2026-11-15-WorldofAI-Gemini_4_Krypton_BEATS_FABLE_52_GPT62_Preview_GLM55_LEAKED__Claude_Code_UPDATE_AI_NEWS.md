# Gemini 4 Krypton BEATS FABLE 5.2!?, GPT-6.2 Preview, GLM-5.5 LEAKED & Claude Code UPDATE! AI NEWS

**Channel:** WorldofAI
**Published:** 2026-11-15
**Source:** https://www.youtube.com/watch?v=iXvttGCoc1g

## TL;DR
A weekly roundup that is mostly leaks. The one piece of hard, decision-relevant signal is Anthropic's model-selection guidance for Claude Code: Opus 5.5 at medium effort is the daily driver; raise effort before switching to Fable 5.2; use Sonnet 5.5 for well-scoped tasks and Haiku 5.5 for classification, search and sub-agents. All four have 1M-token context. The headline "Gemini 4 Krypton beats Fable 5.2" is unverified leak chatter, and the host himself says it feels closer to Sonnet 5.5 on webdev.

## Key Takeaways
- **Claude model routing guidance (Anthropic):** the host cites a 52-task Claude Code comparison: Opus 5.5 solved 84.6% vs Fable 5.2 at 82.7%, with Fable about 2.8x more expensive per solved task. Reserve Fable for hard migrations, complex architecture, deep research and long autonomous runs.
- **Gemini 4 Krypton (unconfirmed):** a new checkpoint was reportedly spotted on 13 November behind the "Hydrogen" label in Arena and the API. Demos (three.js rocket engine, SVG controllers, CSGO-style clone) are cherry-picked. Rumoured release is next week, at "Fable-level but cheaper".
- **Claude Code / Claude app:** custom themes via mods (local sessions); Projects gets a proactive coordinator across parallel threads, `/btw` side questions, `/fork` to branch threads, thread reminders, read-only thread sharing and a redesigned threads panel. In public beta for Pro and Max.
- **Agent payments:** ChatGPT Wallet (US Pro, with Amex, Mastercard and Visa; agents buy without seeing card details; per-transaction security check), and Google Wallet connected to Gemini for US users.
- **Agent orchestration:** Antigravity's `/run-workflow` generates a reviewable, reusable Python script that coordinates sub-agents. Deterministic orchestration instead of prompt-driven drift.
- **Math:** Google claims Gemini-4 multi-agent systems produced machine-checked formalizations, including a 1.8M-line Lean proof built from 29,000 sub-agent calls.
- **Other items:** a GPT-6.2 "Astra" preview (leaked outputs only); a GLM-5.5 benchmark leak claiming it beats Opus 5.5 (possibly fake); DeepSeek exposing app features via API with hints of paid tiers; Meta Muse Spark 1.4 spotted in a PR; a Qwen 4.0 Max preview stealth upgrade; OpenAI reportedly winding down its robotics team after 5 months; Perplexity's "teammate" agent on Mac; Starship reportedly caught at the tower.
- **Anthropic IPO:** Dario Amodei says the main reason is more compute and a cash buffer between "low-compute and high-compute worlds".

## Architecture & Optimization Mechanics
- **Anthropic's guidance is model routing as policy.** The rule is to escalate effort within a model before escalating to a pricier model. That is a two-axis router (model × reasoning budget), and it shows the effort knob is often the cheaper lever.
- **Shared 1M context across tiers** removes context length as a reason to route upward, so routing can be based purely on difficulty.
- **Haiku for sub-agents** reflects the orchestrator-worker cost structure: frontier planner, cheap workers.
- **Deterministic workflow scripts (Antigravity)** are another case of replacing prompt-level control with code-level control, the same theme as Lauren Tan's lint-over-prose argument.

## Grounded Context (Web Enrichment)
Fable 5.2 launched on 9 November at $8/$40 per million tokens, double Opus 5.5's $4/$20. Opus 5.5 remains Claude Code's default, and Anthropic tells developers to start with the cheaper model. I found no source for the exact 84.6% vs 82.7% numbers. Third-party results are mixed: at matched high effort Fable can be cheaper per task (FrontierCode 2.0, vendor-reported), while at max effort Artificial Analysis found Fable about 2.6x more expensive per task. The video's "2.8x" is consistent with the max-effort picture.

On Krypton, as of 9 November only community leaks of a "krypton-a" checkpoint existed. Google's API listed only Gemini 4 Argon, with Carbon limited to cyber defenders since 28 October. Arena outputs are cherry-picked and unattributable, so "beats Fable" is not established. Anthropic's IPO is real: the S-1 discloses $542 to $567B in compute commitments, including up to $120.5B with SpaceX through 2029. Valuation reports range from $965B to over $2T.

## Real-World Application / Actionable Step
- **Adopt Anthropic's two-axis routing in your own router research:** add reasoning effort as a routing dimension alongside model choice. Benchmark "Opus-medium → Opus-high → Fable-high" escalation against direct routing on your task mix, and report cost per solved task, not accuracy alone.
- **Default Claude Code to Opus 5.5 medium,** escalate effort on failure, and reserve Fable for multi-hour autonomous jobs. Push sub-agent and search work to Haiku 5.5.
- **Wait for Krypton's official release and pricing** before switching any pipelines. Re-evaluate if it lands at Gemini 4 introductory pricing with independent benchmarks.

Sources:
- [claudefa.st: Fable 5.2 vs Opus 5.5](https://claudefa.st/blog/models/claude-fable-5-2-vs-opus-5-5)
- [The New Stack: Anthropic Fable vs Opus cost](https://thenewstack.io/anthropic-fable-opus-cost/)
- [kie.ai: What is Gemini 4 Krypton?](https://kie.ai/blog/what-is-gemini-4-krypton)
- [TestingCatalog: Gemini 4 Carbon checkpoint on Arena](https://www.testingcatalog.com/google-tests-new-gemini-4-carbon-checkpoint-arena.md)
- [Fortune: Anthropic S-1 compute strategy](https://fortune.com/2026/10/26/anthropics-s1-ipo-reveals-the-inner-workings-of-its-fast-evolving-compute-strategy/)
- [Fortune: Dario Amodei's financing mechanics](https://fortune.com/2026/11/04/dario-amodei-wants-a-country-of-geniuses-in-a-data-center-realizing-that-vision-requires-tricky-financial-mechanics-anthropics-ipo-filing-shows/)
