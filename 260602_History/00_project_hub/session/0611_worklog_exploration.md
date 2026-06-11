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

(진행하며 라운드 append)
