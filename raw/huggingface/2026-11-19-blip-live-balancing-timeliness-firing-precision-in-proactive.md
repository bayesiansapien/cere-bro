---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.142453+00:00
arxiv_id: 2611.21553
url: https://huggingface.co/papers/2611.21553
arxiv_url: https://arxiv.org/abs/2611.21553
date: 2026-11-19
---

# BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video Agents

Streaming video understanding is becoming increasingly important for real-world interactive systems. Such systems must be proactive for natural and useful human interaction: they should respond as soon as sufficient evidence becomes available while avoiding premature, redundant, or incorrect responses. We present BLIP-Live, a framework unifying data, metrics, harness, and training around a shared formulation of proactivity as effective causal response decisions balancing the two competing objectives of responding vs silence. First, we construct BLIP-Live-780K dataset containing human annotations of proactive response content and timing, which defines this desired behavior. We then propose PAUC-F, a metric to effectively measure our desired proactive behavior. PAUC-F combines existing response timeliness metrics with firing precision to reward early useful responses without rewarding excessive firing. With our desired behavior defined and measurable, we finally investigate model-agnostic inference harnesses that draw out proactive streaming capabilities of offline vision language models (VLMs), together with training pipelines that learn to further improve their proactive responsiveness. Across both settings, we find that combinations of sliding visual windows, online interaction memory, and structured response outputs consistently yield strongest proactive performance. Our experiments result in two models, with our BLIP-Live-Qwen model achieving state-of-the-art performance across four proactive streaming benchmarks, with gains up to 44% over baselines and outperforming multiple closed API models. Our code and data will be released publicly.
