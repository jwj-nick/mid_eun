<!-- 00_project_hub/session/0611_worklog_americas.md -->
# 0611 — Worklog: `americas` 지역 허브 (북미·남미 2에피소드) 자율 제작

> Nick 지시(0611): "americas 자율진행. 이후에 powers 2차분 자율진행."
> 계획 SSOT: `plan/0610_plan_hub_americas.md` · 구조 SSOT: `10_docs/SERIES_ROADMAP.md`

## Round 1 — 착수·구조 결정 (NCC)

**구조 (plan §0 그대로 + 경로 설계):**
- 지역 허브 랜딩 `/history/americas/` (자체 카드 2장 + 상위 허브 링크) — `/history/index.html` 패턴 복제, 배포 repo에 직접 작성.
- 에피소드 2개를 **중첩 배치**: `/history/americas/north-america/`, `/history/americas/latin-america/`.
  - 근거(실측): 엔진의 허브 백링크가 `../index.html` 하드코딩 → 중첩 배치 시 자동으로 **americas 랜딩**을 가리킴. 엔진 변경 0으로 지역 허브 계층 완성.
  - 인물 도감 역링크는 `related[].ep = "americas/north-america"` 형태로 — build_people의 `../../<ep>/` 패턴이 중첩 경로를 그대로 지원(실측 확인).
- 소스는 평소대로 `30_content/north-america/`, `30_content/latin-america/` + `50_app/<slug>/` 빌드, 배포 시 중첩 폴더로 복사.

**사전 발견·수정한 버그:** 인물 도감 색인이 `EP_ORDER=["ww2","imperialism"]` 밖 인물을 조용히 누락 — powers·exploration 10인이 색인에 안 보이던 상태. EP_ORDER 시대순 확장 + fallback 그룹(경고 출력)으로 수정·배포 완료(`e801055`/`cc8d78e`).

**범위:**
- 북미 6섹션: natives(원주민의 땅)→colonies→revolution(1776)→expansion(서부 개척과 눈물의 길★균형)→civil-war→modern
- 남미 5섹션: civilizations(마야·아스텍·잉카)→conquest→colonial(300년)→independence(볼리바르·아이티)→modern
- 인물 +6 (도감 31→37): 워싱턴·링컨·시팅 불(북미) / 볼리바르·산마르틴·투생 루베르튀르(남미)
- 균형 원칙(plan §3): 원주민·노예·이민이 **주체**. 개척 서사 = 원주민 비극과 동시 서술. 아이티=노예가 세운 공화국 강조.

**작업 순서:** ①[로컬] 북미 6섹션→②[로컬] 남미 5섹션→③people 6인→커밋→④[네트워크·단독] 이미지(섹션 ~11+초상 6) 소싱·육안 검수→⑤빌드·G0~G2·audit→⑥americas 랜딩+허브 연결+exploration 교차링크→⑦배포·라이브 검증→⑧문서.

## Round 2 — 제작 기록 (NCC, 0611)
1. ✅ [로컬] 북미 6섹션 + 남미 5섹션(임시 JSON→조립) + 인물 6인(도감 37). 커밋 `4c2d96d`.
2. ✅ [네트워크·단독] Commons 17점 소싱(검색→다운로드, 실패 2건은 정확제목 재시도) — **전점 PD/CC 확인 + 육안 검수**. 눈물의 길(Lindneux)=비PD 사전 회피 → American Progress(1872)로 대체(연출 분석 콘텐츠화). 워싱턴 미완성 캔버스 상단 크롭.
3. ✅ 이미지 11블록 연결 → 재빌드 → G1(데이터 스크립트 node check)·G2(6:6, 5:5) PASS. 도감 색인 6그룹 확인.
4. ✅ hist-audit ×2 (수정 1건: 아르헨티나 실종자 '인권단체 추정' 명기). 기록 = `20_research/{north,latin}-america/audit.md`.
5. ✅ americas 랜딩 작성(배포 repo) + 메인 허브 '지역 허브' 구획(사이드바·카드) + exploration 다리 2개(conquest·slave-trade) 추가·재빌드.
6. ✅ 배포 복사: `history/americas/{index.html, north-america/, latin-america/}` + people 37인 + exploration.

**결정/교훈:**
- 중첩 배치(`americas/<ep>/`)는 엔진 백링크(`../index.html`)와 우연히 완벽 호환 — 지역 허브 계층이 엔진 변경 0으로 성립.
- 색인 버그(EP_ORDER)처럼 '빌더의 조용한 누락'은 fallback+경고로 원천 차단하는 패턴이 옳음 — build_people에 적용 완료.
- 11섹션 일괄 제작에서도 '섹션 임시 JSON→조립 검증' 패턴 무사고 유지.

(이하 배포 검증 라운드 append)
