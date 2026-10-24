#!/usr/bin/env python3
"""Microduck read-only AI runtime inventory. No secrets or config contents."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
TOOLS = {
    "antigravity": [str(Path.home() / ".local/bin/agy"), "--version"],
    "codex": ["codex", "--version"],
    "opencode": [str(Path.home() / ".opencode/bin/opencode"), "--version"],
    "ollama": ["/usr/local/bin/ollama", "--version"],
}

def probe(argv, timeout=8):
    started = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True,
                                timeout=timeout, check=False)
        output = (result.stdout or result.stderr).strip().splitlines()
        return {"status": "ok" if result.returncode == 0 else "failed",
                "exit_code": result.returncode,
                "version": output[0][:160] if output else "",
                "elapsed_ms": round((time.monotonic() - started) * 1000)}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"status": "unavailable", "error_type": type(exc).__name__,
                "elapsed_ms": round((time.monotonic() - started) * 1000)}

def main():
    inventory = {"schema_version": 1, "workspace": str(ROOT),
                 "tools": {name: probe(argv) for name, argv in TOOLS.items()}}
    print(json.dumps(inventory, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
