# Reddit farmer

Polls a curated list of high-signal AI subreddits via Reddit's public JSON API (no auth, no API key required) and writes one Markdown file per subreddit per day under `raw/reddit/`.

The daily digest reads these files as a sixth source alongside HuggingFace, RSS, Gmail, Twitter, and Kurate. Reddit signal is community-curated discussion and practitioner reports — complementary to the paper/blog-heavy other sources.

## Subreddit list (sourced from deep research 2026-05-10)

| Subreddit | Sort | Score gate | Tier | Why |
|-----------|------|-----------|------|-----|
| **LocalLLaMA** | top/day | ≥50 | 1 | Single highest-signal sub for inference, quantization, GGUF/AWQ/EXL2, KV cache tricks, llama.cpp internals, GPU rigs. |
| **MachineLearning** | top/day | ≥30 | 2 | Filtered to `[R]/[P]` flair only — drops the `[D]` discussion noise. Generic news excluded. |
| **MLScaling** | new | 0 | 1 | Gwern-flavored sub on scaling laws and frontier evals. Low volume, extremely high signal. |
| **CUDA** | new | 0 | 1 | Kernels, ptxas, TensorRT, FlashAttention-adjacent. Direct hits for GPU optimization. |
| **LLMDevs** | top/day | ≥30 | 2 | Production LLM dev chatter — routing patterns, agent deployment. Score gate suppresses self-promo. |
| **ControlProblem** | top/day | ≥20 | 2 | Alignment / interpretability / safety. Maps to responsible-ai topic. |
| **HPC** | new | 0 | 1 | Clusters, interconnects, datacenter. Low cadence but Tier 1 hardware-side context. |
| **reinforcementlearning** | top/day | ≥15 | 2 | RLHF / RLVR / agent-trajectory adjacent. |

Explicitly **not** subscribed: `r/singularity`, `r/OpenAI`, `r/Anthropic`, `r/ClaudeAI`, `r/LangChain`, `r/ArtificialInteligence`, `r/aiwars` — high noise, vendor-PR, or speculation-dominant.

## How it works

- **No auth**: hits public endpoints `https://www.reddit.com/r/<sub>/{new,top}.json`.
- **Filters**: per-sub `min_score`, optional `flair_whitelist`, drops `stickied` and `over_18` posts. 24h lookback by default.
- **Dedup**: `connectors/reddit/.state/seen_post_ids.json` tracks post IDs across runs (last 5000). Re-running within the window is safe and produces no duplicates.
- **Polite scraping**: 1.5s sleep between subreddits, single request each, identifies itself with a real User-Agent.

## Output

One file per subreddit per day:

```
raw/reddit/2026-05-10-r-localllama.md
raw/reddit/2026-05-10-r-machinelearning.md
…
```

Each post entry carries title, score, comment count, flair, posted timestamp (UTC), author, permalink, external link (for link posts), and the self-post body (truncated to 1500 chars).

## Running

```bash
python3 connectors/reddit/farmer.py            # idempotent — skips if today's files exist
python3 connectors/reddit/farmer.py --force    # re-run even if files exist
```

Pinned daily by the 9am IST LaunchAgent (`~/.local/bin/cerebro-morning-digest.sh`) alongside the Gmail, Twitter, and Kurate farmers.

## Tuning

Edit `connectors/reddit/config.json`:

- Add or remove subreddits in the `subreddits` array.
- Raise `min_score` to be more selective.
- Add `flair_whitelist: ["R", "P"]` to a top-sort sub to restrict to specific flair tokens.
- Adjust `tier_default` so the digest knows the baseline tier for each sub (1 = Deep Dive worthy, 2 = standard, 3 = Quick Hit).

If a sub starts dominating the feed with noise, raise its score gate. If it's too quiet, switch its sort to `new` and drop `min_score` to 0.
