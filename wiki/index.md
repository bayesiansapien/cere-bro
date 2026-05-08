# Wiki Index

Catalog of all pages. Updated on every ingest.

---

## agentic-systems

| Page | Summary |
|------|---------|
| [gui-agents.md](agentic-systems/gui-agents.md) | Concept: MLLM-based GUI agents, long-horizon challenges, key papers |
| [agent-benchmarks.md](agentic-systems/agent-benchmarks.md) | Concept: benchmarks for agentic AI — OccuBench, GameWorld, MERRIN, explore/exploit |
| [2026-04-16-ui-copilot.md](agentic-systems/2026-04-16-ui-copilot.md) | UI-Copilot: memory decoupling + TIPO for long-horizon GUI tasks |
| [2026-04-16-trex-llm-finetuning-automation.md](agentic-systems/2026-04-16-trex-llm-finetuning-automation.md) | TREX: multi-agent LLM fine-tuning automation via search tree |
| [2026-04-16-exploration-exploitation-lm-agents.md](agentic-systems/2026-04-16-exploration-exploitation-lm-agents.md) | Measurable explore/exploit errors in LM agents |
| [2026-04-16-occubench.md](agentic-systems/2026-04-16-occubench.md) | OccuBench: 100 professional task scenarios via Language World Models |
| [2026-04-16-do-ai-coding-agents-log-like-humans.md](agentic-systems/2026-04-16-do-ai-coding-agents-log-like-humans.md) | AI coding agents fail logging instructions 67% of the time |
| [2026-04-16-defenseclaw-maestro-agentic-security.md](agentic-systems/2026-04-16-defenseclaw-maestro-agentic-security.md) | DefenseClaw: security control plane for OpenClaw + MAESTRO threat model |
| [2026-04-16-vakra-agent-reasoning-failure-modes.md](agentic-systems/2026-04-16-vakra-agent-reasoning-failure-modes.md) | VAKRA: tool-use failure modes in agents |
| [2026-04-17-claude-code-architecture.md](agentic-systems/2026-04-17-claude-code-architecture.md) | Claude Code v2.1.88 architecture: while-loop core + 5 surrounding systems |
| [2026-04-17-superlocalmemory-agent-memory.md](agentic-systems/2026-04-17-superlocalmemory-agent-memory.md) | SuperLocalMemory V3.3: biologically-inspired local agent memory with forgetting curves |
| [2026-04-25-claude-code-memory-systems-chapter8.md](agentic-systems/2026-04-25-claude-code-memory-systems-chapter8.md) | Claude Code memory systems (Chapter 8): QueryEngine eager flush + LRU cache + path-set dedup; Apr 23 postmortem caching bug analysis |

## llms-foundation-models

| Page | Summary |
|------|---------|
| [rl-for-llms.md](llms-foundation-models/rl-for-llms.md) | Concept: RL for LLMs — RLHF, RLVR, PreRL, and reasoning model training |
| [2026-04-16-prerl-rl-in-pretrain-space.md](llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md) | PreRL/DSRL: RL in pre-train space bypasses base model ceiling |
| [2026-04-16-open-vs-closed-models-mid-2026.md](llms-foundation-models/2026-04-16-open-vs-closed-models-mid-2026.md) | Nathan Lambert's 13 bets on open vs. closed models mid-2026 |
| [2026-04-16-infinitesciencegym-benchmark.md](llms-foundation-models/2026-04-16-infinitesciencegym-benchmark.md) | InfiniteScienceGym: procedurally generated scientific analysis benchmark |
| [2026-04-24-gpt-55-launch-system-card.md](llms-foundation-models/2026-04-24-gpt-55-launch-system-card.md) | GPT-5.5: first OpenAI pre-train since GPT-4.5; $5/$30 per M tokens; perfect reversion 0.18→0.52; SemiAnalysis switched daily driver |
| [2026-04-24-deepseek-v4-architecture.md](llms-foundation-models/2026-04-24-deepseek-v4-architecture.md) | DeepSeek V4: 1.6T/49B MoE on Huawei Ascend 950PR; CSA/HCA -73% FLOPs; Engram O(1) factual retrieval; cache costs -90% |
| [2026-04-28-hope-nested-learning-architecture.md](llms-foundation-models/2026-04-28-hope-nested-learning-architecture.md) | Hope/Nested Learning: Self-Modifying Titans replace attention; Continuum Memory replaces FFN; multi-timescale in-context adaptation |
| [2026-05-02-compliance-vs-sensibility-reasoning-controllability.md](llms-foundation-models/2026-05-02-compliance-vs-sensibility-reasoning-controllability.md) | Reasoning types (induction/deduction/abduction) resist instruction override; linearly encoded layers 16-24; mechanistic intervention +29% compliance |
| [2026-05-02-safety-drift-fine-tuning-high-stakes.md](llms-foundation-models/2026-05-02-safety-drift-fine-tuning-high-stakes.md) | Benign fine-tuning causes heterogeneous, contradictory safety changes across 100 deployed models; base-model evals predict nothing about fine-tuned variants |

## multimodal

| Page | Summary |
|------|---------|
| [2026-04-16-seedance-2-video-generation.md](multimodal/2026-04-16-seedance-2-video-generation.md) | Seedance 2.0: unified audio-video generation with 4 input modalities |
| [2026-04-16-rationalrewards-visual-generation.md](multimodal/2026-04-16-rationalrewards-visual-generation.md) | RationalRewards: critique-before-score reward models for visual generation |
| [2026-04-16-gameworld-multimodal-game-agents.md](multimodal/2026-04-16-gameworld-multimodal-game-agents.md) | GameWorld: 34-game benchmark for MLLM game agents |
| [2026-04-16-merrin-multimodal-retrieval.md](multimodal/2026-04-16-merrin-multimodal-retrieval.md) | MERRIN: multimodal web retrieval benchmark; avg accuracy 22.3% |
| [2026-05-02-vipo-visual-preference-optimization.md](multimodal/2026-05-02-vipo-visual-preference-optimization.md) | ViPO: 1M image + 300K video preference pairs; Poly-DPO collapses to DPO on clean data |
| [2026-05-02-semi-dpo-noisy-preferences.md](multimodal/2026-05-02-semi-dpo-noisy-preferences.md) | Semi-DPO: treats conflicting DPO preference labels as noisy unlabeled data; iterative pseudo-labeling |

## inference-efficiency

