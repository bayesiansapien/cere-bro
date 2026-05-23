# ACC: Compiling Agent Trajectories for Long-Context Training

**Date:** 2026-05-23
**Arxiv:** [2605.21850](https://arxiv.org/abs/2605.21850)
**HF papers:** [https://huggingface.co/papers/2605.21850](https://huggingface.co/papers/2605.21850)
**Raw source:** [farmer/huggingface](../../raw/huggingface/2026-05-23-acc-compiling-agent-trajectories-for-long-context-training.md)

## TL;DR

ACC (Agent Context Compilation) takes raw multi-turn agent trajectories from search, software-engineering and database agents and re-compiles them into long-context QA pairs where the original question is paired with all tool responses and environment observations gathered across many turns. The model is then trained to answer the question directly, without tool use, given that long context. Training Qwen3-30B-A3B with ACC pushes MRCR from 50.2 to 68.3 (+18.1) and GraphWalks from 69.9 to 77.5 (+7.6), comparable to Qwen3-235B-A22B while preserving general capabilities on GPQA, MMLU-Pro, AIME, IFEval.

## Why this matters

The 04-18 LongAct paper showed that long-context training signal is concentrated in a small fraction of tokens (the high-magnitude saliency positions). The 04-16 TIP paper (Token Importance in on-Policy distillation) showed that most teacher-generated tokens carry no real signal. ACC works at a third axis: **the long-context training data itself is missing**, because standard agent SFT masks tool responses and only supervises turn-level tool choice. The supervision blind spot is exactly where the scattered evidence lives. ACC unmasks it.

## Mechanism

Standard agent SFT: question → (tool call → tool response masked) × N → answer. The tool responses are not gradient-bearing; only the turn-level tool selection token positions are. ACC inverts this: take the same trajectory and emit a single QA pair where the response contains all tool returns interleaved, and the model trains to predict the final answer directly. This makes the dependency between the original question and the evidence explicit, and the model has to integrate across the long context, not just decide what to call next.

## Key takeaways

- MRCR: 50.2 → 68.3 (+18.1) on Qwen3-30B-A3B.
- GraphWalks: 69.9 → 77.5 (+7.6).
- Reaches Qwen3-235B-A22B-class performance on long-context dependency benchmarks at 30B active.
- Preserves general capabilities (GPQA, MMLU-Pro, AIME, IFEval flat or slightly up).
- Mechanism analysis: ACC-trained model shows task-adaptive attention restructuring and expert specialization.

## Gaps

The 30B-A3B → 235B-A22B equivalence is at MRCR and GraphWalks only. Whether the gain transfers to AgentBench, BrowseComp, or production tool-use benchmarks is not shown. Whether ACC is complementary to or substitutive of long-document continued-pretraining recipes (MMProLong family) is open. Trajectory-source bias is not analyzed: search trajectories may differ in dependency structure from software-engineering trajectories, and the gain decomposition by source is not given.

## Related wiki pages

- [KV cache](./kv-cache.md) — the inference-side complement to ACC's training-side fix.
- [LongAct (2026-04-18)](2026-04-18-longact-saliency-sparse-rl.md) — saliency-sparse RL on long context.
- [MMProLong (2026-05-14)](2026-05-14-mmprolong-long-context-vlm.md) — long-context VLM training recipe.
- [EndPrompt (2026-05-19)](2026-05-19-endprompt-terminal-anchoring-long-context-extension.md) — short-sequence extension via terminal anchoring.

## Research angle

If ACC works because tool responses contain the scattered evidence the model needs to integrate, then production agent logs are a new pretraining corpus that nobody had named as one. The labs sitting on Cursor / Claude Code / Windsurf trajectory data have a training-data moat that does not require expensive long-document curation. The question worth tracking: do you need verified-correct trajectories, or do failures help too? If failures help, the moat grows; if not, only labs with strong outcome verification benefit.
