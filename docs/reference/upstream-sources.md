# 공식 Microduck 소스·기술자료 위치

확인 기준: 2026-10-24. 첨부된 microduck-main.zip 및 기술자료 안내 ZIP을 검토해 링크를 정리했습니다. ZIP 파일 자체는 저장소에 추가하지 않습니다.

| 목적 | 원본 |
|---|---|
| 소스 코드 | https://github.com/pollen-robotics/microduck |
| 전체 소스 ZIP | https://github.com/pollen-robotics/microduck/archive/refs/heads/main.zip |
| 기술 문서 목차 | https://github.com/pollen-robotics/microduck/blob/main/docs/README.md |
| 개발 규약 | https://github.com/pollen-robotics/microduck/blob/main/AGENTS.md |
| 개발 기여 규칙 | https://github.com/pollen-robotics/microduck/blob/main/CONTRIBUTING.md |
| 로봇 제어 명령 | https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md |
| PC Bluetooth 도구 | https://github.com/pollen-robotics/microduck/blob/main/docs/robot/duckctl.md |
| 외부 AI/카메라 FAQ | https://github.com/pollen-robotics/microduck/blob/main/docs/faq.md |
| 시뮬레이션 | https://github.com/pollen-robotics/microduck/blob/main/docs/robot/simulation.md |
| 설계 | https://github.com/pollen-robotics/microduck/tree/main/docs/design |
| 제품 개요 | https://pollen-robotics.com/microduck/ |
| 공식 보도자료 키트 | https://pollen-robotics.com/microduck/press-kit/ |
| 학습·시뮬레이션 | https://github.com/pollen-robotics/microduck_rl |

## 참조 원칙
- 원본 ZIP에는 소스·docs·배포 파일이 포함되어 있으므로 별도 ZIP을 매번 풀 필요가 없습니다.
- 코드의 구체 동작은 공식 GitHub **최신 파일**을 직접 확인하십시오.
- upstream `AGENTS.md`는 카메라 소비 기본 경로로 WebRTC를 명시하고 `media.stream`을 프레임 단방향 fallback으로 설명합니다. 세부 설계는 공식 원문을 따릅니다.
- 배송 전 관찰·추정과 배송 후 실기기 검증을 구분하십시오.
- 최종 제품 사양은 배송품 및 제조사 최신 공개 문서와 대조해야 합니다.
