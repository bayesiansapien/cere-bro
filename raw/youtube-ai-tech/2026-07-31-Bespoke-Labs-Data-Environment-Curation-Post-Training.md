# Data and Environment Curation for Post-Training LLMs (Mahesh Sathiamoorthy, Bespoke Labs)

**Channel:** AI Engineer
**Published:** 2026-07-31
**Source:** https://www.youtube.com/watch?v=ewtOo0scUh0

## TL;DR
Sathiamoorthy (ex-Google DeepMind, now Bespoke Labs CEO) argues the industry bottleneck for agent post-training is not compute, models, or training infra, all of which are now commoditized. It is data and RL environments, which he treats as the same thing in different shapes. Drawing on the OpenThoughts and OpenThoughts-Agents open datasets, he reports several counterintuitive curation findings: sampling 16 answers to one question beats answering 16 questions once, stronger teacher models are frequently worse teachers, and answer filtering plus synthetic task augmentation largely fail. He also lands a practical enterprise result at Intuit Credit Karma where post-training replaced a bloated compliance prompt, improving compliance, latency, and throughput simultaneously.

## Key Takeaways
- **The bottleneck has moved.** Compute is well defined, good base models exist, and post-training infra is solved by Tinker, Fireworks, and Slime. What enterprises and even frontier labs lack is high-quality data and RL environments.
- **Treat RL environments as data.** Same asset class, different shape. This reframing is what lets the same curation methodology apply to both.
- **Reliability gates autonomy.** Long-horizon agents fail because something breaks at some step (wrong tool, wrong assumption). Prompting and harness changes are levers, but post-training is the durable one and is what frontier labs actually use.
- **Multiple samples per question beat more questions.** For a fixed 10K-sample budget, 16 traces on fewer questions outperforms 1 trace on many. Sathiamoorthy's hypothesis: fine-tuning consumes the reasoning traces, so diversity of reasoning paths per problem is the signal, not breadth of problems.
- **Stronger models are not better teachers.** Confirmed in both the reasoning and the agent line of work. Certain Qwen models outperformed Claude models as trajectory teachers.
- **What did not work.** Answer filtering, synthetic question rewriting, and task augmentation all underdelivered relative to expectation in the agent setting.
- **SFT carries most of the load.** In OpenThoughts-Agents, SFT contributed the bulk of the gains. RL is compute-intensive and bought the last few percentage points. For enterprises specifically, SFT alone is usually sufficient.
- **Credit Karma case study.** The credit card recommendation explanation feature needed a long rules list for compliance, which blew up latency. Naive fine-tuning caused number hallucination (the dataset was saturated with "0% APR", so the model regurgitated it). The fix: replace literal numbers with structural tags in the training pairs, forcing the model to learn the form rather than memorize values. Compliance, latency, and throughput all improved, and Intuit now owns the model instead of renting an increasingly expensive frontier API.
- **Reference stack for agent post-training.** Three layers. Bottom: sandboxes, rollout orchestration, checkpoint/snapshot/rollback for long-horizon runs. Middle: RL environment construction, quality measurement, versioning. Top: SFT, RL, and GEPA-style reflective prompt optimization applied to system prompts and harnesses.

## Architecture & Optimization Mechanics
The tag-substitution trick from the Credit Karma work is the most transferable engineering insight here and it generalizes well beyond compliance text. When a fine-tuning corpus has heavy value imbalance in a slot (one APR value dominating), the model learns the marginal distribution of that slot instead of the conditional mapping. Abstracting the slot to a tag removes the memorizable target and forces the model to learn structure. This is the same failure mode Amit sees in quantized models that collapse to modal outputs, and the same fix applies: strip the high-frequency literal from the supervision signal.

The multi-sample-per-question result has a direct compute implication. Teacher inference is the dominant cost in distillation data generation, and this says to spend it on depth (many rollouts per prompt) rather than breadth. For a distillation budget, that changes the whole generation plan: fewer prompts, higher n, and keep all traces rather than best-of-n filtering, since answer filtering was one of the things that did not help.

