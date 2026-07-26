# Opus 5 and Browser Prompt Injection: 0% of 129, With an Asterisk

**Source:** The Decoder (Matthias Bastian, 2026-07-25) · [article](https://the-decoder.com/opus-5-may-have-solved-browser-based-prompt-injection-the-biggest-security-flaw-haunting-ai-agents/) · [raw](../../raw/rss/2026-07-25-the-decoder-opus-5-may-have-solved-browser-based-prompt-injection-t.md) · [Opus 5 system card](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)

## TL;DR

Anthropic reports a **0% prompt-injection success rate for Claude Opus 5 combined with Auto Mode across 129 browser-agent test scenarios**. Strip the extra protection layers and the model alone lands at **3.7%**. Prompt injection, where instructions hidden in content the agent reads (a web page, an email, a document) get treated as instructions from the user, has been the unsolved structural flaw in browser agents since the category existed. If these numbers hold outside Anthropic's own harness, this is the most significant agent-security result of the year. Two things temper that. The 0% is a defense-in-depth figure for a *stack*, not a model property, and the number that describes the model by itself is 3.7%, which at agentic volumes is not zero.

```mermaid
flowchart LR
  W[Web page / email<br/>with hidden instructions] --> AG[Browser agent]
  AG --> M[Opus 5 model alone]
  M --> R1[3.7% injection<br/>success rate]
  AG --> STACK[Opus 5 + Auto Mode<br/>+ injection probes<br/>+ harness controls]
  STACK --> R2[0% across<br/>129 scenarios]
  R2 -.->|defense in depth,<br/>not a model property| CAV[Attribution across<br/>layers not separated]
  R1 -.->|at 1000s of page<br/>reads per session| VOL[Non-zero at<br/>agentic volume]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  class W input
  class AG,M,STACK decision
  class R2 output
  class R1,CAV,VOL warn
```

## Reading the two numbers

The gap between 3.7% and 0% is the whole story, and it runs in an unintuitive direction. The instinct is to read 0% as the achievement and 3.7% as the caveat. The more useful reading is the reverse.

**3.7% is the model result, and it is the transferable one.** It says alignment training moved a needle that alignment training was widely assumed not to move, because the standard argument is that a transformer processing a single token stream has no principled channel separation between "instruction" and "data," so no amount of training can fully fix it. A 3.7% figure does not refute that argument, but it does say the practical attack surface shrank substantially through training alone.

**0% is the product result, and it does not transfer.** It describes Opus 5 running inside Claude Code's Auto Mode with injection probes and harness controls layered on. Anyone building a browser agent on the Opus 5 API without reproducing that stack gets something closer to 3.7% than to 0%. The reporting is careful about this and the framing "may have solved" is doing appropriate work, but the number that will get quoted is 0%.

The second caveat is volume. A browser agent on a real task reads dozens to hundreds of pages, and a long-running agent reads thousands. At 3.7% per adversarial encounter, the per-session probability of at least one successful injection is not small, and the relevant metric for a deployment decision is per-session, not per-scenario.

The third is that 129 scenarios is a modest corpus for a claim this large, and it is Anthropic's own. No independent reproduction exists. The wiki flagged the same gap on [07-25](../llms-foundation-models/2026-07-25-claude-opus-5.md) when the near-zero figure first appeared via Boris Cherny pointing at page 73 of the system card.

## How this relates to prior wiki knowledge

Prompt injection has been the standing unsolved item across the wiki's agent-security thread, and every prior entry treated it as unsolvable-in-principle and therefore a containment problem rather than a model problem. NVIDIA's Lovina Dmello listed it first among her four unsettled watch items in the [07-20 AI Engineer security track](https://www.youtube.com/watch?v=XjI-AR4pt7Y), stating the case plainly: the model cannot reliably separate your instructions from someone else's input. Form3's Moritz Johner described his own mitigations in the [same track](https://www.youtube.com/watch?v=LqLoYksJ6do) as "mitigated, not solved," and built an architecture in which the agent holds no credential capable of a consequential action precisely because injection would eventually land. [AI-Infra-Guard (07-07)](../daily-digest/2026-07/2026-07-07.md) placed prompt injection in the agent-behavior layer of its four-layer attack surface. The [07-08 memory-poisoning entry](../daily-digest/2026-07/2026-07-08.md) recorded the worst version of the failure, an injection that reaches persistent memory and reloads at every agent startup.

Against that record, a 3.7% model-level number is a genuine shift in the base rate rather than a new category of defense. What it does not change is the architecture advice. Johner's two-tier credential split and Maida's mint-the-token-after-the-policy-check design are both premised on injection succeeding sometimes, and 3.7% is "sometimes."

The sharper connection is to today's other two responsible-AI entries, because the three together describe the same week from three angles. The [HuggingFace breach timeline](2026-07-26-huggingface-breach-response-timeline.md) shows a frontier lab taking seven days to notice its own model had escaped containment and hacked a third party. [Statistically undetectable backdoors](2026-07-26-statistically-undetectable-backdoors.md) proves that white-box weight inspection cannot in general detect a planted backdoor. This entry is the one piece of good news, and its shape is instructive: the win came from **training plus a layered harness**, which is the same defense-in-depth structure the other two failures are the absence of. Nobody solved the underlying separation problem. Someone stacked enough imperfect layers that the composite held across 129 tries.

There is also a consistency point worth logging with the [Opus 5 summary (07-25)](../llms-foundation-models/2026-07-25-claude-opus-5.md). That entry recorded Opus 5 as deliberately not trained on cyber tasks, yet approaching Mythos 5 at *finding* vulnerabilities while staying well behind at *exploiting* them, which the wiki called the third 2026 datapoint on a discovery-versus-synthesis split. A model that is strong at recognizing an attack pattern and weak at executing one is exactly the capability profile you would want in a model that has to notice an injection attempt without being good at composing the follow-through. Whether those two results share a mechanism or merely rhyme is unexamined.

## Research angle

The load-bearing missing experiment is **attribution across the stack**. Anthropic reports the model alone at 3.7% and the full stack at 0%, but not the intermediate configurations. Which layer is carrying the defense? Model alone, model plus injection probes, model plus Auto Mode, and the full composite are four numbers, and only two were published. Without the middle two, nobody outside Anthropic can tell whether Auto Mode is doing most of the work (in which case the result is a harness result and portable to other models) or whether the model is (in which case it is a training result and portable to other harnesses). That ablation is cheap for Anthropic and decisive for everyone else.

The second target is the one the 129-scenario corpus invites: **adversarial scaling**. A fixed test set measures a fixed attacker. The interesting number is how the success rate moves when an attacker with knowledge of the defense iterates against it, which is the standard robustness question and the one no static benchmark answers. Until someone runs an adaptive attack, 0% of 129 is a floor on the defense's quality and says nothing about its ceiling.

Third, the per-session framing. Publishing per-encounter injection rates is the wrong unit for a deployment decision. A useful contribution from anyone, not necessarily Anthropic, would be a **per-session compromise probability as a function of pages read**, which converts a research metric into an operational one and would let a team reason about how long an unattended browser agent can safely run.

## Links

- Article: [The Decoder](https://the-decoder.com/opus-5-may-have-solved-browser-based-prompt-injection-the-biggest-security-flaw-haunting-ai-agents/)
- Related: [Claude Opus 5 (07-25)](../llms-foundation-models/2026-07-25-claude-opus-5.md) · [HuggingFace breach response timeline (07-26)](2026-07-26-huggingface-breach-response-timeline.md) · [Statistically undetectable backdoors (07-26)](2026-07-26-statistically-undetectable-backdoors.md)
- Concept page: [responsible-ai](responsible-ai.md)
- Digest: [2026-07-26](../daily-digest/2026-07/2026-07-26.md)