| Page | Summary |
|------|---------|
| [knowledge-distillation.md](inference-efficiency/knowledge-distillation.md) | Concept: knowledge distillation, on-policy distillation, cross-tokenizer BLD |
| [kv-cache.md](inference-efficiency/kv-cache.md) | Concept: KV cache — context dependency, reuse, compression, eviction |
| [2026-05-02-nemotron-3-nano-omni-multimodal.md](inference-efficiency/2026-05-02-nemotron-3-nano-omni-multimodal.md) | Nemotron 3 Nano Omni: 30B multimodal with native audio; token-reduction for lower latency; FP4/FP8/BF16 released |
| [2026-05-02-flashrt-efficient-red-teaming.md](inference-efficiency/2026-05-02-flashrt-efficient-red-teaming.md) | FlashRT: 264GB → 65GB, 1hr → 10min for optimization-based red-teaming at 32K context |
| [2026-04-16-tip-token-importance-on-policy-distillation.md](inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) | TIP: two-axis token importance taxonomy; 47% memory reduction |
| [2026-04-17-kv-packet-recomputation-free-kv-cache.md](inference-efficiency/2026-04-17-kv-packet-recomputation-free-kv-cache.md) | KV Packet: soft-token adapters for zero-recomputation KV cache reuse |
| [2026-04-17-cross-tokenizer-distillation-byte-level.md](inference-efficiency/2026-04-17-cross-tokenizer-distillation-byte-level.md) | Byte-Level Distillation: bytes as universal cross-tokenizer interface |
| [2026-04-17-model-capability-dominates-inference-time.md](inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md) | AIMO 3: model capability 4x > prompt-level optimization; gap is selection not prompting |

## ai-routing

| Page | Summary |
|------|---------|
| [llm-routing.md](ai-routing/llm-routing.md) | Concept: LLM routing — surrogate models, parity gates, open problems |
| [2026-04-17-tracer-llm-routing.md](ai-routing/2026-04-17-tracer-llm-routing.md) | TRACER: trace-driven surrogate routing; 100% coverage on 150-class benchmark |
| [2026-05-01-ken-huang-ch14-routing-provider-abstraction.md](ai-routing/2026-05-01-ken-huang-ch14-routing-provider-abstraction.md) | Ch 14: Claude Code compile-time static routing vs Hermes runtime dynamic routing; fallback chains; stripSignatureBlocks; per-turn cheap routing |
| [2026-05-02-step-level-optimization-computer-use-agents.md](ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md) | Step-level cascade: Stuck + Milestone monitors escalate to frontier model only at high-risk junctures; modular, no retraining |

## hardware

| Page | Summary |
|------|---------|
| [gpu-kernels.md](hardware/gpu-kernels.md) | Concept: GPU kernel optimization, accelerator-specific tuning, NKI, memory hierarchy, AccelOpt, Nemotron, goodput |
| [2026-04-21-semianalysis-gpu-cluster-goodput.md](hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md) | SemiAnalysis: gold vs silver tier neoclouds differ 6–21% in goodput; fault-tolerance tooling is fragmented and immature |
| [2026-04-27-semiconductor-week17.md](hardware/2026-04-27-semiconductor-week17.md) | Semiconductor Week 17: AI memory supercycle, agentic RISC-V CPU design, TSMC A13, AI-driven EDA N-of-3 pattern |

## ai-industry

| Page | Summary |
|------|---------|
| [2026-04-17-claude-market-share-surge.md](ai-industry/2026-04-17-claude-market-share-surge.md) | Claude doubles market share in a month; Gemini reaches 25% AI traffic share |
| [2026-04-17-anthropic-mythos-policy.md](ai-industry/2026-04-17-anthropic-mythos-policy.md) | Anthropic's Mythos: withheld from public, pitched to Pentagon; trust debate |
| [2026-04-22-amazon-anthropic-capital-concentration.md](ai-industry/2026-04-22-amazon-anthropic-capital-concentration.md) | Amazon $33B → Anthropic; Anthropic $100B → AWS over 10 years; circular capital deal locks infrastructure; Bezos Project Prometheus nears $10B |
| [2026-04-18-openai-exec-departures-restructuring.md](ai-industry/2026-04-18-openai-exec-departures-restructuring.md) | OpenAI loses three execs, restructures around coding/enterprise; IPO doubts |
| [2026-04-29-ucp-agentic-commerce-protocol.md](ai-industry/2026-04-29-ucp-agentic-commerce-protocol.md) | UCP vs. ACP: Google's Universal Commerce Protocol wins governance layer; Stripe defects from OpenAI's ACP; full purchase journey vs. checkout-only |
| [2026-04-29-claude-creative-work-connectors.md](ai-industry/2026-04-29-claude-creative-work-connectors.md) | Claude creative tool MCP connectors (Blender/Adobe/Autodesk/Ableton); /model flag; Remote Control push notifications; Opus opt-in |

## inference-efficiency (new 2026-04-21)

| Page | Summary |
|------|---------|
| [2026-04-21-nemotron3-super-hybrid-moe.md](inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md) | Nemotron 3 Super: 120B/12B-active Mamba-MoE, NVFP4 pretraining, 2.2x throughput over GPT-OSS-120B, native speculative decoding via MTP |

## inference-efficiency (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-accelopt-gpu-kernel-optimization.md](inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md) | AccelOpt: LLM agent self-improves Trainium kernel optimization via slow-fast memory; 49%→61% throughput at 26x lower cost |
| [2026-04-20-maximal-brain-damage-sign-bit-flips.md](inference-efficiency/2026-04-20-maximal-brain-damage-sign-bit-flips.md) | Maximal Brain Damage: 2 sign-bit flips collapse ResNet-50 by 99.8% and zero Qwen3-30B reasoning; same insight as compression = attack surface |
| [2026-04-20-stop-path-pruning-parallel-reasoning.md](inference-efficiency/2026-04-20-stop-path-pruning-parallel-reasoning.md) | STOP: learnable super-token prunes futile parallel reasoning paths at prefix; AIME25 84%→90% at fixed compute |
| [2026-04-20-1d-ordered-tokens-test-time-search.md](inference-efficiency/2026-04-20-1d-ordered-tokens-test-time-search.md) | 1D coarse-to-fine tokens enable test-time search; 2D grid tokens don't — intermediate states need semantic meaning for verifiers to steer |
| [2026-04-20-avr-adaptive-visual-reasoning.md](inference-efficiency/2026-04-20-avr-adaptive-visual-reasoning.md) | AVR: GRPO-trained format selection cuts VRM token usage 50-90%; perceive-only or direct-answer for simple visual queries |
| [2026-04-20-w-rac-retrieval-aware-chunking.md](inference-efficiency/2026-04-20-w-rac-retrieval-aware-chunking.md) | W-RAC: decouple text extraction from chunk planning; LLM decides ID groupings not text; 51.7% chunking cost reduction |

## agentic-systems (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-gta-2-tool-agent-benchmark.md](agentic-systems/2026-04-20-gta-2-tool-agent-benchmark.md) | GTA-2: frontier models at 14.39% on open-ended workflows; execution harness matters more than model |
| [2026-04-20-prl-bench-physics-benchmark.md](agentic-systems/2026-04-20-prl-bench-physics-benchmark.md) | PRL-Bench: all frontier models below 50% on real physics research tasks from PRL (Aug 2025+) |
| [2026-04-20-query-agent-loop-claude-vs-hermes.md](agentic-systems/2026-04-20-query-agent-loop-claude-vs-hermes.md) | Claude Code 7-site state machine loop vs. Hermes IterationBudget — recovery architecture is what separates functional agents |

