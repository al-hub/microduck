# Development roadmap

## P0 foundations
1. Initial repository scaffold and ignore rules.
2. Official base-feature matrix: supported vs unverified.
3. Windows/WSL environment and pinned prerequisites.
4. Official simulator checkout and reproducible smoke test.

## P1 extensions
5. Common robot control API with safe action allowlist and simulator adapter.
6. Korean STT and TTS interfaces with offline/mock testing.
7. LLM command planner with structured schema and confirmation gate.

## P2 integration
8. End-to-end Korean voice → planner → safe action → simulator → result reporting.

## Gates
- G0: source provenance, version pin, storage review.
- G1: reproducible simulator run and captured evidence.
- G2: automated negative/safety tests.
- G3: robot arrival and separate real-device acceptance tests.

Metrics: setup success, action latency, successful task execution, fail-safe action, STT command accuracy.
