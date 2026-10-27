---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800369+00:00
arxiv_id: 2610.31810
url: https://huggingface.co/papers/2610.31810
arxiv_url: https://arxiv.org/abs/2610.31810
date: 2026-10-26
---

# PaperFormalizer: Author-in-the-Loop Autoformalization of Research Papers in Lean

Even a carefully proofread paper can leave small gaps in its proofs or its stated assumptions. We introduce PaperFormalizer, a Lean-based agentic pipeline that helps authors find and close such gaps in their own papers and turn each paper into a Lean-verified version. Starting from the LaTeX source, PaperFormalizer transcribes the paper into a dependency graph of statements, audits each statement in natural language for faithfulness, ambiguity and correctness, and then formalizes and proves the statements in Lean against Mathlib, optional domain libraries and the author's personal toolkit. Only the author knows what a statement is meant to say and how a formalization gap in a result is best fixed. The pipeline therefore stops and asks the author whenever a statement admits more than one reading, presents every repair, in natural language and TeX symbols, as a proposal that the author can accept, decline or redirect, and leaves to the author every decision that could potentially change what the paper claims. The output is an annotated and revised version of the paper, a report of the changes, and Lean code in which each declaration is linked to the statement it formalizes. The author's toolkit grows as more papers are formalized, and authors can share their verified papers so that researchers who build on them can reuse their Lean code. By making verified papers practical to produce, PaperFormalizer aims to make research that rests on mathematical proofs more robust. PaperFormalizer runs inside a coding agent (Claude Code or Codex) and is available at https://github.com/Jiyuan-Tan/PaperFormalizer. Papers with Lean code shared by users are available at https://paperformalizer.org.
