# The memory tax, and other cheap checks that win

**TL;DR.** **The memory tax (2610.34073):** on LongMemEval, PersonaMem and MINT-Eval, many dedicated agent-memory systems score below naive retrieval over the raw history while costing more. The paper splits net value into memory *benefit* (questions memory answers that RAG misses) and memory *tax* (questions RAG gets that memory loses). The tax comes from rewriting history, which drops or distorts facts; retrieving from raw history alongside memory and reranking both cuts it. **Thinking-in-Bets (2610.34654):** an agent writes its claims, checks and confidence into a private checklist before reading user feedback, then revises only weak claims. False reversals on patch review fall from 12.2% to 0.02% across five Gemini models, training-free. **OAT (2607.12747, first covered 10-26)** recirculated: failure attribution learned only from ~100 successful trajectories, no LLM call at inference.

## Relation to prior wiki pages
- [Agent memory](agent-memory.md): second paper in two days after Raw-RAG (10-27, plain retrieval over chat history beats agent memory) and the 10-23 MemoryTax evidence. The 10-23 Looking Ahead asked a memory vendor to answer with frontier-class readers; still unanswered.
- Same shape as today's harness-verification result: the cheap independent check beats the elaborate built-in mechanism.

Raw: [Thinking-in-Bets](../../raw/huggingface/2026-10-27-thinking-in-bets-at-test-time-reduces-sycophantic-revisions.md) · [arXiv 2610.34073](https://arxiv.org/abs/2610.34073) · [arXiv 2610.34654](https://arxiv.org/abs/2610.34654)
