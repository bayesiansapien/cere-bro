# AI Engineer NYC (Day 3): OpenAI, Blackstone, Ramp, Coinbase, Apollo, Citadel, Basis, Runway, Compute Trading

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=jiUC6IUMdvc

## TL;DR
The full Day 3 livestream of AIE New York 2026: about 25 talks with a finance and compute-markets slant. Three threads matter for Amit. (1) **Compute is becoming a traded commodity.** SemiAnalysis, SF Compute, Jump Trading and Compute Exchange/Silicon Data argue that cost per *useful* token depends on the operator more than the chip, that credit (not power) is the binding constraint for neolabs, and that the GPU forward curve flipped from backwardation to contango in 2026. CME's H100/B200 rental-index futures are the first hedging tool. (2) **Applied labs are doing their own optimization work.** Ramp post-trained a Qwen 3.5 35B retrieval subagent that beats Opus 4.6 at finance QA with lower latency, is testing Cartridges (offline-trained KV caches), runs 10k-agent swarms on open-weight models at about 1/5 the cost, and sells a router. Prime Intellect pitches overnight continual learning in the weights. (3) **Finance trust comes from determinism outside the model.** Kepler's pointer-dereferencing design (the model cannot print a number it did not look up), Basis's behavior specs, Coinbase's "deterministic DAG outside, adaptive loop inside," and Citadel Securities' state-estimator world model all point the same way. Weakest claims: OpenAI's "the data wall is solved" and the Navier-Stokes reference (still unverified), and vendor-survey statistics from Sonar and Jellyfish.

## Key Takeaways
- **Ramp Labs:** LLM use cases grew 123% YoY while per-feature unit costs fell as frontier prices dropped. Three applied-research bets: a specialist post-trained model, Cartridges, and agentic map-reduce swarms. Also "Portal": transfer a LoRA-style post-train latent across model versions and families to amortize post-training cost.
- **OpenAI (ChatGPT for Financial Services):** licensed and self-hosted financial data on its web-index infrastructure instead of relying on flaky third-party MCPs, so it can post-train on that data. Inside OpenAI, Codex's share of finance, legal and recruiting AI output went from about 0 to about 90% between January and June 2026, with the jump tied to the February desktop app, not a model release. Finance-specific post-training is targeting expert-level earnings forecasting in 2027.
- **SemiAnalysis:** same B200s and the same model (8k in, 1k out, 100 tok/s/user target) gave about 200 vs 300 tok/s depending on serving stack and batch settings. That is a 1.5x cost gap per acceptable token on identical hardware. Cost-curve position is relative: improving more slowly than competitors means losing.
- **SF Compute:** credit is hit before power. Lenders underwrite the customer, not the cluster, so neolabs put their whole round into deposits. Without liquid compute markets the industry consolidates TSMC-style and the startup layer disappears.
- **Jump Trading:** compute trades "dark," in bilateral OTC chats. Token prices fell while GPU rental prices stayed firm (Jevons). CoreWeave-style 15 to 25% prepayments mean a Series B raising $40M for a $100M 3-year contract keeps about $10M of runway.
- **Compute Exchange / Silicon Data:** 100+ verified providers and 80k GPUs. The reserved-contract term structure moved from downward sloping (2025) to contango (2026), meaning the market expects prices to rise. H100 residual values are above straight-line depreciation and B200 trades above MSRP on the secondary market.
- **Sonar:** lines of code up 2450% and commits up 240% with async agents, but releases only up 30%. Humans agree with wrong AI output 4 times out of 5 ("cognitive surrender"). LLM judges flip 7 to 17% of verdicts on identical replays and 7 to 34% when asked "are you sure?".
- **Bloomberg (security):** "Rule of two": an agent may have any two of untrusted input, sensitive data and external action. All three requires human sign-off. Real incidents covered: DNS exfiltration from a "no-web" sandbox, Morse-code prompt injection draining a wallet, a malicious npm MCP that behaved for 15 releases and added BCC exfiltration in v16, and an agent that dropped a prod database during a declared code freeze.
- **Jellyfish:** AI spend per developer is up 60x YoY, merged PRs per engineer are up 43%, and cost per merged PR (salary plus tokens) is down 26%. AI is about 2.5% of PR cost on average and 8.5% for the heaviest spenders, who got +67% throughput.
- **Kepler (ex-Citadel):** code writes every number. The model plans and dereferences hashed fact pointers, so it structurally cannot emit an unresolved number. Retrieval is wide, then narrowed: ANN plus BM25 to about 200 docs, then RRF to about 60, then a cross-encoder.
- **Citadel Securities:** an "institutional world model" built as a robotics-style state estimator (update, age, observe, grade, correct). Half of project delivery dates move within 2 months, and 90% of those moves are later dates. Backtest: "green but flagged" projects were 2x as likely to turn yellow or red.
- **Prime Intellect:** treat the model like a codebase. Traces become evals, which become environments, which drive nightly RL runs on idle daytime inference capacity. Routing and "decision models" are the easiest entry point because the labels are cheap.
- **Basis:** "behavior specs" as rubrics over trajectories that have no ground truth, plus trajectory forking and cheap sub-agent "simulations" to debug harness behavior.
- **Runway:** next-frame prediction at scale learns physics. "World interface models" render interactive UIs with no 3D engine. Continuum is a video-model OS with "visual thinking" for coding agents. Most of it is promised within 8 to 12 months.

