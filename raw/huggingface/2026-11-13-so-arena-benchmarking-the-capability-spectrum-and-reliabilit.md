---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.524979+00:00
arxiv_id: 2611.15777
url: https://huggingface.co/papers/2611.15777
arxiv_url: https://arxiv.org/abs/2611.15777
date: 2026-11-13
---

# SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models

System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions. We introduce SO-Arena, a benchmark characterizing the capability spectrum and decision reliability of System One models across 11 domains and five capability families. For the capability spectrum, SO-Arena offers evidence-grounded evaluation through reliable sources and manual verification of reference labels against model-visible inputs; fine-grained capability assessment through domain-specific difficulty criteria; and realistic interactive evaluation, where models iteratively execute actions in sandboxes. Reasoning-intensive tasks further enable system one-two comparison. Beyond accuracy, SO-Arena assesses decision reliability through two complementary measures: decision stability under controlled option-set changes and missing-answer recognition when no valid option is available. Evaluations across 21 models reveal that the benefits of scaling and additional reasoning vary substantially across domains. More importantly, strong overall performance does not necessarily imply reliable decision-making: the best-performing System One model ranks only seventh in reliability. Together, these findings highlight the need to characterize capability spectrum and decision reliability as complementary dimensions, providing a systematic view of the strengths and limitations of System One models.
