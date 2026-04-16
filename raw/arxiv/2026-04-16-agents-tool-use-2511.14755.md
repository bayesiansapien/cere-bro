---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2511.14755
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2511.14755
published: 2026-04-16
authors: Albert Lin, Alessandro Pinto, Somil Bansal
---

# Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis

**arXiv:** https://arxiv.org/abs/2511.14755
**Authors:** Albert Lin, Alessandro Pinto, Somil Bansal

## Abstract

arXiv:2511.14755v2 Announce Type: replace-cross  Abstract: As perception-based controllers for autonomous systems become increasingly popular in the real world, it is important that we can formally verify their safety and performance despite perceptual uncertainty. Unfortunately, the verification of such systems remains challenging, largely due to the complexity of the controllers, which are often nonlinear, nonconvex, learning-based, and/or black-box. Prior works propose verification algorithms that are based on approximate reachability methods, but they often restrict the class of controllers and systems that can be handled or result in overly conservative analyses. Hamilton-Jacobi (HJ) reachability analysis is a popular formal verification tool for general nonlinear systems that can compute optimal reachable sets under worst-case system uncertainties; however, its application to perception-based systems is currently underexplored. In this work, we propose RoVer-CoRe, a framework for the Robust Verification of Controllers via HJ Reachability. To the best of our knowledge, RoVer-CoRe is the first HJ reachability-based framework for the verification of perception-based systems under perceptual uncertainty. Our key insight is to concatenate the system controller, observation function, and the state estimation modules to obtain an equivalent closed-loop system that is readily compatible with existing reachability frameworks. Within RoVer-CoRe, we propose novel methods for formal safety verification and robust controller design. We demonstrate the efficacy of the framework in case studies involving aircraft taxiing and NN-based rover navigation. Code is available at the link in the footnote.