## Talk-by-Talk Notes

### Ramp Labs: chasing capabilities while waiting for the frontier
- **Specialist model:** Opus 4.6 orchestrating Ramp Sheets was slow and burned thinking tokens on spreadsheet exploration. With Prime Intellect they post-trained Qwen 3.5 35B as a financial-QA/retrieval subagent. It beat Opus 4.6 on exact-task accuracy at much lower latency, and the frontier model stays the orchestrator. This is the planner/executor split Amit routes for.
- **Cartridges:** compress the month-end-close corpus (ledger, aging report, documents) offline into a KV cache, ready before the accountant logs in on day 1. The speaker claims 20 to 30x more context per KV budget and calls it a lower lift than post-training. He expects labs to eventually ship it as API-level continual learning.
- **Swarms:** 10,000 parallel agents pentested all of Ramp, with LLM dedup and adversarial reproduction. They found 7 high-severity bugs, including a Lua injection by email that spanned several components, none of them individually unsafe. Open-weight models at about 5x cheaper lost little detection rate because swarm breadth compensates.
- **Products:** token-spend management (semantic taxonomy of LLM usage, tax credits) and Ramp Router (NVIDIA "Switchyard"-style strategies, flex offloading for latency and cost).

### Sonar: engineering confidence into agentic software factories
- 5% of developers run agentic software factories today and 34% expect to within a year (39% in financial services). The figures come from Sonar's own unreleased survey.
- Agent token cost varies 30x on the same task in large codebases, mostly spent on navigation. Code translation accuracy is 91% at 10k LOC and collapses by 50k.
- Compounding errors: 95% per step over 20 steps gives 36%. METR's 80% horizon is much flatter than the 50% horizon.
- "Code confidence formula" = intent x guide rails x verification x evidence (multiplicative, so any zero gives zero). Their "Vortex" guide-rail product claims -36% tokens and -92% issues per commit. These are vendor numbers.

### Coinbase: trusting agents in policy-driven workflows
- Policy is "the original system prompt." Model the process as a DAG (Airflow) of gated steps, with each node an inner cyclic loop (LangGraph) of work, check and feedback.
- Inject the DAG state into the agent's context so it knows where it sits. "The loop is only as trustworthy as the check."
- Autonomy ramp: supervised, then sampled, then exception-only, gated by measured confidence thresholds. Recipe: deterministic outside, adaptive inside.

