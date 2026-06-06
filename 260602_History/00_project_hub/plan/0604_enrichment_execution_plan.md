<!-- 00_project_hub/plan/0604_enrichment_execution_plan.md -->
# Plan — Enrichment 실행 플랜 (작업순서 · 체크포인트 · 시스템 동반갱신)

> 아이디어 보드(`session/0604_enrichment_ideas.md`)를 **실제 작업 순서**로 변환.
> 핵심 약속: **라운드 1개 = 엔진 재사용 블록 1개**, 그리고 **매 블록마다 콘텐츠뿐 아니라 스킬/스키마/audit/agent도 함께 갱신**한다(시스템이 콘텐츠와 같이 자란다).

## ▶ 진행 로그 (지속 갱신)
- **0604 Phase 0 ✅** — 피드백 루프 인프라(`00_project_hub/feedback/관찰표_양식.md`). (허브 자동화는 후속)
- **0604 R1 quiz ✅** — 엔진 quiz 블록(클릭→정답/오답/해설) + 스키마 + ww2·imperialism 각 3섹션 샘플 + hist-content-write/audit 갱신 → 배포. (전 섹션 확장 가능)
- **0604 R2 notes-export ✅** — 사이드바 "📝 내 메모 모아보기" → 전 섹션 메모 취합·인쇄/PDF·복사(엔진 기능, 전 에피소드 자동) + 인쇄 CSS → 배포.
- **0605 R1 퀴즈 전 섹션 확장 ✅** — ww2·imperialism **16/16 섹션** 모두 적용 + 퀴즈 위치를 섹션 끝(메모 직전)으로 정돈 → 배포.
- **0605 R3 map ✅→재작업** — 처음엔 손그림 SVG였으나 피드백("실제 지도 쓸 것") 반영해 **Leaflet+OpenStreetMap 실제 인터랙티브 지도**로 전면 교체(마커 팝업·38선 폴리라인). 아프리카·한반도 적용. 스키마/스킬/audit 갱신.
- **0605 챕터별 시각화 아이디어 문서 ✅** — `10_docs/VISUALIZATION_IDEAS.md` (16챕터 전부, 블록·자산·우선순위). 핵심: 옛 국경은 **공개도메인 역사지도 image 블록(🔧 신설)** 으로.
- **0605 지도 전략 SSOT ✅** — 흩어진 지도 생각을 `10_docs/0605_map_strategy.md`로 통합. 외부조사(`0605_ext_*.md`) 비판평가: Mapbox·실시간 API 거름(키 노출/토큰), **Leaflet 단일 유지**, 4유형 분류 채택, 옛 국경=PD image 블록.
- 다음: (제안) ① image 블록 신설→PD 역사지도 ② map 실지도 챕터 확대 ③ compare 블록.

---

## 0. 원칙
1. **블록 단위로 진화.** 각 enrichment = 엔진의 새 컴포넌트(스키마 블록 타입). 한 번 만들면 모든 에피소드가 `episode.json`에 선택적으로 넣어 사용 → 일회성 하드코딩 금지.
2. **콘텐츠 + 시스템 동반 액션.** 블록을 만들 때 반드시: `EPISODE_SCHEMA.md`(계약) · `hist-content-write`(쓰는 법) · `hist-audit`(점검 항목) · `hist-app-build`(검증) · 오케스트레이터/PROGRESS를 함께 갱신.
3. **딸 피드백이 우선순위를 정한다.** 함께 본 반응 → `learner-profile` → `hist-distill` → 다음 라운드 재정렬.

---

## 1. 표준 "블록 추가" 워크플로우 (모든 라운드 공통)

