---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.22174
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2512.22174
published: 2026-04-16
authors: Muhammad Zeeshan Karamat, Sadman Saif, Christiana Chamon Garcia
---

# BitFlipScope: Scalable Fault Localization and Recovery for Bit-Flip Corruptions in LLMs

**arXiv:** https://arxiv.org/abs/2512.22174
**Authors:** Muhammad Zeeshan Karamat, Sadman Saif, Christiana Chamon Garcia

## Abstract

arXiv:2512.22174v2 Announce Type: replace-cross  Abstract: Large Language Models (LLMs) deployed in practical and safety-critical settings are increasingly susceptible to bit-flip faults caused by hardware degradation, cosmic radiation, or deliberate fault-injection attacks such as Rowhammer. These faults silently corrupt internal parameters and can lead to unpredictable or dangerous model behavior. Localizing these corruptions is essential: without identifying the affected region, it is impossible to diagnose the source of degradation, apply targeted corrective measures, or restore model functionality without resorting to costly fine-tuning or full retraining. This work introduces BitFlipScope, a scalable, software-based framework for identifying fault-affected regions within transformer architectures under two deployment scenarios. When a clean reference model is available, BitFlipScope performs differential analysis of outputs, hidden states, and internal activations for detecting anomalous behavior indicative of corruption to pinpoint or localize faults. When no reference model exists, it uses residual-path perturbation and loss-sensitivity profiling to infer the fault-impacted region directly from the corrupted model. In both settings, the framework not only enables effective fault diagnosis but also supports lightweight performance recovery without fine-tuning, offering a practical path to restoring corrupted models. Together, these capabilities make BitFlipScope an important step toward trustworthy, fault-resilient LLM deployment in hardware-prone and adversarial environments.