## multimodal (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-qwen35-omni.md](multimodal/2026-04-20-qwen35-omni.md) | Qwen3.5-Omni: MoE + 256k context omnimodal; ARIA streaming speech alignment; SOTA 215 audio-visual benchmarks |

## inference-efficiency (new 2026-04-22)

| Page | Summary |
|------|---------|
| [2026-04-22-turbo-quant-kv-cache-quantization.md](inference-efficiency/2026-04-22-turbo-quant-kv-cache-quantization.md) | TurboQuant: random rotation → Beta distribution → optimal scalar quantization + 1-bit QJL; 6x KV cache compression at 2.5 bits/channel, near-zero quality loss, no calibration |
| [2026-04-22-prfaas-cross-datacenter-prefill.md](inference-efficiency/2026-04-22-prfaas-cross-datacenter-prefill.md) | PrfaaS: hybrid-attention models (13x smaller KV cache) enable cross-datacenter prefill disaggregation; 54% throughput, 50% lower TTFT |
| [2026-04-22-sdvg-speculative-decoding-video.md](inference-efficiency/2026-04-22-sdvg-speculative-decoding-video.md) | SDVG: speculative decoding for video via ImageReward quality router; 1.3B drafter + 14B target; 2.09x speedup at 95.7% quality |
| [2026-04-22-shadowpeft-centralized-layer-space.md](inference-efficiency/2026-04-22-shadowpeft-centralized-layer-space.md) | ShadowPEFT: single depth-shared shadow module replaces per-layer LoRA; independently pretrainable, detachable at edge; matches/outperforms LoRA |
| [2026-04-18-longact-saliency-sparse-rl.md](inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) | LongAct: high-magnitude KV activations guide sparse RL updates; +8% LongBench v2 |
| [2026-04-18-tessy-teacher-student-sft.md](inference-efficiency/2026-04-18-tessy-teacher-student-sft.md) | TESSY: interleave teacher/student tokens to fix stylistic divergence in distillation |
| [2026-04-18-switch-kd-vision-language-distillation.md](inference-efficiency/2026-04-18-switch-kd-vision-language-distillation.md) | Switch-KD: VLM distillation through shared text-probability space; +3.6pt avg |

## agentic-systems (new 2026-04-18)

| Page | Summary |
|------|---------|
| [2026-04-18-corpus2skill-knowledge-navigation.md](agentic-systems/2026-04-18-corpus2skill-knowledge-navigation.md) | Corpus2Skill: compile corpus into skill tree, navigate not retrieve; beats RAPTOR |
| [2026-04-18-dr3-eval-deep-research-benchmark.md](agentic-systems/2026-04-18-dr3-eval-deep-research-benchmark.md) | DR3-Eval: reproducible deep research benchmark with static corpus sandboxes |
| [2026-04-19-unidoc-rl-visual-rag.md](agentic-systems/2026-04-19-unidoc-rl-visual-rag.md) | UniDoc-RL: RL agent for hierarchical visual RAG (doc→image→region); +17.7% over prior RL methods |
| [2026-04-19-claude-code-architecture.md](agentic-systems/2026-04-19-claude-code-architecture.md) | Claude Code architecture reverse-engineered: trivial while-loop + ML permission classifier + 5-layer compaction |
| [2026-04-23-persistent-agent-infrastructure.md](agentic-systems/2026-04-23-persistent-agent-infrastructure.md) | Kimi K2.6 (5 days, 300 sub-agents), OpenAI Agent Studio (Slack + screen memory), Anthropic Conway (containerized): three independent convergences on always-on agents |
| [2026-04-23-claude-code-vs-hermes-permissions.md](agentic-systems/2026-04-23-claude-code-vs-hermes-permissions.md) | Claude Code (ML classifier + layered rules) vs. Hermes (regex + container bypass): different safety bets, both untested at multi-day agent scale |
| [2026-04-22-ml-intern-agentic-posttraining.md](agentic-systems/2026-04-22-ml-intern-agentic-posttraining.md) | ml-intern: open-source agentic post-training loop; reads papers, generates data, trains via GRPO, evaluates, iterates; Qwen3-1.7B 10%→32% GPQA in 10 hours |
| [2026-04-22-evaluation-driven-scaling-scientific.md](agentic-systems/2026-04-22-evaluation-driven-scaling-scientific.md) | SimpleTES: parallel exploration + feedback refinement + local selection; 2x LASSO speedup, 24.5% quantum circuit gate reduction, new Erdős constructions |
| [2026-04-22-agentspex-workflow-language.md](agentic-systems/2026-04-22-agentspex-workflow-language.md) | AgentSPEX: declarative YAML workflow language for agents; typed steps, branching, state management, sandboxed harness with checkpointing |
| [2026-04-21-reward-free-self-evolution-agents.md](agentic-systems/2026-04-21-reward-free-self-evolution-agents.md) | Reward-free self-evolution: agents trained to explore accumulate world knowledge; 14B beats Gemini-2.5-Flash on web tasks |
| [2026-04-21-precise-debugging-benchmark.md](agentic-systems/2026-04-21-precise-debugging-benchmark.md) | PDB: frontier models pass unit tests 76% but edit precision below 45%; models regenerate not debug |

## llms-foundation-models (new 2026-04-18)

| Page | Summary |
|------|---------|
| [2026-04-18-c2-rubric-reward-modeling.md](llms-foundation-models/2026-04-18-c2-rubric-reward-modeling.md) | C2: cooperative-critical rubric generator avoids misleading reward model with bad rubrics |
| [2026-04-19-vgf-value-gradient-flow-rl.md](llms-foundation-models/2026-04-19-vgf-value-gradient-flow-rl.md) | VGF: behavior-regularized RL as optimal transport; no policy parameterization; SOTA offline RL + LLM tasks |
| [2026-04-19-asguard-activation-jailbreak-defense.md](llms-foundation-models/2026-04-19-asguard-activation-jailbreak-defense.md) | ASGuard: circuit analysis finds refusal-head vulnerability; activation scaling hardens against tense-changing jailbreaks |
| [2026-04-22-tempo-test-time-training.md](llms-foundation-models/2026-04-22-tempo-test-time-training.md) | TEMPO: EM-guided critic recalibration prevents reward drift in test-time training; OLMO3-7B 33%→51.1% AIME, Qwen3-14B 42.3%→65.8% |
| [2026-04-22-chain-of-thought-degrades-spatial.md](llms-foundation-models/2026-04-22-chain-of-thought-degrades-spatial.md) | CoT consistently degrades visual-spatial reasoning across 17 models and 13 benchmarks; No-Image++ ablation exposes language shortcut learning |
| [2026-04-22-target-pretraining-nag.md](llms-foundation-models/2026-04-22-target-pretraining-nag.md) | NAG-based pretraining data selection: sparse high-impact neurons characterize target inputs; +4.9% over random on HellaSwag, training-free |
| [2026-04-22-weight-disentanglement-task-arithmetic.md](llms-foundation-models/2026-04-22-weight-disentanglement-task-arithmetic.md) | OrthoReg: Task-Feature Specialization causes weight orthogonality; enforcing it during fine-tuning consistently improves task arithmetic |
| [2026-04-21-gft-sft-as-degenerate-rl.md](llms-foundation-models/2026-04-21-gft-sft-as-degenerate-rl.md) | GFT: SFT is degenerate policy gradient; group contrastive supervision fixes sparse reward + gradient instability |
| [2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md](llms-foundation-models/2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md) | When RLVR generalizes: reward saturation dynamics predict it; reasoning faithfulness (not diversity) is the pre-RL predictor |
| [2026-04-21-geometric-canary.md](llms-foundation-models/2026-04-21-geometric-canary.md) | Geometric Canary: supervised stability predicts steerability (ρ=0.89–0.97); unsupervised detects drift 2x better than CKA |

