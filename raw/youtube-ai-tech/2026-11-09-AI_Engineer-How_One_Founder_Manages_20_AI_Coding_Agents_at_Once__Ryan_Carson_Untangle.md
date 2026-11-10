# How One Founder Manages 20 AI Coding Agents at Once (Ryan Carson, Untangle)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=BTtyguoPvBU

## TL;DR
Ryan Carson is a 5x founder now building Untangle, a B2B AI paralegal for family law firms. He runs engineering as an agent hierarchy built entirely from Devin cloud sessions. A human talks, mostly by voice, to an "engineering manager" agent that never writes code. That manager pulls tickets from Linear (one ticket = one PR) and supervises about 20 builder agents (5 to 25 is the workable range). A deterministic 15-minute cron forces the manager to read every child session. Each builder gets up to three review loops and spawns a QA child. A separate merge-queue manager agent coordinates collisions. The human gate is a recorded video of each feature passing its tests. Hiring follows the same philosophy: no screening calls, just screen recordings of candidates operating agents, ranked by an agent, then a paid 16-hour trial.

## Key Takeaways
- **Org chart:** humans (priorities, customers) → manager agent(s), which are plain named sessions → about 20 builders each → a reviewer and a QA child per builder. Each person can run one or two manager sessions.
- **The bottleneck is human attention, not compute.** Past about 25 builders, the human can no longer follow what the manager reports, and things "spin out of control."
- **Don't trust the manager to self-schedule.** Its supervision is non-deterministic, so a scripted automation makes it read every child session every 15 minutes (10 was too often).
- **Never talk to builders directly.** All communication goes through the manager, which answers technical questions and clears small blockers on its own.
- **Review cap:** three builder-reviewer loops at most, then important unresolved bugs escalate to the manager, then to the human.
- **QA agent:** a child of the builder that runs QA. "This is cheap, spin up as many agents as you can," limited only by merge-queue throughput.
- **Video proof:** each builder records the feature working with green or red test results (Devin's built-in "test" feature). The human must watch it on a real screen. He calls this the single gate you can't skip.
- **Agents message each other:** sessions know about each other and coordinate to unblock work. He says the messages are concise and useful.
- **Merge-queue manager:** a dedicated agent that serializes shared resources such as DB migration numbers and orders the queue intelligently, sitting on top of GitHub merge queues.
- **Strong opinion:** "If you're coding locally, stop." Cloud agents are a prerequisite for this kind of parallelism.
- **Hiring pipeline:** an unpaid ~45-minute screen recording of the candidate shipping a PR on their own app with an agent, no instructions given → an agent stack-ranks the videos and transcripts (he overrode its top pick the first time and was wrong to) → the top 5 get a paid fixed-fee 16-hour trial with a Devin seat, NDA and Loom recording → agent-assisted pick → only then a human call.

## Architecture & Optimization Mechanics
- **This is a hierarchical multi-agent control system with a fixed polling rate.** The 15-minute cron is a forced observation step. Without it, supervision in an LLM-managed tree decays because the manager doesn't reliably pay attention to every child. The general principle: put deterministic scaffolding around non-deterministic supervisors.
- **The fan-out limit (about 20 to 25) comes from human bandwidth.** The real limit is the information rate of manager-to-human summaries. Better summarization and filtering of what escalates would let fan-out grow, so it's a compression problem in its own right.
- **Bounded review loops (k=3) cap the cost of each PR.** It's an early-exit rule: stop iterating when the marginal fix rate falls, and escalate the hard cases. That's the same structure as cascade routing, with the cheap path handling most cases and the expensive tier (human) seeing only escalations.
- **The merge-queue manager is a lock and coordination service** implemented as an agent. Deterministic resources (migration IDs) would be better served by a real lock or allocator. Using an LLM there is convenient but fragile.
- **Missing from the talk:** cost per PR, defect escape rate, merge-queue latency. He's honest that the process "will be useless a week from now."

## Grounded Context (Web Enrichment)
Carson has documented this workflow publicly over 2026, though the agent counts vary by venue. He has cited 5 to 10 cloud agents shipping 22 to 40 PRs a day on *How I AI*, said he spent $20k on Devin in a month, and described 15 concurrent Devin agents covering engineering, customer success and investor updates ([How I AI / ChatPRD](https://www.chatprd.ai/how-i-ai/how-ryan-carson-manages-40-prs-a-day-with-devin-and-codex), [Lenny's Newsletter](https://lennysnewsletter.com/p/i-spent-20000-on-devin-in-a-month), [O'Reilly Radar](https://www.oreilly.com/radar/ryan-carson-is-a-one-person-code-factory/), [The Neuron](https://theneuron.ai/explainer-articles/ryan-carson-teaches-greg-isenberg-how-to-run-an-ai-software-factory/)). The "20 per manager" figure in this talk is the largest he has claimed, and it's anecdotal. He also has an obvious affinity with Devin, which hosted much of his earlier content.

The architecture is not new (manager/worker, bounded critique loops, a serialized merge queue). What it adds is a practitioner's calibration: a 15-minute polling interval, three review loops, about 20 builders, and video as the human gate. The hiring approach is untested at scale. It favors people who already maintain a public or side app, and an agent ranking recorded candidates raises bias and legal (EEOC/AI-hiring audit) issues, which he doesn't address.

## Real-World Application / Actionable Step
- **For your own research engineering:** set up a manager session plus 5 to 10 builder sessions for experiment sweeps (one ticket = one config/ablation). Add a scheduled forced-read of all children, rather than trusting the manager to poll.
- **Cap critique loops at 3** in any agentic pipeline you build, and log the escalation rate. That rate is your quality-routing signal.
- **Routing research angle:** treat "manager → builder → reviewer → human" as a cost cascade and measure the escalation fraction at each tier. It's a real-world dataset for learned deferral policies.
- **Replace LLM coordination of deterministic resources** (IDs, locks, GPU slots) with actual allocators. Keep the agent for judgment calls only.
