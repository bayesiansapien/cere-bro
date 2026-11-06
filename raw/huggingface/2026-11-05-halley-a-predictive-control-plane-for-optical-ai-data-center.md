---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.298912+00:00
arxiv_id: 2611.04408
url: https://huggingface.co/papers/2611.04408
arxiv_url: https://arxiv.org/abs/2611.04408
date: 2026-11-05
---

# Halley: A Predictive Control Plane for Optical AI Data Center Networks

A frontier AI model is trained in an AI data center, on tens of thousands of accelerators joined by a dedicated network, and every training step ends with all of them exchanging data at once. Between racks, that network is optical, and each of its four layers, from lasers to switches, runs a fixed or after-the-fact policy. Lasers sharing an enclosure, cooling, and power can fail together. At a fixed spare ratio, correlated failure provably caps a pool's availability however large it grows. In this paper, we present a comprehensive predictive control plane framework, called Halley, that reads each resource's next state and acts before the failure occurs. It has four components, each carrying a formal guarantee: LightReserve that sizes the laser pool to provide a coverage bound, FoldFit that schedules the switch within 11/9 of the optimal, ThermaLead that holds a microring with one-step-ahead control, and TriageGuard that protects the highest-risk modules first. Halley gives each layer a predictive controller that defers to the deployed policy when unsure. Composed from simulations at that point, effective goodput, the share of ideal throughput kept, rises from 65.2\% to 76.5\% if a window that exhausts its spares is lost. If only the dark channels' bandwidth is lost, it reaches 67.4\%. Per megawatt, that is up to 1.03--1.17 times the training; for the same training, up to 3.3--14.7\% less data center capacity. Halley's fallback circuits are formally verified and are shown to achieve close timing on a commercial FPGA, and pass a 130~nm signoff.