The weak-teacher result deserves scrutiny rather than acceptance. It is consistent with the distillation literature on capacity gap, where a teacher too far above the student produces traces the student cannot fit. But the talk offers no controlled evidence separating capacity gap from trace-format mismatch (Qwen traces may simply be stylistically closer to a Qwen student). Before adopting "use a weaker teacher" as policy, run the ablation with teacher and student from different families.

The three-layer stack diagram converges on the same decomposition Ross Taylor presented in the adjacent talk (algorithms, environments, compute), which is a mild signal that the field is settling on this factorization rather than a strong independent confirmation.

## Grounded Context (Web Enrichment)
The OpenThoughts line of work is real and well cited. The paper (arXiv 2506.04178, "OpenThoughts: Data Recipes for Reasoning Models") was accepted at ICLR 2026, produced through four generations starting at BespokeStratos-17K and ending at OpenThoughts3-1.2M and OpenThinker3-7B. The intermediate OpenThoughts-114K spans math (89K), code (20K), science (4K), and puzzles (1K), distilled from DeepSeek-R1. The datasets have been downloaded hundreds of thousands of times and cited by Thinking Machines, Microsoft, Nvidia, Meta, Amazon, and AI2, so the John Schulman name-drop in the talk is accurate rather than promotional. OpenThoughts-Agents launched December 2025.

The commercial context the talk soft-pedals: Bespoke Labs raised $40M in July 2026 specifically to build RL environments for reliable agents, roughly three weeks before this talk. Read the "environments are the bottleneck" thesis with that in mind. It is probably correct, and it is also the pitch.

GEPA, mentioned almost in passing at the end, is worth more attention than the talk gives it. The paper (arXiv 2507.19457) was accepted as an ICLR 2026 oral and reports beating GRPO by 6 points on average, up to 19 points, using up to 35x fewer rollouts, plus beating MIPROv2 by over 10 points. The mechanism is a Pareto front over per-instance top performers combined with natural-language reflection on rollout traces. For anyone whose RL budget is the constraint, 35x fewer rollouts for better results is the more important number in this entire talk.

Sources: [OpenThoughts paper](https://arxiv.org/pdf/2506.04178), [OpenThoughts GitHub](https://github.com/open-thoughts/open-thoughts), [Curator](https://github.com/bespokelabsai/curator), [Bespoke Labs $40M raise](https://bespokelabs.ai/blog/bespoke-labs-raises-40m-to-build-environments-that-enable-reliable-agents), [GEPA paper](https://arxiv.org/abs/2507.19457)

## Real-World Application / Actionable Step
1. **Try GEPA before spending another RL cycle.** 35x fewer rollouts for a 6 to 19 point gain over GRPO is the highest ROI item here. If any part of the routing stack has a tunable system prompt or router policy expressed in text, GEPA optimizes it at a fraction of the RL cost. Start there this week.
2. **Restructure distillation generation toward depth.** On the next distillation run, switch from one trace per prompt across many prompts to n=16 traces across fewer prompts, keeping all traces unfiltered. Cheap A/B, and it contradicts the default best-of-n instinct.
3. **Run the teacher-capacity ablation properly.** Do not just adopt a weaker teacher. Test one strong teacher and one mid-tier teacher, both from a family different from the student, to separate capacity gap from stylistic affinity. The answer determines the teacher budget for every future distillation.
4. **Apply tag abstraction to any imbalanced fine-tuning slot.** Audit distillation and fine-tuning corpora for high-frequency literal values in structured slots. Replace them with placeholders before training. This is a fifteen-minute preprocessing change that prevents a whole class of hallucination.
5. **Note the SFT-first ordering for cost-constrained work.** If SFT captures most of the gain and RL buys the tail, then for internal tooling and enterprise-grade targets the RL infrastructure investment may be premature. Sequence SFT to saturation, measure the residual, then decide whether RL is worth the environment build.