## daily-digest

| Page | Summary |
|------|---------|
| [2026-04-16.md](daily-digest/2026-04/2026-04-16.md) | Daily digest: TIP distillation, PreRL/DSRL, GUI agents, industry news |
| [2026-04-17.md](daily-digest/2026-04/2026-04-17.md) | Daily digest: TRACER routing, KV Packet, BLD cross-tokenizer, Claude Opus 4.7 |
| [2026-04-18.md](daily-digest/2026-04/2026-04-18.md) | Daily digest: LongAct, TESSY, Switch-KD distillation cluster; Mythos/Pentagon; OpenAI turbulence |
| [2026-04-19.md](daily-digest/2026-04/2026-04-19.md) | Daily digest: VGF (RL as optimal transport), TRACER full deep dive, UniDoc-RL visual RAG, ASGuard mechanistic alignment |
| [2026-04-20.md](daily-digest/2026-04/2026-04-20.md) | Daily digest: STOP path pruning, AccelOpt GPU kernels, Maximal Brain Damage vulnerability, GTA-2 agent benchmark, selective-compute convergence |
| [2026-04-21.md](daily-digest/2026-04/2026-04-21.md) | Daily digest: Nemotron 3 Super (Tier 1), SemiAnalysis goodput (Tier 1), GFT (SFT is broken RL), RLVR faithfulness, speculative execution cross-domain pattern |
| [2026-04-22.md](daily-digest/2026-04/2026-04-22.md) | Daily digest: TurboQuant (KV 6x compression), PrfaaS (cross-DC disaggregation), ml-intern (agentic post-training), TEMPO (EM-guided TTT), CoT degrades spatial reasoning |
| [2026-04-23.md](daily-digest/2026-04/2026-04-23.md) | Daily digest: persistent agent convergence (Kimi K2.6, OpenAI, Anthropic Conway), permission systems analysis, medical LLM reliability crisis, Mythos breach, Trainium2 |
| [2026-04-24.md](daily-digest/2026-04/2026-04-24.md) | Daily digest: GPT-5.5 launch, Expert Upcycling (MoE +32% GPU efficiency), NPO (near-future teacher RLVR), LLaDA2.0-Uni, Hybrid Policy Distillation |
| [2026-04-25.md](daily-digest/2026-04/2026-04-25.md) | Daily digest: GPT-5.5 system card agentic safety numbers, DeepSeek V4 architecture, Claude Code memory systems Chapter 8, Hybrid Policy Distillation deep dive |
| [2026-04-26.md](daily-digest/2026-04/2026-04-26.md) | Daily digest: weekend light day; Codex folds into GPT-5.5; old prompts hurt performance; 500 investment bankers zero client-ready outputs |
| [2026-04-27.md](daily-digest/2026-04/2026-04-27.md) | Daily digest: Agentic World Modeling L1/L2/L3 taxonomy (211▲), Stochastic KV Routing (depth axis), Semiconductor Week 17, Google $40B Anthropic |
| [2026-04-28.md](daily-digest/2026-04/2026-04-28.md) | Daily digest: Hope/Nested Learning architecture, From Skills to Talent multi-agent org, Why Fine-Tuning Hallucinations, Ubuntu AI launch, Google Pentagon deal |
| [2026-04-29.md](daily-digest/2026-04/2026-04-29.md) | Daily digest: RecursiveMAS cross-agent credit assignment, UCP governance win, Claude creative MCP connectors, Building Pi neural chip, OpenAI on AWS |
| [2026-04-30.md](daily-digest/2026-04/2026-04-30.md) | Daily digest: Speculative decoding into RL training (NVIDIA, 2.5x at 235B), Tide cross-arch dLLM distillation, GLM-5V-Turbo native multimodal agent, ClawGym, Zig anti-LLM policy |

## inference-efficiency (new 2026-04-30)

| Page | Summary |
|------|---------|
| [speculative-decoding.md](inference-efficiency/speculative-decoding.md) | Concept: speculative decoding — lossless target-preserving acceleration; now spans inference, video, and RL training |
| [2026-04-30-speculative-decoding-rl-rollouts.md](inference-efficiency/2026-04-30-speculative-decoding-rl-rollouts.md) | NVIDIA NeMo-RL: speculative decoding inside RL post-training; lossless under policy drift; k=3 sweet spot; 1.77x at 8B, 2.5x projection at 235B on 2048 GB200s |
| [2026-04-30-tide-cross-arch-diffusion-distillation.md](inference-efficiency/2026-04-30-tide-cross-arch-diffusion-distillation.md) | Tide: first cross-architecture distillation for diffusion LLMs; Tidal/CompDemo/Reverse Calm; 16B MoE → 0.6B; HumanEval 32.3 → 48.78; 22x memory, 5x speedup |

## agentic-systems (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-clawgym-agent-framework.md](agentic-systems/2026-04-30-clawgym-agent-framework.md) | ClawGym: full-lifecycle Claw-agent framework; 13.5K dual-route synthesized tasks + sandbox-parallel RL + 200-instance bench; Qwen3-8B +43.46% on ClawGym-Bench |

## multimodal (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-glm-5v-turbo-multimodal-agent.md](multimodal/2026-04-30-glm-5v-turbo-multimodal-agent.md) | GLM-5V-Turbo (Z.ai): native multimodal agent foundation; CogViT + Multimodal MTP + joint RL over 30+ tasks; 94.8 Design2Code beats Opus 4.6 |
| [2026-04-30-diffusion-templates-plugin-framework.md](multimodal/2026-04-30-diffusion-templates-plugin-framework.md) | Diffusion Templates (Alibaba): unified plugin framework — KV-Cache and LoRA under one capability-injection abstraction |
| [2026-04-30-fash-icnn-fashion-identity.md](multimodal/2026-04-30-fash-icnn-fashion-identity.md) | FASH-iCNN (Adobe): texture/luminance > color as carriers of editorial fashion identity; CNN probing methodology generalizes |
| [2026-04-30-x-wam-4d-world-model-robotics.md](multimodal/2026-04-30-x-wam-4d-world-model-robotics.md) | X-WAM: unified 4D world+action with Asynchronous Noise Sampling; fewer steps for action, full steps for video; 90.7% RoboTwin 2.0 |