| 스텝 | 할 일 | ✅ 체크포인트(DoD) |
|---|---|---|
| 1 설계 | 블록 스키마 필드 + UX 1줄 스케치 정의 | `EPISODE_SCHEMA.md`에 블록 초안 적힘 |
| 2 엔진 구현 | `40_build/templates/episode.html`에 렌더러 + CSS | 신규 CSS/JS가 기존 블록과 충돌 없음 |
| 3 스키마 확정 | `EPISODE_SCHEMA.md` 블록 카탈로그에 정식 등록 | 필드·예시 문서화 |
| 4 시범 적용 | ww2 또는 imperialism `episode.json` 1곳에 삽입 | 의미 있는 실제 사용처 1개 |
| 5 빌드·검증 | `build.py` → JS check → parity → 모바일/접근성 | JS_OK · 기존 에피소드 회귀 없음(둘 다 재빌드) |
| 6 배포 | `hist-deploy` (해당 에피소드만 커밋) | 라이브 200 · 동작 확인 |
| 7 **시스템 갱신** | `hist-content-write`에 사용법 / `hist-audit`에 점검항목 / 오케스트레이터·PROGRESS 갱신 | 4개 파일 반영 |
| 8 회고 | 딸 반응 → `hist-distill` → 원칙/learner-profile | 다음 우선순위 갱신 |

> 게이트: 5·6 통과 못하면 다음 라운드로 넘어가지 않는다. 7은 6과 **같은 라운드에서** 반드시 수행(미루지 않음).

---

## 2. 작업 순서 (Phase별)

### Phase 0 — 상시 인프라 (먼저, 1회 셋업)
| 트랙 | 내용 | ✅ 체크포인트 |
|---|---|---|
| **F-루프 (E2)** | `50_app/<slug>/`에 대응하는 딸 반응 기록 루틴: `feedback/` 폴더 + "함께 보기 관찰표" 양식, learner-profile 연결 | 관찰표 양식 1개, 첫 기록 칸 |
| **허브 자동화 (시스템)** | 현재 손편집인 허브 카드 추가를 `hist-deploy`가 자동 갱신하도록(허브를 data+build로 전환 검토) | hist-deploy 실행 시 허브 카드 자동 반영 |

### Phase 1 — Quick Wins (탐구학습 직결) ◀ 추천 시작
| 라운드 | 블록 | 효과 | ✅ 체크포인트 | 동반 시스템 갱신 |
|---|---|---|---|---|
| R1 | **C1 `quiz`** 섹션 끝 미니 체크(1~2문, 정답강요X·즉시 해설) | 가벼운 확인·복습 | 정답/해설 토글, 점수 강박 없음, 모바일 OK | content-write에 quiz 작성법, audit에 "정답·해설 정확/수위" 항목 |
| R2 | **D1 notes-export** 내 메모 모아보기+인쇄/복사 | 발표·보고서 초안(학교 직결) | 전 섹션 메모 1화면 취합, 인쇄/복사 동작, localStorage 유지 | content-write(반영 불필요·엔진 기능), audit "개인정보 로컬저장 안내" |

### Phase 2 — 역사 흥미·이해
| 라운드 | 블록 | ✅ 체크포인트 | 동반 시스템 갱신 |
|---|---|---|---|
| R3 | **A1 `map`** 인터랙티브 지도(정적 SVG + 핫스팟 클릭 설명) | 핫스팟 툴팁/패널, 모바일 탭, 출처 표기 | content-write 지도 데이터 작성법, research에 "지도/좌표·출처" 수집, audit "지리 정확성" |
| R4 | **B2 `compare`** before/after 슬라이더(분단·전쟁 전후) | 드래그/터치 슬라이더, 캡션, 접근성 | content-write compare 작성법, audit "비교 이미지 출처·오해소지" |

### Phase 3 — 인물·몰입·분위기
| 라운드 | 블록 | ✅ 체크포인트 | 동반 시스템 갱신 |
|---|---|---|---|
| R5 | **D3 인물 갤러리** `/history/people/`(에피소드 가로지르는 인물 색인) | 에피소드 people 집계, 허브 사이드바 링크 | 허브 자동화와 연계, distill로 인물 표준 정련 |
| R6 | **B3 `choice`** "너라면?" 선택지 분기 → 결과·해설 | 2~3 선택지, 해설, 단정 회피(균형) | content-write choice 작성법, audit "선택지 균형·역사 왜곡 없음" |
| R7 | **A3 `image`** 시대 분위기 이미지/AI 이미지(히어로/카드) | 출처·라이선스 표기, 로딩·대체텍스트 | research에 이미지 출처/생성 프롬프트, audit "저작권·수위", 90_video 파이프 연계 |

