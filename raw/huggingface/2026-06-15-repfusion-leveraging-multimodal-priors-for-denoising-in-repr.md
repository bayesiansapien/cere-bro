---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14700
url: https://huggingface.co/papers/2606.14700
arxiv_url: https://arxiv.org/abs/2606.14700
date: 2026-06-15
---

# RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space

Large language models (LLMs) are widely used in text-to-image (T2I) systems, but they are typically limited to text encoding, while denoising is handled by newly trained generative backbones. The emergence of representation autoencoders (RAEs) shifts the generation target toward semantically structured visual representations, creating a latent space that is more compatible with pretrained LLM priors. Inspired by multimodal LLMs (MLLMs), where an MLP projector is sufficient to align clean visual representations with a pretrained LLM, we repurpose the MLLM itself as a noisy representation encoder, extending this mechanism from clean to noisy inputs. We present RepFusion, which uses the resulting MLLM outputs as the conditioning signal for a diffusion transformer. In controlled comparisons at similar inference budgets, RepFusion outperforms baselines that devote comparable capacity to newly initialized denoisers. These results demonstrate that MLLMs provide strong priors for denoising visual representations and that, by conditioning on evolving noisy representations, test-time compute can be productively spent on repeated MLLM conditioning in modern T2I systems.
