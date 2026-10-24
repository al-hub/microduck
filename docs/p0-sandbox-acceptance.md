# #10 P0 — 실행 격리 구현 수용 기준 및 적용 전 점검표 (2026-10-24)

## 이번 실행 확인
- MCP `environment`: 연결 정상, Microduck 작업 디렉터리 확인.
- `read_text(AI.md)`, `read_text(docs/mcp-execution-policy.md)`, `list_files(scripts)`: 성공.
- `run_dev_check(python_compile_mcp)`: 현재 요청이 안전 검사에 의해 차단됨. 원인 미확정.
- **실제 호스트 격리 도구 존재 여부, 신규 정책 테스트, 서비스 갱신 및 세 CLI 독립 TDD는 수행하지 않음.**

## R0: 상태/읽기
수용: 기존 환경 조회, 허용 문서 읽기, 비밀 파일 거부. 반환 크기 제한 및 허용 경로 제한 유지.

## R1: 사전 정의된 테스트
수용: 정해진 작업 ID 및 고정 argv/cwd로만 실행, 종료 코드와 제한된 stdout/stderr 수집. 임의 명령 문자열 전달 금지. 외부 Git hook 및 Python `-c` 차단.
현재는 호출 자체가 차단되어 재검증 보류.

## R2: 실제 코딩을 위한 OS 격리
필수: 비밀 없는 별도 홈, 작업 디렉터리 외 쓰기 불가, upstream read-only 또는 미마운트, 네트워크 기본 차단(모델 endpoint 필요 시 별도 제한), child process 포함 프로세스 그룹 timeout/kill, CPU/메모리 제한. 단순 argv 검사나 `--sandbox` 플래그만으로 승인하지 않음.
호스트 rootless container/bubblewrap/systemd-run 등 사용 가능 여부는 실행 허용 후 **읽기 전용 검사**로 확인. 설치/권한 변경하지 말 것.
수용 테스트: 작업영역 쓰기 성공, 외부 경로 쓰기 실패, 자격증명 접근 실패, 네트워크 차단, timeout child 정리, stdout 마스킹. 모두 실제 exit/로그 증빙.

## R3/R4 운영 경계
R3(서비스 변경/업데이트)는 기존 백업, 미리 준비한 롤백, 서비스/터널/원격 MCP 헬스 확인 후 적용. R4(sudo/권한 전체 개방/물리 로봇)는 기본 불허.

## 세 CLI 순차 TDD
같은 작은 Python 함수 명세를 별도 worktree로 복제.
1. Red 실패 exit 확인
2. agent가 파일 생성/수정, 파일 해시와 git diff 확인
3. Green 테스트 통과(exit 0)
4. 명확한 Refactor 변경과 회귀 테스트 통과
5. 다른 agent의 read-only 코드 리뷰
6. 시간/토큰(제공되는 경우에만)/비용(확인되는 경우에만) 기록
작업 중 인증 오류/쿼터 부족 또는 sandbox 부재시 해당 도구 BLOCKED로 두고 다른 작업으로 진행.

## 주의
- 신규 문서는 설계 및 재개 기준이며 운영 적용 성공 증거가 아니다.
- 기존 CLI 인증 정보 또는 서비스 설정을 직접 노출/변경하지 않는다.
- `run_command` 차단을 다른 인터프리터나 임의 자식 프로세스로 우회하지 않는다.
