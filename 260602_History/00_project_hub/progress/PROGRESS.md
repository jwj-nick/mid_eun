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
| hist-page-review (신설 0607) | 🟡 seed — 페이지 완결성·깊이·일관성 점검(hist-audit 보완) |

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
- (0606) **ww2 심화 설계 plan ✅** `plan/0606_ww2_film_people_dynamics.md` (영화·인물·역학 3형식, 순서 a→인물→b, 창의장치 C1~C5)
- (0606) **에피소드→도감 역링크 ✅** — 엔진 personBlock에 slug 링크('인물 도감에서 더 보기'), 두 에피소드 재배포(도감↔이야기 양방향 순환 완성).
- (0606) **(a) movies 블록 ✅ 라이브** — ww2 영화 연계: 쉰들러·피아니스트(europe)·이오지마(pacific)·오펜하이머(postwar). 적합성 신호등🟢🟡🔴 + '실화 vs 각색' + 위키 ko/en 검증 링크. https://jwj-nick.github.io/history/ww2/
- (0606) **(P) 인물 +6인 ✅ 라이브** — 도감 12인: 페르디난트·프린치프·쉰들러·슈필만·오펜하이머·사다코 추가. ww2 섹션 인물카드(slug)·영화↔도감 연결. 모티프: 안네↔사다코(전쟁 양쪽 끝 소녀), 오펜하이머↔사다코(만든 자↔당한 자). https://jwj-nick.github.io/history/people/
- (0606) **(b) relations 역학관계도 ✅ 라이브** — ww2 한국전쟁: 냉전 대리전 구도(🟥스탈린·마오·김일성 ↔ 🟦트루먼·맥아더·이승만) + 긴장선(트루먼vs맥아더 해임=문민통제 등). 엔진 relations 블록 신규.
- (0607) **검증 워크플로우 정식화 ✅** — hist-deploy §검증 G0~G3(빌드/JS_OK/자원 200·실물·ko제목/라이브 대기루프) + hist-app-build JS_OK 게이트. "추론 금지, 실측만."
- (0607) **허브 링크 누락 수정 ✅ 라이브** — 상단바(topbar)에 '🏛️ 역사 허브'(모바일에서 항상 보임). 엔진 1곳 → 두 에피소드 전파.
- (0607) **지도 C 시작** — 계획 `plan/0607_map_C_execution_plan.md`(A Leaflet+B SVG, B적극) + 비전 `10_docs/0607_map_next_level.md`(N1~N9 후보·로드맵·리뷰R1~R5). Mapbox 제외(키·과금·불필요), 미래 MapLibre.
- (0607) **공식 문서**: `10_docs/MAP_TOOLKIT.md`(지도 툴·규칙) + `plan/0607_visual_content_masterplan.md`(전 페이지 비주얼·내용 강화, 대상수준 계층적 깊이) + `plan/0607_page_imperialism_korea.md`(첫 대상 세부).
- (0607) **첫 대상 '위기의 조선' 심층 개선 ✅ 라이브** — 신규 재사용 엔진 **battlemap**(Leaflet+ant-path, 동학+청일/러일) + **deepdive**(계층적 깊이 '더 깊이': 인과사슬·갑오개혁·인내천·명칭논쟁·전봉준 공초) + voice(공초 1차사료)+compare(갑오개혁). 동학 marchmap→battlemap 승격(위치/겹침 해소).
- (0607) **C 1단계 — 동학 marchmap ✅ 라이브(리뷰 대기)** — 신규 marchmap 엔진(역사지도 위 SVG 곡선 진격로 + 단계 스테퍼 + dashoffset 애니, 저항/침탈 색). imperialism/korea 우금치 6국면. 좌표=표준 bounds 계산(시각 미세조정은 Nick 리뷰 후).
- (0607) **후속 아이디어 3종 ✅ 라이브** — ① 인물 도감 18인(한국전쟁 6인 추가→역학도 노드 드릴다운) ② ww2 사라예보 '만약에?' 반사실 choice(도화선vs원인) ③ imperialism 조선 각축 역학도(청·일·러 3진영, relations 재사용·green 추가).
- (0607) **'위기의 조선' image+chart ✅ 라이브** — image(전봉준 압송 1895, PD/Wikimedia, 사진 story) + chart(개항장 누적 추이 1876~99). 페이지 비주얼·내용 3축 강화 진행. Nick 코멘트="구성 다시 생각해보기"(피드백 루프).
- (0607) **'위기의 조선' Round2 완결성 보강 ✅ 라이브** — 🆕 **`hist-page-review` 스킬 신설**(페이지 완결성/깊이/일관성 5렌즈, hist-audit 보완). 완결성 점검으로 잡은 3대 공백 보강: ① 갑오개혁 주체(군국기무처→김홍집) ② 마지막 왕조·권력구도(고종/순종/흥선대원군, 대원군 쇄국 vs 명성황후 외교) ③ 일본 부상(메이지유신 deepdive + **chart:1 속도 차트**). chart 배열 엔진 확장. deepdive 7항목. 인과사슬에 러일·을사늑약 다리.
- (0607) **'위기의 조선' Round1 구성 재편 ✅ 라이브** — Nick 확정(Q1~Q4). ① 옛 map 제거(중복) ② **엔진 업그레이드: 블록 순서 데이터화** `renderBlocks()`+섹션 `order`(하위호환, 전 페이지 공통) ③ korea 새 흐름 재배열(동학서사→열강각축→나라변화) ④ **oldmap 블록 신설**+고지도1818(PD 시대감) + **경복궁1886**(PD/Smithsonian, image 배열 2장). 재사용 확보: order·oldmap·image배열(EPISODE_SCHEMA·MAP_TOOLKIT 등재). G0~G3 통과.
- (0607) ⚠️ **워크플로우 교훈 — 도구 결과 손실·인코딩**: `[Tool result missing]`/"내부 오류"의 실측 근본원인 = cp949 콘솔이 한글·이모지 stdout에서 `UnicodeEncodeError`로 죽어 결과 손실. `CLAUDE.md §도구 결과 손실·인코딩·타임아웃 프로토콜(A~E)` 신설: PYTHONIOENCODING=utf-8 선제, 한글 콘솔 덤프 회피(파일+Read/ASCII요약), grep 좁게, 결과없음 시 추론금지·즉시 멱등 프로브, 유한 대기루프, 실측 보고.
- (0606) ⚠️ **치명 교훈 — 멈춤 없는 workflow**: foreground Agent 다중 await가 hang→수시간 동결+감지불가 사고. `CLAUDE.md §멈춤 없는 병렬·대량 작업 프로토콜` 신설 + hist-research·오케스트레이터 갱신(background+폴링 / 2개 배치+체크포인트 / 인라인 우선 / 실측 보고).

## 다음 액션
- ⬜ Ep02(`imperialism`) 제작 시작 → 각 seed 스킬 정련
- ⬜ Ep01 검색링크(🔍) 3개 특정 영상 핀 교체
- ⬜ (선택) 첫 영상 실험 / 인물 갤러리(`/history/people/`)

## 로그
- 0602 Ep01 베타 → near-final → 배포. 허브/계층 정리.
- 0603 마스터플랜 + 에피소드 로드맵 + 워크플로우 셋업 세션.
- 0604 빌드 시스템 추출(스키마·템플릿·빌더) + ww2 스키마 전환·재배포 + 스킬 7 + 오케스트레이터.
