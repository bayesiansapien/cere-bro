# How to Build an Agent That Builds the Culture (Zach Bruggeman, Ramp)

**Channel:** AI Engineer
**Published:** 2026-11-20
**Source:** https://www.youtube.com/watch?v=MDI81OaZAD4

## TL;DR
Ramp's in-house cloud coding agent, Inspect, now writes and ships about 75% of Ramp's code. It runs fully remote, multiplayer sandboxes that spin up in under 5 seconds, wired into all company tools. The talk is about the social design that made it stick, not the plumbing. (1) Run **one shared agent for the whole company**, so every improvement spreads instantly and nobody pays per-person setup costs. (2) Make **every session public by default**, so PR reviewers see the full conversation, tool calls, screenshots, and verification videos. That turns trust-building into a group activity. (3) Let people **extend the agent without permission**. Engineers built "Review Buddy", a code review agent, on Inspect's PR triggers, which replaced rotating off-the-shelf tools. Inspect is now available to outside companies.

## Key Takeaways
- **Lesson 1, kill information silos:** with per-person agent setups, about 15 minutes of setup × thousands of people × every frontier change adds up to lost days and uneven skill across the org. A single strong baseline removed the need for a mandate.
- **Learning by watching:** no formal AI training sessions. Users ask Inspect to summarize how a teammate structures prompts or breaks down problems, based on their public sessions.
- **Product feedback for free:** watching unexpected usage tells the Inspect team which native primitives to build next.
- **Lesson 2, trust is built in public.** Example: an OTel exporter on Cloudflare Workers called `fetch` but never read or cancelled the response body. Inspect first blamed "instrumentation". After public prodding it found the root cause, and the patch fixed it. A skeptical user who had threatened "I'll just use Claude Code" became a collaborator within an hour.
- **Reviewable artifacts:** PRs carry the session transcript plus a browser-verification-agent video, not a bare 400-line diff.
- **Lesson 3, think bigger together:** he pushes back on lone-wolf AI operator culture. Ask your team what you have been waiting to build, then build it together.

## Architecture & Optimization Mechanics
- **Centralization = a single optimization target.** One agent means one config, so a skill, model, or prompt improvement is effectively an org-wide deploy. This is the cultural counterpart to Warp's factories-as-code (see the Zach Lloyd entry, same date).
- **Public sessions double as an eval corpus.** Every session is visible, so failure analysis and trajectory mining are free. That data could feed routing decisions or distillation of a cheaper in-house model.
- **Verification agents** (browser click-through video) move trust from reading code to checking behavior. That is how 75% agent-authored code becomes reviewable at scale.

## Grounded Context (Web Enrichment)
Ramp announced external Inspect on 2026-10-27 as an early-access cloud agent that turns Slack, GitHub, Linear, or web tasks into visually validated, reviewed PRs. It also open-sourced an "Open-Inspect" blueprint built on Modal sandboxes ([Ramp blog](https://ramp.com/blog/introducing-inspect), [Modal](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal), [Ramp support](https://support.ramp.com/inspect-overview)). The 75% figure is self-reported and inconsistent across sources: 74% of merged code in one write-up, about 40% in a ZenML summary, and about 60% in January rising to 75% by May ([explainx](https://explainx.ai/blog/ramp-inspect-cloud-coding-agent-launch-74-percent-merged-code-2026), [ZenML](https://zenml.io/llmops-database/building-a-custom-background-coding-agent-for-production-software-development)). Critics note that "75% of PRs" is not "75% of engineering work", since PR size and difficulty vary ([FourWeekMBA](https://fourweekmba.com/ai-ramp-inspect-agent-coding-verification-bottleneck/)).

The talk is also a product launch. The cultural lessons hold up independently. Defaulting to public sessions is the most transferable idea, and it costs almost nothing to adopt.

## Real-World Application / Actionable Step
- **Make your team's agent sessions public by default** (shared channel or a session log store). Pair every perf-optimization PR with its agent transcript and benchmark run, so reviewers can check the methodology, not just the diff.
- **Standardize one baseline agent config** for your research group (shared skills for vLLM profiling, quant eval harness, pruning sweeps). Let individuals fork it, but merge improvements upstream.
- **Mine public sessions** for recurring task types. Those make the first routing-classifier dataset: which tasks a small model handles and which need the frontier model.
