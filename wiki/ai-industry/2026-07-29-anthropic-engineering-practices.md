# How Building Software Is Changing at Anthropic

**Source:** [The Pragmatic Engineer, Gergely Orosz, 2026-07-28](https://newsletter.pragmaticengineer.com/p/inside-anthropic) · [raw/rss](../../raw/rss/2026-07-28-pragmatic-engineer-how-building-software-is-changing-at-anthropic.md)

## TL;DR

Orosz visited Anthropic's SF office and interviewed four people: Katelyn Lesse (Head of Engineering, Claude Platform), Jarred Sumner (creator of Bun, now working on Bun and Claude Code), Thariq Shihipar (Claude Code engineering and education), and David Hershey (Applied AI, working with Cursor, Cognition, and Perplexity). The value is that it reports what did *not* change alongside what did, which most AI-transformation coverage does not.

**What changed.** Prototyping is more fluid. **Verification now takes more time than implementation**, which is the single most load-bearing inversion in the piece. Code review and testing are increasingly done by AI. Design is ongoing rather than upfront, teams run more projects at once, and there is a **maximum of two engineers per project**.

**The headline number.** Migrating Bun, a 500K+ line project, from Zig to Rust. Orosz frames it as a twelve-month project for a small team, historically impractical. It took the project's creator **less than two weeks (11 days) and about $165K of tokens**.

**What stayed the same.** Two-pizza teams. Planning still matters. PRDs are still relevant on complex projects. Context switching is still hard. And the ratio of time spent coding versus testing has not shifted much, which sits oddly next to the verification-exceeds-implementation claim and is worth noting rather than smoothing over.

**The counterexample the piece keeps.** Claude Managed Agents, one of the Platform team's hardest projects, still took **six months** and required mid-way re-architecture. Infrastructure work did not compress.

## The claim that generalizes

The through-line is that **the bottleneck moved from producing code to establishing that code is correct**. That is consistent with what [Boris Cherny said in the same week's Startup School talk](../../raw/youtube-ai-tech/2026-07-27-Boris-Cherny-Building-Claude-Code.md): the real skill is no longer prompt engineering but elicitation plus verification, and his multi-week autonomous Swift port worked because the prompt included a pixel-by-pixel comparison loop against the running Electron app. Two independent accounts from inside the same company converging on verification as the binding constraint is a stronger signal than either alone.

The "maximum two engineers per project" detail is the most concretely checkable organizational claim, and the most transferable. If verification rather than implementation is the constraint, adding engineers to a project buys less than it used to, and the optimal team gets smaller while the number of concurrent projects goes up. That is a falsifiable prediction about org structure, not a vibe.

## How it lands against the wiki's other threads

**It is the strongest current evidence for the recursive-improvement thesis that [Romero's essay (07-28)](2026-07-29-google-withdrew-world-models.md) argues Hassabis rejects.** Romero's hypothesis is that DeepMind's leadership sees automating AI research with coding agents as an off-ramp or a dead end, and is betting on world models instead. An 11-day 500K-line language migration and a self-maintaining Claude Code codebase are exactly the compounding artifacts the coding-agent bet predicts. The six-month infrastructure project is the counter-evidence in the same article, and it is specific: the compression is real for well-specified transformation work and absent for work that requires deciding what to build.

**The token cost is the number the wiki should keep.** $165K for one migration is a concrete price for a task class. Read against Altman's claim in the same week that worldwide inference demand grows roughly 10x per year and that "we will sort of never be out of the compute shortage," it is a datapoint on why: the tasks people now hand to models are ones that were previously not attempted at all, so demand is not substituting for existing spend, it is new. That is the demand-side argument behind every KV cache and compression paper on [inference-efficiency](../inference-efficiency/kv-cache.md).

**And it is the supply-side context for the week's pricing fights.** [Cursor customers are contesting renewals](https://www.theinformation.com/articles/cursor-customers-fight-price-hikes-contract-talks) after the shift to usage-based pricing, one quoted about $1.5M against a prior $200K for the same usage, while Claude Code retains enterprise dominance despite surging costs. Anthropic is describing internally the workflow that justifies the bill; customers are negotiating over whether it is worth it. Both are true.

## Gaps

Access journalism with four interviewees selected by the company, no measurements outside the ones Anthropic chose to share, and the Bun migration is a best case in every dimension (the world expert on the codebase, a mechanical language port with a working reference implementation, and unlimited internal model access). The unresolved internal contradiction, that verification takes longer than implementation while the coding-versus-testing time ratio has not much changed, is not addressed. A promised follow-up covering OpenAI will make the comparison more useful.

## Related

- [The actual reason why Google "fell out" of the AI race (07-29)](2026-07-29-google-withdrew-world-models.md)
- [The big AI labs are competing with your own data (07-29)](2026-07-29-labs-competing-with-your-data.md)
- [Daily digest 2026-07-29](../daily-digest/2026-07/2026-07-29.md)
