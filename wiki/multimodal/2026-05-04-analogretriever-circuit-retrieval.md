# AnalogRetriever — Cross-Modal Representations for Analog Circuit Retrieval

**Source:** HuggingFace Daily Papers
**Raw:** [raw/huggingface/2026-05-04-analogretriever-cross-modal-representations-analog-circuit-retrieval.md](../../raw/huggingface/2026-05-04-analogretriever-cross-modal-representations-analog-circuit-retrieval.md)
**arXiv:** https://arxiv.org/abs/2604.23195
**Date:** 2026-05-04
**Tier:** 4 — narrow-domain retrieval (analog circuit IP)

## TL;DR

Tri-modal retrieval framework for analog circuit search across SPICE netlists, schematics, and functional descriptions. Two-stage repair pipeline lifts netlist compile rate from 22% → 100% on Masala-CHAI. Encodes schematics and descriptions with a VLM and netlists with a port-aware relational GCN; curriculum contrastive learning maps all three into a shared embedding space. Recall@1 of 75.2% averaged over 6 cross-modal directions. Integrates as a RAG module in the AnalogCoder agentic framework.

## Quick note

Tier 4. Domain-specific. The methodological piece that's transferable is the data-quality repair pipeline (22% → 100% compile rate) — a clean instance of the "data quality dominates" thread that ViPO (05-02) raised in visual preferences.
