---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14169"
url: "https://huggingface.co/papers/2605.14169"
arxiv_url: "https://arxiv.org/abs/2605.14169"
date: 2026-05-17
---

# BOOKMARKS: Efficient Active Storyline Memory for Role-playing

Memory systems are critical for role-playing agents (RPAs) to maintain long-horizon consistency. However, existing RPA memory methods (e.g., profiling) mainly rely on recurrent summarization, whose compression inevitably discards important details. To address this issue, we propose a search-based memory framework called Bookmarks, which actively initializes, maintains, and updates task-relevant pieces of bookmarks for the current task (e.g., character acting). A bookmark is structured as the answer to a question at a specific point in the storyline. For each current task, Bookmarks selects reusable existing bookmarks or initializes new ones (at storyline beginning) with useful questions. These bookmarks are then synchronized to the current story point, with their answers updated accordingly, so they can be efficiently reused in future grounding rounds. Compared with recurrent summarization, Bookmarks offers (1) active grounding for capturing task-specific details and (2) passive updating to avoid unnecessary computation. Bookmarks significantly outperforms RPA memory baselines on 85 characters from 16 artifacts.
