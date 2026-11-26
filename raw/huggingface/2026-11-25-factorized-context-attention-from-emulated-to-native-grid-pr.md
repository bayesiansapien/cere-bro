---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32423
url: https://huggingface.co/papers/2611.32423
arxiv_url: https://arxiv.org/abs/2611.32423
date: 2026-11-25
---

# Factorized Context Attention: From Emulated to Native Grid Probing

Models read a book, an hour of video, or an image in one forward pass. As the context grows, this pass slows down, loses accuracy, and stops at the context window. Sparse attention is efficient, but keeps the other two limitations. Grid probing, a recent training-free method, recovers the accuracy and extends the reach by asking a frozen model the same question about short local and strided spans of the input, but every question repeats the whole computation, since each span is encoded again. Our insight is that grid probing is emulated attention, an attention pattern reproduced from outside the model through prompts, since each probe only restricts which part of the input the question can see. We introduce Factorized Context Attention (FCA), a training-free block-sparse attention that runs the same pattern natively, as the attention of the model itself. FCA encodes the input once into a KV cache, reads all spans as masked sequences in one batched forward, and uses a stair position schedule to keep every span inside the trained position range. Across long video understanding, long-context text inference and image grounding, FCA matches the accuracy and the reach of grid probing at a fraction of its cost. It gains about 10 points over the single pass on long video and 9 to 14 points on long novels, finds needles in videos of over a thousand frames and in texts four times the length of the window, and answers a later question about the same input in as little as a tenth of the time of grid probing. Native attention thus keeps what emulated attention gains without its cost, all with existing frozen language and vision-language models.