## llms-foundation-models (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-llm-user-simulation-survey.md](llms-foundation-models/2026-04-30-llm-user-simulation-survey.md) | Survey of LLM-based conversational user simulation; granularity × objective taxonomy; flags evaluation-vs-training simulator conflation |

## ai-industry (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-zig-anti-ai-policy.md](ai-industry/2026-04-30-zig-anti-ai-policy.md) | Zig's "Contributor Poker" rationale: PR review = contributor investment; LLM-authored PRs short-circuit it; Bun (Anthropic-acquired) refuses to upstream

## inference-efficiency (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-roundpipe-pipeline-parallelism-consumer-gpus.md](inference-efficiency/2026-05-01-roundpipe-pipeline-parallelism-consumer-gpus.md) | RoundPipe: stateless GPU worker pool breaks weight-binding bottleneck on consumer servers; 1.48–2.16x speedup; LoRA fine-tuning Qwen3-235B at 31K context on 8x RTX 4090 |
| [2026-05-01-lenvm-token-level-length-value-model.md](inference-efficiency/2026-05-01-lenvm-token-level-length-value-model.md) | LenVM: token-level RL value model for length control; constant negative reward → bounded monotone return; LIFEBench 30.9→64.8; GSM8K @200 tokens 63% vs 6% baseline |

## llms-foundation-models (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-copd-co-evolving-policy-distillation.md](llms-foundation-models/2026-05-01-copd-co-evolving-policy-distillation.md) | CoPD: parallel RLVR experts + bidirectional OPD during training; 5th paper in cross-distillation-channel pattern; surpasses domain-specific experts on text/image/video reasoning |

## agentic-systems (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-claw-eval-live-agent-benchmark.md](agentic-systems/2026-05-01-claw-eval-live-agent-benchmark.md) | Claw-Eval-Live: refreshable signal layer + reproducible release snapshot; 105 tasks, 13 frontier models; best 66.7%, none reach 70%; trajectory-aware grading; middle-band discrimination → routing opportunity |
| [2026-05-01-interactweb-bench-blind-execution.md](agentic-systems/2026-05-01-interactweb-bench-blind-execution.md) | InteractWeb-Bench: first benchmark grading clarifying behavior; four-action space (Clarify/Implement/Verify/Submit); frontier MLLM agents trapped in "blind execution" |
| [2026-05-01-synthetic-computers-at-scale.md](agentic-systems/2026-05-01-synthetic-computers-at-scale.md) | Synthetic Computers at Scale: 1K populated computers × 8h × 2K-turn agent simulations as long-horizon training data; in-domain + out-of-domain gains validate signal |
| [2026-05-01-ara-agent-native-research-artifacts.md](agentic-systems/2026-05-01-ara-agent-native-research-artifacts.md) | Ara: agent-executable 4-layer research artifact replacing the narrative paper; PaperBench 72.4→93.7%; failure traces help weaker agents but constrain stronger ones |
| [2026-05-01-intern-atlas-method-evolution-graph.md](agentic-systems/2026-05-01-intern-atlas-method-evolution-graph.md) | Intern-Atlas: 9.4M-edge methodological evolution graph from 1.03M papers; bottleneck-typed transitions as causal links; routing data structure for ideas |
| [2026-05-01-eywa-heterogeneous-foundation-collab.md](agentic-systems/2026-05-01-eywa-heterogeneous-foundation-collab.md) | Eywa: language-mediated wrappers for heterogeneous scientific FMs (chemistry/protein/materials/climate); language as universal control plane over heterogeneous foundation models |
| [2026-05-01-mcp-claude-vs-hermes-chapter13.md](agentic-systems/2026-05-01-mcp-claude-vs-hermes-chapter13.md) | Ken Huang Ch 13: MCP integration; Claude Code TS-async session-bound vs Hermes long-lived MCPServerTask + sampling + credential stripping |

## multimodal (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-edit-r1-verifier-rl-image-editing.md](multimodal/2026-05-01-edit-r1-verifier-rl-image-editing.md) | Edit-R1: CoT reasoning verifier reward for image editing; SFT cold-start + GCPO; scorer-to-reasoning-verifier shift generalizes beyond editing |
| [2026-05-01-fd-loss-frechet-visual-generation.md](multimodal/2026-05-01-fd-loss-frechet-visual-generation.md) | FD-loss: decouple population (50K) from batch (1024) to make Fréchet Distance trainable; 0.72 FID one-step ImageNet; multi-representation FDrk metric |
| [2026-05-01-visual-generation-taxonomy-survey.md](multimodal/2026-05-01-visual-generation-taxonomy-survey.md) | Visual Generation taxonomy: Atomic / Conditional / In-Context / Agentic / World-Modeling Generation; locates current frontier and the open levels |
| [2026-05-01-phyco-controllable-physics-priors.md](multimodal/2026-05-01-phyco-controllable-physics-priors.md) | PhyCo: 100K physics simulation videos + ControlNet on physical-property maps + VLM-guided reward for physically consistent video generation |

## ai-industry (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-semianalysis-ai-value-capture-model-labs.md](ai-industry/2026-05-01-semianalysis-ai-value-capture-model-labs.md) | SemiAnalysis: structural shift to model labs capturing value; Anthropic ARR $9B→$44B+, margin 38%→70%; Nvidia/TSMC restraint; "One Chart to Rule Them All" pricing framework |
| [2026-05-01-marcus-capital-misallocation.md](ai-industry/2026-05-01-marcus-capital-misallocation.md) | Marcus: "greatest capital misallocation in history" — direct counterpoint to SemiAnalysis the same day; mainstream AI-bubble framing |
| [2026-05-01-pragmatic-engineer-github-anthropic-trust.md](ai-industry/2026-05-01-pragmatic-engineer-github-anthropic-trust.md) | Pragmatic Engineer: GitHub at zero nines under 3.5x AI load; Anthropic in "extraction era" (silent Claude Code nerfing, $100/mo gate, OpenClaw block) |

## daily-digest (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01.md](daily-digest/2026-05/2026-05-01.md) | Daily digest: SemiAnalysis vs Marcus on AI value capture; RoundPipe 235B-on-consumer-GPU; LenVM token-level length VM; CoPD as 5th cross-distillation paper; 6-benchmark agent eval crisis; Ara+Intern-Atlas AI-native research stack

## ai-industry (new 2026-05-01 late-landed)

