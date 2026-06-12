---
name: hist-person
description: 인물 도감 v3 — 인물 1명을 추가하거나 기존 인물을 풀스펙(10초카드·어록·더 깊이·갤러리·경로지도·더 공부하기)으로 보강한다. 절차 SSOT = 10_docs/PEOPLE_GUIDE.md. 호출 예시 — "/hist-person 링컨 보강", "/hist-person 새 인물 메넬리크".
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, Agent
metadata:
  project: 260602_History
  ssot: 10_docs/PEOPLE_GUIDE.md, 10_docs/EPISODE_SCHEMA.md §People-gallery v3
  standard: 안중근(an-junggeun) 페이지 = v3 풀스펙 표준 견본
---

# hist-person — 인물 도감 추가·보강 (v3/v3.1)

데이터 = `30_content/people/people.json` (SSOT) · 빌더 = `40_build/build_people.py` · 산출 = `50_app/people/`
**스키마·패널 구성·작성 규칙 = `10_docs/PEOPLE_GUIDE.md`** (이 스킬은 절차 실행기, 가이드가 법전)

## 목표 수준 (두 층 동시)
- 중1 quick review: 10초 카드 → 생애 → 연표에서 완결.
- 전문 식견 성인: '더 깊이'(사학사 논쟁·사료 비판·국제법 등) + '더 공부하기'(평전·1차 사료·영상·장소)가 **그 인물 공부의 시발점**이 되게.
- 표준 견본 = **안중근 페이지** (v3 풀스펙 + v3.1 갤러리·경로지도).

## 절차 (PEOPLE_GUIDE §3의 7단계 실행)
1. **선정/진단** — 신규면 `whyHere`부터 작성(못 쓰면 보류). 보강이면 현재 entry 필드 실측(before 기록).
2. **리서치** — 사실·연도 교차 확인. **어록은 원출처 추적**: 직접 인용 / 요지 / 전언(원출처 논쟁) 3등급으로 구분 표기. 서지는 실존 확인된 것만.
3. **작성** — v3 필드(quickCard·whyHere·quotes·deepDive 3~5·network·figuresLink·study). 중1 문장(bio)과 성인 문단(deepDive) 의식적 분리. study 항목은 URL 없이도 가치 있게(제목·저자·note), URL은 검증 후에만.
4. **시각자료(v3.1, 해당 시)** —
   - `gallery`: Commons API로 유묵·서신·실물 사진 검색(extmetadata 라이선스 실측) → PIL 리사이즈 → **전점 육안 검수**(Read 툴로 직접 보기 — 오선정 전례: 데스마스크·전투도면).
   - `journey`: 생애 이동 경로 5~7점(실좌표 대조) + path. caption에 '현재 지도' 명시.
   - **포스터·책 표지는 이미지 금지(저작권) → 링크로 대체.**
5. **링크 검증** — 영상은 WebSearch→**oembed 실재+공식 채널 확인**(비공식·삭제 영상 배제). 도서는 알라딘 검색 URL 패턴(200 확인). 위키류는 200.
6. **빌드·게이트** — `PYTHONIOENCODING=utf-8 python 40_build/build_people.py` → 신규 패널 마커 grep 확인 + journey 있으면 인라인 스크립트 node --check + **v2 페이지에 Leaflet 미주입 확인**(하위 호환).
7. **audit·배포** — PEOPLE_GUIDE §4 체크리스트 7항목(기록은 `20_research/` 해당 audit에 append) → 트리 복사(`cp -r 50_app/people/. <repo>/history/people/`) → 양 repo 커밋·push → 라이브 200(+자산) 실측.

## 원칙 (위반 금지)
- 영웅화·악마화 금지 — lightShadow·deepDive에 그림자 실체 있게. 패배자·피해자는 주체로.
- 네트워크 명령은 단독·최소(curl/wget/gh 묶음 금지), 로컬 커밋 먼저. heredoc 금지(python은 Write→실행→rm).
- 신규 등재보다 기존 47인 보강 우선. EP_ORDER(시대순 색인 그룹)는 빌더 상단 — 새 ep 추가 시 갱신.
- 보고는 추론 아닌 실측(before/after 수치, 라이브 200).
