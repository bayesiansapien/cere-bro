---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.29429
url: https://huggingface.co/papers/2609.29429
arxiv_url: https://arxiv.org/abs/2609.29429
date: 2026-09-25
upvotes: 2
---

# Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures

Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed label per call. Jev, a model trained with reinforcement learning for calibrated decisions (RLCD), answers many typed questions about one input with calibrated probabilities in a single call. Whether it detects alignment failures has not been measured. We present RLCDAlignBench, which benchmarks Jev on ten alignment failures: sycophancy, jailbreaks, deception, prompt injection, hallucination, privacy violation, social bias, reward hacking, concealing uncertainty, and power seeking. It spans 44 benchmarks and five target models, labelled by each benchmark's scorer and, on two, by humans. Many of these failures are relational, defined against a reference, such as the user's belief or an injected instruction, that the response alone does not reveal. Our key idea is therefore to vary what Jev is asked separately from what it sees: the question's wording and answer type on one side, the fields of the input on the other. A single generic question reaches a median AUROC of 0.886 zero-shot and beats supervised baselines on most benchmarks. Question wording matters little, while context matters more, mostly through fields that encode the label. Jev matches the reference scorer's agreement with human labels, surfaces label defects in existing benchmarks, and costs 63x less than LLM-judge scorers. Code and data: https://github.com/sumleo/RLCDAlignBench.
