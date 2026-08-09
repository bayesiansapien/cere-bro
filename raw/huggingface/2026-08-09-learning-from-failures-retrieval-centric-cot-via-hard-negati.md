---
source: farmer/huggingface
farmed: 2026-08-09T07:10:01.249497+00:00
arxiv_id: 2608.06060
url: https://huggingface.co/papers/2608.06060
arxiv_url: https://arxiv.org/abs/2608.06060
date: 2026-08-09
---

# Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval

Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates. Recent methods mitigate this limitation by generating Chain-of-Thought (CoT) rationales to enrich the query representation. However, such reasoning is typically derived from the query alone: it explains what the query describes, but not what the retriever misunderstands. We argue that effective retrieval reasoning should instead be conditioned on retrieval feedback. Based on this insight, we introduce UniME-R1, an embedder-adviser framework that learns to reason over initially retrieved candidates and generate Retrieval-Centric Chain-of-Thought (RC-CoT). The adviser analyzes candidates individually to identify the discriminative cues confused by the embedder. If the target appears in the initial top-k set, UniME-R1 directly reranks the candidates; otherwise, it generates RC-CoT to refine the retrieval direction and performs full-corpus re-retrieval with a dual-mode embedder. To train the framework, we mine hard negatives to simulate realistic retrieval failures, jointly optimize direct retrieval and RC-CoT-augmented retrieval, and align the adviser with retrieval outcomes through supervised learning and retrieval-oriented reinforcement learning. Extensive experiments on MMEB-V2 and a diverse set of general multimodal retrieval benchmarks demonstrate that UniME-R1 consistently improves retrieval performance over strong baselines.
