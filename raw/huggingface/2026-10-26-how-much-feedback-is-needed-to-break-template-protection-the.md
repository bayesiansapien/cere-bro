---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801739+00:00
arxiv_id: 2610.25118
url: https://huggingface.co/papers/2610.25118
arxiv_url: https://arxiv.org/abs/2610.25118
date: 2026-10-26
---

# How Much Feedback Is Needed to Break Template Protection? The Geometric Vulnerability of Biometric Authentication

Biometric authentication systems increasingly use privacy-preserving mechanisms to protect sensitive templates. However, the authentication interface itself may still leak information that enables reconstruction attacks. Prior attacks exploit released similarity scores, whereas more advanced systems reveal only the binary accept/reject decision. This binary feedback provides substantially less information, making template reconstruction far more challenging.
  In this work, we introduce query-efficient reconstruction attacks under extremely limited feedback, addressing two key limitations of prior attacks. First, we introduce the first attack that reconstructs protected biometric templates using only authentication success/failure feedback by exploiting the geometric constraints of biometric authentication. Second, we introduce distribution-aware query-efficient reconstruction methods for score-releasing systems, achieving a more realistic threat model by reducing the number of required queries by a factor of 5times compared to recent prior score-based attacks. Finally, we combine these two insights by incorporating a pretrained facial diffusion prior into our geometric binary attack, reducing the number of required queries by a factor of 5times.
  Our findings reveal a fundamental security limitation of biometric authentication: independently of the template protection mechanism, the authentication process itself exposes geometric information that can enable perfect template reconstruction up to numerical precision. Moreover, the distribution of biometric templates can be leveraged to make significantly more effective reconstruction attacks.
