# Agent instructions — al-hub/microduck

- Read README.md, docs/ROADMAP.md, docs/FEATURE_MATRIX.md and the related Issue before working.
- Project-specific AI/voice/control code belongs here; upstream firmware, SDK, motion policies and simulator are external pinned dependencies.
- Implement changes with SRP and TDD: failing test → minimum implementation → refactor; record evidence and limitations in the Issue.
- Require explicit allowlisted action mapping, timeouts, safety checks and a user-accessible emergency stop before hardware control.
- Keep simulation and real-hardware adapters separate behind a common interface.
- Never claim simulator or actual robot validation unless executed and observed.
- Never commit secrets, large binaries, upstream clones or generated output; update .gitignore before adding new asset types.
- Use Issue → branch → PR → CI → merge; avoid direct main code changes except agreed project bootstrap.
- Do not auto-download multi-GB artifacts without size and storage review.

## Reference documentation and provenance

- Begin hardware/API feasibility checks at [docs/reference/INDEX.md](docs/reference/INDEX.md).
- Use [docs/reference/upstream-sources.md](docs/reference/upstream-sources.md) to open the upstream source and design docs directly, instead of repeatedly unpacking snapshots.
- [docs/reference/specifications-ko.md](docs/reference/specifications-ko.md) is an unofficial, date-stamped Korean summary. Confirm critical details against the latest official materials; unknown capabilities require hardware validation.
- Do not vendor the full Pollen Robotics repository or upstream ZIP into this project. Keep changes and verification outcomes in project Issues.
