# Microsoft VS Code Auto-Inserts "Co-Authored-by Copilot" Even With AI Off

**Source:** The Decoder
**Raw:** [raw/rss/2026-05-03-the-decoder-microsoft-caught-sneaking-co-authored-by-copilot-into-v.md](../../raw/rss/2026-05-03-the-decoder-microsoft-caught-sneaking-co-authored-by-copilot-into-v.md)
**URL:** https://the-decoder.com/co-pilot-becomes-a-co-author-in-vs-code-without-being-asked/
**Date:** 2026-05-03
**Tier:** Industry — trust / transparency

## TL;DR

Microsoft was caught injecting `Co-Authored-by Copilot` lines into Git commits made through VS Code — even when AI features were turned off entirely. The Decoder framing emphasizes the "without permission" angle.

## Why it matters

The opt-out vs opt-in line is moving against users on multiple fronts the same week (ChatGPT ads default-on 05-02; this co-author injection 05-03). For developers specifically, there is a trust-and-attribution question: commit attribution is a load-bearing artifact for code provenance, license compliance, and (downstream) AI-training data filtering. Misattribution at scale corrupts the data the next generation of models is trained on. Connects to Marcus on "vibe slop" (05-01), Pragmatic Engineer / Armin Ronacher (04-29) — the production code-provenance signal is degrading from multiple angles at once.
