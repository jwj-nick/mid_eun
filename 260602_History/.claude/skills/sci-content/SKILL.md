---
name: sci-content
description: 과학기술 트랙(tracks/sci-tech 등 과학 계열) 콘텐츠를 '호기심 엔진'으로 작성한다. tracks-write(고등/일반·교과 연결·외부 링크)를 상속하되, 정확성 위에 과학적 경이·엣지를 의무화 — "오늘 너무 당연한 것이 그 전엔 존재하지 않았다, 상상이 가니?"를 자극한다. 호출 예시 — "sci-content sci-tech revolution", "과학혁명 호기심 강화".
allowed-tools: Read, Write, Edit, Bash, WebSearch
metadata:
  project: 260602_History
  scope: 과학 계열 트랙 (tracks/sci-tech …)
  stage: 콘텐츠 작성 (과학 전용 — 호기심 엔진)
  ssot: 10_docs/EPISODE_SCHEMA.md, plan/0616_plan_scitech_curiosity_upgrade.md, plan/0615_plan_track_scitech.md
  status: seed
---

# sci-content — 과학 콘텐츠 작성 (호기심 엔진)

> **`tracks-write`(일반 분야 트랙)를 상속** + **과학적 경이/엣지를 의무화.** 차이: tracks-write=정확한 통사 / **sci-content=정확 + 경이.** 과학 트랙은 이 스킬로 작성·감수. (Nick 0616: "그냥 역사 얘기라 평이하고 엣지가 없다 → 호기심 유발 필요.")

## 0. 대상·톤
- 대상 = 고등학생·일반인(tracks-write 상속). 문체 = 교양 과학서 평서체 + **엣지**.
- **경이 먼저(wonder-first), 연대기 나중.** hook을 날짜·인물로 열지 않는다. '지금 너무 당연한 것을 낯설게'로 연다.
- 짧고 센 문장 + 직접 호명("지금 네 손안의…") + 감각적 대비(어둠·통증·굶주림·속도·거리). 단, 과장·왜곡 금지(수치는 출처/대략값).

## 1. 호기심 엔진 — 5장치 (정거장당 ≥3, mind-bender 1, spark 1, '그 전엔 없었다' 1 필수)
1. **🤯 그 전엔 없었다(낯설게):** 당연한 것을 "N년 전엔 없었다"로 충격 제시.
2. **🔍 일상 속 숨은 과학:** 매일 쓰면서 안 궁금했던 것의 정체(폰 GPS↔상대성, 영상↔코덱, 빵↔질소고정).
3. **🌀 상식 뒤집기(mind-bender):** 직관을 깨는 '와, 진짜?' 한 방.
4. **❓ 만약 없었다면(counterfactual):** 그것 없는 하루/세상 — 주로 reflect에 배치.
5. **📊 숫자의 충격:** 규모 체감 비교(에니악 vs 폰, 비압축 영상 등).

## 2. 정거장 구조 (wonder-first)
`hook(경이/도발 ①③)` → **`spark`(🤯 '그 전엔 없던 세상' + mind)** → `why(그래서 무엇이 바뀌었나 + 숨은 과학 ②)` → `cards(메커니즘·인물)` → `image×2(≥2)` → `lens/choice` → `connect` → `links(외부 심화)` → `quiz(호기심형)` → `reflect(만약 없었다면 ④)`.

### `spark` 블록 (엔진 — 0616 신설)
`spark:{ icon?, title, body, mind? }` → 🤯 강조 콜아웃. `body`='그 전엔 없던 세상'·counterfactual, `mind`=상식 뒤집는 한 줄. 정거장당 1개.

## 3. 절차
1. 리서치: 통설 + **경이 포인트**(그 전엔 없던 것·일상 속 숨은 과학·mind-bender·충격 수치) 수집.
2. 작성: 위 구조로. hook·spark에 호기심 집중.
3. 외부 링크(`links`, 200검증) + 이미지 ≥2(`hist-visuals`, 전점 Read 검수).
4. 빌드 → 감수(호기심 게이트 포함) → deploy.py(백그라운드) → G3.

## 4. 품질 게이트
- [ ] `build.py` 무오류
- [ ] **정거장당 호기심 장치 ≥3 + mind-bender 1 + `spark` 1 + '그 전엔 없었다' 1**
- [ ] hook이 경이/도발로 열림(날짜·인물 나열 X)
- [ ] 사실 정확(과장·왜곡 0, 수치 출처/대략값) · 고등/일반 수준 · 교과 연결 · 외부 링크 200 · 이미지 ≥2
- [ ] 전문 영역(코덱·반도체·NPU 등) 전문가(Nick) 검수

## 5. 관련
- 계획: `plan/0616_plan_scitech_curiosity_upgrade.md`(호기심 엔진) + `plan/0615_plan_track_scitech.md`. worklog: `session/0615_scitech_build_worklog.md`.
- 상속: `tracks-write`(일반 트랙). 이미지: `hist-visuals`. 스키마: `EPISODE_SCHEMA.md`(`spark`·`links` 포함).
