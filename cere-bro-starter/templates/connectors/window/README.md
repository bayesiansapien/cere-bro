# Collection window

`build_window.py` decides which raw inputs belong to which daily digest, so nothing is missed and nothing is counted twice.

- Digest D covers the US-Eastern day D-1 and is written at the daily cutoff (`config.json: cutoff_local`), which should be just after US-Eastern midnight in your timezone.
- Windows are defined by **capture time**: a ledger records when each raw file was first seen; digest D gets every file first captured between the previous cutoff and D's cutoff. Late items land in the next window, flagged late.
- `build_window.py --digest-date D` writes the manifest `raw/_windows/D.md` (+ `.json`) and lists stale sources; `--close` freezes the window and advances the watermark; `--next` previews the open window (used by the Media Zone live draft).

Set `local_utc_offset_minutes` (e.g. 330 for IST, -300 for EST, 60 for CET) and `cutoff_local` (HH:MM). State lives in `.state/` (gitignored).
