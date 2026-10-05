# We Built an AI Support Agent That Resolves 80% of Tickets (AssemblyAI)

**Channel:** AI Engineer
**Published:** 2026-10-04
**Source:** https://www.youtube.com/watch?v=pyvRID_CZZU

## TL;DR
Matt Lawler, a forward deployed engineer (FDE) at AssemblyAI, describes "Joey," an in-house support agent built on the Claude Agent SDK that replaced an off-the-shelf docs bot. With about 1,000 API signups a day and one onboarding engineer, the vendor bot resolved only 10% of conversations and could not be tuned (no access to prompt, tools or RAG). Joey reached 80% end-to-end resolution in its first week for about $700 a month in tokens plus infrastructure, and now also speaks via AssemblyAI's own Voice Agent API. The real lesson is ownership of the stack and iteration speed, not model magic. The 80% figure is plausible but self-reported, and the metric definition deserves scrutiny.

## Key Takeaways
- **Off-the-shelf failed on control, not capability:** 10% resolution, and every fix was "on the roadmap." Owning the prompt, tools and retrieval was the unlock.
- **Architecture, four parts:** (1) all docs, changelog and pricing pages synced as local Markdown on every docs deploy, with source URLs for citation; (2) Voyage embeddings for first-pass retrieval; (3) agentic file-system search (grep and read) as fallback when retrieval is insufficient or answers need multiple sources; (4) Dockerized and deployed on Railway, about 30 seconds from PR to live.
- **Instructions as the main lever:** a very large CLAUDE.md of guardrails (claimed "30,000 lines") updated after every bad conversation. Fixes have been shipped mid-conversation.
- **Agent, not chatbot:** file system, code writing and debugging, tool calls, memory of past conversations via Pylon (the support platform that also tracks his metrics).
- **No cherry-picking claim:** every inbound channel hits Joey first; humans only reachable via Joey escalation. 20% escalated for legitimate reasons (rate changes, data opt-outs, legal agreements).
- **Escalations as a roadmap:** each escalation category becomes the next automation (a BAA link, then self-serve pricing quotes and negotiation).
- **Voice mode:** speech-in, speech-out over one websocket (STT, LLM, TTS), with barge-in and turn-taking handled. Dogfooding the product customers build on.
- **FDE thesis:** automate yourself out of the job; build what your customers build to earn empathy for latency and turn-taking problems.

## Architecture & Optimization Mechanics
The retrieval design is a two-tier cascade worth noting: cheap dense retrieval answers most queries quickly, and only hard or multi-hop queries escalate to agentic file-system search, which costs many more tool calls and tokens. That is query routing by difficulty applied to retrieval rather than model choice, and it is likely why $700 a month covers roughly 1,000 conversations a day (on the order of $0.02 per conversation, which implies heavy prompt caching or a mostly small-model path; the talk does not say which model).

The weak spot is the "30,000-line CLAUDE.md." At typical line lengths that is several hundred thousand tokens, which either exceeds the context window or dominates per-call cost and invites lost-in-the-middle failures. Most likely the figure counts the synced docs, or the instructions are loaded selectively. Either way, accreting a guardrail per bad conversation is the "accidental architecture" pattern: it works at first and degrades as rules conflict. A per-category eval set tied to each escalation reason would make the iteration loop measurable instead of anecdotal.

## Grounded Context (Web Enrichment)
80% is good but not exceptional in 2026. Intercom reports Fin's average resolution rate at 76% across 12,000 customers, with top performers at 80% to 84%, and notes that Fin itself started at 23%. The pattern Intercom reports, that resolution tracks the completeness of the knowledge base, matches AssemblyAI's jump: the vendor bot likely had stale or partial docs, while Joey syncs the full docs on every deploy. Caveat on the metric: "resolved with no human" usually means "not escalated," which counts users who gave up as successes. Intercom itself moved from "resolutions" to "outcomes" billing for this reason. AssemblyAI did not report CSAT or reopen rates.

The supporting products check out. AssemblyAI launched the Voice Agent API in May 2026 at a flat $4.50 per hour covering STT, LLM, TTS, turn detection and tool calling, around 1 second end-to-end latency. Voyage AI is owned by MongoDB (acquired February 2025, about $161M), and its Voyage 4 family (including an open-weight voyage-4-nano) is now integrated into MongoDB Atlas. A daily.dev listing confirms the talk; there is no independent write-up of Joey's metrics.

Sources: [daily.dev talk listing](https://daily.dev/posts/we-built-an-ai-support-agent-that-resolves-80-of-tickets-assemblyai-9atuibku9), [Intercom: resolutions to outcomes](https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/), [AI support resolution benchmarks 2026](https://www.lorikeetcx.ai/articles/resolution-rate-ai-customer-support-benchmarks-2026), [Introducing AssemblyAI Voice Agent API](https://www.assemblyai.com/blog/introducing-our-voice-agent-api), [Voice Agent API $4.50/hr](https://blockchain.news/news/assemblyai-voice-agent-api-launch), [MongoDB acquires Voyage AI](https://investors.mongodb.com/news-releases/news-release-details/mongodb-announces-acquisition-voyage-ai-enable-organizations), [Voyage 4 models](https://www.mongodb.com/company/newsroom/press-releases/mongodb-sets-a-new-standard-for-retrieval-accuracy-with-voyage-4-models)

## Real-World Application / Actionable Step
- **Steal the retrieval cascade for routing research:** dense retrieval first, agentic search only on low-confidence queries. Measure the fraction escalated and tokens per tier; it is a clean testbed for difficulty-aware routing policies.
- **Replace "resolution rate" with outcome metrics** in any agent you evaluate: reopen rate within 7 days and post-conversation CSAT, otherwise silent abandonment inflates the number.
- **Cap instruction-file growth:** if you maintain agent instruction files (including this wiki's CLAUDE.md), pair every new rule with a regression example and prune conflicting rules periodically, rather than accreting guardrails.
- **Cost benchmark to remember:** a capable docs-grounded support agent at about 1,000 conversations a day for roughly $700 a month is the bar any in-house or vendor quote should be compared against.
