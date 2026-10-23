# Microduck AI Extensions

AI/voice/control extensions and test plans for the Microduck robot. This is **not** a fork or mirror of the upstream firmware.

## Project scope
- Preserve upstream robot firmware, motion policies and simulator in a separate local checkout.
- Build Korean STT/TTS, language-model command planning, safe action gateway, perception and simulation tests.
- Validate in simulation before real robot execution. No unbounded model-generated motor commands.

## Start here
1. Read [AGENTS.md](AGENTS.md), [roadmap](docs/ROADMAP.md) and [feature matrix](docs/FEATURE_MATRIX.md).
2. Create a local `workspace/microduck` with this repo in `app/` and official sources in `upstream/` (ignored if inside this checkout).
3. Follow [setup plan](docs/SETUP.md). Official upstream URL/commit and simulator commands must be independently checked before execution.
4. Work through GitHub Issues in P0 → P1 → P2 order.

## Storage policy
Do not commit simulator checkouts, binary model weights, datasets, logs or recordings. Track upstream URLs/commits, artifact checksums and reproducible download scripts. Never commit credentials.

## Status
Initial scaffold and issue planning only. PC execution, simulation and hardware checks are **not verified**.
