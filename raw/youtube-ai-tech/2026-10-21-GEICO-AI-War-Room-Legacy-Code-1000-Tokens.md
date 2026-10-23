# One Day, $1,000 in Tokens: An AI War Room for Legacy Code (Ford Prior, GEICO)

**Channel:** AI Engineer
**Published:** 2026-10-21
**Source:** https://www.youtube.com/watch?v=DouK81O8R3o

## TL;DR
GEICO Claims Tech found that AI had compressed the coding "inner loop" but major changes were still bottlenecked by the "outer loop": getting the right people to make the right decisions with the right facts. They built a multiplayer AI war room (decision makers, one driver, Slack mission channel, design studio, code repos, agent fleets) orchestrated by FleetKit, a markdown rule framework co-built with Anthropic on top of the open-source code-modernization plugin. With a $1,000 one-day token budget per mission, they mapped three legacy claims domains (millions of lines of code) and produced deployable or fully ratified changes. The most useful finding for cost work: Sonnet 5.5 matched or beat Fable on their legacy-code benchmark.

## Key Takeaways
- **Context:** engineers had at most 25% bandwidth for major (V1 to V2) work after patches and minor upgrades. Agents now take patch and minor work spec-to-deploy.
- **Three missions** (uplift / transform / reimagine taxonomy from Anthropic's code-modernization plugin): Rentals extended an existing API and identified ~8,500 avoidable calls/month; Damages and Salvage produced new agent-callable APIs and a ratified migration plan with API specs and mockups. The Salvage work surfaced a real prod bug.
- **FleetKit:** markdown rules and protocols that sit above the system prompt. Takes a goal, dispatches "leader" agents for research and approach, pushes decisions into a human-in-the-loop queue (GitHub issues style), then dispatches "builder" agents. Uses beads for agent task tracking. Output is a "material change" (change request or PR).
- **Human gating via artifacts:** a nine-step process emits HTML worksheets (auto-saved, filled by named owners pinged from a roster) and editable architecture diagrams that agents re-read. Teams kept the diagrams afterward. Questions were high quality, surfacing edge cases nobody had considered.
- **Split of value:** vendor supplies swappable parts (harness, model, FleetKit, plugin). GEICO supplies the non-replaceable parts: context (standards, decision archaeology, tool bindings), methods (skills), and judgment (who decides at which gate).
- **Runtime:** cloud agents did heavy code crunching over legacy DSLs; local agents on the driver's laptop used pre-prod enterprise MCPs via a bindings file.
- **Cost lessons:** do not let a Fable session create crons (each tick spawns a new Fable session and burns budget). Prompt caching hit rates were much higher than expected. Subagent behavior was quirky.
- **Next:** stronger gate enforcement, model-selection decision models in the harness, better context search than flat markdown, and audio transcription of war-room conversation as an input.

## Architecture & Optimization Mechanics
- **Model routing is the hidden headline.** Fable for orchestration and steering, Sonnet 5.5 for builder subagents writing legacy code at equal or better quality. At list prices (~$10/$50 vs ~$2/$10 per M tokens) that is roughly a 5x cost cut on the highest-volume token stream.
- **Prompt caching dominates economics** in this pattern: a large, stable legacy-code and standards context reused across many subagents. High cache-hit rates are structural, not luck.
- **Deterministic gate checks** (did the prior step produce its required artifact files) are a cheap verifier that prevents expensive agents from proceeding on missing state.
- **Failure mode worth noting:** autonomous scheduling by an expensive model. Any self-spawning loop must be pinned to a cheap model or a non-LLM scheduler.
- Prior's claim that FleetKit-style steering needs "Opus 4.8 and beyond" is a speculative capability threshold, not something they measured.

## Grounded Context (Web Enrichment)
GEICO's own tech blog post ("Inside the Fable War Room," adapted from his AI Engineer NYC talk on October 13, 2026) confirms the setup but is more candid than the talk: none of the three missions was a finished end-to-end delivery. Agents got work to a point where engineers took over the last stretch. The blog also swaps the labels relative to the talk (Salvage as transform with new agent-callable APIs, Damages as reimagine needing two extra review days for sign-off), so the "one day" framing does not hold for the reimagine case. The code-modernization plugin is public in Anthropic's official plugin marketplace with a preflight, assess, map, extract-rules, brief, reimagine, transform, harden workflow. FleetKit itself is not open source yet. Third-party benchmarks support the Sonnet 5.5 finding: on Vals AI Code Migration, Sonnet 5.5 scores ~69.8% vs ~55.1% for Fable 5, and ~83.1% vs ~80.5% on Terminal-Bench 2.1, at about one fifth the per-token price. Treat aggregator numbers as directional; Fable 5.1 leads on broader coding indices.

Sources: [GEICO tech blog: Inside the Fable War Room](https://www.geico.com/techblog/inside-the-fable-war-room/), [Code-modernization plugin listing](https://claudemarketplaces.com/plugins/anthropics-claude-plugins-official/code-modernization), [Gradually: Sonnet 5.5 vs Fable 5](https://www.gradually.ai/en/llm-comparison/claude-sonnet-5.5-vs-claude-fable-5/)

## Real-World Application / Actionable Step
- Run the same benchmark GEICO did on your own agent pipelines: use recently merged code as golden data, then compare frontier vs mid-tier model on the builder role. Expect the mid-tier to win on cost-adjusted quality for well-contextualized code generation.
- Use this as a routing case study: planner/orchestrator on the frontier model, executors on the cheaper model, with deterministic artifact checks between steps. Measure cache-hit rate per role; it is the second largest cost lever after model choice.
- Add a hard rule to your harnesses: no self-scheduling or cron creation from frontier-model sessions. Route any periodic check to a small model or plain script.
