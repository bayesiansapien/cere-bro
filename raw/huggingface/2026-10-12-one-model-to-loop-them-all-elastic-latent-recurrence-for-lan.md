---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.223723+05:30
arxiv_id: 2610.12582
url: https://huggingface.co/papers/2610.12582
arxiv_url: https://arxiv.org/abs/2610.12582
date: 2026-10-12
---

# One Model to Loop Them All: Elastic Latent Recurrence for Language Models

A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count. At one loop, however, such models typically fall well short of a non-recurrent model of the same size, a one-loop tax that makes a separate non-recurrent model the better choice whenever latency matters. We present Elastic Latent Recurrence (ELR), a recipe for training looped language models without this tax. At one loop, an ELR model costs the same to serve as a non-recurrent model of the same size and, trained on the same data, reaches similar accuracy. Each additional loop then buys more accuracy for more inference compute. Three choices make this work: a gated state update with a learned step size, loop counts mixed within each optimizer update, and conditioning each pass on its loop index and budget. The first two preserve one-loop accuracy, and the third lowers loss at every additional loop. Mixed depths can be introduced late in pretraining to limit the added training cost, and with zero-initialized conditioning added at the switch, this late schedule reaches lower loss than mixed-depth training from scratch. In MoE models, reusing first-loop expert routes on later loops cuts mixed-depth update time by 11.7% with no measurable change in accuracy. At inference, keeping only the last loop's attention KV cache holds attention KV memory at its one-loop level while retaining most of the gain from additional loops. On 4B dense and 30B-A3B MoE hybrid models, ELR at one loop is 0.52 points below and 1.04 points above its matched baseline on a ten-task average, and four loops add 7.25 and 4.75 points. Carried through post-training, the recipe yields Koi-4B, a single checkpoint that scores an estimated 18 on the Artificial Analysis Intelligence Index at one loop, matching Qwen3.5-4B, and 29 at four loops.