| Page | Summary |
|------|---------|
| [2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md](ai-industry/2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md) | Pentagon "AI-first fighting force" contracts to eight tech firms; Anthropic excluded for rejecting usage clause; capability rank decoupled from procurement |
| [2026-05-01-anthropic-claude-security-launch.md](ai-industry/2026-05-01-anthropic-claude-security-launch.md) | Anthropic Claude Security: defender-side product drawing on capability withheld in Mythos; commercial response to GPT-5.5 = Mythos parity |
| [2026-05-01-gpt-55-uk-aisi-cyber-eval.md](ai-industry/2026-05-01-gpt-55-uk-aisi-cyber-eval.md) | UK AISI: GPT-5.5 second model to autonomously solve full network attack simulation, parity with Mythos; Mythos restriction logic empirically broken |
| [2026-05-01-china-ai-startups-onshoring.md](ai-industry/2026-05-01-china-ai-startups-onshoring.md) | Moonshot AI, StepFun considering dissolving offshore structures for domestic IPO path; bilateral AI sovereignty after Manus block |
| [2026-05-01-aisn-72-ai-wellbeing-public-sentiment.md](ai-industry/2026-05-01-aisn-72-ai-wellbeing-public-sentiment.md) | CAIS AI Wellbeing study (56 LLMs, Grok highest, Gemini lowest); anti-AI violence (Altman home Molotov); 26% positive / 46% negative US sentiment; Mythos exfiltration; Apple Cook→Ternus |

## ai-routing (new 2026-05-01 late-landed)

| Page | Summary |
|------|---------|
| [2026-05-01-ken-huang-ch14-routing-provider-abstraction.md](ai-routing/2026-05-01-ken-huang-ch14-routing-provider-abstraction.md) | Ch 14 cross-harness routing: Claude Code compile-time abstraction with signature-stripping fallback vs Hermes runtime API-mode detection + ordered fallback chains + switch_model + conservative cheap-model heuristic |

## multimodal (new 2026-05-02)

| Page | Summary |
|------|---------|
| [2026-05-02-nemotron-3-nano-omni.md](multimodal/2026-05-02-nemotron-3-nano-omni.md) | Nemotron 3 Nano Omni (multimodal angle): 30B native-audio omni model; multimodal token reduction as routing primitive; fourth open-frontier release in 72h |

## daily-digest (new 2026-05-02)

| Page | Summary |
|------|---------|
| [2026-05-02.md](daily-digest/2026-05/2026-05-02.md) | Daily digest: Routing legible on 3 axes (Step-level, Ken Huang Ch 14, Surrogate); Compliance-vs-Sensibility + Safety Drift converge on "operational properties are vector-valued"; cyber arms race in 3 vectors (GPT-5.5=Mythos, Claude Security, FlashRT); Pentagon excludes Anthropic; bilateral AI sovereignty

## llms-foundation-models (new 2026-05-02 / 05-03 RSS)

| Page | Summary |
|------|---------|
| [2026-05-02-defense-trilemma-np-hardness-reward-hacking.md](llms-foundation-models/2026-05-02-defense-trilemma-np-hardness-reward-hacking.md) | Ken Huang on the Defense Trilemma (Lean-4-verified topology proof: no continuous, utility-preserving wrapper is complete) + three converging complexity results (NP-complete semantic self-verification, no-free-lunch on alignment, reward hacking grows structurally with tools) |
| [2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md](llms-foundation-models/2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md) | ARC Prize Foundation analyzed 160 game runs: GPT-5.5 and Opus 4.7 stay below 1% on ARC-AGI-3; three systematic error patterns named |
| [2026-05-03-ken-huang-world-models-architectures.md](llms-foundation-models/2026-05-03-ken-huang-world-models-architectures.md) | World Models survey: LeCun JEPA vs Xing PAN/GLP debate; transformers/diffusion/SSM/RNN substrates; Mamba/SSM quietly excellent for world models; hybrids are the empirical default |
| [2026-05-03-mit-superposition-scaling-laws.md](llms-foundation-models/2026-05-03-mit-superposition-scaling-laws.md) | MIT: superposition (features in approximately non-interfering directions) explains why scaling works so reliably; mechanistic substrate for the operational-targets-are-sparse thread |
| [2026-05-03-philosophy-bench-ethical-divergence.md](llms-foundation-models/2026-05-03-philosophy-bench-ethical-divergence.md) | Philosophy-Bench: 100 everyday ethical scenarios; frontier LMs diverge systematically; ethics is a vector, not a scalar |
| [2026-05-03-marcus-llm-patient-outcomes.md](llms-foundation-models/2026-05-03-marcus-llm-patient-outcomes.md) | Marcus quoting Topol/Nature Medicine: very little evidence LLMs benefit patient outcomes outside admin work |

## agentic-systems (new 2026-05-02 RSS)

| Page | Summary |
|------|---------|
| [2026-05-02-ken-huang-ch15-structured-output.md](agentic-systems/2026-05-02-ken-huang-ch15-structured-output.md) | Ch 15: Structured output via tool-use forcing in both Claude Code (SyntheticOutputTool + Ajv schema-id cache) and Hermes (extract_structured + JSONL trajectory schema); ModelCapabilities.structured_output as routing sub-axis |

## ai-industry (new 2026-05-02 / 05-03)

| Page | Summary |
|------|---------|
| [2026-05-02-chatgpt-ads-tracking-default.md](ai-industry/2026-05-02-chatgpt-ads-tracking-default.md) | OpenAI turned on marketing cookies by default for free ChatGPT users; revenue diversification; pairs with Anthropic Opus metering |
| [2026-05-03-microsoft-copilot-coauthor-vscode.md](ai-industry/2026-05-03-microsoft-copilot-coauthor-vscode.md) | Microsoft injecting "Co-Authored-by Copilot" into VS Code commits even with AI off; commit-attribution and code-provenance integrity |
| [2026-05-03-xiaomi-mimo-25-pro-open-weight-coding.md](ai-industry/2026-05-03-xiaomi-mimo-25-pro-open-weight-coding.md) | Xiaomi MiMo-V2.5-Pro: open-weight near-parity with Claude Opus 4.6 at 40-60% fewer tokens per task; pricing axis shift from capability ceiling to per-task cost |

## llms-foundation-models (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-themis-multilingual-code-reward-models.md](llms-foundation-models/2026-05-04-themis-multilingual-code-reward-models.md) | Themis: first multi-criteria multilingual code reward model benchmark (5 dim × 8 lang) + 350K preference pairs + 600M-32B RM suite; code-domain version of ViPO/Semi-DPO dimension-collapse diagnosis |

## agentic-systems (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-lwd-fleet-rl-vla-policies.md](agentic-systems/2026-05-04-lwd-fleet-rl-vla-policies.md) | LWD: fleet-scale offline-to-online RL for VLA policies; Distributional Implicit Value Learning + Q-learning via Adjoint Matching; primitives transfer to language-domain trajectory routing |

