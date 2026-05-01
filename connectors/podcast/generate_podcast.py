#!/usr/bin/env python3
"""
Daily digest → two-host podcast audio.

Usage:
    python generate_podcast.py                    # today's digest
    python generate_podcast.py 2026-04-30         # specific date
    python generate_podcast.py 2026-04-30 --voice voices/amit.wav  # with voice clone
    python generate_podcast.py 2026-04-30 --script /path/to/script.json  # pre-written script

Script generation priority (no API key needed):
  1. --script flag → load from JSON file
  2. claude CLI available → generate via Claude Code session (default)
  3. ANTHROPIC_API_KEY set → use Anthropic client directly

Hosts:
    A (Amit) — Chatterbox-Turbo, male; cloned from --voice sample if provided
    B (Alex)  — Kokoro ONNX, female voice 'af_sky'

Output: wiki/daily-digest/YYYY-MM/podcasts/YYYY-MM-DD.mp3
        Final audio is natively at 1.25x speed — press play, no adjustment needed.

Voice cloning: record 1–3 min of natural speech as WAV → pass via --voice flag.
    Pre-made sample: voices/amit.wav (extracted from Zoom 2026-04-27)
"""

import sys
import os
import re
import json
import shutil
import argparse
import subprocess
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT  = Path(__file__).resolve().parents[2]
DIGEST_DIR = REPO_ROOT / "wiki" / "daily-digest"
CLAUDE_CLI = shutil.which("claude") or "claude"

# ── prompt ────────────────────────────────────────────────────────────────────

SCRIPT_SYSTEM = """\
You are writing a script for a real podcast — not a summary read-aloud, but a genuine two-host conversation with depth, personality, and forward momentum.

HOSTS:
- AMIT (male, the analyst): Deep AI researcher. Obsessed with inference efficiency, KV cache, distillation, GPU optimization, and routing systems — these are his core research areas. When a topic hits one of those areas he goes deeper, gets more animated, and connects it to things he's already been tracking. Uses short punchy sentences mixed with longer explanations when something excites him. Thinks out loud. Has opinions. Uses "I" freely.
- ALEX (female, the co-host): Sharp, curious, engaged. Not just an interviewer — a peer who follows the field. Reacts authentically, pushes back when something sounds too neat, asks the question the listener is forming. Can be skeptical, surprised, or genuinely excited. Short reactive turns mixed with longer follow-ups.

ATTENTION PRIORITY — weight your coverage accordingly:
  TIER 1 — deep treatment, 6–10 exchanges each:
    routing systems (LLM routing, multimodal routing, agent trajectory routing)
    KV cache
    compression / distillation / quantization / pruning
    GPU kernels and optimization (FlashAttention, kernel fusion, batching)
    GPU hardware (Hopper, Blackwell, memory hierarchy)
    speculative decoding / inference efficiency
  TIER 2 — standard treatment, 3–5 exchanges:
    general LLM papers, new architectures (SSM, MoE, hybrid), agentic reasoning
  TIER 3 — brief, 1–2 exchanges:
    multimodal, vision-language, audio-video (unless touching Tier 1)
  TIER 4 — one line or skip:
    robotics hardware, spatial reconstruction, game benchmarks

When a paper spans tiers, treat at the highest applicable tier.

TARGET LENGTH:
  The final audio plays at 1.25x speed.
  Write enough for 20–22 minutes at normal speaking pace (~2800–3200 words total).
  After 1.25x this gives the listener exactly 16–18 minutes.

STRUCTURE — follow this order precisely:

[OPENING — ~2 min]
Alex opens naturally — names the date, drops a hook about what's most surprising or exciting about today's batch. Not a topic list. One observation that makes the listener lean in. Amit fires back with the sharpest single insight from today. Brief riff on the dominant theme. Energetic, immediate.

[TODAY'S MAP — ~1.5 min]
Alex runs through what they'll cover — framed as "here's the territory" not a dry list. She calls out the Tier 1 topics by name with one line about why each one matters today specifically. Amit adds what's different about today's versions of these topics versus prior work he's been tracking.

[DEEP DIVES — ~12 min total]
Cover papers and industry items in tier order. For each topic:
  Tier 1 paper: 6–10 exchanges. Start with the core mechanism — not the abstract, the actual thing that makes it work. Explain WHY it works at a mechanistic level. Connect explicitly to prior papers Amit has been following (name them). Amit says things like "what gets me about this..." / "the thing nobody's said yet is..." / "I keep coming back to...". End each Tier 1 section with what the follow-up work needs to address.
  Tier 2 paper: 3–5 exchanges. Key finding, one mechanism point, one implication.
  Industry items: 2–4 exchanges. What happened, why it matters, what it signals.
  Between topic shifts, Alex provides a 1-sentence bridge: "Okay, different world next..."

[CONNECTING THE DOTS — ~2 min]
Amit surfaces the cross-paper pattern from today's batch — what does today say collectively about where the field is heading? Name specific papers and their dates. Synthesis, not summary. Alex asks: "If you had to bet on one specific thing in 90 days?" Amit makes one falsifiable, named prediction with a timeframe.

[CLOSING — ~1.5 min]
Alex: what should listeners actually do after today — one paper to read, one repo to watch, one claim to track? Amit answers concretely. Natural warm close — sounds like two people wrapping up a real conversation, not scripted.

CONVERSATIONAL RULES:
- Short reactive turns are essential: "Right.", "Hmm.", "Wait—", "Okay.", "Yeah.", "Go on.", "That tracks.", "Hold on."
- Amit interrupts himself: "Actually — no, the more interesting thing is..."
- Alex challenges: "Skeptic in me says this is just rebranding X." / "Devil's advocate..."
- Vary rhythm constantly: rapid 2-line ping-pong, then a longer explanation, back to rapid
- No "great question", no "absolutely", no "that's fascinating" as empty filler
- Technical terms fine — one short gloss on first use, then use freely

OUTPUT FORMAT — one turn per line, strictly alternating, no blank lines between turns:
AMIT: [spoken words only]
ALEX: [spoken words only]

No stage directions. No asterisks. No parentheticals. Every line starts with AMIT: or ALEX:.
"""


