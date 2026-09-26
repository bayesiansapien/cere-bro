# HUGE AI NEWS: GPT-6 Sol & Luna, Opus 5.5, Sonnet 5.5, Haiku 5.5, Qwen 4.0, & Trump To Change AI!

**Channel:** WorldofAI
**Published:** 2026-09-23
**Source:** https://www.youtube.com/watch?v=GJIkBVSoxUw

## TL;DR
The week of 22 September 2026 was about price, not intelligence. OpenAI's GPT-6 Sol and Luna halve prices relative to GPT-5.6 while landing **flat** on the Artificial Analysis Intelligence Index. Anthropic's Opus 5.5 delivers Fable-class capability at 20% lower list price, with Sonnet 5.5 and Haiku 5.5 confirmed for the coming weeks. Alibaba named four Qwen 4 tiers (Max, Plus, Flash, 27B), but they are still in training, with a 5 to 10T-parameter roadmap for Qwen 4.5/5. Tencent's HY Image 3.5 preview costs 2 cents per image. Trump told the UN that US government documents will now call AI "super intelligence." The creator's own framing is correct: frontier labs are competing on cost per unit of intelligence now, which is exactly the regime where routing earns its keep.

## Key Takeaways
- **GPT-6 Sol:** $2 / $10 per MTok (was $4 / $20 for GPT-5.6 Sol). On AutomationBench at xhigh effort it beats Opus 5 at max for about 9% of the cost per task. AA cost per Intelligence Index task falls from $1.99 to $1.06.
- **GPT-6 Luna:** $0.10 / $0.50 (was $0.20 / $1.20, so output fell 58%, more than half). About 5.4 points better than its predecessor at high effort and 58% cheaper per task. AA cost per task falls from $0.18 to $0.07.
- **Intelligence is flat.** AA puts GPT-6 Sol within 1 point of GPT-5.6 Sol, with gains on some evaluations and regressions on others. This is a distillation and efficiency release branded as a generation bump.
- **Hallucination drop is mostly abstention.** Sol's hallucination rate fell from 92% to 60%, Luna's from 93% to 77%. But Sol now attempts only 83% of questions (vs 99%), and accuracy fell from 59% to 54%. It is more calibrated, not more knowledgeable.
- **Opus 5.5 vs Sol head-to-head** (AIML API, four one-shot 3D scenes): Opus cost $4.37, Sol about $0.34, a roughly 13x gap. Opus output is visibly richer. On a NYC three.js prompt Sol emitted a single static frame with no render loop. Sol closes the gap with more detailed prompting.
- **Anthropic:** Sonnet 5.5 and Haiku 5.5 officially confirmed "in the coming weeks." Claude users received a one-time rate-limit reset, expiring around 22 October. OpenAI's Codex offered a similar banked reset.
- **Qwen 4:** Max, Plus, Flash and 27B were announced at Apsara on 22 September. No weights, prices, dates or benchmarks. The 5 to 10T target is for Qwen 4.5/5, not Qwen 4. The creator presents these as imminent. They are not.
- **HY Image 3.5 preview (Tencent):** 30% higher human-eval win rate vs HY Image 3.0, up to 2K output, $0.02 per image, reference images free.
- **Trump "SI":** after an X poll ("superior intelligence" won with 52% of 184K votes), he told the UN on 22 September that US documents will use "super intelligence," and that the US will "encourage it, not rein it in." Breaking Defense reports the terminology change is now ordered across agencies.

## Architecture & Optimization Mechanics
The GPT-6 Sol/Luna release is a clean example of **frontier compression as a product line**: the same intelligence at half the serving cost. OpenAI has not disclosed the method, but a flat capability score with a ~50% cost cut and a large behavioral shift toward abstention fits distillation from GPT-6 Astra plus post-training calibration. It could also be a smaller or sparser serving footprint (quantization, more aggressive MoE sparsity). Two points matter for Amit:

