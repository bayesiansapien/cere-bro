---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.224908+05:30
arxiv_id: 2610.07018
url: https://huggingface.co/papers/2610.07018
arxiv_url: https://arxiv.org/abs/2610.07018
date: 2026-10-12
---

# When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language Models

Vision-language models (VLMs) have achieved strong performance in multimodal reasoning, yet they remain prone to generating plausible but incorrect answers. Self-verification offers a practical way to improve answer reliability without relying on external judges, but existing methods typically depend on a single verification criterion or fixed prompt, resulting in incomplete and unstable reliability estimates. We first systematically analyze how verifier capability and prompt design affect verification performance. Our findings show that stronger verifiers provide more reliable judgments, while verification performance is highly sensitive to prompt choice, with no single prompt consistently dominating across tasks. Guided by these findings, we propose MOTIVE, a Multi-View Self-VerificatiOn wiTh RelIability-Guided SelectiVE Rethinking framework for reliable multimodal reasoning. MOTIVE evaluates each candidate answer from complementary verification perspectives and learns a correctness-aligned reliability score through correctness-grounded multi-view verification learning. During inference, this score governs an accept-or-rethink decision, allowing reliable answers to be returned directly while uncertain ones trigger history-guided rethinking. Extensive experiments across diverse multimodal benchmarks and VLM backbones demonstrate that MOTIVE consistently outperforms strong self-verification and self-correction baselines. Further results show that reliable verification improves accept-or-rethink decisions and reduces unnecessary reasoning turns, enabling more reliable and efficient self-verification without an external judge.
