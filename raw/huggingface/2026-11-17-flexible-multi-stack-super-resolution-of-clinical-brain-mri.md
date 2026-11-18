---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.115004+00:00
arxiv_id: 2611.21412
url: https://huggingface.co/papers/2611.21412
arxiv_url: https://arxiv.org/abs/2611.21412
date: 2026-11-17
---

# Flexible Multi-Stack Super-Resolution of Clinical Brain MRI Using Hetero-Orientation Variational Encoding: Expert Reader Evaluation in a Nigerian Cohort

High-resolution brain MRI is important for neuroradiological assessment, yet routine clinical protocols often rely on fast, anisotropic 2D acquisitions, particularly in resource-constrained settings. These acquisitions may differ in orientation, alignment and anatomical coverage, resulting in partially overlapping image stacks. Existing learning-based super-resolution methods typically rely on single, under-constrained inputs or fixed multi-stack configurations with idealised acquisition geometry. We introduce MS-HVED, a sequence-agnostic framework for flexible multi-stack brain MRI super-resolution. Available axial, coronal and sagittal stacks are independently encoded into multi-scale Gaussian posteriors and fused using a field-of-view-aware Product-of-Gaussians formulation that limits contributions from unsupported regions. Physics-informed domain randomisation simulates heterogeneous clinical acquisition conditions, including obliqueness, partial coverage and imaging artefacts. MS-HVED achieved competitive or superior reconstruction fidelity across synthetic benchmarks and improved downstream tissue segmentation relative to low-resolution inputs. To assess generalisation beyond the training cohorts, we performed external clinical validation on 30 routine brain MRI examinations from a Nigerian cohort, representing an under-represented population in medical imaging research. These examinations formed the largest component of a blinded reader study involving 44 real cases and seven expert neuroradiologists. In the Nigerian cohort, MS-HVED was preferred over the supervised baseline for overall image quality in 187 of 210 paired assessments. Across all clinical cohorts, MS-HVED achieved higher overall-quality scores with all available inputs (5.93 vs. 4.49, p<.001), with the preference persisting when axial or coronal inputs were omitted (p<.001). Code at github.com/cai4cai/ms-hved
