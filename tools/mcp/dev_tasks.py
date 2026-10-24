"""Microduck R1 dedicated development checks (not a shell or AI agent executor).

This module is a candidate for an explicitly registered MCP tool.
It cannot enforce an OS sandbox, so only fixed read/test tasks are exposed.
"""
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path("/home/al-hub/workspace/microduck").resolve()
TASKS = {
    "inventory_tests": ([sys.executable, "-B", "-m", "unittest", "discover",
                         "-s", "experiments", "-p", "test_agent_inventory.py"], ROOT),
    "policy_tests": ([sys.executable, "-B", "-m", "unittest", "discover",
                      "-s", "experiments", "-p", "test_command_policy.py"], ROOT),
    "agent_smoke_tests": ([sys.executable, "-B", "-m", "unittest", "discover",
                           "-s", "experiments/agent-smoke", "-p", "test_score_band.py"], ROOT),
}

def run_registered_test(task_id: str) -> dict:
    if not isinstance(task_id, str) or task_id not in TASKS:
        return {"ok": False, "error": "unknown task id", "allowed": sorted(TASKS)}
    argv, workdir = TASKS[task_id]
    start = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=workdir, capture_output=True,
                                text=True, timeout=20, check=False)
        return {"ok": result.returncode == 0, "task_id": task_id,
                "exit_code": result.returncode,
                "stdout": result.stdout[:4000], "stderr": result.stderr[:4000],
                "elapsed_seconds": round(time.monotonic()-start, 3)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "task_id": task_id, "error": "timeout"}
