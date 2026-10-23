# Feature matrix (pre-delivery)

This is a planning matrix, not an assertion that specific hardware features are present on delivered units.

| Class | Feature | Baseline/target | Verification |
|---|---|---|---|
| Basic | Walk, turn, stand, sit, recover, kick, grasp | Check official release/firmware and simulator action catalog | Not verified |
| Basic | Gamepad and local connectivity | Verify shipped bundle + official manual | Not verified |
| Basic | Sensors, camera, microphone, speaker | Validate against official hardware specification | Not verified |
| Development | SDK, simulator and policy runtime | Pin upstream commit, inspect and smoke-test | Not verified |
| AI | Korean speech input/output | Custom extension | Not implemented |
| AI | LLM natural language command planning | Custom extension | Not implemented |
| AI | Camera-based perception | Custom extension | Not implemented |
| Autonomous | Continuous goal pursuit and recovery | Later extension, safety gated | Not implemented |

Evidence should include: official source URL, release/commit, test steps, expected vs actual result and date.
