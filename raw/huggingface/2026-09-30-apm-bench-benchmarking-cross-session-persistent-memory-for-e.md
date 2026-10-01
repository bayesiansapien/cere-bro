---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37559
url: https://huggingface.co/papers/2609.37559
arxiv_url: https://arxiv.org/abs/2609.37559
date: 2026-09-30
---

# APM-Bench: Benchmarking Cross-session Persistent Memory for Egocentric Streaming Video Assistants

To serve as real-world personal assistants, streaming video models need persistent memory that retains past experiences for later use. Yet existing streaming benchmarks and methods often focus on individual continuous videos or short clips, overlooking that real-world interactions are often intermittent and require memory to persist across interruptions. To fill this gap, we introduce APM-Bench, which reformulates real-world streaming interaction as multi-session life trajectories. It contains 549 sessions, 104 trajectories, and 2,719 candidates, spanning both objective and open-ended questions. Each session is a video with fine-grained annotations, and sessions within a trajectory revolve around related activities. Models then use persistent memory to answer questions about past sessions and provide proactive responses while maintaining real-time interaction. This raises challenges: persistent memory must be storable, selectively retain information, be injected at the right time, and remain efficient. Moreover, finite storage may leave required evidence unavailable, so assistants should recognize missing evidence. Therefore, we systematically evaluate general video models under different memory protocols and diverse specialized streaming memory systems, and test whether models acknowledge insufficient evidence. Our evaluation reveals a clear utility--latency--storage trade-off: existing methods still struggle to simultaneously achieve reliable long-term recall, low overhead, and effective proactive assistance across sessions. APM-Bench provides a comprehensive testbed for developing and comparing persistent memory systems under realistic streaming conditions. We hope it encourages future work that jointly considers utility, latency, and storage toward more practical persistent memory for real-world streaming assistants.
