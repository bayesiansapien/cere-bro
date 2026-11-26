#!/usr/bin/env python3
"""
Transcribe a Cerebro Radio episode locally, so the next episode's continuity step
knows what the hosts actually said.

Reads  wiki/daily-digest/YYYY-MM/podcasts/DATE/DATE.m4a
Writes connectors/notebooklm/episodes/DATE/transcript.md

Uses mlx-whisper on Apple Silicon (`uv tool install mlx-whisper`), about 5 minutes
for a 50-minute episode. Skips if the transcript already exists or the audio is missing.

Run: python3 connectors/notebooklm/transcribe.py DATE [--force]
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CFG = json.loads((HERE / "config.json").read_text())
MODEL = CFG.get("transcribe_model", "mlx-community/whisper-large-v3-turbo")


def transcribe(date, force=False):
    audio = REPO / "wiki" / "daily-digest" / date[:7] / "podcasts" / date / f"{date}.m4a"
    out = HERE / "episodes" / date / "transcript.md"
    if out.exists() and not force:
        print(f"transcript {date}: already exists")
        return 0
    if not audio.exists():
        print(f"transcript {date}: no audio at {audio}")
        return 1
    exe = shutil.which("mlx_whisper") or str(Path.home() / ".local/bin/mlx_whisper")
    if not Path(exe).exists():
        print("transcript: mlx_whisper not installed (uv tool install mlx-whisper); skipping")
        return 1
    print(f"transcript {date}: transcribing {audio.name}...")
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run([exe, str(audio), "--model", MODEL, "-f", "txt", "-o", tmp, "--language", "en",
                            "--verbose", "False"], capture_output=True, text=True, timeout=3600)
        txt = Path(tmp) / f"{date}.txt"
        if r.returncode or not txt.exists():
            print(f"transcript {date}: failed: {(r.stderr or r.stdout)[-300:]}")
            return 1
        lines = [l.strip() for l in txt.read_text().splitlines()]
    # Whisper emits stray "!" lines on silence; drop them and collapse repeats.
    lines = [l for l in lines if l and not re.fullmatch(r"[!.\s]+", l)]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"# Cerebro Radio transcript, {date}\n\n"
                   "Machine transcription (mlx-whisper); speaker turns are line breaks, names may be misspelled.\n\n"
                   + "\n".join(lines) + "\n")
    print(f"transcript {date}: {len(' '.join(lines).split())} words -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    sys.exit(transcribe(args[0], "--force" in sys.argv))
