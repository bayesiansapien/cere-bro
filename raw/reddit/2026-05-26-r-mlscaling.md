# r/MLScaling | 2026-05-26 IST | sort=new
> Scraped 2026-05-26 10:15 IST | lookback=24h | tier_default=1
> Gwern-flavored sub on scaling laws + frontier evals. Low volume but extremely high signal. Take everything.

### "Advancing Mathematics Research with AI-Driven Formal Proof Search", Tsoukalas et al 2026

**Meta:** score=8 · comments=0 · tier=1 · flair=R, T, Emp, G, RL · posted=2026-05-26 00:15Z
**Author:** u/gwern
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tnqjvp/advancing_mathematics_research_with_aidriven/](https://www.reddit.com/r/mlscaling/comments/1tnqjvp/advancing_mathematics_research_with_aidriven/)
**Link:** [https://arxiv.org/abs/2605.22763#deepmind](https://arxiv.org/abs/2605.22763#deepmind)

---

### "[Google's] tokens...consumed by its services has risen to 3.2 quadrillion a month, up from 480trn a year ago"

**Meta:** score=13 · comments=1 · tier=1 · flair=N, G, Econ · posted=2026-05-26 00:06Z
**Author:** u/gwern
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tnqbzx/googles_tokensconsumed_by_its_services_has_risen/](https://www.reddit.com/r/mlscaling/comments/1tnqbzx/googles_tokensconsumed_by_its_services_has_risen/)
**Link:** [https://www.economist.com/business/2026/05/20/google-is-dethroning-openai-as-the-king-of-consumer-ai](https://www.economist.com/business/2026/05/20/google-is-dethroning-openai-as-the-king-of-consumer-ai)

---

### Training on interruptible GPUs without losing runs when one gets reclaimed

**Meta:** score=0 · comments=0 · tier=1 · posted=2026-05-25 20:48Z
**Author:** u/you_dont_know_me_25
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tnlfs5/training_on_interruptible_gpus_without_losing/](https://www.reddit.com/r/mlscaling/comments/1tnlfs5/training_on_interruptible_gpus_without_losing/)

If you train on interruptible capacity, you know the pain: an instance gets reclaimed or crashes mid-run, you lose hours of progress, and then you babysit the next attempt so it doesn't happen again.

I built something that makes the run survive it. If a GPU dies, your training keeps going and finishes — you don't restart, you don't babysit. Premium-tier reliability on interruptible-priced hardware: start a job, walk away, come back to a finished model. Your existing script runs unchanged.

Would love this community's take on whether that changes what you'd be willing to run on interruptible capacity. Disclosure: I built it — invite-only beta → [https://vaultlayer.cloud/](https://vaultlayer.cloud/)

---

### Building a production-ready image translation pipeline for marketplace images — need advice on reducing latency

**Meta:** score=2 · comments=6 · tier=1 · posted=2026-05-25 16:53Z
**Author:** u/AfternoonNew5909
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tnewfd/building_a_productionready_image_translation/](https://www.reddit.com/r/mlscaling/comments/1tnewfd/building_a_productionready_image_translation/)

&amp;#x200B;

I’m building an image translation feature for marketplace/e-commerce images.

Example:

User uploads a product image with English text/specs → selects a target language → gets the same image back with translated text while preserving the original layout/design.

Current pipeline:

GPT-4.1 handles image understanding + translation

GPT-image-2 performs text replacement on the image

Current performance:

Translation: \~8–15s

Image processing: \~40s–1.5min per image

The output quality is actually decent, including text placement/layout.

The main problem is latency.

In production, users may process multiple marketplace images in batches, so the current pipeline feels too slow and expensive to scale.

I also experimented with a Canvas/Fabric.js rendering approach, but maintaining consistent quality across different image styles/layouts became difficult.

Goals:

Reduce processing time significantly

Support batch image processing

Keep output quality/layout consistency

Support multilingual translations at scale

Ideally move closer to near real-time performance

Would love suggestions on:

Faster alternatives to GPT-image-2

Better architectures for production-scale image localization

Whether OCR + manual rendering is a better long-term approach

Hybrid workflows others are using in production

Current stack:

Azure AI Foundry

GPT-4.1

GPT-image-2

Would really appreciate insights from anyone working on image localization, OCR pipelines, or multilingual marke

[…truncated, see permalink]

---

### The Dark Between the Stars: AI Interpretability is a Revolutionary Skill

**Meta:** score=8 · comments=2 · tier=1 · posted=2026-05-25 12:37Z
**Author:** u/Better-Date3020
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tn7x55/the_dark_between_the_stars_ai_interpretability_is/](https://www.reddit.com/r/mlscaling/comments/1tn7x55/the_dark_between_the_stars_ai_interpretability_is/)
**Link:** [https://micahbornfree.substack.com/p/the-dark-between-the-stars-ai-interpretability](https://micahbornfree.substack.com/p/the-dark-between-the-stars-ai-interpretability)

---

### how to build AI Systems that optimize Happiness (for AI Researchers)

**Meta:** score=0 · comments=1 · tier=1 · flair=R · posted=2026-05-25 11:02Z
**Author:** u/Which_Pitch1288
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tn5som/how_to_build_ai_systems_that_optimize_happiness/](https://www.reddit.com/r/mlscaling/comments/1tn5som/how_to_build_ai_systems_that_optimize_happiness/)
**Link:** [https://i.redd.it/0ms7iebbm93h1.png](https://i.redd.it/0ms7iebbm93h1.png)

---
