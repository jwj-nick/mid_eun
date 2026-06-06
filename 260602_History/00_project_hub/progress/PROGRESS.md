<!-- 00_project_hub/progress/PROGRESS.md -->
# PROGRESS — 역사 허브 추적 대시보드

> 한눈에 보는 진행 상태. 갱신: 0604.

## 시스템 (제작 인프라)
| 항목 | 상태 | 위치 |
|---|---|---|
| 마스터플랜 | ✅ | `plan/260603_history_hub_master_plan.md` |
| Episode Content Schema | ✅ | `10_docs/EPISODE_SCHEMA.md` |
| 렌더 엔진(템플릿) | ✅ | `40_build/templates/episode.html` |
| 빌더 | ✅ | `40_build/build.py` |
| 스킬 7개 | 🟡 seed (app-build=✅validated) | `.claude/skills/hist-*` |
| 오케스트레이터 | 🟡 seed | `.claude/agents/hist-episode-orchestrator.md` |
| 배포 계층(허브/에피소드/mid1링크) | ✅ | `jwj-nick.github.io/history/` |

## 에피소드
| # | slug | 제목 | 단계 | 라이브 |
|---|---|---|---|---|
| 01 | `ww2` | 세계대전 이야기 | ✅ 배포 (스키마/빌드 전환 완료) | https://jwj-nick.github.io/history/ww2/ |
| 02 | `imperialism` | 제국주의와 19세기 | ✅ 배포 (audit 0 치명·3 패치) | https://jwj-nick.github.io/history/imperialism/ |
| — | `coldwar` | 냉전(F2) | 후보 (다음) | — |

## 스킬 정련 상태 (추출형)
| 스킬 | 상태 |
|---|---|
| hist-app-build | ✅ validated (ww2 재현) |
| hist-episode-plan / research / content-write / audit / deploy / distill | 🟡 seed — Ep02에서 정련 |

## Enrichment (콘텐츠/품질 개선)
- 아이디어 보드: `session/0604_enrichment_ideas.md`
- **▶ 활성 계획(작업순서): `plan/0605_replan.md` (S0 서사·정서레이어 + S1~S7 블록 + T1~T4)**
- 창의 재검토(참여장치 9): `10_docs/0605_viz_creative_review.md`
- (참고) 이전: `plan/0604_enrichment_execution_plan.md` — 8스텝 워크플로우·원칙은 유효
- 원칙: 라운드 1개 = 엔진 재사용 블록 1개 + 스킬/스키마/audit/agent 동반 갱신
- (0604) 허브 `/history/` 사이드바+고급 리디자인 + 전 에피소드 사이드바 '허브로' 링크 ✅ 라이브
- (0604) **Phase0 피드백 루프 ✅ / R1 quiz ✅ / R2 notes-export ✅** (엔진 블록, 두 에피소드 라이브)
- (0605) **R1 퀴즈 16/16 ✅ / R3 지도 = Leaflet 실제 지도로 교체 ✅**(손그림 폐기, 아프리카·한반도) 라이브
- (0605) **챕터별 시각화 아이디어 문서 ✅** `10_docs/VISUALIZATION_IDEAS.md`
- (0605) **지도 전략 SSOT ✅** `10_docs/0605_map_strategy.md` (외부조사 통합·비판평가: Leaflet 단일 유지, Mapbox/실시간API 거름)
- (0605) **S0 서사·정서 레이어 ✅ 라이브** — 두 에피소드: 역사 탐정+또래 프레이밍, reflect 16개 편지✉️/단서🔎화, 미스터리 훅(안네·아편전쟁). 엔진 변경 0. 커밋 7cb269e
- (0605) **S1 image 블록 ✅ 라이브** — PD 1914 식민 아프리카 역사지도(imperialism, 현대지도+옛지도 나란히) + 엔진 image/hotspot + 자산 파이프라인(build.py). 커밋 744457f
- (0605) **S2 map 확대 ✅ 라이브** — 실좌표 지도 6곳(ww2: 안네 은신처·유럽전선·태평양 / imp: 인도·아편·조선). 각 에피소드 1→4곳. 커밋 f63a9fa
- (0605) **S3 voice 블록 ✅ 라이브** — 일기·편지체(임칙서 상상·안네 실제) + 실제/상상 배지. 커밋 fa4d649
- (0605) **S4 chart 블록 ✅ 라이브** — 자체 막대 + 체감비교(대공황 실업률·아편 수입). 커밋 e6704f4
- (0605) **S5 compare 블록 ✅ 라이브** — 단계 토글(한국전쟁 전선 4단계·메이지 유신 전후). 커밋 66319d6
- (0605) **S6 인물 도감 ✅ 라이브** — `/history/people/` 크로스에피소드 색인(6명, build_people.py) + 허브 링크/카드. 커밋 e47c6c2
- (0605) **S7 choice 블록 ✅ 라이브** — '너라면?' 도덕적 딜레마(안네 이웃·동학) + 균형 해설. 커밋 598c7b1
- **🎉 S0~S7 전체 자율진행 완료** — 참여장치 9개 + 블록 6종 두 에피소드 라이브. 최종 결과로 다음 방향 모색(Nick)
- (0606) **P 인물 도감 v2 ✅ 라이브** — 단일소스 `30_content/people/people.json`(에피소드에서 분리) + `build_people.py` 재작성으로 **인물별 페이지** 6종 생성. 사진(Wikimedia, 출처표기)·다국어 이름(원어/발음/로마자/영어/한국어)·생애·연표·빛과 그림자·**관련 에피소드 섹션 역링크**(도감↔이야기 순환)·공식 링크·"편지" 메모. https://jwj-nick.github.io/history/people/<slug>/ 6인물 + 이미지 전부 200 검증.
- (0606) ⚠️ **치명 교훈 — 멈춤 없는 workflow**: foreground Agent 다중 await가 hang→수시간 동결+감지불가 사고. `CLAUDE.md §멈춤 없는 병렬·대량 작업 프로토콜` 신설 + hist-research·오케스트레이터 갱신(background+폴링 / 2개 배치+체크포인트 / 인라인 우선 / 실측 보고).

## 다음 액션
- ⬜ Ep02(`imperialism`) 제작 시작 → 각 seed 스킬 정련
- ⬜ Ep01 검색링크(🔍) 3개 특정 영상 핀 교체
- ⬜ (선택) 첫 영상 실험 / 인물 갤러리(`/history/people/`)

## 로그
- 0602 Ep01 베타 → near-final → 배포. 허브/계층 정리.
- 0603 마스터플랜 + 에피소드 로드맵 + 워크플로우 셋업 세션.
- 0604 빌드 시스템 추출(스키마·템플릿·빌더) + ww2 스키마 전환·재배포 + 스킬 7 + 오케스트레이터.
