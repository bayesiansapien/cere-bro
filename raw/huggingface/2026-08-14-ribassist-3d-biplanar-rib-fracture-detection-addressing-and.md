---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.06914
url: https://huggingface.co/papers/2608.06914
arxiv_url: https://arxiv.org/abs/2608.06914
date: 2026-08-14
---

# RibAssist 3D: Biplanar Rib-Fracture Detection, Addressing, and Selective 3D Localization from CT-Derived Projections

Rib fractures are common and time-consuming to localize on computed tomography (CT). We ask whether fractures detected independently in two orthogonal CT-derived projections (anteroposterior and lateral) can be paired across views and triangulated into reliable 3D points at a controlled rate of false outputs, and we answer it with a staged diagnostic study. The projection geometry is exact, and given correct correspondence, localization is accurate (median 4.0 mm, 88% within 10 mm, 93.6% rib-exact). On a sealed 55-case cohort, a large share of fractures is in principle recoverable (61.1% dual-view availability, and a correct pair present in the candidate graph for 58.4% of fractures), yet the binding limitation is neither geometry nor localization but confidence-limited cross-view correspondence. A controlled detector-by-correspondence factorial attributes the operational gain to lateral-detector quality rather than the tested matching methods; retraining the lateral detector produces the first nonzero controlled-budget reconstructions. Under a deliberately conservative commitment policy, a pre-specified sealed pass promotes 15 of 601 fractures to correct 3D localizations at 0.436 false points per case (2.50% end-to-end commitment yield), and committed points are accurate (median 1.49 mm, 93% rib-exact). The low yield is a consequence of confidence-gated abstention, not of geometry or detection: the study establishes a reproducible framework for selective 3D localization and identifies cross-view correspondence as the dominant operational bottleneck.
