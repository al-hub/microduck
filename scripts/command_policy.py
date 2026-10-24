"""Fail-closed argument screening for proposed Microduck MCP developer commands.

Not a security sandbox: approved tools can spawn children or access other files.
Deployment requires OS-level containment and service restart validation.
"""
from pathlib import Path

ALLOWED = {
    "git": {"status", "diff"},
    "python3": {"--version", "-V", "-m"},
    "agy": {"--version"},
    "codex": {"--version"},
    "opencode": {"--version"},
}
MODULES = {"unittest", "ast"}
BLOCKED_TOKENS = ("--dangerously", "--auto", "--yolo", "--full-auto", "--skip-permissions")
DENY_DIRS = {"upstream", ".ssh", ".config", "secrets", "credentials", "private"}

def validate(argv, cwd):
    if not isinstance(argv, list) or not argv or any(not isinstance(a, str) or not a for a in argv):
        raise ValueError("invalid argv")
    name = Path(argv[0]).name
    if name not in ALLOWED or len(argv) < 2 or argv[1] not in ALLOWED[name]:
        raise ValueError("command not approved")
    if any(part in DENY_DIRS for part in Path(cwd).parts):
        raise ValueError("restricted cwd")
    if any(any(token in arg for token in BLOCKED_TOKENS) for arg in argv):
        raise ValueError("unsafe option")
    if name == "python3" and argv[1] == "-m":
        if len(argv) < 3 or argv[2] not in MODULES:
            raise ValueError("python module not approved")
        if argv[2] == "ast" and len(argv) > 3:
            raise ValueError("ast parameters not approved")
    if name == "git" and len(argv) > 2 and any(
        arg.startswith("--exec") or arg.startswith("--config-env") or arg == "-c"
        for arg in argv[2:]
    ):
        raise ValueError("git options restricted")
    return True
