# LightOnOCR-2-1B: half a million pages a day on one GPU, for under a cent per thousand

**Date ingested:** 2026-09-19
**Source:** X home feed via [@thisguyknowsai](https://x.com/thisguyknowsai/status/2100896749183467750) · LightOn
**Links:** [Model card](https://huggingface.co/lightonai/LightOnOCR-2-1B) · [Technical report](https://huggingface.co/papers/2601.14251)
**Raw:** [raw/twitter/feed/2026-09-19-morning-ranked.json](../../raw/twitter/feed/2026-09-19-morning-ranked.json)

## TL;DR

LightOn shipped a **1B-parameter end-to-end OCR model**, Apache-2.0, that reads a PDF, scan or photo and writes out clean correctly-ordered text in a single pass, replacing the usual multi-stage pipeline of layout detection, region classification, per-region recognition and reading-order reconstruction. It scores **83.2 overall on olmOCR-Bench** and **89.6 on the arXiv-math split** while being roughly **9x smaller** than competing systems, runs at **5.71 pages/second on one H100**, which is about **493,000 pages per day**, and costs **under one cent per 1,000 pages**. It is 3.3x faster than Chandra, 5x faster than dots.ocr and 1.7x faster than OlmOCR, handles tables, receipts, forms, multi-column layouts and math with LaTeX output in 11 languages, and runs on vLLM, SGLang, Ollama and LM Studio.

## Why it belongs on the efficiency page rather than the vision page

The vision-language content here is routine. What is not routine is the **cost per unit of work**, and that is a number with immediate consequences for anything that ingests documents at scale, including this wiki's own pipeline. At under a cent per thousand pages, the marginal cost of OCR stops being a line item and becomes rounding error. The arithmetic that used to gate document-heavy pipelines, "can we afford to OCR the whole corpus or only the parts we think we need," disappears, and with it a whole class of retrieval architectures that exist to avoid paying it.

The structural claim is the more interesting one. Multi-stage OCR pipelines are brittle in a specific way: each stage's errors compound into the next, and the reading-order reconstruction step at the end is where most of the damage shows up. Collapsing the pipeline into one model that emits ordered text directly removes the compounding, which is the plausible reason a 1B model beats 9B-class systems rather than merely matching them.

**One caveat the model card itself flags and the tweet does not.** On olmOCR-Bench, the "headers and footers" style sub-task rewards *omission* rather than transcription, so a model that outputs nothing scores perfectly. LightOn excludes that sub-task from its Overall figure to keep the number honest. That is a good practice and it means the 83.2 is not directly comparable to a leaderboard number computed with the sub-task included.

## How this relates to prior wiki state

**It is the third artifact in a single day making the same argument at three different scales**, which is the threshold this wiki uses to call something a pattern. [Needle 3 (09-19)](2026-09-19-needle-3-sliceable-automation-model.md) ships an 8-29 MB tool-calling model whose 4-layer slice is claimed to match DeepSeek V4 Flash after one epoch of tuning. The [Jev clone wave (09-19)](../ai-routing/2026-09-19-jev-open-clones-commoditization.md) produced a 706K-parameter, 2.8 MB decision model that beat a hosted frontier-backed decision service 99.7% to 83.6% on form filling. LightOnOCR is 1B beating 9B. **Three results, three task families, one claim: for a task with a narrow well-specified output contract, a small specialised model does not merely approach the general model, it beats it.** The common factor is that all three give up open-ended generation, and all three spend the recovered capacity on the contract.

This is the constructive counterpart to the wiki's long-running observation that benchmark accuracy on general capability does not predict deployment economics.

## Gaps

- **olmOCR-Bench is one benchmark**, and LightOn built the model. No third-party evaluation exists yet.
- The 5.71 pages/second figure is throughput on an H100 with no stated batch size, concurrency, or input resolution, which are the three things that move OCR throughput most.
- 11 languages is narrow for a document-processing claim, and the languages are not enumerated in the tweet.
- No accuracy-versus-degradation curve for poor scans. Clean PDFs and phone photos of crumpled receipts are very different problems, and the marketing collapses them.
