# How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models (David Abitbol, Revolut)

**Channel:** AI Engineer
**Published:** 2026-10-29
**Source:** https://www.youtube.com/watch?v=Ok6QdZHCcI8

## TL;DR
Revolut (80M customers, EU-regulated bank) serves GLM-5.x to about 2,000 engineers from 56 self-hosted B200s at a blended $0.30 per million tokens, roughly 1/10 of its prior Anthropic and OpenAI spend. Unlimited flat-cost tokens, not better models, produced the big productivity jump: after the April 2026 switch, coding time fell 60% and lead time 70%, versus 20%/10% from Gemini and little measurable gain from budget-capped Claude Code. Over April to August they tuned serving on fixed hardware from TTFT >10s at ~3 RPS to 1.6s at 7+ RPS. Frontier closed models stay available as the exception. This is one of the most concrete public self-hosting case studies so far, and it is directly relevant to Amit's inference and routing work.

## Key Takeaways
- **Budget caps killed ROI.** Engineers spending $1k-10k/month on closed models showed little lead-time gain under strict limits. Flat, unlimited tokens let people use AI for low-value-per-token work (Jira, Confluence, inbox), which is where lead time actually goes. Lead time improved more than coding time.
- **Fleet sizing:** 56 B200 for 2,000 engineers on an ~750B MoE (GLM-5.3). Roughly 36 engineers per GPU.
- **SLOs that matter:** TTFT under 3s (above 5s, complaints flood Slack). Interactivity of ~200 tok/s/user is enough because engineers run parallel tasks and check back; off-peak (after 5pm) users get ~800 tok/s.
- **Tuning result:** same 56 GPUs, TTFT down 88% while demand rose 76%.
- **His parameter list:** cap context at 256k ("long context is a scam"), NVFP4 on Blackwell (claims ~40% footprint saving vs FP8 with no quality loss), TP8 over TP4 even when weights fit on 4 GPUs because KV cache is the bottleneck, prefix-cache hit rate above 90% for coding, plus speculative decoding and prefill scheduling tweaks.
- **Text-only model workaround:** a local router in the harness sends image tasks to a vision model (Gemini or GLM Flash) and keeps GLM as the main brain. "Take the smarter model and solve vision another way."
- **Harness:** OpenAI-compatible Responses API endpoints plugged into OpenCode and Codex.
- **Compliance recipe (EU bank):** coding agents classified as human-in-the-loop, not autonomous, backed by a sandbox with approve/deny command rules (allow grep, deny gradle). Chinese-origin weights hosted in data-equivalency jurisdictions (US, EU, UK, Israel) with zero data retention and strong OpenTelemetry for incident forensics.

## Architecture & Optimization Mechanics
- **KV cache, not weights, sets the parallelism degree.** With a ~40B-active MoE whose weights fit on TP4, going TP8 halves per-GPU weight memory and doubles KV capacity. For coding workloads with long shared prefixes and many concurrent sessions, that buys batch size and prefix-cache residency, which drives TTFT down. This is the core reason the same 56 GPUs absorbed 76% more load.
- **Prefix caching is the hidden multiplier.** Agentic coding resends the same system prompt, repo context and conversation every turn. A >90% hit rate means most prefill is skipped, which is why TTFT, not decode speed, was the tunable bottleneck.
- **Context cap = KV budget.** Serving 256k instead of 1M bounds worst-case KV allocation per sequence and prevents a few long sessions from starving the batch.
- **NVFP4 claim needs a caveat.** He says "FP4 to FP8," but the saving runs FP8 to FP4. "Zero loss" is optimistic. Public GLM-5.3 NVFP4 checkpoints quantize only the routed-expert linears and keep attention, shared experts, embeddings and early dense layers in BF16, which is precisely why the loss is small. Full-model FP4 would not be free.
- **Unit economics:** $0.30/M tokens blended includes idle capacity. SemiAnalysis InferenceX benchmarks GLM-5.3 on B200 near $0.07/M at ~200 tok/s/user, so Revolut is running at roughly 25% of benchmark efficiency, which is normal for diurnal internal traffic. Off-peak capacity is the obvious place to soak up batch jobs.

## Grounded Context (Web Enrichment)
GLM-5.3 launched 2026-08-14 as an open-weight MoE of about 743-753B total and ~39-40B active parameters, native FP8, text-only, with weights released about two weeks later after extra safety review. Its license reportedly changed from GLM-5.2's MIT to a custom GLM-5.3 license, which a regulated bank should check. GLM-5.3-Flash is a separate ~320B/18B-active multimodal MoE, matching the speaker's "GLM Flash" vision fallback. Community and Inferact NVFP4 checkpoints exist (~433-465 GB) using expert-only quantization. Speaker's "800B parameters" is a slight overstatement.

Independent cost analyses agree self-hosting a ~750B GLM pays off only for sustained, high-volume or compliance-bound workloads (one estimate: ~$36k/month for a single node), and that APIs or GLM coding plans are cheaper for spiky use. Revolut fits the profitable case exactly: 2,000 always-on users plus regulatory pressure to control data residency. No independent coverage of Revolut's setup was found, so the 90% saving and productivity numbers are self-reported, and the productivity chart conflates model change with lifting budget caps.

## Real-World Application / Actionable Step
- **Steal the tuning checklist for any vLLM/SGLang deployment:** (1) cap `max_model_len` at the real p99 need, (2) try TP8 vs TP4 and measure KV blocks free and preemption rate, (3) instrument prefix-cache hit rate and target >90% for agentic traffic, (4) FP8 to NVFP4 on expert linears only, then run a held-out eval before declaring "no loss."
- **Routing research opportunity:** Revolut's text/vision split is a crude modality router. The bigger win is a difficulty router between GLM-5.3 and GLM-5.3-Flash (18B active) for routine edits, which could double effective fleet capacity. Quantify it on a coding trace set with accept-rate as the quality signal.
- **Compression experiment:** measure GLM-5.3 quality vs which layers go to NVFP4 (experts only, plus shared experts, plus attention). This mixed-precision sensitivity curve is exactly the kind of result Revolut-style operators need and rarely publish.
- **Fill the off-peak trough:** if Amit runs a shared cluster, schedule eval sweeps and distillation data generation after hours, as Revolut's 800 TPS evening numbers show the capacity is sitting idle.
