---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24791
url: https://huggingface.co/papers/2610.24791
arxiv_url: https://arxiv.org/abs/2610.24791
date: 2026-10-20
---

# UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling

Unified audio-video creation requires a single model capable of text-conditioned joint synthesis, bidirectional cross-modal generation, and instruction-guided editing across both modalities. Existing methods rely heavily on paired corpora, which are scarce for joint generation and even rarer for editing. Consequently, they are spent learning single-branch generative and editing capabilities that abundant unimodal data could readily teach, rather than on the cross-modal coupling. Furthermore, prevailing systems apply a single shared noise schedule to both modalities, neglecting two critical limitations. First, due to the significant discrepancy in information density, video requires prolonged high noise to organize spatial and motion structure, whereas the sparser audio signal can settle earlier during the synthesis process, the dynamics a uniform schedule might compromise. Second, lockstep denoising leaves asymmetric workflows, such as conditioning on one modality to synthesize or edit another, untrained. We present UniAVC, which addresses both obstacles. It first trains each branch on unimodal dataset to full generative and editing competence, and subsequently dedicates paired data to exploit cross-modal correspondence. Modality-decoupled schedulers meanwhile warp the noise schedule independently from a shared timestep, while subtasks with one clean modality directly supervise asymmetric configurations. These settings respectively enable intent-aware editing, which preserves one modality intact while enlisting it to constrain the other, and post-inference self-refinement, which regenerates only an unsatisfactory branch against an accepted one. UniAVC thus spans multiple creation tasks from a single set of weights without task-specific adapters.
