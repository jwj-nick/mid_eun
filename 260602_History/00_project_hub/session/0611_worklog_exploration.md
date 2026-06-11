<!-- 00_project_hub/session/0611_worklog_exploration.md -->
# 0611 — Worklog: `exploration` 허브(바다 너머로 — 대항해시대) 자율 제작

> Nick 지시(0611): powers 1차 배포 직후 "다음 에피소드 생성 진행 바람". 우선순위 ② = exploration.
> 계획 SSOT: `plan/0610_plan_hub_exploration.md` · 구조 SSOT: `10_docs/SERIES_ROADMAP.md`

## Round 1 — 착수·범위 (NCC)

**범위: 8섹션 전체 1차 완성** (plan §1 그대로 — 시대 서사가 한 흐름이라 분할 없이):
`why-sea`(왜 바다로) → `pioneers`(포르투갈·스페인) → `columbus`★ → `magellan` → `conquest`(아스텍·잉카) → `slave-trade`(삼각무역·노예) → `commerce`(상업혁명) → `toward-modern`(근대로)

**인물 (도감 25→31인)**: 1차 = 엔히크·콜럼버스·마젤란·코르테스·**목테수마·아타우알파**(정복당한 쪽의 얼굴, 균형 핵심). 다 가마·피사로는 섹션 인물카드(도감 링크 없이)로 두고 도감은 차기(plan §2의 6~8인 중 6 먼저).

**균형·수위 (이 에피소드 최우선 원칙, plan §3)**:
- '발견'≠중립 — 이미 살던 사람들에겐 침략. 모든 정복·노예 섹션에 voice(상상, 존엄)와 deepdive 양쪽 시선.
- 잔혹 직접묘사 절제(중간항로·정복 전쟁), 숫자는 '추정 논쟁' 명기(타이노·멕시코 인구 등).
- 탈서구중심 장치: 정화(鄭和) 비교 deepdive(왜 중국이 아니라 유럽이?), 라푸라푸·틀락스칼라·마룬 공동체.

**기술 결정**:
- EP 04. 허브 흐름 밴드에선 시대순 맨 앞(대항해 → … → 세계대전).
- 마젤란 세계일주 battlemap = 경도 서진 연속 표기(동반구 경도에 −360 적용, ww2 태평양 +360 기법의 거울) — 날짜변경선 단절 방지.
- 섹션 시대색: 바다 계열 그라데이션(청록→남청→황혼).
- star = `columbus`(빛과 그림자 논쟁의 입구).
- yt: 기검증 ID 풀에 이 시대 영상 없음 → WebSearch+oembed로 신규 2~3개 검증, 나머지 search형.

**작업 순서 (powers와 동일 표준 + 강화된 G1)**:
① [로컬] episode.json 8섹션(임시 JSON→조립·검증) + people 6인 → 커밋
② [네트워크·단독] Commons 이미지(섹션 ~8 + 초상 6) 검색→검토→다운로드→**전점 육안 검수** / yt 검증
③ [로컬] 연결·빌드·G0~G2(데이터/엔진 분리 node check)·hist-audit
④ 허브 카드(EP04)·교차링크(imperialism#industry↔commerce, powers↔없음, americas 예고) → 커밋
⑤ [네트워크·단독] push → 배포 repo → 라이브 검증
⑥ 문서: PROGRESS·ROADMAP·plan 개선 아이디어 append

## Round 2 — 제작 기록 (NCC, 0611)
1. ✅ [로컬] 8섹션 작성(임시 JSON→조립, choice 스키마 교정·typo 교정 포함) — 115KB, terms 15, 전 섹션 deepdive 5. 인물 6인 → 도감 31인. 커밋 `d5ef9ff`.
2. ✅ [네트워크·단독] Commons 14점 소싱(검색→재검색 2건→썸네일 API 다운로드, TIFF 원본 회피) — **전점 PD, 전점 육안 검수**. 그림의 '연출'(밴덜린 빛/그늘, 다 가마 기념화 시점)을 미디어 리터러시 콘텐츠로 역이용.
3. ✅ 이미지 블록 8개 연결(toward-modern은 oldmap) → 재빌드 → G1(데이터/엔진 분리)·G2(8:8) PASS.
4. ✅ hist-audit 인라인: 수정 1건(코르테스 '배 불태움' 통념 → 좌초·해체 사실로 교정, bio에 통념 교정 문구). 기록 `20_research/exploration/audit.md`.
5. ✅ 허브: 사이드바 04 + 흐름 밴드(대항해→유럽 열강↔제국주의→세계대전) + EP04 카드(⛵). imperialism#industry에 '앞 칸' 역링크.
6. ✅ 문서: PROGRESS·ROADMAP ✅ 갱신, plan §6 구현기록·§7 개선 아이디어 6건.

**결정/교훈:**
- 마젤란 battlemap: 서진 경도 −360 연속 표기 — 출발 세비야(−6)와 귀환 세비야(−366)가 지도상 한 바퀴 떨어져 보이는 것을 '지구를 돌았다는 증거'로 caption에서 역이용.
- yt는 전부 search형(허위 ID 금지 원칙) — 핀 교체는 백로그(plan §7-1).
- 8섹션 일괄 제작도 '섹션별 임시 JSON→조립 검증' 패턴으로 무사고 — 이 패턴을 신규 에피소드 표준으로.

(이하 배포 검증 라운드 append)
