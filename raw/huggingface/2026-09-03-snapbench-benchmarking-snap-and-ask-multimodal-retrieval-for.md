---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.29607
url: https://huggingface.co/papers/2608.29607
arxiv_url: https://arxiv.org/abs/2608.29607
date: 2026-09-03
---

# SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions

Mobile AI acts as a visual oracle, empowering users to snap a picture of something and ask for information. Snap-and-ask retrieval is now one of the most common entry points for mobile AI, yet photos are often blurry, while text questions may be short or mistyped. Existing benchmarks only test on clean inputs or do not isolate paired robustness in snap-and-ask retrieval. Therefore, we introduce SnapBench, the first paired benchmark for robust snap-and-ask multimodal retrieval, spanning 1,145 queries, 9,085 gallery items under 53 controlled corruption conditions with human annotations. We evaluate 16 multimodal retrievers, covering dual-tower encoders and embedding-based VLMs. Results show that image corruptions substantially degrade retrieval, while text corruptions mainly affect text-only retrieval and have limited impact on joint retrieval. Clean image-only retrieval often outperforms joint retrieval, indicating the coarse-text drag and the lack of cross-modal fallback under noisy inputs. SnapBench provides a controlled testbed for evaluating robust retrieval in snap-and-ask scenarios. We further propose MOOR (Modality-anchored, Outlier-aware, Optimal Reweighting), a simple adaptive fusion approach, highlighting the need for reliability-aware modality calibration in snap-and-ask retrieval.