# ── context builder ───────────────────────────────────────────────────────────

def extract_wiki_summaries(digest_path: Path) -> str:
    """Read wiki summary pages linked from the digest for full source depth."""
    text = digest_path.read_text()
    pattern = re.compile(r'\[(?:Full summary|Wiki)\]\(([^)]+\.md)\)')
    summaries = []
    seen = set()
    # digest lives in digest-md/ subfolder; links use paths relative to the
    # parent month directory, so resolve from parent.parent
    base = digest_path.parent.parent
    for match in pattern.finditer(text):
        rel = match.group(1)
        abs_path = (base / rel).resolve()
        if abs_path in seen or not abs_path.exists():
            continue
        seen.add(abs_path)
        try:
            summaries.append(f"=== SOURCE: {abs_path.name} ===\n{abs_path.read_text()}\n")
        except Exception:
            pass
    return "\n".join(summaries)


def build_context(digest_path: Path, date_str: str) -> str:
    digest_text = digest_path.read_text()
    summaries   = extract_wiki_summaries(digest_path)
    parts = [f"DATE: {date_str}", "", "=== DAILY DIGEST ===", digest_text]
    if summaries:
        parts += ["", "=== FULL WIKI SUMMARY PAGES (primary source content) ===", summaries]
    return "\n".join(parts)


# ── script generation ─────────────────────────────────────────────────────────

def _parse_turns(text: str) -> list[dict]:
    turns = []
    for line in text.strip().splitlines():
        line = line.strip()
        if line.startswith("AMIT:"):
            turns.append({"speaker": "A", "text": line[5:].strip()})
        elif line.startswith("ALEX:"):
            turns.append({"speaker": "B", "text": line[5:].strip()})
    return turns


