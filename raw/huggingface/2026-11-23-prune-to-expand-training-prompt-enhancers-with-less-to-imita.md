---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.251538+00:00
arxiv_id: 2611.27229
url: https://huggingface.co/papers/2611.27229
arxiv_url: https://arxiv.org/abs/2611.27229
date: 2026-11-23
---

# Prune to Expand: Training Prompt Enhancers with Less to Imitate

Prompt enhancement (PE) refines concise user prompts into detailed descriptions to improve the compositional aesthetics of generated images while preserving user intent. A common practice constructs supervised fine-tuning (SFT) pairs by deriving short, user-like prompts from dense captions, implicitly assuming that captions that improve image generation also provide effective supervision. In this paper, however, we uncover a counterintuitive finding: PE models trained on caption pairs with substantial generation gains perform comparably to those trained on pairs with only marginal gains. We argue that dense captions can impose redundant supervision by requiring PE models to reproduce image-specific details weakly related to user intent. Motivated by this discrepancy, we introduce Prune to Expand (P2E), a simple text-only method that refines dense-caption supervision by selectively removing redundant sentences under a per-example deletion bound while preserving explicit user requirements and informative visual structure. Extensive experiments under identical training configurations demonstrate that P2E improves alignment with human preferences and visual quality over conventional dense-caption SFT across diverse image categories and visual generators.
