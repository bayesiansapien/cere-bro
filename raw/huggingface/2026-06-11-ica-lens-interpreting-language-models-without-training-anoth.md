---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.11722
url: https://huggingface.co/papers/2606.11722
arxiv_url: https://arxiv.org/abs/2606.11722
date: 2026-06-11
---

# ICA Lens: Interpreting Language Models Without Training Another Dictionary

Finding interpretable directions in language-model representations is critical for understanding and controlling model behavior. Sparse autoencoders (SAEs) have become the standard tool for this purpose, but using them as the default first lens often requires training, storing, and evaluating large overcomplete dictionaries. This bottleneck limits rapid exploration and raises a fundamental question: how much interpretable structure is already visible from activation geometry before training another neural dictionary? Our intuition is simple: many interpretable directions are selective on tokens, and these directions should look less Gaussian than random directions. We therefore revisit independent component analysis (ICA), a classical method for finding non-Gaussian directions, as a compact lens for language-model interpretability. We find that ICA has been underestimated for LLM interpretability, because prior uses often relied on off-the-shelf ICA implementations that are brittle on LLM activations and lacked systematic tools for inspecting and evaluating the recovered directions. To bridge these gaps, we introduce ICALens, the first practical workflow for stable, efficient, and auditable ICA analysis of LLM representations. It combines an optimized GPU-parallel FastICA pipeline with LLM-specific stability recipes and better fitting diagnostics, enabling efficient and reliable layer-wise analysis. Across GPT-2 Small, Gemma 2 2B, and Qwen 3.5 2B Base, ICALens efficiently recovers compact, human-interpretable directions without per-layer gradient-based dictionary training. On SAEBench, ICA is competitive with public SAEs in sparse probing and outperforms them in targeted probe perturbation under small-to-medium budgets. These results suggest that ICA should not be viewed as a weak baseline, but as an efficient and complementary first lens for exploring language-model representations.