def generate_script_via_cli(digest_path: Path, date_str: str) -> list[dict]:
    """Generate script using the local claude CLI — digest only (no wiki pages) to keep context small."""
    digest_text = digest_path.read_text()
    full_prompt = f"{SCRIPT_SYSTEM}\n\nNow write the podcast script:\n\nDATE: {date_str}\n\n{digest_text}"
    result = subprocess.run(
        [CLAUDE_CLI, "-p", "--model", "claude-sonnet-4-6"],
        input=full_prompt,
        capture_output=True,
        text=True,
        timeout=600,
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude CLI failed:\n{result.stderr}")
    return _parse_turns(result.stdout)


def generate_script_via_api(digest_path: Path, date_str: str) -> list[dict]:
    """Generate script using Anthropic API (requires ANTHROPIC_API_KEY)."""
    import anthropic
    context = build_context(digest_path, date_str)
    client  = anthropic.Anthropic()
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SCRIPT_SYSTEM,
        messages=[{"role": "user", "content": f"DATE: {date_str}\n\n{context}"}],
    )
    return _parse_turns(msg.content[0].text)


def load_script(script_path: str) -> list[dict]:
    with open(script_path) as f:
        data = json.load(f)
    for turn in data:
        assert turn.get("speaker") in ("A", "B"), f"Bad speaker: {turn}"
        assert isinstance(turn.get("text"), str)
    return data


# ── TTS: Host A — Chatterbox-Turbo ───────────────────────────────────────────

_chatterbox_model = None

def _get_chatterbox():
    global _chatterbox_model
    if _chatterbox_model is None:
        import torch
        from chatterbox.tts_turbo import ChatterboxTurboTTS
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        print(f"  Loading Chatterbox Turbo on {device}...")
        _chatterbox_model = ChatterboxTurboTTS.from_pretrained(device=device)
    return _chatterbox_model


def render_host_a(text: str, out_path: str, voice_sample: str | None = None):
    import torchaudio
    model = _get_chatterbox()
    wav = model.generate(text, audio_prompt_path=voice_sample)
    torchaudio.save(out_path, wav, model.sr)


# ── TTS: Host B — Kokoro ONNX ────────────────────────────────────────────────

_kokoro_model = None

def _get_kokoro():
    global _kokoro_model
    if _kokoro_model is None:
        from kokoro_onnx import Kokoro
        models_dir = Path(__file__).parent / "models"
        print("  Loading Kokoro...")
        _kokoro_model = Kokoro(
            str(models_dir / "kokoro-v0_19.onnx"),
            str(models_dir / "voices.json"),
        )
    return _kokoro_model


def render_host_b(text: str, out_path: str):
    import soundfile as sf
    model = _get_kokoro()
    samples, sr = model.create(text, voice="af_sky", speed=1.0, lang="en-us")
    sf.write(out_path, samples, sr)


# ── stitch + speed ────────────────────────────────────────────────────────────

def _atempo_chain(speed: float) -> str:
    filters = []
    remaining = speed
    while remaining > 2.0:
        filters.append("atempo=2.0")
        remaining /= 2.0
    while remaining < 0.5:
        filters.append("atempo=0.5")
        remaining /= 0.5
    filters.append(f"atempo={remaining:.4f}")
    return ",".join(filters)


