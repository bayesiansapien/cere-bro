---
source: farmer/huggingface
farmed: 2026-09-12T06:06:40.318302+00:00
arxiv_id: 2608.15380
url: https://huggingface.co/papers/2608.15380
arxiv_url: https://arxiv.org/abs/2608.15380
date: 2026-09-12
---

# Adaptive Bridge: A Proxy-Based Decoupling Layer for Mitigating DDS Backpressure in ROS 2

In systems built on Robot Operating System 2 (ROS 2) and using Data Distribution Service (DDS), a single network-impaired or throttled subscriber on a RELIABLE topic can cause backpressure that degrades throughput and latency for all other subscribers, including safety-critical ones sharing the publisher, because the publisher's DDS writer can no longer accept new samples. We present Adaptive Bridge, a proxy-based layer that decouples critical subscribers from degraded or noncritical ones, thereby isolating the critical path through topic splitting and dynamic rate control. The proxy acts as a middleman and subscribes to the original topic and republishes the messages to two independent DDS writers: one RELIABLE writer for critical nodes and one BEST EFFORT writer for noncritical or degraded nodes, thus isolating the degraded nodes and safeguarding the publisher and critical nodes from backpressure. A probe-based classifier actively monitors subscriber health through sampling with hysteresis and adjusts subscriber rate limits in real time. We evaluate the system under a Gilbert-Elliott bursty wireless loss model using a reproducible Docker-based harness. The results show that using the Adaptive Bridge in our evaluation harness reduces the critical subscriber tail p95 latency from up to 15 s to 1.55 ms across all impairment severities while preserving the publisher's configured throughput.
