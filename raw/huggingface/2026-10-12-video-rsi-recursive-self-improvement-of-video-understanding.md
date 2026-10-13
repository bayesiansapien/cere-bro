---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.221563+05:30
arxiv_id: 2609.37950
url: https://huggingface.co/papers/2609.37950
arxiv_url: https://arxiv.org/abs/2609.37950
date: 2026-10-12
---

# Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video understanding agent uses its own language model to revise its harness. Through active video investigation, the model revisits the original training videos to test competing failure explanations with additional observations, grounding proposed changes in evidence beyond the existing trace. Cost-aware harness evolution turns these diagnoses into reusable revisions and determines which revisions to retain by considering both answer accuracy and visual cost. Across our evaluation settings on video understanding benchmarks, the evolved agent improves accuracy while processing fewer frames and achieves competitive accuracy-efficiency trade-offs against existing video understanding agents. These results demonstrate the potential for video understanding agents to improve their own evidence acquisition and use through harness evolution. Code is available at https://github.com/bingjunluo/Video-RSI .
