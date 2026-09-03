---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.01925
url: https://huggingface.co/papers/2609.01925
arxiv_url: https://arxiv.org/abs/2609.01925
date: 2026-09-03
---

# CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing

The attention prefilling phase of long-context LLM inference scales quadratically, making self-attention a severe computational bottleneck. Traditional sparse attention methods mitigate this through fixed patterns or offline profiling, but lack the flexibility to adapt to input-dependent attention structure. Recent dynamic methods address this by routing heads to sparse patterns in real-time, but rely on indirect routing proxies with overhead and budget allocation mechanisms that overlook the post-softmax mass hierarchy. We present CRISP (Cliff-awaRe Input-adaptive Sparse Prefilling), which identifies and addresses two structural challenges in this dynamic routing paradigm. First, we show that the routing decision can be read directly off the structure of the proxy attention map. We replace the Jensen-Shannon Divergence (JSD) routing with C_struct, a structural proxy that measures mass at Vertical-Slash compatible positions and reproduces JSD's routing decisions while eliminating both the pooled matmul and subsequent KL divergence overhead. Second, we formalize the post-softmax mass cliff and demonstrate theoretically that strictly cumulative coverage thresholds accumulate O(n) background noise at long contexts. CRISP navigates this via a sink-aware threshold grounded in the noise floor. Empirically, across InfiniteBench, RULER and LongBench on two model families, CRISP is the strongest sparse method overall and matches or exceeds exact dense attention on retrieval-heavy benchmarks, recovering up to +28.0 pp on retrieval tasks over baselines and achieving up to a 5.30x attention speedup at 512k tokens, driven primarily by our O(n) noise elimination during selection while preserving structural integrity.
