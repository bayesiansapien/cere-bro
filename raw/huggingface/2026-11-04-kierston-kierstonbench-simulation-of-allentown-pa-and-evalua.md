---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.367091+05:30
arxiv_id: 2611.04785
url: https://huggingface.co/papers/2611.04785
arxiv_url: https://arxiv.org/abs/2611.04785
date: 2026-11-04
---

# Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language Models in Crime Investigation and Surveillance Tasks

Large language models are candidates for collecting and analyzing records in criminal investigations and mass surveillance. Their capability and accuracy in this work cannot currently be measured. Real deployments lack the ground truth needed to score a model's conclusions, and no benchmark evaluates these capabilities in a simulated environment. We present Kierston, a city-scale simulation engine, and KierstonBench, a benchmark that tests these capabilities against known simulated events. Kierston models approximately 125,000 residents of Allentown, Pennsylvania, generating their daily activities and the telecommunications, financial, administrative and license-plate records that surveillance and investigative systems collect about them. These records derive from a common behavioral timeline and are distributed across sources representing separate providers. Models investigate through a restricted records interface, linking observations across sources without access to the underlying simulation. The benchmark comprises 32 task families covering record linkage, routine reconstruction, incident investigation and assessment of deceptive accounts. In an evaluation of sixteen language models, most could not perform records investigation and submitted identifications the records did not support. A small number of frontier models solved most of the tasks and abstained when evidence was insufficient. In some cases these models still fell for common deceptions and assumptions, and none replaced an investigator.