def stitch_mp3(turn_files: list[str], out_path: str, speed: float = 1.25):
    inputs = []
    for f in turn_files:
        inputs += ["-i", f]
    n = len(turn_files)
    concat = "".join(f"[{i}:a]" for i in range(n)) + f"concat=n={n}:v=0:a=1[concat]"
    speed_filter = _atempo_chain(speed)
    filter_expr = f"{concat};[concat]{speed_filter}[out]"
    subprocess.run(
        ["ffmpeg", "-y"] + inputs +
        ["-filter_complex", filter_expr, "-map", "[out]", "-q:a", "2", out_path],
        check=True, capture_output=True,
    )


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("date", nargs="?", default=str(date.today()),
                        help="Digest date YYYY-MM-DD")
    parser.add_argument("--voice", metavar="WAV",
                        help="Voice sample WAV for Host A (Amit) — enables voice cloning. "
                             "Default: voices/amit.wav if it exists.")
    parser.add_argument("--script", metavar="JSON",
                        help="Pre-generated script JSON. Skips script generation entirely.")
    parser.add_argument("--speed", type=float, default=1.25,
                        help="Final MP3 playback speed (default: 1.25)")
    args = parser.parse_args()

    date_str   = args.date
    year_month = date_str[:7]

    month_dir   = DIGEST_DIR / year_month
    digest_path = month_dir / "digest-md" / f"{date_str}.md"
    if not digest_path.exists():
        print(f"ERROR: Digest not found: {digest_path}", file=sys.stderr)
        sys.exit(1)

    pod_dir = month_dir / "podcasts"
    pod_dir.mkdir(parents=True, exist_ok=True)
    out_mp3 = pod_dir / f"{date_str}.mp3"

    # resolve voice sample: explicit --voice > default voices/amit.wav
    voice_sample = args.voice
    if not voice_sample:
        default_voice = Path(__file__).parent / "voices" / "amit.wav"
        if default_voice.exists():
            voice_sample = str(default_voice)

    print(f"Digest:  {digest_path}")
    print(f"Output:  {out_mp3}  ({args.speed}x speed baked in)")
    print(f"Voice:   {voice_sample or 'default Chatterbox voice'}")

    # ── script generation ────────────────────────────────────────────────────
    if args.script:
        print(f"\nLoading script from {args.script}...")
        turns = load_script(args.script)
    elif os.environ.get("ANTHROPIC_API_KEY"):
        print("\nGenerating script via Anthropic API (with full wiki source pages)...")
        turns = generate_script_via_api(digest_path, date_str)
    elif shutil.which("claude"):
        print("\nGenerating script via claude CLI (digest only — for deep source coverage, "
              "generate the script in a Claude Code session and pass via --script)...")
        turns = generate_script_via_cli(digest_path, date_str)
    else:
        print(
            "\nERROR: No script generation method available.\n"
            "Options:\n"
            "  1. In a Claude Code session: ask Claude to generate the script,\n"
            "     then run: python generate_podcast.py --script /tmp/script.json\n"
            "  2. Set ANTHROPIC_API_KEY environment variable.\n"
            "  3. Install Claude Code CLI (https://claude.ai/code).",
            file=sys.stderr,
        )
        sys.exit(1)

    total_words  = sum(len(t["text"].split()) for t in turns)
    est_normal   = total_words / 130
    est_final    = est_normal / args.speed
    print(f"Script:  {len(turns)} turns / ~{total_words} words")
    print(f"         ~{est_normal:.0f} min normal → ~{est_final:.0f} min at {args.speed}x")

    # ── TTS rendering ────────────────────────────────────────────────────────
    with tempfile.TemporaryDirectory() as tmp:
        turn_files = []
        for i, turn in enumerate(turns):
            wav_path = os.path.join(tmp, f"turn_{i:03d}.wav")
            label   = "AMIT" if turn["speaker"] == "A" else "ALEX"
            preview = turn["text"][:60] + "..." if len(turn["text"]) > 60 else turn["text"]
            print(f"  [{i+1:2d}/{len(turns)}] {label}: {preview}")
            if turn["speaker"] == "A":
                render_host_a(turn["text"], wav_path, voice_sample)
            else:
                render_host_b(turn["text"], wav_path)
            turn_files.append(wav_path)

        print(f"\nStitching {len(turn_files)} segments at {args.speed}x → {out_mp3.name}...")
        stitch_mp3(turn_files, str(out_mp3), speed=args.speed)

    size_mb = out_mp3.stat().st_size / 1_048_576
    print(f"Done.  {size_mb:.1f} MB → {out_mp3}")


if __name__ == "__main__":
    main()
