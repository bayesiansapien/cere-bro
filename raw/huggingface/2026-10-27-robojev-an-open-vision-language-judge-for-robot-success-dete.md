---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33718
url: https://huggingface.co/papers/2610.33718
arxiv_url: https://arxiv.org/abs/2610.33718
date: 2026-10-27
---

# RoboJev: An Open Vision-Language Judge for Robot Success Detection

Many robot manipulation videos do not indicate whether the task was successfully completed. RoboJev-27B is an open-weight vision-language model that takes a task instruction, 10 frames of a manipulation attempt, and (if available) final frames from auxiliary cameras and predicts whether the robot accomplished the task. RoboJev-27B is a variant of JEV-27B-VL, trained with a rank-32 LoRA adapter on the language model only (keeping the vision encoder frozen) using 52,598 episode records. It also uses a source-specific KL penalty that applies only to research data, anchoring predictions closer to the original model on those sources. It uses a calibrated two-token readout that outputs success/failure probabilities in a single forward pass. On 268 held-out episodes of the same robot model (SO-101), RoboJev-27B attains 95.2% balanced accuracy and 0.993 AUROC. It also generalises to episodes collected by unseen labs/robots (AUROC = 0.890 over 459 episodes) as well as to clearly labelled community-collected episodes (accuracy = 93.3% over 135 episodes), where the base model attains an AUROC = 0.900 on the unseen-lab/robot subset with the same inputs. It takes 0.26 seconds per episode (median, serial) to infer on a single H100, which is about \0.19 per 1,000 success predictions at 2.69 per GPU-hour (not including media processing and serving costs). RoboJev-27B is released together with its inference code, along with a transparent evaluation: 20,628 predictions organized into 29 model/protocol entries are made available to facilitate browsing and to enable reproducible benchmarking of success detection. We also compare against strong API-based frontier VLMs, which take in fewer input frames (4 images from the primary camera only); note that this comparison is not strictly like-for-like because RoboJev-27B is given more frames at inference.