### Phase 4 — 마감 품질·확장 (선택·후순위)
A2 타임라인 고도화 / A4 미니 차트 / A5 인물 초상 / B4 플립카드 / B5 성취 배지 / C2 완주 퀴즈 / C3 study-quiz 연동 / E6 영상 핀 정례화 / E7 영상 제작(딸 참여). 각각 같은 8스텝·체크포인트로.

### 횡단 (매 라운드 적용)
- **E1** audit 멀티 페르소나 + **병렬 에이전트 동시발사·개수검증**(Ep02 교훈, 이미 hist-research 반영).
- **E3** frontend-design 플러그인으로 신규 블록 비주얼·접근성 패스.
- **E5** 접근성·모바일(대비·터치타깃·글자크기) — 폰 우선.

---

## 3. 시스템(스킬/agent/스키마) 진화 트랙 — 무엇이 어떻게 누적되나
| 자산 | 매 블록마다 갱신되는 것 |
|---|---|
| `10_docs/EPISODE_SCHEMA.md` | **블록 카탈로그 SSOT** — 새 블록 타입·필드·예시 누적 |
| `40_build/templates/episode.html` | 블록 렌더러·CSS (엔진이 곧 컴포넌트 라이브러리) |
| `.claude/skills/hist-content-write` | 블록별 "쓰는 법" 가이드 |
| `.claude/skills/hist-audit` | 블록별 점검 항목 (사실·수위·접근성·출처) |
| `.claude/skills/hist-app-build` | 신규 블록 렌더 검증 체크 |
| `.claude/skills/hist-research` | 블록이 요구하는 자료(지도·이미지·출처) 수집 항목 |
| `.claude/skills/hist-deploy` | 허브 카드 자동 갱신(Phase 0 자동화 후) |
| `.claude/agents/hist-episode-orchestrator` | "사용 가능한 블록 카탈로그" 인지 → 자율 제작 시 활용 |
| `00_project_hub/progress/PROGRESS.md` | **블록 카탈로그 상태표** + 라운드 진행 |

---

## 4. 추적 (PROGRESS.md에 추가할 블록 카탈로그)
| 블록 | 라운드 | 엔진 | 스키마 | 시범적용 | audit항목 | 상태 |
|---|---|---|---|---|---|---|
| quiz (C1) | R1 | ✅ | ✅ | ✅ (6섹션 샘플) | ✅ | **완료 0604** |
| notes-export (D1) | R2 | ✅ | ✅ (엔진) | ✅ (전 에피소드) | ✅ | **완료 0604** |
| map (A1) | R3 | ✅ | ✅ | ✅ (2곳) | ✅ | **완료 0605** |
| compare (B2) | R4 | ⬜ | ⬜ | ⬜ | ⬜ | 대기 |
| people-gallery (D3) | R5 | ⬜ | ⬜ | ⬜ | ⬜ | 대기 |
| choice (B3) | R6 | ⬜ | ⬜ | ⬜ | ⬜ | 대기 |
| image (A3) | R7 | ⬜ | ⬜ | ⬜ | ⬜ | 대기 |
> 라운드 완료 시 이 표를 PROGRESS.md로 옮겨 갱신.

---

## 5. 다음 액션 (Nick 선택)
- **추천 시작: Phase 0(피드백 루프 셋업) → R1 quiz → R2 notes-export.** (인프라 → 학교 직결 quick win 2개)
- 또는 흥미 우선이면 **R3 map**부터.
- 비용/제작(A3 이미지·E7 영상)은 Phase 3 이후, 딸 반응 보고 결정.

→ "R1 시작" 또는 원하는 블록을 지정하면, 위 8스텝을 한 라운드로 자율 실행(콘텐츠+시스템 동반 갱신 포함)하겠습니다.
