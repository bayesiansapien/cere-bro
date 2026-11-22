# Google ACHIEVED RSI?! New Stealth Model BEATS Fable 5.2, Anthropic Post IPO, Genie 4 & MORE

**Channel:** WorldofAI
**Published:** 2026-11-20
**Source:** https://www.youtube.com/watch?v=6NT9TsT6iMc

*Secondary domain: finance (Anthropic IPO).*

## TL;DR
A daily AI news roundup. The headline is speculation that Google has "closed the RSI loop": four model releases in two weeks, a small Gemini 4 Neon beating the larger Carbon and Argon, a "Helium" model teased via a periodic-table catalog, and a Google paper on agents that self-improve their own **harness** using persistent memory. The creator overclaims that the leaks "confirm it all". The paper is harness-level optimization, not weight-level RSI. Other items: the stealth model **Gestalt** tops the Frontier Design Benchmark at about 200 Elo above Fable 5.2; **Anthropic's record IPO** ($83 → opened $111.50 → closed $97.17); Genie 4; Grok 4.8 A/B-tested live on X; GPT Live 1.1 with standby; a DeepMind essay on four paths to ASI; and an unconfirmed rumor of a $50B Jensen chip venture.

## Key Takeaways
- **Google cadence:** Gemini 4 Neon (small, "Rev 28" post-training on the "Rev 27" Hydrogen pretrain) reportedly outperforms the medium models Carbon and Argon. Helium (probably a Flash-lite tier) is next. Sergey Brin says Google is "on the RSI treadmill".
- **Self-Improvement Memory paper:** an agent iteratively edits its own tools, prompts, and scaffolding and logs every edit, its rationale, and its effect. The memory approach won 9 of 10 coding runs (+2.36 avg), and harness improvements evolved on Claude Opus transferred to Gemini.
- **Gestalt:** about 1931 Elo on Contra/BenchFlow Frontier Design, 90% win rate. Origin unknown. Candidates are Anthropic (post-IPO flagship), Google, Zhipu, or a Renmin University Gaoling School project of the same name and slogan.
- **Anthropic IPO:** $81.34B base offering plus a $26B private placement → about $104.8B net proceeds. Biggest IPO on record. Lockup expiries in December, January, and February add supply. The creator plans to DCA over 1 to 6 months and cites SpaceX's post-IPO 54% drawdown as precedent.
- **Dario post-IPO:** AI could compress 100 years of science into 10. Anthropic will "pace" training and deployment for safety regardless of business or political pressure, and will move more top researchers to safety.
- **Grok 4.8:** multiple variants are silently A/B-tested via Grokbot on X, with real-usage success fed back into RL. That is a production data flywheel.
- **DeepMind ASI essay:** four paths: scale, new paradigms, coordinating millions of agents, and RSI. Effective compute is growing about 10× per year, so $1B of AI work today costs about $1K in 10 years. Capping training compute would not stop the multi-agent path.
- **Smaller items:** Genie 4 (interactive worlds with native audio and live prompt editing, plus an agent), Antigravity native SSH, GPT Live 1.1 standby mode (cuts idle cost for voice agents), ChatGPT Health on more platforms, Microsoft Canvas (MAI Image 2.7 Flash), DeepSeek Open Motion plugin.

## Architecture & Optimization Mechanics
- **Neon > Carbon/Argon is a post-training story.** A small model on an older pretrain beating larger siblings after a new post-training dataset is evidence that **post-training data quality dominates parameter count** at this tier. That is the distillation and compression thesis in a frontier lab's own lineup.
- **Harness-level self-improvement is cheap RSI.** No gradient updates. The search space is prompts, tools, and control flow, and the memory acts like an optimizer state that persists across models. The cross-model transfer result (Opus → Gemini) is the important one. Harness improvements are partly model-agnostic, but the Opus-evolved harness first *underperformed* Gemini's seed harness, so some re-adaptation is still needed.
- **GPT Live 1.1 standby** is an inference-cost optimization for long-lived sessions. Idle connections no longer burn active compute. Expect the same pattern (KV-cache parking, session hibernation) across real-time serving.
- **10× effective compute per year** combines hardware, algorithmic efficiency, and inference cost declines. Efficiency research (quant, sparsity, better kernels) is a big share of that multiplier.

## Grounded Context (Web Enrichment)
Anthropic priced at $83 on 2026-11-18 and began trading on Nasdaq (ANT) on 2026-11-19. It opened at $111.50, hit $115.10 intraday, and closed at $97.17 (+17.1%) on a day of broad index losses ([FourWeekMBA](https://fourweekmba.com/ai-anthropic-closes-day-one-at-97-17-up-17-from-83-ipo/), [TechRepublic](https://www.techrepublic.com/article/news-anthropic-ipo-nasdaq-trading-debut/), [Al Jazeera](https://www.aljazeera.com/economy/2026/11/19/anthropic-starts-trading-in-the-us-after-blockbuster-ipo)). Valuation depends on share count: about $1.28T basic (the video's figure), about $1.5T at the IPO price including options and RSUs, and about $1.75 to 1.8T fully diluted at the close. One outlet mis-reported the close as $87.17.

Gestalt is confirmed at 1931 Elo against Fable 5.2's 1713, and above human "golden" designs (1739). But on the rubric score it got 83/100 against 84 for Fable 5.2 and Opus 5.5, and Contra has not disclosed its tools, retries, or cost. So "mogging every model" is overstated ([pasqualepillitteri](https://pasqualepillitteri.it/en/news/35144/stealth-model-gestalt-beats-fable-5-2-frontier-design-benchmark), [techbytes](https://techbytes.app/posts/two-stealth-models-just-appeared-on-the-leaderboard-both-ahead/)). The Google harness-memory paper exists in some form. Secondary coverage reports a workspace benchmark rising 68.41 → 84.75 with memory vs 73.42 without, on an Opus-5.5-to-Gemini transfer. It sits alongside related Google work (Harness², RRSI to stop harnesses overfitting their tests), but model versions conflict across write-ups ([FourWeekMBA](https://fourweekmba.com/ai-google-paper-agent-harness-memory-lifts-score-73-4-to-84-8/), [The Decoder](https://the-decoder.com/google-researchers-find-a-way-to-keep-self-improving-ai-agents-from-memorizing-their-tests/)). The "Google achieved RSI" claim rests on an anonymous leaker and release cadence. There is no evidence of weight-level autonomous improvement. Note too that the transcript calls Jensen "former Nvidia CEO", which is unverified, and the $50B venture is pure rumor.

## Real-World Application / Actionable Step
- **Try harness-memory on your own agent workflows.** Keep a structured log of every prompt, tool, or config change to your research agents (kernel tuning, quant sweeps), with its measured effect. Feed it back to the agent as context. It is cheap and transfers across model swaps.
- **Routing/distillation:** use Neon's result as a prior. Before scaling a compressed model's parameters, invest in better post-training data. A small model with frontier-quality post-training can beat a larger sibling.
- **Anthropic stock (finance):** if you want exposure, follow the creator's sound approach. Wait for the December to February lockup expiries and first earnings, then DCA. Do not chase the open.
- **Real-time serving:** if you run voice or agent sessions, implement idle-session KV-cache offload and standby states. That is the GPT Live 1.1 pattern.