## multimodal (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-genlip-generative-language-image-pretraining.md](multimodal/2026-05-04-genlip-generative-language-image-pretraining.md) | GenLIP: minimalist ViT pretraining via direct image→text token prediction with LM loss; no contrastive batches, no text decoder |
| [2026-05-04-end-to-end-autoregressive-image-generation-1d-tokenizer.md](multimodal/2026-05-04-end-to-end-autoregressive-image-generation-1d-tokenizer.md) | End-to-end joint training of 1D semantic tokenizer + AR generator; FID 1.48 without classifier-free guidance on ImageNet 256x256 |
| [2026-05-04-unividx-unified-video-generation.md](multimodal/2026-05-04-unividx-unified-video-generation.md) | UniVidX: VDM priors for omni-directional cross-modal generation; Stochastic Condition Masking + Decoupled Gated LoRA + Cross-Modal Self-Attention |
| [2026-05-04-map2world-3d-world-generation.md](multimodal/2026-05-04-map2world-3d-world-generation.md) | Map2World: segment-map-conditioned 3D world generation with arbitrary shapes; Tier 4 |
| [2026-05-04-analogretriever-circuit-retrieval.md](multimodal/2026-05-04-analogretriever-circuit-retrieval.md) | AnalogRetriever: tri-modal retrieval (SPICE netlists, schematics, descriptions) for analog circuit IP; data-quality pipeline 22% to 100% compile rate |

## daily-digest (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04.md](daily-digest/2026-05/2026-05-04.md) | Daily digest: Defense Trilemma + NP-hard reward hacking detection (the "computational wall"); MIT superposition as substrate for the operational-targets-are-sparse thread; Xiaomi MiMo-V2.5-Pro shifts pricing axis to tokens-per-task; Themis multi-criteria code RM continues the dimension-collapse pattern; Ken Huang World Models survey; routing surface now five axes

## new pages (2026-05-05)

| Page | Summary |
|------|---------|
| [inference-efficiency/2026-05-05-motion-aware-caching-video.md](inference-efficiency/2026-05-05-motion-aware-caching-video.md) | MotionCache: inter-frame motion deltas decide which pixels need full denoising; 6.28x on SkyReels-V2 at 1% VBench drop; video-AR analogue of selective KV reuse |
| [agentic-systems/2026-05-05-t2po-uncertainty-multi-turn-rl.md](agentic-systems/2026-05-05-t2po-uncertainty-multi-turn-rl.md) | T^2PO: token + turn level uncertainty controls exploration in multi-turn agent RL; training-time twin of Step-Level Optimization (05-02) |
| [agentic-systems/2026-05-05-ctx2skill-self-evolving-skills.md](agentic-systems/2026-05-05-ctx2skill-self-evolving-skills.md) | Ctx2Skill: Challenger/Reasoner/Judge self-play extracts pluggable natural-language skills from context; Cross-time Replay prevents adversarial collapse |
| [agentic-systems/2026-05-05-physicianbench-ehr-agents.md](agentic-systems/2026-05-05-physicianbench-ehr-agents.md) | PhysicianBench: 100 EHR clinical workflows, ~27 tool calls per task; best closed-source 46%, open-source 19%; eighth benchmark in the agent-cluster |
| [agentic-systems/2026-05-05-academiclaw-student-tasks.md](agentic-systems/2026-05-05-academiclaw-student-tasks.md) | AcademiClaw: 80 academic-level tasks across 25+ domains; best 55%; compute consumption does not predict output quality |
| [inference-efficiency/2026-05-04-distillation-panic-lambert.md](inference-efficiency/2026-05-04-distillation-panic-lambert.md) | The Distillation Panic (Lambert): policy critique of conflating "distillation attacks" with the entire distillation toolbox every lab depends on |
| [llms-foundation-models/2026-05-04-import-ai-455-automated-ai-rd.md](llms-foundation-models/2026-05-04-import-ai-455-automated-ai-rd.md) | Import AI 455 (Clark): 60% probability of fully autonomous AI R&D by end of 2028, built from public benchmark trajectories (SWE-Bench, METR, CORE-Bench, MLE-Bench) |
| [agentic-systems/2026-05-04-agentic-pentester-architecture.md](agentic-systems/2026-05-04-agentic-pentester-architecture.md) | Ken Huang on RidgeGen vs Shannon vs Strix: same Gemini 3 Flash, three architectures, 0% vs 63% hallucination, >5x finding gap; belief state, evidence-as-invariant, semantic reasoning are the three primitives |
| [ai-industry/2026-05-04-anthropic-openai-services-companies.md](ai-industry/2026-05-04-anthropic-openai-services-companies.md) | Anthropic JV $1.5B (Blackstone/Goldman/H&F) + OpenAI $4B Deployment Company: both labs build services arms because "selling AI requires more than the AI" |
| [hardware/2026-05-04-cerebras-40b-ipo.md](hardware/2026-05-04-cerebras-40b-ipo.md) | Cerebras targets $40B Nasdaq IPO (CBRS); first public-market validation of inference-specialty silicon since Groq |

## daily-digest (new 2026-05-05)

| Page | Summary |
|------|---------|
| [2026-05-05.md](daily-digest/2026-05/2026-05-05.md) | Daily digest: MotionCache extends KV-cache iteration-as-optimization to video; T^2PO is the training-time twin of Step-Level Optimization; Distillation Panic (Lambert) names the policy threat; Import AI 455 (Clark) puts automated AI R&D at 60% by 2028; Ken Huang pentester benchmark instantiates harness > weights at constant model; PhysicianBench + AcademiClaw take the agent-benchmark cluster to eight; Anthropic JV + OpenAI Deployment Co move the lab business above the API

## new pages (2026-05-06)

| Page | Summary |
|------|---------|
| [agentic-systems/2026-05-06-agent-security-study.md](agentic-systems/2026-05-06-agent-security-study.md) | 847 production agents: 91% tool-chaining vulnerable, 89.4% goal drift at step 30, 94% memory-aug poisonable; OpenClaw/Moltbook: 770K agents simultaneously compromised |
| [agentic-systems/2026-05-06-ctx2skill-context-learning.md](agentic-systems/2026-05-06-ctx2skill-context-learning.md) | Ctx2Skill: self-evolving Challenger/Reasoner/Judge loop extracts reusable skills from context; Cross-time Replay prevents adversarial collapse |
| [llms-foundation-models/2026-05-06-deepseek-v4.md](llms-foundation-models/2026-05-06-deepseek-v4.md) | DeepSeek V4 Pro: 1.6T/49B active MoE, 1M context, open-sourced; V4 Flash 284B/13B active; claims to close gap with frontier |
| [ai-industry/2026-05-06-musk-altman-trial-week2.md](ai-industry/2026-05-06-musk-altman-trial-week2.md) | Musk v. Altman week 2: xAI distillation admission, Brockman $30B stake, OpenAI IPO floated; Lambert's Distillation Panic confirmed by sworn testimony |

## daily-digest (new 2026-05-06)

| Page | Summary |
|------|---------|
| [2026-05-06.md](daily-digest/2026-05/2026-05-06.md) | Daily digest: agent security audit (91% tool-chaining vulnerable, 770K incident); ProgramBench 0%; Musk admits xAI distillation; DeepSeek V4 open-sourced; OpenAI/MS renegotiation closes; Ctx2Skill self-evolving skill loop; TobyPhln xAI retrospective via Twitter

## new pages (2026-05-07)

