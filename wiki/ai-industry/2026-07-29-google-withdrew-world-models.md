# The Actual Reason Why Google "Fell Out" of the AI Race

**Source:** [The Algorithmic Bridge, Alberto Romero, 2026-07-28](https://www.thealgorithmicbridge.com/p/the-actual-reason-why-google-fell) · [raw/rss](../../raw/rss/2026-07-28-algorithmic-bridge-the-actual-reason-why-google-fell-out-of-the-ai-race-ch.md)

## TL;DR

An ~8,000-word argument with one hypothesis, stated plainly and flagged by the author as informed speculation rather than confirmed fact: **Google is not losing the AI race, it withdrew from it.** Romero's claim is that Demis Hassabis does not believe automating AI research with coding agents (systems that write better AI systems, the thing Amodei and Altman are both betting on) is the correct path to human-level general AI. DeepMind's leadership reads that bet as an off-ramp at best and a dead end at worst. Hassabis is betting instead on **world models**: systems that understand and simulate physical reality rather than predicting the next token.

The second half of the argument is the part worth keeping, because it is structural rather than psychological. The race is between two theories of intelligence *and* between two kinds of company. OpenAI and Anthropic are startups that need AI to become a business on a financing clock. Google is an incumbent whose existing business can subsidize a slower, different bet for years. Those two facts are not independent: only the incumbent can afford to be wrong for a long time.

## The load-bearing claim

Recursive self-improvement through coding agents is the compounding story that justifies current frontier-lab valuations. If Hassabis is right that it plateaus, the bet that looks conservative today (spend a decade on models that simulate the world) is the one that pays, and the labs racing hardest are racing toward a wall. If he is wrong, Google spent its lead on a detour while competitors compounded.

Romero is explicit that no executive will confirm this, and that Google's official position is still direct competition. The evidence is circumstantial: the slower release pace, the underwhelming I/O event, the heavyweight departures, and the consistent research direction. Treat it as a well-argued hypothesis rather than reporting.

## Why this matters against the wiki's research record

**The world-model thesis is not just an executive's preference this week, it is a visible research cluster.** [Wonder (07-29)](../llms-foundation-models/2026-07-29-wonder-video-world-model.md) landed on HuggingFace the day after this essay: a real-time camera-controllable video world model with a sparse-attention memory mechanism that attends to a small set of relevant context tokens regardless of context length, generating minute-scale video at 16 FPS. The same Kurate weekly board carries two more: **Persistent Computational State: A Session-Centric Runtime for Generative World Models** (cs.AI #6, [2607.21669](https://arxiv.org/abs/2607.21669)-adjacent, score 1544, ai_rating 7.0) and **On the Identifiability of Controlled World Models** (cs.LG #10, score 1516). Three world-model papers scoring highly in one week, one of them explicitly a *runtime* paper about how you serve them, is what a research direction looks like when it is being industrialized rather than explored.

**The counter-evidence is equally visible and lands the same week.** [The Pragmatic Engineer's Anthropic profile (07-28)](2026-07-29-anthropic-engineering-practices.md) reports a 500K-line Bun migration from Zig to Rust done in 11 days for about $165K of tokens, a task the piece frames as previously a twelve-month project. Boris Cherny's Startup School talk describes Claude Code maintaining itself through twenty to thirty daily routines. That is the recursive-improvement thesis producing exactly the compounding artifacts it predicts. Romero's essay does not engage with this evidence because it was published the same day.

**And the industry is hedging in a direction that fits neither story cleanly.** The [Pacing the Frontier letter](https://pacingthefrontier.com), signed by more than 1,100 frontier-lab employees and endorsed by both OpenAI and Anthropic, asks the US government to help build tools to *deliberately slow* the frontier of automated AI development. You do not ask for a brake on a road you think is a dead end. The letter is the strongest available evidence that the labs believe their own recursive-improvement thesis, which makes Hassabis's dissent a genuine minority position rather than a consensus everyone privately shares.

## Gaps

Circumstantial by construction, and the author says so. The strongest counter-argument the essay does not address is that world models and coding-agent self-improvement are not mutually exclusive, and Google is doing both, so "withdrew" may be over-reading a portfolio allocation as a strategic exit. There is also no financial analysis of how long the subsidy argument actually holds if Gemini loses consumer share.

## Related

- [Wonder (07-29)](../llms-foundation-models/2026-07-29-wonder-video-world-model.md)
- [The big labs are competing with your own data (07-29)](2026-07-29-labs-competing-with-your-data.md)
- [Daily digest 2026-07-29](../daily-digest/2026-07/2026-07-29.md)
