# PC-first Microduck work entrypoint

Updated: 2026-10-24 (Asia/Seoul)

## User instruction
When the user says "마이크로덕 작업하자", resume this repository's PC-first workflow immediately, without restarting planning. Target is the user's previously configured always-on Windows laptop via the ClosePaw -> paired Termux -> Tailscale/SSH route, NOT the assistant's sandbox.

## Verified 2026-10-24
- ClosePaw Android app reachable, v0.1.80/code81.
- Operation discovery exposes `linux.shell.exec` for paired Termux but it is **not ready**: `termux_not_running`.
- No successful PC SSH or hardware inventory was obtained. Do not say PC environment, simulator, dependencies, directory or smoke tests have passed.

## Resume sequence
1. Read `AGENTS.md`, `docs/SETUP.md`, `docs/ROADMAP.md`, related Issues #1-#4.
2. Discover ClosePaw operations and readiness. If Termux is not running, report the one concrete blocker; do not pretend shell access. When feasible, request user to launch Termux/bridge on phone; do not repeatedly retry a failed operation.
3. Once `linux.shell.exec` is ready, use **read-only** Termux commands to inspect SSH aliases/config and available PC route (do not print secrets). Verify exact target before PC changes. Use network.tailscale.status if private network access fails.
4. On the PC, inventory Windows, WSL distro, CPU/GPU, RAM, available disk, Python, Git, network, permissions; record verified output and dates in Issue #3.
5. Prepare `workspace/microduck/{app,upstream,assets,results}` with this repo cloned in `app`; make large upstream assets local-only. Respect existing user data.
6. Verify official upstream manufacturer, simulator URL, license, pinned tag/commit, dependencies and download size before installing or executing. No automatic multi-GB downloads before size/storage review.
7. Create reproducible setup/smoke scripts, check command exit statuses, then verify simulator startup and basic motion in PC environment; add evidence to Issues #3/#4.
8. Mark development environment READY only when PC SSH, directory, dependencies and at least one reproducible smoke test are verified. Separately mark SIMULATOR READY only after actual simulator execution passes. Tell user the exact reached readiness stage.

## Status at handoff
BLOCKED AT PC ACCESS: paired Termux process not running. GitHub planning/scaffold exists, PC deployment and simulator tests not yet verified.