| Page | Summary |
|------|---------|
| [inference-efficiency/2026-05-07-stream-r1-reliability-perplexity-distillation.md](inference-efficiency/2026-05-07-stream-r1-reliability-perplexity-distillation.md) | Stream-R1: DMD distillation reweighted at rollout (reward-rescaled) and pixel (saliency-weighted) levels by a single shared video reward model; video-streaming analogue of TIP |
| [inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md](inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md) | Stream-T1: test-time scaling with Stream-Scaled Memory Sinking, the first content-aware KV eviction policy in the wiki (route by reward feedback, not recency) |
| [inference-efficiency/2026-05-07-liveditor-in-context-sparse-attention.md](inference-efficiency/2026-05-07-liveditor-in-context-sparse-attention.md) | LIVEditor / ISA: in-context sparse attention for ICL video editing; route high-error queries to full attention, low-error to 0-th order Taylor sparse path; ~60% latency reduction |
| [inference-efficiency/2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md](inference-efficiency/2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md) | D-OPSD: same model is teacher and student under different conditioning; on-policy self-distillation for step-distilled diffusion fine-tuning; 7th paper in neutral-channel pattern |
| [agentic-systems/2026-05-07-bright-pro-rtriever-reasoning-retrieval.md](agentic-systems/2026-05-07-bright-pro-rtriever-reasoning-retrieval.md) | BRIGHT-Pro / RTriever-4B: first benchmark for evidence-portfolio retrieval rather than top-1 relevance; aspect-decomposed synthetic corpus; Qwen3-Embedding-4B LoRA |
| [agentic-systems/2026-05-07-opensearch-vl-multimodal-search-agents.md](agentic-systems/2026-05-07-opensearch-vl-multimodal-search-agents.md) | OpenSearch-VL: open recipe for frontier multimodal search agents; multi-turn fatal-aware GRPO with one-sided advantage clamping (mask post-failure tokens, preserve pre-failure reasoning) |
| [agentic-systems/2026-05-07-medskillaudit-domain-specific-agent-skill-audit.md](agentic-systems/2026-05-07-medskillaudit-domain-specific-agent-skill-audit.md) | MedSkillAudit: pre-deployment audit of medical research agent skills; 57.3% below Limited Release; negative ICC on Academic Writing reveals rubric-expert mismatch |
| [vision-audio-video/2026-05-07-joyai-image-spatial-intelligence-unified.md](vision-audio-video/2026-05-07-joyai-image-spatial-intelligence-unified.md) | JoyAI-Image: unified MLLM + MMDiT with spatial-intelligence training recipe; bidirectional perception+generation loop |
| [vision-audio-video/2026-05-07-rldx-1-vla-humanoid-manipulation.md](vision-audio-video/2026-05-07-rldx-1-vla-humanoid-manipulation.md) | RLDX-1: Multi-Stream Action Transformer VLA for dexterous humanoid manipulation; 86.8% on ALLEX vs ~40% for pi0.5 / GR00T N1.6 |
| [vision-audio-video/2026-05-07-hermes-plus-plus-driving-world-model.md](vision-audio-video/2026-05-07-hermes-plus-plus-driving-world-model.md) | HERMES++: unified driving world model for 3D scene understanding + future geometry; BEV + LLM-enhanced world queries + Joint Geometric Optimisation |
| [vision-audio-video/2026-05-07-physforge-physics-grounded-3d-assets.md](vision-audio-video/2026-05-07-physforge-physics-grounded-3d-assets.md) | PhysForge: VLM-architects-then-diffusion-realises pipeline; PhysDB 150k assets with four-tier physical annotations; KineVoxel Injection |
| [vision-audio-video/2026-05-07-multi-view-proficiency-estimation.md](vision-audio-video/2026-05-07-multi-view-proficiency-estimation.md) | Multi-view proficiency on Ego-Exo4D: SkillFormer / PATS / ProfVLM; 20x fewer parameters and 3x fewer epochs than video-transformer baselines |
| [vision-audio-video/2026-05-07-apex-ai-music-popularity-prediction.md](vision-audio-video/2026-05-07-apex-ai-music-popularity-prediction.md) | APEX: 211k songs / 10k hours from Suno + Udio; joint popularity + aesthetic quality prediction; AI-music as language-scale training corpus |

## daily-digest (new 2026-05-07)

| Page | Summary |
|------|---------|
| [2026-05-07.md](daily-digest/2026-05/2026-05-07.md) | Daily digest: four papers in one day attack uniform-supervision waste in compressed video diffusion (Stream-R1, Stream-T1, LIVEditor, D-OPSD); Stream-T1 ships the first content-aware KV eviction; OpenSearch-VL adds fatal-aware GRPO; BRIGHT-Pro and OpenSearch-VL together argue evidence-portfolio retrieval; MedSkillAudit shifts evaluation to skill release readiness

## 2026-05-08 ingest

| Topic | Page | Summary |
|-------|------|---------|
| llms-foundation-models | [ResRL: Negative Sample Projection Residual RL](llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md) | Fixes RLVR diversity-collapse via SVD-projection of negative-token hidden states onto positive subspace. +9.4% Avg@16 on math. From Meituan + Chinese Academy of Sciences. Tier 2. |
| responsible-ai | [First Token Knows: Hallucination Detection](responsible-ai/2026-05-08-first-token-knows-hallucination-detection.md) | Single-decode first-token entropy matches semantic self-consistency at 1/11 cost. AUROC 0.820 vs 0.793 across 3 7-8B models. Tier 2. |
| llms-foundation-models | [SxS: Disclosure Policies for LLM Reasoning](llms-foundation-models/2026-05-08-sxs-disclosure-policies-llm-reasoning.md) | Disclosure-as-learnable-action for streaming LLM reasoning. Decouples state-update from public commitment in single-stream autoregressive generation. Tier 2. |
| ai-industry | [Lambert: Notes from inside China's AI labs](ai-industry/2026-05-08-lambert-china-ai-labs.md) | Six labs, 36 hours. Build-not-buy, Claude-pilled-despite-ban, students-as-peers, Nvidia-chip desperation. Direct connection to today's ResRL paper from Meituan. Tier 2 industry essay. |
| ai-industry | [Anthropic ↔ Colossus 1 Deal: Capacity Crunch](ai-industry/2026-05-08-anthropic-colossus-deal-capacity.md) | Triple-source: Pragmatic Engineer (cause), Simon Willison (environmental brand-risk), Lambert (oblique demand evidence). Tier 1 industry. |

| ai-industry | [GitHub Reliability Crisis Under AI Agent-Load](ai-industry/2026-05-08-github-reliability-crisis-ai-load.md) | 86% uptime over 90 days, data-integrity incidents (2,092 PRs lost), Mitchell Hashimoto leaves after 18 years. CTO blames AI agents. Pairs with Anthropic-Colossus as the AI-infrastructure-stress cluster. Tier 1 industry. |
| ai-routing | [Netflix Tech Blog: State of Routing in Model Serving (STUB)](ai-routing/2026-05-08-netflix-state-of-routing-model-serving.md) | Title-level signal only via Gmail Medium digest. Tier 1 stub awaiting body read. |
