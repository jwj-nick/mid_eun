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
| 스킬 9개 | 🟡 seed (app-build=✅validated) | `.claude/skills/hist-*` (에피소드 6단계 + page-review + distill + **hist-person**) |
| 오케스트레이터 | 🟡 seed | `.claude/agents/hist-episode-orchestrator.md` |
| 배포 계층(허브/에피소드/mid1링크) | ✅ | `jwj-nick.github.io/history/` |

## 에피소드
| # | slug | 제목 | 단계 | 라이브 |
|---|---|---|---|---|
| 01 | `ww2` | 세계대전 이야기 | ✅ 배포 (스키마/빌드 전환 완료) | https://jwj-nick.github.io/history/ww2/ |
| 02 | `imperialism` | 제국주의와 19세기 | ✅ 배포 (8/8 풀 업그레이드) | https://jwj-nick.github.io/history/imperialism/ |
| 03 | `powers` | 유럽 열강 열전 | ✅ 완성 (7/7: 도입·영·프·독·러·벨·후발 / 도감 38인) | https://jwj-nick.github.io/history/powers/ |
| 04 | `exploration` | 바다 너머로 — 대항해시대 | ✅ 배포 (8/8 풀 업그레이드) | https://jwj-nick.github.io/history/exploration/ |
| 05 | `renaissance` | 다시 태어난 인간 — 르네상스·종교개혁 | ✅ 배포 (7/7) | https://jwj-nick.github.io/history/renaissance/ |
| 06 | `revolutions` | 자유를 향하여 — 계몽·시민혁명 | ✅ 배포 (7/7) | https://jwj-nick.github.io/history/revolutions/ |
| 🌎 | `americas` | 아메리카 허브 (북미 6 + 남미 5섹션, 도감 37인) | ✅ 배포 (랜딩+2에피소드) | https://jwj-nick.github.io/history/americas/ |
| ✉️ | `figures` | 사람의 자리 — 짝으로 읽는 인물 이야기 | ✅ 배포 (6섹션, 도감 가로지르기) | https://jwj-nick.github.io/history/figures/ |
| 07 | `coldwar` | 냉전 — 총성 없는 50년 (8/8: 두진영·핵·베를린·쿠바·대리전·우주·데탕트·장벽붕괴) | ✅ 배포 (0614) | https://jwj-nick.github.io/history/coldwar/ |
| 08 | `globalization` | 탈냉전과 세계화 (7/7: 소련해체·세계화·인터넷·9·11·EU·중국부상·세계화 명암) | ✅ 배포 (0614) | https://jwj-nick.github.io/history/globalization/ |
| 09 | `new-order` | 새로운 질서 — 다극·미중·AI (7/7: 금융위기·다극·미중·반도체·연결된위기·AI·열린결말) — **시간 사슬 끝** | ✅ 배포 (0614) | https://jwj-nick.github.io/history/new-order/ |
| 🔬 | `tracks/sci-tech` | 과학기술 — 인류가 세상을 푸는 법 (12정거장·호기심 엔진·고등/일반) | ✅ 배포 (0616) | https://jwj-nick.github.io/history/tracks/sci-tech/ |
| 💹 | `tracks/finance` | 경제·금융 **4부작 허브** — 돈의 발명(10)·금융을 만든 사람들(7)·돈과 힘(7)·돈과 삶/자녀에게(7) = 31정거장+랜딩. 호기심 엔진·고등/일반·⚠️투자조언0 | ✅ 배포 (0618) | https://jwj-nick.github.io/history/tracks/finance/ |
| ↳ | `…/finance/{history,people,empire,wisdom}` | 4개 에피소드 + 랜딩(자녀에게 보내는 편지) | ✅ 배포 (0618) | …/finance/people · /empire · /wisdom |
| ⚽ | `tracks/sports` | 축구 **3부작 허브**(전문가 수준) — 역사(6)·빅리그 시스템(6)·세계의 축구(6) = 18정거장. 승강제·이적상각·FFP·스포츠워싱 등 시스템 심층 | ✅ 배포 (0619) | https://jwj-nick.github.io/history/tracks/sports/ |
| — | `tracks/*` (나머지) | 예술·문화 트랙 | 🟡 계획됨 (`plan/0614_masterplan_renaissance_to_ai.md` §3) | — |

