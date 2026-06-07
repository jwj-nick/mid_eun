---
name: hist-page-review
description: 한 섹션(페이지)의 완결성·깊이·내적 일관성을 점검한다. "이 페이지만 읽어도 이야기가 닫히는가, 자연스러운 질문에 답하는가, 고등/일반 깊이가 충분한가, 블록끼리 어긋나지 않는가"를 본다. hist-audit(사실·수위·균형 게이트)과 보완 관계. 호출 예시 — "/hist-page-review imperialism korea", "위기의 조선 완결성 점검".
allowed-tools: Read, Write, Edit, Bash
metadata:
  project: 260602_History
  stage: 5.5 페이지 완결성
  ssot: 10_docs/EPISODE_SCHEMA.md, 00_project_hub/plan/0607_visual_content_masterplan.md
  status: seed
---

# hist-page-review — 페이지 완결성·깊이·일관성 점검

> hist-audit이 "틀린 곳/위반"을 잡는 **게이트**라면, 이 스킬은 "**빠진 곳·얕은 곳·어긋난 곳**"을 잡는 **완결성 리뷰**다.
> 대상 수준 = 계층적 깊이: 중1 본문은 입구로 유지하되, **고등/일반(deepdive)** 기준으로 깊이를 본다. (중1 눈높이 과보호 금지 — 깊이는 deepdive로 확장)

## 입력
- `30_content/<slug>/episode.json`의 한 섹션 + 렌더(`50_app/<slug>/`).
- 먼저 **섹션 본문을 그대로 덤프**해서 읽는다(추론 금지). utf-8 파일로 써서 Read.
  - `PYTHONIOENCODING=utf-8 python` 으로 hook/why/cards/people/timeline/compare/voice/deepdive/connect/chart/image 텍스트를 `_dump.txt`에 추출 → Read → rm.

## 5개 점검 렌즈
1. **완결성(Completeness)** — 이 페이지만 읽어도 이야기가 **시작→전개→끝**으로 닫히나? 큰 사건·인물·결과 중 **빠진 핵심**은? (예: 사건만 있고 *주체*가 없다 / 결과만 있고 *원인*이 없다.)
2. **자연스러운 질문(Reader's Questions)** — 호기심 있는 독자가 떠올릴 "누가? 왜? 얼마나? 그래서?"에 페이지가 답하나? 답이 없으면 **gap**.
3. **깊이(Depth, 고등/일반)** — deepdive가 교과서 한 줄을 넘어 **인과·구조·논쟁·1차사료**까지 가나? 용어 정밀? 비교·수치(chart)로 규모가 체감되나?
4. **내적 일관성(Consistency)** — cards·timeline·battlemap·deepdive의 **연도·인명·인과가 서로 어긋나지 않나**? source 필드에 본문이어야 할 정보가 잘못 들어가 있지 않나?
5. **연결(Connectivity)** — hook이 why로, why가 본문으로, connect가 다음 섹션으로 매끄럽게 이어지나? 시간 점프(예: 1895→1910)에 다리가 있나?

## 동작
- 렌즈별 **발견 목록** 작성 → 심각도(🔴빠진 핵심 / 🟡얕음 / 🟢선택) → **보강안**(어느 블록에 무엇을). 깊이는 우선 **deepdive**로, 규모는 **chart**로, 인물 공백은 **people**로.
- 사실 보강은 검증 가능한 표준 사실 + source 표기. (사실 자체의 정오는 hist-audit과 교차.)

## 출력
- 플랜 파일(`00_project_hub/plan/0607_page_<slug>.md`)에 **`## Round N — 완결성 리뷰`** 로 발견·보강안 기록(피드백 루프). 채팅엔 요약.
- 확정 후 데이터(episode.json) 보강 → 빌드/JS_OK/배포(G0~G3, hist-deploy) → 재리뷰.

## 완결성 게이트 (이 페이지가 '기준 사례'가 되려면)
- [ ] 큰 사건마다 **원인·주체·결과**가 다 있다(사건 나열만 ❌).
- [ ] 독자의 "누가/왜/얼마나/그래서"에 본문 또는 deepdive가 답한다.
- [ ] deepdive가 고등/일반 깊이(인과·구조·논쟁·사료)에 도달.
- [ ] 블록 간 연도·인명·인과 불일치 0. source 필드 오용 0.
- [ ] 시간 점프에 다리가 있고 connect가 다음 섹션과 이어진다.

## 관계
- **hist-audit**(단계 5, 사실·수위·균형·접근성 게이트)와 **상호 보완**. 보통 page-review로 빠진 곳을 채운 뒤 audit으로 정오·수위를 친다.