1. **Cost per task, not cost per token, is the metric that moved.** Sol's AA cost per task nearly halves, in line with the list price cut, so token efficiency stayed roughly constant. Opus 5.5 behaves differently: price per token fell, but at max effort tokens per task rose. Routers that price on per-token rates will misrank these two models.
2. **Abstention changes the router contract.** A model that declines 17% of the time is a different kind of component from one that answers 99% of the time. For cascades, abstention is a useful escalation signal: a Sol refusal is a free, calibrated trigger to escalate to Opus 5.5 or Astra, without needing a separate confidence estimator.

The emerging price ladder, per MTok input/output: Luna $0.10/$0.50, MiMo-V2.6-Pro $0.43/$0.87, Sol $2/$10, Opus 5.5 $4/$20. That spans 40x on output. With four models at clearly separated price points, a learned router has plenty to exploit.

## Grounded Context (Web Enrichment)
Artificial Analysis's own write-up, "GPT-6 Sol and Luna push the cost efficiency frontier," confirms the video's pricing and hallucination numbers and adds the key caveat the creator skips: the hallucination improvement comes from the model declining more often, and raw accuracy regressed 5 points. Heise and DataCamp describe the release the same way, as prices halved with performance nearly unchanged. The creator's instinct that he "expected more" is correct and well founded.

On Qwen 4, Pandaily and CellCog both stress that Alibaba's press release says the family is "currently in training," with no date. The video's excitement about a local 27B "on par with frontier" is speculation. On Trump, The Hill, Fox and Breaking Defense confirm the UN remarks and the agency-wide terminology order. The practical confusion, flagged by several outlets, is that "superintelligence" already means ASI (smarter than any human) in the research community. Federal documents using "SI" for today's systems will muddy policy language, including any future compute-threshold or frontier-model rules. PBS's fact-check of the speech also notes his dismissal of AI-risk concerns, which fits the "encourage, not rein in" stance.

## Real-World Application / Actionable Step
- **Rebuild your router's cost table this week.** Add GPT-6 Luna ($0.10/$0.50) as the floor tier and Sol ($2/$10) as the mid tier. Measure cost per *task* on your own eval set at each effort level instead of relying on list price.
- **Use Sol's abstention as a routing signal.** Build a two-stage cascade: Sol at xhigh first, and escalate to Opus 5.5 only on explicit abstention or verifier failure. Measure what fraction of Opus-quality answers you retain versus Opus-only cost. The AutomationBench result (Sol at 9% of Opus 5's cost) suggests a large saving.
- **Do not plan around Qwen 4 27B yet.** Keep Qwen 3.x and MiMo-V2.6-Flash as your local compression and quantization testbeds until weights actually ship.
- **Policy watch:** if you write grant, compliance or public-sector documents, expect US federal usage of "super intelligence (SI)." Keep precise terms (LLM, frontier model) in technical writing so it is not conflated with ASI.

## Sources
- [Artificial Analysis: GPT-6 Sol and Luna push the cost efficiency frontier](https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier)
- [heise: GPT-6 Sol and Luna, OpenAI halves prices](https://www.heise.de/en/news/GPT-6-Sol-and-Luna-OpenAI-halves-prices-11463147.html)
- [DataCamp: GPT-6 Sol and Luna](https://www.datacamp.com/blog/gpt-6-sol-and-luna)
- [Pandaily: Qwen4 family in training, 5 to 10T roadmap](https://pandaily.com/alibaba-qwen4-training-roadmap-5-10t-apsara-2026)
- [CellCog: Qwen 4 in training, no date](https://cellcog.ai/blog/qwen-4-release-date/)
- [The Hill: Trump seeks to rename AI "super intelligence"](https://thehill.com/homenews/administration/6104142-trump-renames-ai-super-intelligence/)
- [Breaking Defense: agencies ordered to use "super intelligence"](https://breakingdefense.com/2026/09/trump-orders-all-us-agencies-to-refer-to-ai-as-super-intelligence/)
- [PBS: fact-checking Trump's 2026 UNGA speech](https://www.pbs.org/newshour/politics/fact-checking-trumps-speech-to-the-2026-united-nations-general-assembly)
