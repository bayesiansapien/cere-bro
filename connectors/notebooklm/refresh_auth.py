#!/usr/bin/env python3
"""
Self-heal NotebookLM (nlm) auth from the local Chrome session, so podcast
generation stays AUTOMATED instead of needing a periodic interactive `nlm login`.

nlm authenticates NotebookLM with 5 Google cookies (SID/HSID/SSID/APISID/SAPISID).
Those live for months in a logged-in browser, so when nlm's cached token lapses we
re-extract them from Chrome (via browser_cookie3) and feed them to nlm through its
non-interactive `nlm login --manual --file` path. Same self-heal pattern as the
X (x-cookies.json) and LinkedIn (li_at) connectors.

SECURITY (Google cookies grant full account access — treat as top-secret):
  - The temp cookie file is written chmod 600 and DELETED immediately after nlm
    ingests it (finally block), so no long-lived secret file sits on disk.
  - Cookie VALUES are never printed, logged, or committed. Only names/counts.
  - Nothing here writes to a version-controlled path.

Exit 0 = nlm auth is valid (already, or after a successful re-seed).
Exit 1 = could not heal (e.g. Chrome is not logged into Google). The caller
         should skip the podcast step and notify — it must NOT pretend it worked.

Run:  python3 connectors/notebooklm/refresh_auth.py
"""

import json
import os
import stat
import subprocess
import sys
import tempfile

REQUIRED = ["SID", "HSID", "SSID", "APISID", "SAPISID"]
# nlm prefers the .google.com-domain values; grab the __Secure-*PSID family too
# because Google's cookie rotation leans on them for long-lived sessions.
WANT = REQUIRED + [
    "__Secure-1PSID", "__Secure-3PSID", "__Secure-1PSIDTS", "__Secure-3PSIDTS",
    "__Secure-1PSIDCC", "__Secure-3PSIDCC", "__Secure-1PAPISID", "__Secure-3PAPISID",
    "NID", "OSID", "SIDCC", "1P_JAR",
]


def nlm_auth_ok(timeout: int = 45) -> bool:
    """True if nlm can list notebooks (a real, cheap authenticated call)."""
    try:
        r = subprocess.run(["nlm", "notebook", "list"],
                           capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0 and ('"' in r.stdout)
    except Exception:
        return False


def extract_google_cookies() -> list:
    """Pull the wanted Google cookies from the local browser. Returns a list of
    {name, value, domain} Chrome-format dicts. Values stay in memory only."""
    import browser_cookie3 as bc
    out, seen = [], set()
    for loader in (getattr(bc, "chrome", None), getattr(bc, "brave", None), getattr(bc, "edge", None)):
        if loader is None:
            continue
        try:
            cj = loader(domain_name="google.com")
        except Exception:
            continue
        for c in cj:
            if c.name in WANT and c.name not in seen:
                out.append({"name": c.name, "value": c.value, "domain": c.domain})
                seen.add(c.name)
        if all(k in seen for k in REQUIRED):
            break
    return out


def main() -> int:
    # 1. Already valid? Nothing to do (this call also nudges nlm's own refresh).
    if nlm_auth_ok():
        print("nlm auth OK — no re-seed needed.")
        return 0

    print("nlm auth expired — re-seeding from the local Chrome Google session...")

    # 2. Extract cookies from the browser.
    try:
        cookies = extract_google_cookies()
    except Exception as e:
        print(f"  cookie extraction failed ({e.__class__.__name__}) — cannot auto-heal.")
        return 1
    have = {c["name"] for c in cookies}
    missing = [k for k in REQUIRED if k not in have]
    if missing:
        print(f"  missing required Google cookies {missing} — is Chrome logged into "
              "Google/NotebookLM? Cannot auto-heal; a one-time `nlm login` is needed.")
        return 1
    print(f"  extracted {len(cookies)} Google cookies (values redacted); required set present.")

    # 3. Write a chmod-600 temp file, feed it to nlm, DELETE it immediately.
    fd, path = tempfile.mkstemp(prefix="nlm-cookies-", suffix=".json")
    try:
        os.fchmod(fd, stat.S_IRUSR | stat.S_IWUSR)  # 0600
        with os.fdopen(fd, "w") as f:
            json.dump(cookies, f)
        try:
            r = subprocess.run(["nlm", "login", "--manual", "--file", path],
                               capture_output=True, text=True, timeout=120)
            # Do NOT echo r.stdout verbatim (may surface account details). Status only.
            print(f"  nlm login --manual exit={r.returncode}")
        except Exception as e:
            print(f"  nlm login --manual failed to run: {e.__class__.__name__}")
    finally:
        try:
            os.remove(path)
        except OSError:
            pass

    # 4. Verify the re-seed actually took.
    if nlm_auth_ok():
        print("  ✓ nlm auth re-seeded from the browser — podcast generation can proceed.")
        return 0
    print("  ✗ re-seed did not validate. A one-time interactive `nlm login` is needed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
