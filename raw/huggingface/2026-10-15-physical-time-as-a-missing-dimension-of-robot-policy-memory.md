---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.232327+05:30
arxiv_id: 2610.20524
url: https://huggingface.co/papers/2610.20524
arxiv_url: https://arxiv.org/abs/2610.20524
date: 2026-10-15
---

# Physical Time as a Missing Dimension of Robot Policy Memory Dynamics

Existing robot policy memories typically evolve with observation sequences, implicitly treating each update as the same amount of physical time. Yet identical observation histories can span different durations and require different actions, exposing physical time as a missing dimension of policy memory. We introduce Temporal Flow Policy (TFP), which learns memory dynamics to retain past events and evolve the memory state over measured time intervals. Observations and prior memory determine the content and time scales of each transition; elapsed time determines how far the state advances. TFP conditions diffusion and flow-matching policies through this memory state and is trained with their native imitation objectives. We evaluate TFP with Diffusion Policy and π_{0.5} through controlled comparisons of memory designs. These experiments show that successful timing depends on both measured intervals and retained history. TFP achieves higher average success than the recurrent and state-space memories we equip with the same intervals and than a variant that feeds the interval to a learned gate. Memory readouts recover the time since an event and motion information after occlusion. Changing the supplied intervals systematically delays or advances actions, linking time inputs to behavior. Real-robot tasks requiring timing or memory, together with LIBERO evaluations, demonstrate benefits in physical and general manipulation. These results suggest viewing robot memory not as stored observation history, but as a state that retains past events and evolves with physical time.
