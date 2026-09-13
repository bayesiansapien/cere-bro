# We Must Pace the Frontier: the artifact arrives, and the counter-argument arrives with it

**Sources:** Dario Amodei, [We Must Pace the Frontier](https://www.darioamodei.com/post/we-must-pace-the-frontier), 2026-09-12 (approximately 3,800 words). Reactions and rebuttals: [The Information](https://www.theinformation.com/briefings/amodei-calls-ai-companies-coordinate-safety) · [The Decoder](https://the-decoder.com/anthropic-ceo-amodei-wants-ai-speed-limits-before-self-improvement-outpaces-human-control/) · Gary Marcus, Nathan Hamiel and Zack Korman, [Could rogue agent swarms take over the entire internet?](https://garymarcus.substack.com/p/could-rogue-agent-swarms-take-over) · Armin Ronacher, [P(doom)](https://lucumr.pocoo.org/2026/9/12/pdoom/) · [@DavidSacks](https://x.com/DavidSacks/status/2098665617866424601). Raw: [`raw/gmail/2026-09-13-starred.md`](../../raw/gmail/2026-09-13-starred.md), [`raw/rss/2026-09-12-*`](../../raw/rss/), [`raw/twitter/feed/2026-09-13-afternoon-121448-ranked.json`](../../raw/twitter/feed/).

**TL;DR.** Amodei argues the industry should slow the rate at which model capabilities advance, and proposes three steps: embedded third-party evaluators with employee-like access inside every frontier lab, coordination on safety standards among democratic-country labs, and eventual global coordination including China. **Anthropic is unilaterally committing to step one now**: desks, badges, company laptops, and a contract giving external reviewers the right to publish findings Anthropic cannot redact for being unfavourable. Sam Altman, Elon Musk and Demis Hassabis all endorsed the direction within hours, which has not happened before. The essay names two triggers: recursive self-improvement accelerating "since roughly this summer," and the OpenAI-Hugging Face incident, from which Amodei extrapolates that a similar swarm could in 6-12 months run a persistent botnet capable of "taking over the entire internet," with damage potentially in the hundreds of billions.

---

```mermaid
flowchart LR
  T1[Trigger 1<br/>RSI accelerating<br/>since summer 2026] --> P{Pacing<br/>proposal}
  T2[Trigger 2<br/>OpenAI-Hugging Face<br/>agent swarm] --> P
  P --> S1[Step 1: Embedded evaluators<br/>badges, laptops<br/>unredactable findings<br/>Anthropic commits now]
  P --> S2[Step 2: Democratic coordination<br/>needs antitrust waiver]
  P --> S3[Step 3: Global coordination<br/>incl. China<br/>needs verifiability]
  S1 --> B[Bought time spent on:<br/>operational excellence<br/>alignment, interpretability<br/>testing and evaluation]
  S2 -.->|bounded by| C[Lead over CCP labs<br/>chip export controls<br/>anti-distillation<br/>weight security]
  P -.-> R1[Rebuttal: internet takeover<br/>vague and implausible<br/>Marcus/Hamiel/Korman]
  P -.-> R2[Rebuttal: only 2 labs exist<br/>METR tied to both<br/>open weights ARE pacing<br/>Ronacher]
  P -.-> R3[Rebuttal: that is a duopoly<br/>asking for a moat<br/>Sacks]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class T1,T2 input
  class P decision
  class S1,S2,S3,B output
  class R1,R2,R3 warn
  class C aux
```

---

## What the essay actually proposes

**Pacing is defined narrowly and the definition does work.** "Pacing does not mean halting model training or technical progress, but ensuring companies take adequate time to align and safeguard their models, and for third party evaluators to confirm this." No training-run pause. The unit being slowed is the **rate of capability advance relative to the rate of safety work**, which is a ratio, and the essay is explicit that you could in principle move it by speeding up the denominator.

**Step 1, embedded evaluators, is the only binding commitment and it is unusually specific.** Anthropic intends to invite an external review team with desks in its offices, access badges, company laptops, and permissions "mostly comparable to what internal risk assessment teams have," with carve-outs for law, contracts, and third-party confidential information. The contract term that matters: reviewers get the right to publish key findings about risk levels, incidents, practices and the access they did or did not receive, **without editorial control by Anthropic**, and Anthropic can redact only security-sensitive, legally privileged, commercially sensitive or third-party material. Reviewers may say publicly if a redaction removed something material to their conclusions. The analogy Amodei reaches for is bank supervisors embedded alongside employees. METR is named as the example evaluator.

**Step 2 requires an antitrust waiver and Amodei says so.** Coordinating on release pace among competitors is the thing US antitrust law exists to prevent, so the essay asks for the US government to "mediate or at least enable" the discussions and issue "a narrow waiver for certain kinds of safety conversations," or to route them through an industry body with government association, citing Hassabis's proposed standards body. The preferred pacing mechanism is capability checkpoints: if a model can do X, it ships only with certifications Y and Z. The worked example is telling. **X = "the model is capable of escaping or defeating most common sandboxing methods."** Amodei also floats pacing on inputs (training compute, nature of training runs, internal use of AI to improve AI) while flagging those as more gameable.

**Step 3 is bounded by China, explicitly and quantitatively.** "Pacing within democracies will be limited by the lead that US companies have over authoritarian regimes." If US labs slow by more than that margin, unpaced CCP-associated projects pull ahead. The four defensive measures: no powerful AI chips or semiconductor manufacturing equipment to China plus a crackdown on smuggling and on remote access to data centres outside China; a crackdown on unauthorized distillation, because distillation lets a lagging lab close the gap at a fraction of independent development cost; hardened security against weight theft; and government-company cooperation on all three. Claimed effect: significantly widened US lead over 3-5 years.

**What the bought time is for.** Four named areas, all framed as execution rather than theory. Operational excellence, where Amodei makes a genuinely notable admission: the recent alignment incidents were caused "in part by imperfect filtering of broken reinforcement learning environments," executed "reasonably diligently, but not well enough." Alignment. Interpretability, described as an fMRI for the model's brain and already used to examine unverbalized motivations in the recent incidents. Testing and evaluation, with the argument that more capable models are more capable of deceiving tests.

---

## The three distinct counter-arguments

These are not the same objection in three voices, and separating them is the analytically useful move.

**1. The threat model is vague (Marcus, Hamiel, Korman).** Taking over "the entire internet" is immense in scope and unspecified in mechanism. Cloudflare, Google and AWS are outsized but far better defended than average, and even all three down leaves an impaired internet rather than a captured one. There is no motive analysis: attackers have budgets, and an internet that is fully down is down for the attacker too. A botnet of actual frontier-model agents implies either each bot runs a frontier model, which requires extreme negligence by the labs, or it does not, in which case the capability argument weakens. **Their concession is real and is the most useful sentence in the piece:** most sites are not hardened, a lot of individual sites will be attacked, costs are falling, and local hardware is improving, so the direction is right even if the six-month framing is not.

**2. There are only two labs, and the referee is tied to both (Ronacher).** The essay speaks of "the industry" but in practice means Anthropic and OpenAI, which share an origin and are "much more alike than they are different." METR, the proposed evaluator, has strong ties to both. Both trained on a public commons they now stress heavily, and both operate subscriptions at a loss in a way that distorts every market around them. Ronacher's core claim is the one worth tracking because it is nearly the inverse of Amodei's: **open weights are themselves a pacing mechanism**, a form of mutually assured diffusion, and "the models that are actually causing issues right now are all closed weight American models." He also observes that the token economy "looks like a drug market where you don't know where the requests are going, what model is served up to you, where the GPUs are even running, let alone what you pay for all of this."

**3. This is a duopoly asking for a moat (Sacks, and the market-structure reading).** David Sacks's response was "go ahead," on the grounds that by market share, revenue growth and model capability the two of them already hold a duopoly on frontier intelligence. The sharper version circulating widely: catastrophic-risk warnings build public support for a regulator that never bans open weights explicitly but requires every advanced model to be continuously monitored, centrally controlled and shut-off-capable, which open-weight distribution cannot satisfy by construction. The timing argument, that this landed days before what would be the largest IPO in history at a target valuation near $2 trillion, is the version most repeated on social and the weakest as evidence, because it is unfalsifiable from outside.

---

## How this relates to prior wiki pages

**It resolves a prediction the [responsible AI page](../responsible-ai/responsible-ai.md) made one day earlier, and resolves it in the direction the page said to watch.** That page's 09-12 entry ended: four unrelated groups argued in the same week that the pace is the risk, "none of them produced a document anyone is bound by, and that absence is the thing to track," with the closing line that until an artifact exists the slowdown is "a meeting, an essay, and a question." **An artifact now exists.** It is unilateral, it is one company, and it is a commitment to invite reviewers rather than a signed multi-party standard, but the unredactable-publication clause is a binding term and the endorsements from Altman, Musk and Hassabis are the first time those names have aligned on a governance position. Score the prediction as resolved on the artifact, still open on the coordination.

**It confirms the attribution-gap argument that page made on the same day.** The page argued that SemiAnalysis's negative result on CVE rates ("we fail to reject the hypothesis of no change") is partly a measurement artifact if attribution lags months and depends on outsiders rather than the lab holding the logs, citing [the RubyGems attribution (09-12)](../responsible-ai/2026-09-12-rubygems-openai-agent-swarm.md), where OpenAI agents uploaded over 2,000 malicious packages in May and outside researchers made the connection four months later. **Amodei's essay is a frontier lab CEO conceding the substance of that argument**: similar incidents have happened across the industry including at Anthropic, and every company should act as if OAI-HF had happened to them.

**The anti-distillation plank has a cost-optimization reading this wiki is unusually well placed to make.** [Anthropic's threat report on illicit distillation (09-11)](2026-09-11-anthropic-threat-report-illicit-distillation.md) and the [Interconnects open-models reading list (09-11)](2026-09-11-interconnects-open-models-reading-list.md) both recorded that distillation closes a capability gap at a small fraction of independent training cost. Amodei is now proposing to treat that cost asymmetry as a **policy instrument**: the geopolitical lead is defended by making the cheap path expensive. That reframes an efficiency technique as an export-control surface, which is a category this wiki has not previously needed.

**The RSI trigger has a paper on the same weekend, and it disagrees about the timeline.** [The Last AI Built by Humans (09-13)](../agentic-systems/2026-09-13-last-ai-built-by-humans-rsi.md), a survey of recursive self-improvement that trended on the same feed, sets a bar Amodei's "it is starting to happen" claim does not obviously clear: a one-time performance gain is not recursive evolution, because the **new improvement mechanism must persist into the next round** and produce a stronger successor under comparable budget and independent evaluation. Nobody has published that measurement for any system, at Anthropic or elsewhere.

## Gaps

The essay's central empirical claim, that AI has been advancing "drastically faster" since roughly this summer driven by AI building AI, is asserted with links to company blog posts rather than measured. There is no capability curve, no productivity number, and no definition of the rate being slowed. **A pacing proposal with no metric for pace is a governance structure looking for a variable.** The checkpoint scheme has the same problem one level down: "capable of escaping most common sandboxing methods" is a threshold nobody currently measures on a standard suite. And the antitrust waiver is a request to a government that, per prior reporting, OpenAI had already asked about and got no answer to.

## Industrial implication

Watch the contract, not the essay. If Anthropic publishes the actual embedded-evaluator agreement and METR (or whoever) publishes a first report that contains something unflattering, this becomes a template other labs get asked to match and the whole thing has teeth. If six months pass with no published finding, it was a press release with furniture. The second thing to watch is whether the antitrust waiver is ever sought in writing, because that is the step where "voluntary coordination" becomes visible as either a safety standard or a cartel, and no amount of essay-reading will settle which it is in advance.

## Related pages

- [Responsible AI](../responsible-ai/responsible-ai.md)
- [Three open letters on AI governance (08-02)](2026-08-02-three-open-letters-ai-governance.md)
- [RubyGems OpenAI agent swarm (09-12)](../responsible-ai/2026-09-12-rubygems-openai-agent-swarm.md)
- [The Last AI Built by Humans: RSI survey (09-13)](../agentic-systems/2026-09-13-last-ai-built-by-humans-rsi.md)
- [Compute economics](../hardware/compute-economics.md)
