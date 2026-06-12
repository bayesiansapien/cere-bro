---
source: farmer/huggingface
farmed: 2026-06-12T09:14:57Z
arxiv_id: 2606.08103
url: https://huggingface.co/papers/2606.08103
arxiv_url: https://arxiv.org/abs/2606.08103
date: 2026-06-12
---

# Revisiting Articulated Parts Perception in Robot Manipulation

We are surrounded by various objects with movable, articulated parts, e.g., box, handle, door. An accurate and generalizable perception of articulated parts is essential to enhance robotic manipulation capabilities. Building on this need, recent efforts in articulated parts perception have followed two main directions: One line of work uses pose-based representation, which requires high manual cost; in parallel, affordance-based methods extract future object motion from point tracking without additional manual efforts, but suffer from low-quality data. In this paper, we propose a new representation of articulated parts, Geometric Primary Structure (GPS), an abstraction of the part geometry structure to balance scalability and quality. For efficient and scalable data collection, GPS is integrated with a portable Virtual Reality (VR) device and requires only one minute to annotate one object sequence. This direct human annotation provides higher quality than the estimated affordance. With this efficient VR-GPS system, we collect 41K frames for 234 objects across six part classes, and train a generalizable GPS model with a single RGB-D object image as input. For object manipulation, we deploy a heuristic policy based on GPS prediction. Without any in-domain fine-tuning, our method achieves an 73% success rate, covering 270 initial states for 9 objects. Our code, data and reusable tool are available at this https URL.