## 🗺️ 시리즈 확장 로드맵 (0610)
> **구조 SSOT = `10_docs/SERIES_ROADMAP.md`** (시대 사슬 전체 지도, one hub=one plan). 아래는 진척 요약만.
> 사슬: 르네상스·종교개혁 → 대항해시대 → 계몽·시민혁명 → [유럽 열강 ↔ **제국주의✅**] → **세계대전✅** + 아메리카(병렬). (산업혁명=imperialism#industry가 home)
| 우선 | 시대 허브 | slug | 계획 파일 | 상태 |
|---|---|---|---|---|
| ① | 유럽 열강 | `powers` | `plan/0610_plan_hub_powers.md` | ✅ 완성(0611, 7/7) |
| ② | 대항해시대 | `exploration` | `plan/0610_plan_hub_exploration.md` | ✅ 배포(0611, 8/8) |
| ③ | 아메리카(지역) | `americas` | `plan/0610_plan_hub_americas.md` | ✅ 배포(0611, 랜딩+11섹션) |
| ✅ | 제국주의 | `imperialism` | (배포 완료, 8/8) | ✅ |
| ✅ | 세계대전 | `ww2` | (배포 완료, 8/8) | ✅ |
| ✅ | 계몽·시민혁명 | `revolutions` | `plan/0610_plan_hub_revolutions.md` | ✅ 배포(0612) |
| ✅ | 르네상스·종교개혁 | `renaissance` | `plan/0610_plan_hub_renaissance.md` | ✅ 배포(0612) |

## 스킬 정련 상태 (추출형)
| 스킬 | 상태 |
|---|---|
| hist-app-build | ✅ validated (ww2 재현) |
| hist-episode-plan / research / content-write / audit / deploy / distill | 🟡 seed — Ep02에서 정련 |
| hist-page-review (신설 0607) | 🟡 seed — 페이지 완결성·깊이·일관성 점검(hist-audit 보완) |
| **hist-person (신설 0612)** | 🟡 seed — 인물 도감 v3/v3.1 추가·보강. 법전 `10_docs/PEOPLE_GUIDE.md`, 표준 견본 안중근 |

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
- (0608) **위기의 조선(imperialism/korea) 풀 업그레이드 ✅ = 기준 사례** (R1구성재편·R2완결성·R3대원군+audit). 엔진 `order`·oldmap·image배열·chart배열 신설. + `hist-page-review` 스킬.
- (0608) **ww2#imperialism(1차대전) ✅ 배포** — image2(식민지도CC BY·사라예보CC0)·relations·battlemap·chart·voice·deepdive5·order. 엔진 변경 0.
- (0609) **★ ww2 6개 섹션 일괄 풀 업그레이드 ✅ 전부 배포** (순차 지시). 계획=`plan/0609_page_ww2_{outbreak,europe,pacific,asia,postwar,korea}.md`:
  - **outbreak**: relations(추축↔연합)·battlemap(독일팽창36~39)·voice·deepdive5·image(뮌헨협정 CC BY-SA).
  - **europe**: battlemap4국면(전격전·바르바로사·스탈린그라드·D-Day)·relations(냉전씨앗)·chart(나라별사망자)·voice(레닌그라드)·deepdive5·image(D-Day PD). map→battlemap격상.
  - **pacific**: battlemap4국면(진주만·미드웨이·섬건너뛰기·원폭)·chart(미일생산격차)·voice·deepdive5(원폭논쟁)·image(진주만 PD).
  - **asia**(최빈약): battlemap4국면(병합~광복)·**인물 안중근·윤동주 신설(도감 21인)**·voice(강제동원)·deepdive5(균형)·image(광복1945 PD).
  - **postwar**: relations(냉전진영)·map(분단지점)·chart(1차vs2차)·voice·deepdive5(뉘른베르크·UN·냉전)·image(뉘른베르크 PD).
  - **korea**: battlemap4국면(남침~정전)·chart(전쟁3년vs분단73년)·voice(피란)·deepdive5(대리전·휴전체제·문민통제)·image(흥남철수 PD). compare·relations 유지.
  - 전부 **엔진 변경 0**(데이터만, asia만 people 재빌드). 자산 기준=PD/CC0/**CC BY-SA**(출처표기). 소스(mid_eun)·배포(jwj-nick.github.io) 양쪽 push.
  - ⚠️ **anne(섹션2)는 미상**(Nick URL목록 제외) — 감성 입구라 톤보존 경량패스 대기. **asia 균형 hist-audit 권장.**
- (0609 ★★) **전 페이지 풀 업그레이드 완료 — 두 에피소드 8/8씩 = 16섹션 전부 ✅ 배포** (Nick "끝까지 자율 진행" 지시):
  - **ww2 anne**(경량 패스, 톤 보존): image(은신처 책장 CC0)·deepdive3(미프 히스·홀로코스트 구조·일기가 살아남기까지). battlemap/chart 미사용, 실제 일기 인용·voice·choice 유지. → **ww2 8/8 완성.**
  - **imperialism 나머지 6**: industry(역직기·맨체스터·아동노동)·why-empire(Rhodes Colossus·선발↔후발 제국·홉슨레닌)·scramble(저항 battlemap 아도와·분할속도, 이미지 기존 재사용)·india(1857항쟁·탈산업화 25%→2%)·opium-china(네메시스·삼각무역·원명원)·japan-meiji(이와쿠라·청일러일·철도급증)·toward-war(1914 풍자지도·동맹사슬·발칸→ww2 다리). → **imperialism 8/8 완성.**
  - 자산(전부 PD/CC0/CC BY-SA, 출처표기): munich·dday·pearl_harbor·liberation·nuremberg·korea_war·anne_bookcase(CC0) / imp: industrial_city·imperialism_cartoon·india_1857·opium_war·iwakura_mission·europe_1914_satire. 인물 an-junggeun·yun-dongju. 소싱=urllib Commons API(격리 네트워크), PIL 리사이즈, file 검증. 저작권 논란(Max Desfor AP 등) 회피.
  - 패턴: 섹션별 battlemap(보통 2~4국면)+image+voice+deepdive5+(chart/relations)+order, **엔진 변경 0**(데이터만; asia만 people 재빌드). 계획=`plan/0609_page_{ww2,imp}_*.md` 13개(각 Round1 기록).
  - **남은 권장**: asia 균형 hist-audit / 딸과 함께 보기 → 피드백 / (선택) 인물 더 확장(미프 히스·간디 등) / globe·territory 엔진 승격(why-empire·postwar)은 보류.
- (0607) **첫 대상 '위기의 조선' 심층 개선 ✅ 라이브** — 신규 재사용 엔진 **battlemap**(Leaflet+ant-path, 동학+청일/러일) + **deepdive**(계층적 깊이 '더 깊이': 인과사슬·갑오개혁·인내천·명칭논쟁·전봉준 공초) + voice(공초 1차사료)+compare(갑오개혁). 동학 marchmap→battlemap 승격(위치/겹침 해소).
- (0607) **C 1단계 — 동학 marchmap ✅ 라이브(리뷰 대기)** — 신규 marchmap 엔진(역사지도 위 SVG 곡선 진격로 + 단계 스테퍼 + dashoffset 애니, 저항/침탈 색). imperialism/korea 우금치 6국면. 좌표=표준 bounds 계산(시각 미세조정은 Nick 리뷰 후).
- (0607) **후속 아이디어 3종 ✅ 라이브** — ① 인물 도감 18인(한국전쟁 6인 추가→역학도 노드 드릴다운) ② ww2 사라예보 '만약에?' 반사실 choice(도화선vs원인) ③ imperialism 조선 각축 역학도(청·일·러 3진영, relations 재사용·green 추가).
- (0607) **'위기의 조선' image+chart ✅ 라이브** — image(전봉준 압송 1895, PD/Wikimedia, 사진 story) + chart(개항장 누적 추이 1876~99). 페이지 비주얼·내용 3축 강화 진행. Nick 코멘트="구성 다시 생각해보기"(피드백 루프).
- (0609) **전 페이지 순차 — ww2 #1 "지도를 색칠하던 시대"(1차대전) 풀 업그레이드 ✅ 배포** — 가장 얇던 페이지에 image[2](1914 식민지도 CC BY·사라예보 CC0)+relations(협상↔동맹)+battlemap(사라예보→슐리펜→마른→참호)+chart(상비군)+voice(참호 병사)+deepdive5(MAIN 4원인·발칸·7월위기·총력전)+order. 엔진 변경 0(전부 재사용). 마스터플랜=`plan/0608_upgrade_masterplan_concrete.md`(Nick 확정: 순서OK·냉전보류·엔진 그때그때·인물 함께). 세부=`plan/0608_page_ww2_imperialism.md`.
- (0608) **'위기의 조선' Round3 + 전 페이지 순차 시작** — ① **흥선대원군 인물 추가**(도감 19인, 1883 PD 사진, 위기의 조선 카드) ② **hist-audit 1회**(치명0, 사실·균형 통과). ③ 다음=**전 내부 페이지 순차 업그레이드**(Nick 지시): ww2 첫 페이지 `plan/0608_page_ww2_imperialism.md`(아이디어 정리·코멘트 대기).
- (0608) ⚠️ **치명 교훈 — 승인대기 11h 멈춤**: curl/wget/gh가 `~/.claude/settings.json` ask목록→항상 승인. 빌드와 묶어 11h idle 사고. **최근 14일 8개 CLAUDE.md 전부에 "멈춤·승인대기 방지 프로토콜" 못박음**(네트워크 단독·최소, 로컬 먼저 커밋, WebFetch 우선, 결과없음 시 멱등 프로브). 메모리 `feedback_approval_wait_network`.
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
- 0619~20 **한국사 시리즈(`korea/*`) 고등심화** — 랜딩 + Part1 `ancient`(6)·Part2 `three-kingdoms`(7)+삼국 심화 3페이지(goguryeo·baekje·silla 각 6). **엔진 `legend` 블록 신설**(설화) + 지명 현재위치 그라운딩을 스킬/스키마에 의무화(설화 7편 적용).
- 0620 **Part3 `korea/goryeo`(7) ✅** — 후삼국통일·광종성종·거란여진(서희·강감찬)·무신정권(만적)·**몽골 40년 항쟁★**(강화천도·처인성·삼별초·팔만대장경)·청자/금속활자 문화·원간섭·공민왕→위화도회군. 설화 2편(왕건 버들잎·강감찬 낙성대)+지도 2종+사료/유물 이미지. 남은 3: joseon·modern·east-asia.
- 0620 **Part4 `korea/joseon`(8) ✅** — 건국(정도전·한양)·세종(훈민정음·과학·4군6진)·사림붕당(경국대전·사화)·**임진왜란★**(이순신·의병·명군·정유재란)·병자호란(광해군 중립외교·삼전도)·영정조 실학(탕평·수원화성·정약용)·후기 서민문화(풍속화·판소리·달항아리)·세도정치→강화도조약. 설화 2편(정몽주 선죽교·논개)+지도 2종(임진왜란 형세도·4군6진)+이미지 9종. 앙부일구는 현대 재현품이라 드롭. 남은 2: modern·east-asia.
- 0621 **Part5 `korea/modern`(8) ✅** — 개항(강화도조약)·격변(임오군란·갑신정변·동학)·대한제국(갑오개혁·을미사변·독립협회)·**국권피탈★**(러일전쟁·을사늑약·헤이그·안중근·경술국치)·무단통치3·1운동·임시정부·무장의열문화투쟁(봉오동청산리·윤봉길·조선어학회)·민족말살→1945광복. 설화 2편(파랑새요·아리랑)+지도 2종(국권피탈 글로벌·3·1확산)+이미지 6종. imperialism편 교차링크로 중복회피. 남은 1: east-asia(캡스톤).
- 0621 **왕조 계보 기능 ✅**(Nick 요청 "클릭/터치 펼침 계보, 삼국~조선 각 한 페이지") — 엔진 **`lineage` 블록 신설**(네이티브 `<details>`=클릭/터치 펼침, JS무관) + CSS. `three-kingdoms/lineage`(고구려10·백제8·신라12 주요왕, dynasties 그룹)·`goryeo/lineage`(34왕)·`joseon/lineage`(27왕). ★=핵심 임금. 각 시대 페이지 links에서 계보로 연결. 시각 스크린샷 확인.
- 0621 **캡스톤 `korea/east-asia`(6) ✅ = 한국사 6부 완결** — 관계사 무대·중국(사대조공 실리)·일본(교린통신사양란+연오랑세오녀 설화)·북방(거란여진몽골만주)·**중화질서 속 생존외교★**(서희·광해군 등거리/중립)·오늘의 갈등(동북공정·균형). 이미지 2종(혼일강리도·통신사내조도 PD). 균형(사대≠굴종, 임나일본부설/동북공정 비판). 배포 `802ed00`·G3 PASS·IMG 2/2. 랜딩 6/6 카드 live. **한국사 통사 시리즈 전부 완성.**
- 0621~23 **★★★ 르네상스 이전 세계사 10허브 전부 완성·라이브** (Nick "고교 기본 수준으로, 10허브, 최대한 자율진행"). 별자리+축의시대 척추 모델. 4 Phase: ①origins·②ancient-east·③greece·④rome / ⑤eastern-empires·⑥axial-age / ⑦islam·⑧medieval-europe / ⑨eurasia·⑩other-worlds. 각 5~6섹션 고교수준+설화(legend)+지도+사료 이미지(전점 Read 검수 PD/CC/CC0, 라이선스 정확). 비서구 균형(인도·중국·이슬람·아메리카·아프리카 절반↑). 르네상스 사슬에 연결+한국사/아메리카 교차링크. 마스터 랜딩(history/index.html)에 사이드바+흐름밴드+카드10 진입점 배선. 전 허브 G3 PASS. 계획=`plan/0621_masterplan_premodern_worldhistory.md`. **수준 기준 고교로 영구 상향**(learner-profile·hist-content-write·hist-audit·CLAUDE.md). 엔진 변경 0(legend 재사용).
- 0623 **★★ 3 후속작업 A·B·C 전부 완료 ✅ 라이브** (Nick "자율진행"). **A 도감 고대·중세 8인+figures 4짝**: people.json 52→60(공자·소크라테스·알렉산드로스·진시황·아소카·콘스탄티누스·칭기즈칸·카이사르 v3 full, `_add_ancient_people.py`)+초상 8(복사5·소싱3)+figures 6→10섹션(`_add_figures_pairs.py`, 공자↔소크라테스·알렉산드로스↔진시황·아소카↔콘스탄티누스·칭기즈칸↔카이사르). ⚠️figuresLink=dict. **B lineage 로마황제·중국왕조**: `rome/lineage`(황제17)·`eastern-empires/lineage`(중국왕조13 dynasties그룹), meta.home.lineage 배선(홈 금색버튼+사이드바📜). **C 통합 2D 랜딩**(커밋 배포 `6652aae`): `history/index.html` 상단에 '한눈에 보기 시대×트랙' 2D 매트릭스 additive(가로 6시대 × 세로 4트랙=31 허브칩, 모바일 가로스크롤·sticky 라벨·scoped style) + 사이드바 nav 갭 해소(korea 6부·tracks 3 그룹 누락 추가). 검증: 33링크 존재·헤드리스 mchip=31/erah=6/rlab=4·라이브 폴 mtx-sec PASS(34032B). 엔진 변경 0(lineage 재사용).
- 0624 **★ 종교 허브 'religion/' 착수 — Phase A ✅ 라이브** (Nick "인물·이야기에 종교 추가; 불교·유대교·천주교·기독교·이슬람, 세계·한국 각각"). AskUserQuestion 확정 = **별도 최상위 허브 / 세계 4(그리스도교=천주교+개신교 묶음) / 한국 종교별 다수**. 계획 `plan/0623_plan_hub_religion.md`. **religion/ 랜딩**(40_build/landing/religion_index.html, 세계4·한국3 카드) + **religion/buddhism 캐노니컬**(6섹션: founding·teaching·schools·spread·zen·today; 고등심화 비교종교사; legend 2편 moral로 사실구분; compare 상좌부vs대승; Leaflet 9거점; 퀴즈; 교차링크). 이미지 5 전점 Read 검수(PD/CC0/CC BY-SA 4.0). ⚠️Wikimedia 429 심함 → dharma_wheel/sanchi 못구해 teaching=전법륜인불상 대체·spread=사자주두+지도. 마스터 랜딩 배선(사이드바 그룹+카드+2D '🛐 믿음의 역사' 행, 불교 live). 소스 `062598c`·배포 `599ab5f`·G3 PASS(buddhism 87088B·img200). **다음 Phase B: christianity·judaism·islam(이미지 기존 repo PD 재사용으로 429 회피), C: 한국 3, D: 도감 인물+hist-audit 균형심판.**
- 0624 **★ 종교 허브 Phase B ✅ 라이브 — 세계 4대 종교 완비** (자율진행 중 API error로 배포 마무리만 끊겼던 것 재개·완료). **religion/{christianity,judaism,islam} 각 6섹션** 고등심화 비교종교사. christianity(예수·초대교회·바울·콘스탄티누스 공인→국교·동서분열·중세교회/십자군·종교개혁 루터칼뱅→천주교/개신교 분기·근현대), judaism(아브라함 계약·출애굽 전승·토라/탈무드·성전과 디아스포라·랍비 유대교·중세박해·반유대주의→홀로코스트→이스라엘 **균형·음모론 해체**, 그리스도교·이슬람 공통뿌리), islam(무함마드 **형상0**·쿠란·다섯기둥·수니/시아·정통칼리프·우마이야/아바스·황금기·수피즘·확산; 시각자료=카바·서예·알함브라·아스트롤라베만 인물도상0). 이미지=기존 repo PD/CC0/CC BY-SA 재사용으로 429 회피(샤를마뉴·그리스도이콘·콜로세움·콘스탄티누스·고딕대성당·구텐베르크성경·루터·종교전쟁·메노라·토라·통곡의벽·안네 등 17점). 랜딩 4세계 live/한국3 준비중. 배포 `f77ae56`·G3 PASS(christianity 86513B·judaism 83991B·islam 82901B·전부 200). **다음 Phase C: 한국 3편(korea-buddhism·korea-catholicism·korea-protestant), D: 교차링크+hist-audit 균형심판+마스터 랜딩 3세계 배선.**
