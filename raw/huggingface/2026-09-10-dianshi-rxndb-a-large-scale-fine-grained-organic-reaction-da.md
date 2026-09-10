---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.06703
url: https://huggingface.co/papers/2609.06703
arxiv_url: https://arxiv.org/abs/2609.06703
upvotes: 7
date: 2026-09-10
---

# DianShi-RxnDB: A Large-Scale, Fine-Grained Organic Reaction Data Platform Built via a Fully Automated Pipeline for Researchers and AI Agents

High-quality structured organic reaction data are essential for developing artificial intelligence for chemistry (AI4Chem), yet much of this knowledge remains dispersed across patent text, images, and reaction schemes. We present DianShi-RxnDB, a large-scale, fine-grained organic reaction data platform built via a fully automated extraction and normalization pipeline integrating patent text, images, and reaction schemes. Its corpus covers organic synthesis patents from the USPTO and EPO published between 1976 and 2025, yielding approximately 24 million reaction instances, of which approximately 14.8 million (61.7%) pass automated qualification checks. Each instance represents a specific single-step experiment recording participants, roles, quantities, temperatures, reaction times, yields, experimental procedures, and provenance links to source patents. In a manual evaluation of 1,300 sampled qualified instances, the micro-averaged field-level accuracy was 92.95%. A matched comparison with Pistachio further indicated advantages in deduplicated record counts, representation granularity, and field-level exact agreement. The platform provides a Web research workbench for searching, filtering, comparing, and source-verifying records, and a Model Context Protocol (MCP) service offering AI agents composable structured retrieval tools. DianShi-RxnDB is available at https://dianshi.opendatalab.org.cn/ .
