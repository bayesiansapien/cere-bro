---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.930575+00:00
arxiv_id: 2611.30287
url: https://huggingface.co/papers/2611.30287
arxiv_url: https://arxiv.org/abs/2611.30287
date: 2026-11-24
---

# MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation

AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from completed tasks and consolidating task-specific experience. We therefore propose MMMem, a task-aware multimodal memory framework that extracts and consolidates experience from completed tasks through four complementary strategies. First, source-linked multi-view memory organizes original text, images, and rendered pages alongside generated scene images that combine clues across records for retrieval. Second, source-generated tasks support knowledge alignment at two levels: warm-up consolidates source knowledge into task-relevant experiences in external memory, while self-training adapts the model's parametric knowledge to task demands. Third, the same vision-language model distills completed tasks into experiences that record the task context, conclusion, and support links. Finally, task-aware retrieval recalls source views and relevant experiences for answering and verification, while source-supported reuse guides long-term retention. Across three memory benchmarks and two vision-language readers, MMMem outperforms eight baselines. With Qwen3.5-9B, MMMem achieves relative gains of 36.9%, 17.6%, and 15.2% over the best-performing baselines on LoCoMo, Mem-Gallery, and LooGLE v2, respectively. Ablations show consistent gains from training and memory warm-up, while case studies illustrate how individual components work in practice.
