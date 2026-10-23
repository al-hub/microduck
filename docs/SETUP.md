# PC preparation and simulator verification

Recommended layout (Windows or WSL):
```
workspace/microduck/
  app/         # this repository (al-hub/microduck)
  upstream/    # official source checkout(s), kept outside app
  assets/      # binary models/datasets, never committed
  results/     # logs/recordings, never committed
```

## Sequence
1. Inventory Windows/WSL version, CPU/GPU, Python, Git, disk capacity and network.
2. Verify the official manufacturer organization, simulator documentation, license, release and exact dependency versions.
3. Record upstream URL and commit in `docs/UPSTREAM.md` after verification.
4. Review expected binary sizes before downloading or installing.
5. Use separate virtual environment (not tracked) and install pinned dependencies.
6. Run upstream simulator without changing motion policy; capture startup output, CPU/GPU utilization and basic action smoke test.
7. Attach evidence to Issue #4; mark pass/fail with environment and exact command.

**Current state:** No direct PC session has been established in this chat; no simulator commands have been run.