### OpenAI: ChatGPT for Financial Services (Joseph Kim)
- Built on the public ChatGPT plugin platform: MCP tools, MCP Apps for charts and citation viewers, skills plus shared artifact tools for Excel and PowerPoint, and firm templates. He predicts "multiple $1B businesses built simply as ChatGPT plugins."
- His analogy: MCP and skills are an instruction manual for a junior analyst. Post-training is a 20-year senior analyst who knows the data's quirks.
- Scaling narrative: pre-training stalled at OpenAI and was fixed in 2026 (GPT-5.6 Sol, GPT-6 Astra). Algorithmic efficiency halves required compute about every 8 months. He says sparse attention and compaction "solved" context length.
- "Threshold phenomenon": utility jumps once review time is much smaller than the time saved, even when capability gains are smooth. His three 2027 bets: Excel and PowerPoint mostly unused for models and decks, persistent AI analysts that feel like coworkers, and models beating top experts at earnings forecasting.

### Bloomberg: real agent security incidents and the fixes
- One agent, one short-lived, audience-bound identity. Agent-to-agent mutual auth so a low-privilege agent cannot recruit a high-privilege one.
- Default-deny egress, including DNS. A deterministic invocation broker outside the model, budgets that halt rather than alert, and circuit breakers.
- Delay ingesting new package versions by a week or two. Memory-integrity checks against "sleeper" instructions planted in documents. Put security requirements in the spec.

### Compound: long-running analysts for buy-side finance
- Multiplayer agents with their own Outlook inbox per deal team. They add deliberate latency so the agent does not spam acknowledgements.
- They rewrote Office from scratch with agents in loops, using real Office as the oracle: 1.5T tokens, about 8M LOC, 800k lines of Rust for the Excel engine. A headless engine lets parallel agents recalculate 20 to 30MB workbooks faster than CPU-bound desktop Excel, and they own the write, render, check, fix loop.
- Breadth: swarms grep a 15k-file data room with no vector DB. Depth: the engine exposes a compact model representation instead of dumping openpyxl output into context.

### SemiAnalysis: "a GPU falls to the level of the operator"
- North-star metric is price per successfully completed task at required quality. Price per token is the practical proxy, and GPU-hours are an input, not output.
- ClusterMAX ratings (provisioning, reliability, monitoring, security) apply to managed clusters, not bare metal. They found a provider whose monitoring exposed another customer's logs.
- Rating the operator is a prerequisite for credible compute-futures grades. A rental-index hedge only works if the index tracks *your* rent. Use the boom (demand exceeding supply for an expected 2 to 3 years) to build cost advantage before the cycle turns, especially if you carry leverage.

### San Francisco Compute: why compute markets must exist
- Physically settled forwards. SF Compute operates the hardware and the order book because "brokering clusters is like reselling a hotel room you can't clean."
- Risk chain: sold out, then lead time, then the whole bank balance as a deposit, then delay (the lender needed the customer first), then breakage with no spare liquidity, then over- or under-buying. AI customers are price-sensitive (thin margins, no lock-in), so clouds demand long take-or-pay contracts.
- Thesis: without markets you get TSMC-style consolidation, and the token supply shifts to investment-grade buyers on 5-year contracts. That ends AI startups.

### Jump Trading: the dark pools of compute
- Physical compute trades as bespoke MSA, SLA and order-form bundles over Slack, X and Telegram. Ambiguous specs (which "memory"?) make it non-fungible.
- IEA: data center electricity goes from 485 TWh (2025) to about 950 TWh (2030).
- Middle-market gap: hyperscalers and frontier labs can sign 10-year deals, while Series B companies cannot. There is a role for balance sheets uncorrelated with the AI cycle (prop shops) to bridge with flex contracts, resale rights and hedges.
- Policy: H200 exports to China moved to case-by-case review in January 2026, and the US AI Action Plan explicitly calls for better compute financial markets.

### Compute Exchange / Silicon Data (Carmen Li)
- Neutral by design (owns no GPUs). It verifies UUIDs and inventory, runs DGX/MLPerf-style benchmarks, does KYB on buyers, and turns requests around in 24 hours. Minimum deal is 1 node for 1 month, up to 3 to 5 years. Buyers can sell back over-commitments.
- "Token forwards": a dedicated deployment with fixed model, quantization and SLA, which hedges on-demand API price volatility.
- Silicon Data indices settle the CME contracts. NVIDIA's September investor-day deck cites them. Banks use the residual-value curves to appraise GPU collateral.

