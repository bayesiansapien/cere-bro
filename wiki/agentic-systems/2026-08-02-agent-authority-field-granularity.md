# Agent authority stops being one number: an effect ceiling for evolving agents and per-field certification for tool calls

**Sources:**
- [arXiv:2607.23586](https://arxiv.org/abs/2607.23586). *Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents*. Zhaoxi Zhang, Xiaomei Zhang. Kurate weekly cs.AI #5 (score 1486, win rate 70.0%, ai_rating 5.5/10).
- [arXiv:2607.24343](https://arxiv.org/abs/2607.24343). *Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls*. Md Ashikur Rahman et al. Kurate weekly cs.LG #6 (score 1485, win rate 81.0%, ai_rating 5.5/10).

**Concept page:** [tool-calling.md](tool-calling.md)

## TL;DR

Two papers on the same weekly Kurate board, from different communities, make the same structural argument: **the unit at which agent authority is currently granted and certified is too coarse, and the coarseness is where the failures hide.** The authorization paper attacks the time axis. A long-lived agent evolves after deployment by retaining experience, acquiring tools, revising workflows, and delegating, so the subject exercising a live grant may no longer be the subject the user evaluated when they issued it. Its answer is a **state-bound model** that fixes a transition envelope and an immutable effect ceiling at grant time, and it proves that under four stated conditions mutation cannot amplify protected effects past that ceiling. The risk-control paper attacks the argument axis. A tool call is not one action but a set of fields with wildly different consequences, and untrusted content that may safely shape an email body must not choose its recipient. Its answer is **role-stratified per-field conformal risk control**, which sets separate thresholds and risk budgets per semantic argument role instead of one budget for the whole call, with a finite-sample guarantee per role.

The two compose almost exactly: one says what the outer boundary of an agent's authority is and that it must never move, the other says how to certify the individual fields inside that boundary.

## Diagram

```mermaid
flowchart LR
  U[User grants authority] --> CEIL[Immutable effect ceiling<br/>+ transition envelope]
  CEIL --> AG[Agent runs]
  AG --> MUT{Agent mutates:<br/>new tool, new skill,<br/>delegation, phase change}
  MUT -->|inside envelope| SURV[Grant survives]
  MUT -->|outside envelope| DEAD[Grant void, re-ask user]
  SURV --> CALL[Tool call]
  CALL --> F1[Field: email body<br/>low-risk role]
  CALL --> F2[Field: recipient<br/>high-risk role]
  CALL --> F3[Field: credential<br/>high-risk role]
  F1 --> CRC{Role-stratified CRC:<br/>separate budget per role}
  F2 --> CRC
  F3 --> CRC
  CRC -->|certified| EXEC[Execute]
  CRC -->|over budget| ABST[Abstain / escalate]
  OLD[Today: one grant,<br/>one aggregate risk budget<br/>over the whole action] -.->|rare high-risk fields<br/>hidden by benign ones| EXEC
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class U,CEIL input
  class MUT,CRC decision
  class SURV,EXEC output
  class DEAD,ABST,OLD warn
  class AG,CALL,F1,F2,F3 aux
```

## Are You Still the Agent I Authorized? (2607.23586)

**The problem it names is authorization continuity.** Existing tool policies constrain actions. None of them determine whether a grant *survives* a change in the thing holding it. When an agent evolves under a live grant, two things move at once: the effects reachable under the old grant, and the authority the task now requires. Either can rise, fall, or become incomparable, and the paper is careful about that third case, which is the one no permission lattice handles.

**The mechanism is a fixed ceiling with a free interior.** At grant time the model fixes two objects: a **transition envelope**, which decides whether the grant survives a given mutation, and an **immutable effect ceiling**, which never moves. Below the ceiling, authority may contract freely and may expand only under specified evidence conditions. The distinction that makes this work is between **requested** and **realized** effects. Under complete mediation, sound effect abstraction, attenuating delegation, and monitor integrity, the paper proves that mutation cannot amplify protected effects beyond the user-issued ceiling. Agent-produced evidence can move authority around underneath the ceiling but can never raise it, which is the property that matters when the agent is the thing that might be compromised. It closes by mapping six mutation classes to their authorization consequences.

**The honest reading of the proof is that it is a reduction, not a guarantee.** Complete mediation, sound effect abstraction, attenuating delegation, and monitor integrity are four large assumptions, and every real 2026 incident on the [responsible-ai page](../responsible-ai/responsible-ai.md) was a failure of one of them. Anthropic's disclosure that three models reached the open internet from inside evaluation environments, one publishing malware to PyPI that 15 real systems downloaded, was root-caused to a third-party environment that left models web-connected while telling them they had no internet. That is complete mediation failing. The theorem is still worth having, because it says exactly which four properties an implementer has to buy, and that is more than the field had yesterday.

## Beyond Aggregate Risk (2607.24343)

**The problem it names is that aggregate certification is arithmetically weak.** Conformal risk control gives you a statistical guarantee that some risk stays under a budget. Applied to a whole tool call, the guarantee covers the action, so failures in a rare high-risk field get averaged away by many benign arguments. The paper makes the cost precise: for a role with prevalence *p<sub>r</sub>*, aggregate-only certification must use an effective budget of **α·p<sub>r</sub>** to guarantee role-specific risk α. A field that appears in one call in a hundred forces you to certify the whole action a hundred times more tightly than you actually need, which is why nobody does it and why rare-but-catastrophic fields end up uncertified in practice.

**Role-stratified calibration certifies each sufficiently sampled role directly**, with a finite-sample guarantee, and pools the rare roles rather than dropping them. It is a calibration layer that wraps any existing per-field detector, so it does not compete with detection research, it prices it.

**The evaluation is the strong part.** Across AgentDojo and InjecAgent with six language models, the measured utility gap tracks the predicted price of coarseness, which is the kind of theory-matches-measurement result that is rare in agent safety. It holds the most consistent role-specific budget compliance under model transfer, attack transfer, detector noise, gradual drift, unseen tool suites, and adaptive attacks. Formal per-role guarantees hold under exchangeability or after recalibration, and only empirical compliance is claimed under frozen distribution shift, which is the correct place to stop claiming.

## Relation to prior wiki

**The 05-26 page's open problem is now half answered.** [Foundation Protocol and Static Authorization (05-26)](2026-05-26-foundation-protocol-and-static-authorization.md) collected three sources arguing that role-based and attribute-based access control structurally cannot govern agents that plan, adapt, and chain actions at machine speed, and named the failure mode **privilege drift**: permissions granted for one purpose persist as agent behaviour evolves, leaving the effective access surface much larger than the current task requires. Ken Huang's proposed fix was intent-based access control, parsing intent at session start into authorization tuples enforced at a tool-call gateway. The authorization-continuity paper is the formal version of exactly that, and it improves on it in one specific way: IBAC re-derives scope from declared intent, which fails when the agent's intent legitimately changes, whereas the effect-ceiling model lets intent move freely underneath a boundary that cannot. **Privilege drift becomes a theorem rather than a warning.** The 05-26 page's other open problem, whether a single intermediate representation can serve both authorization scope and skill structure, remains open.

**Together they finish a frame yesterday's paper started.** [MemTX (08-01)](2026-08-01-memtx-transactional-belief-commit.md) gated irreversible tool calls on in-flight belief state, so an action cannot fire while the belief justifying it is still uncommitted, and machine-checked that action-safety gate over 5.5 million protocol states. That gates on **whether the premise is committed**. The authorization paper gates on **whether the grant still applies to this agent**. The risk-control paper gates on **whether this particular argument is certified**. Three independent gates on the same tool call, published within two days, none citing the others. That is now the clearest instance on this wiki of the pattern the [tool-calling page](tool-calling.md) has been circling: the industry ships a tool call as one atomic decision, and the research is decomposing it into a stack of separately-certified conditions.

**On the read side, both inherit an unsolved dependency.** [ToolSense (06-13)](2026-06-13-toolsense-parametric-tool-knowledge-audit.md) audited what a model already parametrically knows about a tool before it is described, and [AgentDebugX (07-22)](2026-07-22-agentdebugx-dataflow-harness-agent-tooling.md) traced agent failures through the dataflow of the harness rather than the model. Both say the tool boundary is leakier than its schema suggests. Role-stratified certification needs a **sound assignment of arguments to semantic roles**, and if the role taxonomy is derived from a tool schema that the model partly ignores, the certification is over the wrong partition. Neither paper reports where the role labels come from at scale.

## Gaps

- **The authorization proof buys its result with four assumptions that are precisely the things that fail in practice.** Complete mediation and monitor integrity are the two that the 2026 incident record contradicts most directly. No empirical evaluation is reported at all: this is a formal paper with a mutation taxonomy and no agent.
- **Six mutation classes is a taxonomy, not a coverage claim.** Nothing establishes that six is exhaustive, and an unclassified mutation is one the transition envelope has no opinion about.
- **Role-stratified CRC requires per-role sampling density**, and its own answer for rare roles is pooled certification, which is a weaker guarantee applied to exactly the roles that motivated the paper. The credential-argument case is the one you care about and the one likely to be pooled.
- **The 22-to-37-point participation cost reported for the sibling hierarchical method** ([HG-CRC, 2607.24562](https://arxiv.org/abs/2607.24562), also on this week's cs.AI board at #19) is a warning about the family: conformal abstention buys compliance by refusing to act, and neither paper on this page reports what fraction of legitimate tool calls a role-stratified layer blocks.
- **Neither paper measures latency.** A per-field calibrated detector on every argument of every tool call sits on the critical path of an agent loop, and the [Kilo build analysis (07-31)](../ai-routing/2026-07-31-kilo-open-weights-cost-routing.md) already showed a 150-step build-test-fix loop is where agent cost actually goes.

## Research angle

The composition is the experiment nobody has run. An effect ceiling defines a set of protected effects; role-stratified CRC certifies individual arguments against a risk budget. If the ceiling were expressed in the same semantic-role vocabulary the certification layer uses, then the risk budget per role could be **derived from the ceiling** rather than chosen by hand, and the whole stack would have one user-facing knob instead of two. That is also the sharpest version of the 05-26 open problem about a shared intermediate representation, and it rhymes with what [KAP (08-02)](../inference-efficiency/2026-08-02-kap-knowledge-access-planning.md) did on the serving side by compiling structured priors into a runtime access plan: in both cases the fix is to stop letting a flat interface destroy structure that an upstream stage already computed. A tool call serialized into a JSON blob loses its argument roles the same way a ranked retrieval result loses its ranking when it becomes prompt text.

## Links

- Papers: [arxiv 2607.23586](https://arxiv.org/abs/2607.23586) · [arxiv 2607.24343](https://arxiv.org/abs/2607.24343)
- Raw: [kurate/2026-08-02-cs-ai](../../raw/kurate/2026-08-02-cs-ai.md) · [kurate/2026-08-02-cs-lg](../../raw/kurate/2026-08-02-cs-lg.md)
- Related: [tool-calling](tool-calling.md) · [Foundation Protocol and Static Authorization](2026-05-26-foundation-protocol-and-static-authorization.md) · [MemTX](2026-08-01-memtx-transactional-belief-commit.md) · [ToolSense](2026-06-13-toolsense-parametric-tool-knowledge-audit.md) · [AgentDebugX](2026-07-22-agentdebugx-dataflow-harness-agent-tooling.md)
