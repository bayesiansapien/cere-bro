# Zig's Anti-LLM Contribution Policy and the "Contributor Poker" Argument

**Date:** 2026-04-30
**Source:** [Simon Willison](https://simonwillison.net/2026/Apr/30/zig-anti-ai/) covering [Loris Cro / Zig Software Foundation](https://kristoff.it/blog/contributor-poker-and-ai/)
**Raw:** [raw/rss/2026-04-30-simon-willison-the-zig-projects-rationale-for-their-firm-anti-ai-contr.md](../../raw/rss/2026-04-30-simon-willison-the-zig-projects-rationale-for-their-firm-anti-ai-contr.md)

## TL;DR

Zig has one of the strictest anti-LLM policies of any major OSS project: no LLMs for issues, PRs, or bug-tracker comments. Zig Software Foundation VP Loris Cro published the rationale: open source review work is an investment in *people*, not just code. PR review time is justified because each new contributor is a long-term asset. LLM-authored PRs break this calculus — the time the maintainer spends doesn't grow a contributor. He calls it "contributor poker" — you bet on the person, not the cards.

The most cutting line from the rationale: *"if a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem?"*

The Bun project (Anthropic-acquired in Dec 2025) runs a fork of Zig and recently shipped a 4× compile speedup with parallel semantic analysis. They explicitly say they will *not* upstream because of Zig's policy. So the policy is now affecting which performance work flows back into the upstream tree.

## Why It Matters

This is the clearest articulation of an anti-LLM open-source position to date — and crucially, it is grounded in a *project economics* argument, not an ethics argument. The argument has bite even if you fully accept LLM-generated code. The choice is structural: PRs are training data for human contributors, and LLM-authored PRs short-circuit that training loop. Projects optimizing for long-term contributor health have a coherent reason to ban them; projects optimizing for code throughput don't.

The Bun divergence is the deployment consequence. Anthropic's flagship JS-runtime acquisition can no longer contribute back to its language's mainline. If more major Zig users follow Bun, the policy creates a permanent fork structure between AI-heavy and AI-free Zig ecosystems.

## Connection to Prior Wiki Knowledge

**Companion to Building Pi (04-29) and Claude Code postmortem (04-23-24).** Mario Zechner (Pi) and Loris Cro (Zig) are making complementary observations from opposite ends:
- Zechner: the *user* of an AI agent struggles with behavioral unpredictability; specialized harnesses help.
- Cro: the *project receiving AI-authored output* struggles because review time stops growing contributors.

Both diagnose the same underlying fact — AI-assisted code shifts the cost structure of software development — and propose different mitigations. Zechner builds a stable harness; Cro builds a wall.

**Connects to "code quality is down everywhere" (Pragmatic Engineer, 04-29).** The 30+ engineering teams Armin Ronacher surveyed reported "vibe slop" shipping to production. Zig's policy is the OSS-side response to the same observation: filter at the contribution boundary rather than fix downstream. Whether the wall holds as AI-assisted code becomes universal is the open question.

## Worth Watching (90 days)

- **Other major OSS projects adopting similar policies.** Zig is currently the most prominent. If even one of {Linux subsystem, Postgres, CPython, LLVM} adopts language with similar bite, the pattern crosses from outlier to convention.
- **Bun fork divergence depth.** If Anthropic invests in Bun's Zig fork as a serious infrastructure tool, the fork stops being temporary. That's the test of whether anti-LLM policies actually push major industrial users away.
- **Compromise positions.** A middle ground — "LLM-assisted PRs accepted with full disclosure and human-attributable rewrite" — has not yet emerged as a stable convention. Some project will try it.

## Related Pages

- [Building Pi (Pragmatic Engineer, 04-29)](2026-04-29-claude-creative-work-connectors.md)
