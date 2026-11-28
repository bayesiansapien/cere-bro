---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34457
url: https://huggingface.co/papers/2611.34457
arxiv_url: https://arxiv.org/abs/2611.34457
date: 2026-11-27
---

# ProxyGenBench: Benchmarking Proxy-Guided Video Generation

Recent video generators produce realistic videos, yet controlling how scenes unfold remains challenging. Structural proxies, such as animated 3D blockouts, guide generation by specifying scene layout, motion, camera behavior, and event order. However, these coarse inputs leave details unspecified and may contain artifacts that should not be reproduced. Successful proxy-guided generation must therefore Preserve intended structure, Complete missing content and correct proxy artifacts, and Bind text, image, and audio conditions to the right entities and events. We introduce ProxyGenBench to study these interacting requirements, with 312 evaluation cases from 60 scenes across three scene tasks and controlled variations in proxy fidelity, text detail, and multimodal inputs. We evaluate five video generators using verified, case-specific checklists. Experiments show that proxies improve spatiotemporal control, but greater proxy detail can coincide with poorer completion, while strong structural adherence does not ensure correct binding.
