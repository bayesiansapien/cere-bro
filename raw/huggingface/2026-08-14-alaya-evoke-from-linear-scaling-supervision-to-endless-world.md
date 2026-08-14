---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.13546
url: https://huggingface.co/papers/2608.13546
arxiv_url: https://arxiv.org/abs/2608.13546
date: 2026-08-14
---

# Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state and redesigning the teacher for long-horizon interactive generation. Scene geometry is maintained in an external, camera-indexed world state bank, from which only view-relevant information is retrieved, keeping the denoiser context bounded as the session grows. Rather than treating the teacher as a fixed generator, we design it for long-horizon supervision: its sparse attention combines chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state, yielding linear growth in memory and compute while enabling supervision over long horizons. Such supervision exposes content drift that stays locally plausible within short windows, while per-chunk conditioning enables prompt changes and event control throughout the sequence. A 30-second distribution-matching objective, applied under self-forced rollouts, transfers both capabilities to a three-step student that uses no classifier-free guidance, improving resistance to long-term drift while preserving responsive conditioning. With bounded context and recurrent external memory, Evoke supports open-ended, continuously evolving generation; on a single H200 at 384times 640, each 1.5,s chunk is generated in 2.11,s. As a three-step world model, Evoke achieves state-of-the-art performance on WBench while remaining competitive on VBench-Long and VBench-2.0.