### Enterprise MCP gateway and agent platform (Intuit Karma engineer)
- Pattern: a dev portal provisions a repo plus workload identity, memory DB, eval tables and secrets per agent. All tool calls go through an MCP gateway with JWE tokens and a Redis session, then namespaced MCP servers. Monitoring uses OTel, Tempo, Prometheus and Grafana. PII redaction happens before the LLM, memory DB and traces.
- "Context optimizer" (select, rerank, dedup, compress) cut a query from 24k to 2.4k tokens, with a typical 70 to 78% saving. No answer-quality metric was shown, so treat the number as unverified.

### Leading at Scale (Michelle Brandt): agent trust in M&A integration
- For each agent, decide what it is permitted to do, who owns it, what evidence it records and what triggers escalation. Map these onto the three-lines model.
- Never deploy without a pre-deployment baseline, for example detection time for synergy slippage. A falling override rate can mean review depth has decayed, and only independent sampling tells the two apart.

### Jellyfish: "tokens are the cheap part"
- Heaviest-spend quintile uses about 2.5B tokens/dev/month vs 60M for the lightest. The top 10% of company-months use about 8x the median's tokens for 25% lower cost per PR. Returns diminish but stay positive.
- Reverts did not rise. PRs got larger, not smaller.

### Nori Agentic: cloud agents for a securities master
- The secmaster is "the left side of every join." Private assets (data centers, GPU clusters, private credit) scale complexity linearly per asset and have no price API. Cell-level provenance against contracts in Drive and email is the labor sink.
- Failure mode: inflexible "software factories" that aim for 100% autonomy with no rich human intervention path.

### Blackstone CTO and Norm AI
- Blackstone: get the data story right first, keep straight-through processing, and inject agents only where humans made judgment calls. They explicitly delay some projects six months, waiting for a model that makes them cheaper. Rewriting internal apps is now often cheaper than versioning them forward.
- Norm: tens of thousands of expert-labeled regulatory evals let them rip out hundreds of thousands of lines of scaffolding when agents arrived. Human-owned core primitives, "conduits not dams" for frontier gains.

### Kepler: verification built in, not bolted on
- Three failure sources: wrong document, wrong number from the right document (e.g. 2023 revenue read from a 2025 10-K), and mental math. The fix is pre-processing into hashed fact IDs, deterministic compute, and post-hoc citation checks. Refusals (no pointer resolved) dropped sharply in production.
- Tenant-scoped search is built into the retrieval layer.

### Google: Gemini 4 Argon plus Managed Agents
- Argon: 1M context and up to 1M output tokens, 64k+ thinking budget, $2 in / $10 out. Managed Agents: remote sandbox with the Antigravity harness, skills and AGENTS.md as files, cron triggers (webhooks coming).
- Credential design to copy: a write-only secret store plus an egress proxy that swaps a dummy env-var value for the real credential *only for allow-listed domains*. A prompt-injected agent can then print its env and leak nothing. Hooks are protected files the agent cannot edit.

### Citadel Securities: an institutional world model
- Parse decks with XML plus a vision model together, since neither works alone. Use a feed-forward longitudinal record and never rewrite past months, which enables backtests.
- Treat a silent sensor as missing data, not zero (the dead-speedometer analogy). A specialist multi-agent review pass more than doubled insightful updates vs single-shot "YOLO" over the corpus.

### Prime Intellect (Will Brown): continual learning for the AI-native org
- Today, expert knowledge reaches the weights through a lossy chain: expert network, then RL-environment vendor, then lab researcher. Closing that loop means a customer's own traces and feedback become training data.
- Widget-card UIs for human decisions double as clean labels. An example customer trained a Pareto-frontier knowledge-work model (spreadsheets and slides) for about $300K, which he calls "employee-scale" spend.

### Accessibility in AI-generated code (Jemima Abu)
- In a single experiment (n=1, which she admits), adding an accessibility skill cut agent cost by 58% and time by about 3x, because the agent stopped reimplementing native semantic elements. The mechanism is plausible but the result is not evidence.

