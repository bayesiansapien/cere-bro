---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928149+00:00
arxiv_id: 2609.33757
url: https://huggingface.co/papers/2609.33757
arxiv_url: https://arxiv.org/abs/2609.33757
date: 2026-09-29
---

# YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality

Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. A single AR-NAR Mixture-of-Transformers (MoT) first writes a readable score specifying melody and harmony, expands it into semantic music tokens, and realizes it as full-song audio. In comparisons using the same checkpoint, experts prefer symbolic planning for overall quality and musicality, with 49.3% of overall preferences versus 34.6% without planning. Experts also favor the unified model over a separate language model and diffusion Transformer. On WildSongBench, YuE2 scores 6.73 on SongBench Global Avg, exceeding all evaluated public baselines. Selecting from eight candidates (best-of-8), YuE2 reaches 6.96, the highest observed mean among all evaluated systems. Expert listening further establishes its competitiveness with proprietary song generators, favoring best-of-8 over Suno v4.5 and yielding nearly balanced preferences against Suno v5. To learn this generation process from recordings without aligned scores, we introduce MERT2 and SheetSage2 to supply semantic and symbolic supervision. MERT2 sets a new state of the art in music representation learning, surpassing previous best results on 14 of 15 MARBLE metrics; SheetSage2 leads 12 of 15 benchmark-metric pairs in our lead-sheet transcription comparison. The same checkpoint follows score edits while largely preserving unedited musical content and generates zero-shot covers without cover-specific training. Its readable score also enables agentic music editing, with external language models translating user feedback into revisions of the composition.
