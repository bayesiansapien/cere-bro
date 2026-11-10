# Stop Doing Agent Archaeology on Your Team's Code (Richard Feldman, Delta)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=Enn9dVrRXAo

## TL;DR
When code is written through agent conversations, the rationale lives in a private transcript, and handoffs lose it. Teammates and future agents then do "agent archaeology," reconstructing why from commits and copy-pasted chat logs. Feldman demos Delta (from the Zed team), a real-time multiplayer environment where the thread is the unit of work. Agent conversation, code diffs, line comments, @-mentions of teammates, synced terminals and review/approval all live in one replicated thread that any later agent can read. Zed says it has stopped using pull requests internally. This is a product pitch, but the underlying claim is sound: decision context is now a first-class artifact and should be versioned alongside code.

## Key Takeaways
- **The handoff problem:** an issue description, commits and a pasted transcript miss abandoned approaches (often never committed) and the reasoning behind decisions.
- **Agent-aware collaboration:** @-mention a coworker mid-thread, and their reply becomes part of the agent's context. The agent can even suggest who to ask (it recommended checking with Feldman about stale "conversation undo" work).
- **Decision weight is preserved:** future agents can tell whether a choice was deep research or a casual "inline error looks better."
- **Real-time replication:** joining a thread instantly creates a local mirror of the collaborator's repo ("Delta worktrees," lighter than git worktrees). Terminal output syncs read-only, with no remote code execution.
- **Model and harness agnostic:** demoed with Opus 5.5, supports ChatGPT subscriptions, and Claude Code via ACP is coming.
- **Sub-threads** isolate tangents, for example "I'm new to this thread, summarize the approach," without polluting the main thread.
- **No PRs:** CI runs and landing happen from the thread, with an explicit sign-off flow for SOC 2. Stand-ups of 30 to 40 people run in one thread. An on-prem pilot is underway for regulated industries. It is in private beta and pricing is TBD.

## Architecture & Optimization Mechanics
- **CRDT-style replication** (DeltaDB) of conversation plus worktree, building on Zed's multiplayer editor heritage. The thread is the atomic unit of context, and access to a thread equals context transfer to an agent.
- **Context cost tradeoff:** "full context for every future agent" means ever-longer threads. Without summarization or retrieval over thread history, onboarding a new agent into a long thread is a large prefill bill. Prefix caching helps only while threads stay append-only.
- **Sub-threads as context partitioning:** this is the same pattern as sub-agents, keeping side explorations out of the main context window.

## Grounded Context (Web Enrichment)
Zed announced Delta in August 2026 and moved it to public beta with a post titled "Replacing Pull Requests with Delta," which includes a Feldman walkthrough. Zed reports that 33 people landed 570 changes to main after dropping PRs internally. Coverage describes DeltaDB as complementing git and CI rather than replacing them, with desktop apps for macOS, Linux and Windows, browser viewing, and Claude Code as the first third-party integration. The talk said "private beta" while Zed's blog says public beta, so the talk was likely recorded before the switch.

The "kill the PR" claim is dogfooding at one 30 to 40 person company that builds the tool, and it is not evidence that it scales. Open questions: how lock-in-heavy is thread history outside git, how auditors treat thread-based sign-off versus PR records, and whether the transcripts are actually useful to future agents or just noisy. The "context archaeology" pain is real, and competing approaches are converging on the same idea, including agent-trace storage in Warp Factories at the same conference and commit-attached session logs in several coding tools.

## Real-World Application / Actionable Step
- **Capture rationale now, without Delta.** For each compression or routing experiment, have the agent write a short decision log (what was tried, what failed, why the chosen config won) committed next to the code. Negative results, like a failed quantization recipe, are the most valuable and most often lost.
- **Use thread history as eval data.** Stored agent conversations with human corrections are labelled examples of where cheaper models fail. Mine them for routing training data.
- **If you trial Delta**, measure the token cost of onboarding an agent into long threads, and prefer sub-threads plus summaries over replaying full history.