### Coder: AI-governance horror stories
- Thesis: LLMs are non-deterministic and do not separate instructions from data, so you lock the infrastructure instead of trusting the model. The stream cut off before the incidents and fixes.

### Apollo / Redding Ridge and Rowspace
- CLO portfolio construction (200 to 400 names against indenture tests) went from 2 to 3 days in Excel to minutes. The weekly warehouse trade reconciliation became an automated, QA-only process. Trust came from forward-deployed engineers mapping which of about 20 sources is the "golden" one.

### Basis: evaluating agent behavior, not just outcomes
- Humans already work with non-deterministic systems, namely their coworkers, and trust comes from process. Coding-style agents push complexity onto users (competency gap) and let individuals invent their own process (process gap).
- Treat agent context as "runtime training data." Behavior specs scale signal far beyond outcome evals. "Nobody wants their agent to move-37 their tax return."

### Runway: world models
- From 128x128 "The Orange" in 2019 to video humans can no longer reliably tell from real (Runway's own measurement). A robotics lab now occupies half the NYC office.

## Architecture & Optimization Mechanics
- **Planner/specialist routing works in production.** Ramp's frontier orchestrator plus a post-trained 35B executor is the cleanest case study of cost and latency routing by subtask type. It also matches Prime Intellect's claim that routing and decision models are the easiest continual-learning wedge: a big-vs-small "was the small one good enough?" judgment produces router labels for free.
- **KV-cache-as-artifact.** Ramp's interest in Cartridges for recurring, schedulable workloads (month-end close) is the right use case. Pay offline compute once per corpus, then serve many sessions with a small cache. This is a compression problem (distilling a long context into a trained cache) squarely in Amit's area.
- **Serving-stack variance exceeds hardware variance.** SemiAnalysis's 1.5x throughput spread on identical B200s comes from software settings and batch concurrency. For anyone benchmarking quantization or kernel work, report cost per *acceptable* token at a fixed interactivity SLO, not peak tok/s.
- **Swarm breadth substitutes for model strength** on recall-type tasks (pentest, data-room review). That is a test-time compute trade-off: N cheap samples vs 1 expensive one, plus an LLM reduce step.
- **Structural anti-hallucination.** Kepler's design is constrained decoding at the semantic level: numbers can only come from dereferenced IDs. It removes numeric hallucination by construction rather than by judge, which matters given Sonar's data that judges flip 7 to 34% of the time.
- **Credential isolation via egress proxy** (Google) and default-deny DNS (Bloomberg) are the two concrete sandbox controls worth copying.

## Market Shifts & Investment Thesis
- **GPU rental prices are rising, not falling.** Silicon Data shows the 2026 forward curve in contango. Independent data agrees: SemiAnalysis-cited one-year H100 leases rose from about $1.70/hr (Oct 2025) to about $2.35/hr (Mar 2026), and reports describe CoreWeave raising prices about 25% in July 2026. That supports neocloud and GPU-lessor cash flows near term and undercuts the "GPUs depreciate in 2 years" bear case for H100-era collateral.
- **Jevons is visible in the data.** Token prices fell while GPU-hour prices held or rose (Jump Trading, A16Z chart). Demand elasticity is outrunning efficiency gains.
- **Credit is the bottleneck.** If SF Compute and Jump are right, the winners are those with investment-grade balance sheets: hyperscalers, NVIDIA as financier, and prop firms entering compute intermediation. Neolab equity gets diluted into deposits.
- **Cycle risk is acknowledged by bulls.** SemiAnalysis explicitly warns that every commodity cycles and leveraged operators with poor cost-curve position will be exposed when supply catches up. They expect 2 to 3 years of visibility.
- **Finance AI is early.** Apollo and Kepler both say most finance AI today formats decks. Real value is in private-markets data plumbing (secmasters, CLO tests, provenance), where vendors such as Rowspace, Nori and Kepler sit.

## Grounded Context (Web Enrichment)
The compute-markets claims mostly check out. CME and Silicon Data announced in August 2026 cash-settled H100 and B200 Rental Index futures on NYMEX: 730 GPU-hours per contract, monthly listings out 36 months, and a target listing date of October 5, 2026, pending CFTC review. Carmen Li said trading would start "in a few weeks," which fits a slip past October 5, though I could not confirm first-day trading or volumes. H100 rental inflation through 2026 is corroborated by several secondary sources. OpenAI's ChatGPT for Financial Services did launch September 10, 2026 on GPT-6 Astra, with Morgan Stanley and Evercore as design partners and Daloopa, PitchBook, LSEG and Crunchbase data, matching Kim's description. Gemini 4 Argon was announced September 30 to a restricted cybersecurity cohort and reached the Gemini app on October 13. The $2/$10 price Philipp quoted appears to be an introductory rate that some sources say will double. Ramp's Prime Intellect spreadsheet model is independently described (a 35B RL-trained subagent beating Opus on spreadsheet search, faster and cheaper than Haiku), and the 10k-agent pentest is attributed to Kimi K2.6 and DeepSeek V4 Pro on Fireworks at about 1/5 the cost. The Cartridges paper (Stanford Hazy Research) reports 38.6x less memory and 26.4x throughput at ICL-level quality, so Ramp's "20 to 30x" is in line, but there is no independent replication yet.

The weaker claims: OpenAI's Navier-Stokes "solution" (September 8, roughly 10k agents over 88 hours with a Lean formalization) has not been accepted by the Clay Institute. One reading says it covers the *forced* case, not the Clay problem, and it comes with a credit dispute with Buckmaster. Kim presenting it as a milestone is marketing. METR's Mythos "16 hours" is a 50% horizon with a 95% CI of 8.5 to 55 hours on only 5 tasks that long, so Sonar's chart is directionally right but noisy. Jellyfish's public H1 2026 data shows the cost-per-PR spread is enormous (about $0.28 to $89 per PR across usage quintiles), and heavy spenders are probably also the better-run orgs. Their "spend more" conclusion is correlational, and a vendor selling spend tracking has every incentive to reach it. In the SemiAnalysis talk's hypothetical, the competitor's cost "falls from 6 to 12," which is a slip: it must fall below 8 for the point to work. Related pages: [[2026-10-12-AI-Engineer-Perpetual-Reliable-Smart-Workflows-Finance]], [[2026-10-12-AI-Engineer-Lethal-Trifecta-Token-Exchange-Keycard]], [[2026-10-12-AI-Engineer-GPU-Neighbor-Side-Channel-MIG-NVLink-Stealthium]], [[2026-10-12-Cerebras-Gimlet-Inference-Token-Demand]], [[2026-10-12-Claude-Managed-Agents-Part1-Brain-Hands]], [[2026-07-31-Applied-Compute-Learning-On-The-Job-Post-Training]], [[2026-09-15-MLST-Ming-Yu-Liu-Cosmos-3-Physical-AI-World-Models]], [[2026-09-27-WorkOS-No-Thats-Not-a-Software-Factory-Ryan-Cooke]].

## Real-World Application / Actionable Step
- **Routing:** copy Ramp's and Prime's pattern. Log every frontier-model call in one high-volume subtask, re-run a 30B-class open model on it, and use frontier-as-judge to label "small was sufficient." That dataset trains your router and is also the RL set for a specialist executor.
- **Cartridges experiment:** pick one static, frequently queried corpus (a paper collection, an internal codebase) and train a cartridge with the Hazy Research self-study recipe on Qwen 3.x. Measure memory, throughput and quality vs full in-context use. It is a natural bridge between KV compression and distillation research.
- **Benchmark hygiene:** when reporting quantization or vLLM wins, state cost per acceptable token at a fixed P50 interactivity target (SemiAnalysis's InferenceX framing). Raw tok/s hides a 1.5x stack effect.
- **Agent security:** adopt the rule of two, default-deny egress including DNS, and proxy-swapped credentials for any research agent with internet and repo access.
- **Portfolio:** treat rising GPU forward curves as supportive for neocloud and GPU-lessor exposure over 12 to 24 months, but size for cycle risk. Watch CME H100/B200 futures open interest and the curve shape as a leading indicator. A flip back to backwardation is the exit signal.
