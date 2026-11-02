# Why We Rebuilt Microsoft Office From Scratch for AI Agents (Yijia Liang, Compound AI)

**Channel:** AI Engineer
**Published:** 2026-11-01
**Source:** https://www.youtube.com/watch?v=v0UkV5qS9E4
**Secondary domain:** finance

## TL;DR
Compound, a startup for buy-side finance agents founded by an ex-Coatue VP, says off-the-shelf options (Office plugins, computer-use VMs, openpyxl, commercial engines) can't run long, parallel analyst workflows. They used coding agents (about 1.5T tokens, about 8M lines of code) to rebuild Excel, PowerPoint, and Word as headless Rust engines. Real Office served as the test oracle. The Excel engine, forked from IronCalc, is about 800k lines of Rust. Owning the engine gives a write, render, check, fix loop, parallel execution, and compact model-readable views of 30MB workbooks. They pair it with email-native multiplayer agents and grep-based agent swarms in place of vector-DB RAG.

## Key Takeaways
- **Why personal agents don't translate to finance:** the "background task" is data room to IC model, deck, and memo (normally about 4 weeks). MDs don't want proactive agents burning tokens. Context means 15k-file data rooms and petabytes in SharePoint or Box, not email and calendar.
- **Multiplayer through email:** every agent gets an inbox, because deals run through 20+ message Outlook threads. Hard parts: per-thread auth under NDA, and adding deliberate latency so an agent doesn't spam acknowledgements when several people reply at once.
- **Office rebuild method:** take an open-source base (IronCalc for Excel), use real Office as the oracle, benchmark against real-world and internal files, and loop agents until outputs match. Rust renderers aim for pixel-perfect parity because firms only trust what downloads and sends correctly.
- **Performance:** headless engines are not tied to a desktop CPU, run in parallel, and recalculate 20MB workbooks about 4x faster than Excel.
- **Context breadth:** skip the vector DB. A lead agent splits the file tree, swarms of agents grep and read, findings come back with source citations, and the loop repeats until done.
- **Context depth:** off-the-shelf LLMs read a 30MB model by dumping it through openpyxl, which is slow, expensive, and lossy. A native engine gives the model a compact structured view and richer tool APIs.
- **Copilot to autopilot:** comps spreading is already automated. 50-page IC decks and firm-specific models are still copilot work. He compares the moment to the Opus 4.5 inflection, when coders started delegating whole tasks once enough tests existed.

## Architecture & Optimization Mechanics
- **An oracle-driven agent loop as a compiler.** Real Office acts as the reference implementation and the loss function. Agents iterate until there are no behavioral diffs. This is the same pattern as distilling a black-box teacher, applied to software instead of weights. Spending 1.5T tokens is credible at 2026 prices for a one-time build.
- **Owning the representation is the main lever.** The Excel engine can produce a compressed, semantic serialization (formula graph, named ranges, sensitivity tables) in place of a cell dump. That is input compression, and it cuts tokens per task, latency, and error rate together. The same principle drives KV-cache and prompt compression.
- **A verifier in the loop:** the render, check, fix cycle needs a deterministic renderer. Without it (openpyxl), the agent guesses formatting blind. This is the familiar "verifiable reward" pattern from RL post-training, applied at inference time.
- **Grep swarms instead of embeddings:** agentic file search replaces ANN retrieval. It costs more tokens per query but has no indexing cost, gives better citation grounding, and has no staleness problem. It works when token prices are low and parallelism is cheap.
- **Skepticism:** "one-for-one replica" of Excel is a very strong claim. Excel has decades of edge cases (volatile functions, iterative calc, array spill, VBA, pivot caches). Expect fidelity gaps on long-tail workbooks. The talk shows no parity benchmark numbers.

## Grounded Context (Web Enrichment)
Public info on Compound is thin. Search found the "Compound for Excel" add-in on Microsoft Marketplace (an agent with read and write access to multi-tab workbooks that pulls from filings and PDFs, autosaving to the cloud) and an f4.fund profile describing a platform for "investment-committee-trustable" finance work ([Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/WA200010984), [f4.fund](https://f4.fund/startups/compound-ai)). Nothing public independently confirms the Rust rebuild, the IronCalc base, the 8M LOC, or the 4x recalc figure. Treat these as founder claims. IronCalc itself is a real open-source Rust spreadsheet engine, which makes it a plausible starting point.

Minor correction: Opus 4.5 launched in late November 2025, not "last December." The broader claim holds. Late-2025 frontier coding models are widely credited with moving developers from autocomplete to delegating whole tasks, and Compound's own build (agents writing millions of lines against an oracle) is an example of that shift.

## Real-World Application / Actionable Step
- **Apply the oracle loop to kernels:** use a reference implementation (PyTorch eager or cuBLAS) as the oracle and have agents iterate on Triton or CUDA kernels for quantized matmuls (for example, W4A8 or 2:4 sparse) until numerics match within tolerance and throughput beats baseline. Same method, smaller scope.
- **Compress what the model reads:** for agents working on model configs or eval logs, write a serializer that outputs a compact semantic summary (layer-wise sparsity, quant scheme per block, eval deltas) instead of raw JSON or logs. Measure token savings and task accuracy.
- **Retrieval routing:** treat "grep swarm vs vector RAG" as a routing decision. Use cheap embedding retrieval for broad lookups and escalate to agentic grep only for questions that need citations or full coverage.
