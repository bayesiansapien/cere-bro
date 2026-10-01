# Robotic factories that build robots

**Channel:** Y Combinator
**Published:** 2026-09-28
**Source:** https://www.youtube.com/watch?v=aNWKngrCrw4

## TL;DR
Tensr (spelled "Tensor" in the auto-captions), a YC startup founded by Berkeley robotics researchers, runs a 12,000 sq ft Bay Area contract factory that manufactures other companies' robot designs, from humanoids to end effectors to ISS hardware. The pitch: "the TSMC of robotics," where every customer order is a data point that makes the factory's own automation better. Short promo clip; the "self-learning factory" claim is aspirational, not demonstrated.

## Key Takeaways
- **Business model:** foundry, not product. Customers bring designs, Tensr makes them mass-manufacturable and builds them.
- **Current output:** full humanoids (Asimov 1, 275+ parts across injection-molded casings, CNC metal, PCBs, actuators), a Berkeley AI Research-derived smart suction gripper that senses grip quality internally, and space-station robots.
- **Speed:** went from robots in an apartment to a running factory within one YC batch.
- **Team pedigree:** ex-Berkeley autonomous Indy car racing (160 mph) plus manufacturing backgrounds.
- **Core thesis:** "the factory is a learning data machine." Each order is treated as an experiment that improves the next run.

## Architecture & Optimization Mechanics
- The data flywheel they describe logs design errors, procurement forecasts, retooling jobs and robot motion traces, then feeds failures back into subsequent runs. Functionally this is online learning over a manufacturing process, analogous to profile-guided optimization for hardware.
- End-state goal is a "dark factory" where capacity is provisioned on demand like cloud compute ("AWS of manufacturing"), with order-to-ship in 24 hours.
- The DFM (design for manufacturing) step, turning lab prototypes into producible parts, is the actual near-term moat. The ML flywheel is unproven at this scale.

## Grounded Context (Web Enrichment)
Web sources confirm the company is **Tensr**, co-founded by Eric Berndt (CEO), Adith Sundram (CTO) and C.K. Wolfe, all Berkeley robotics researchers. Coverage of the factory launch frames it the same way as the video: a physical cloud where robots operate conventional industrial machinery, package and ship. No independent data yet on yields, throughput or how much of the line is actually autonomous today.

The Asimov 1 humanoid it builds is an open-source design (1.2 m, 35 kg, 25 actuated DoF, Raspberry Pi 5 plus Radxa CM5 compute, CERN OHL-S hardware licence) with a DIY kit targeting ~$15,000. That context matters: Tensr is manufacturing an open reference design, which is a good fit for a contract-foundry model but also means low differentiation per unit.

Sources: [Tensr](https://www.tensr.com/), [RuntimeWire](https://runtimewire.com/article/tensr-launches-autonomous-robot-factory), [C.K. Wolfe](https://ckwolfe.org/media/tensor-yc/), [Hackaday: Asimov](https://hackaday.com/2026/05/16/asimov-is-an-open-source-humanoid-robot-for-the-rest-of-us/), [Open Source For You](https://www.opensourceforu.com/2026/05/asimov-v1-open-sources-humanoid-robotics-development/).

## Real-World Application / Actionable Step
- **Low direct relevance to compression/routing.** File as a signal for the embodied-AI supply chain.
- **Edge inference angle:** Asimov-class robots run on Raspberry Pi 5 / CM5-level compute. That is a concrete target for aggressive quantization (INT4/INT8) and distillation of VLA policies. Worth tracking as a deployment benchmark for small-model work.
- **Investment lens:** robot contract manufacturing is a picks-and-shovels play if humanoid volumes ramp. Watch for Tensr's next funding round as a demand indicator.
