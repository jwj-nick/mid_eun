<!-- 00_project_hub/plan/0608_upgrade_masterplan_concrete.md -->
# 0608 — 전 페이지 업그레이드 구체 마스터플랜 (v2, 실측 기반)

> 0607_visual_content_masterplan(고수준 목록)의 **구체화판**. 각 섹션의 **현재 → 구체 추가**(어떤 지도 mode·어떤 이미지·어떤 deepdive) + **새 페이지** 제안.
> 기준 = 위기의 조선(`imperialism/korea`) **'풀 업그레이드' 사례**. 도구는 전부 확보됨(oldmap·battlemap·relations·image[]·chart[]·voice·compare·deepdive·movies·order). 대부분 **데이터만** 작성.
> 대상 수준 = 계층적 깊이(중1 입구 + deepdive 고등/일반).

## 0. 앱 구조 (이름 혼동 정리 ★)
- 허브 `/history/` → **에피소드 2개** + 도감 + maplab
- **에피소드 ww2** "세계대전 이야기" `/history/ww2/` — 8섹션 (한 SPA, 사이드바로 섹션 이동)
- **에피소드 imperialism** "제국주의와 19세기" `/history/imperialism/` — 8섹션 (위기의 조선 포함)
- ⚠️ "imperialism"이 **에피소드 이름**이자 ww2의 **첫 섹션 id**로 겹침 → 혼동 주의. ww2 첫 섹션은 `ww2#imperialism`로 표기.
- 도감 `/history/people/` (19인) · 지도랩 `/history/maplab/`(내부)

## 1. 작업 순서 (Nick 지시 = 전 페이지 순차)
**ww2 섹션 0→7 → imperialism 섹션 0→7(korea 완료라 skip) → 새 에피소드.** 한 페이지 끝낼 때마다 다음을 묻지 않고 순서대로. 각 페이지는 라운드(아이디어→Nick 코멘트→구현→검토→audit).

## 2. ww2 에피소드 — 섹션별 구체 업그레이드
| # | 섹션 | 현재(실측) | 🗺️ 지도 | 🎨 비주얼 | 📚 deepdive(고등/일반) |
|---|---|---|---|---|---|
| 0 | `imperialism` 1차대전 | hook·why·cards·people2·timeline·yt·choice·quiz | **oldmap**(1914 식민 세계지도) + **relations**(협상↔동맹) + **battlemap**(사라예보→서부전선) | image(사라예보 암살)·chart(군비경쟁 전함)·voice(병사 편지)·movies(서부전선·1917) | 제국주의 동력·**1차대전 MAIN 4원인**·발칸 화약고·7월 위기·총력전 (세부=`0608_page_ww2_imperialism.md`) |
| 1 | `outbreak` 2차대전 발발 | hook·why·cards·**chart**·timeline | **territory/oldmap**(베르사유→독일 팽창 36~39) + relations(추축↔연합 형성) | image(뮌헨협정·히틀러 집권 PD)·voice(대공황 가족) | 전간기 경제·바이마르 붕괴·유화정책의 실패 |
| 2 | `anne` 안네 ★ | hook·why·**voice**·cards·people1·**map** | **oldmap/image**(암스테르담 은신처) + battlemap(나치 점령 확산 39~42) | 일기 1차사료 인용 확대·은신처 평면 image | 홀로코스트 구조·반유대주의 역사 (감성 입구 유지) |
| 3 | `europe` 유럽·러시아 | hook·cards·people2·**map**·**movies2** | **battlemap**(스탈린그라드·노르망디 D-Day 화살표) + relations(유럽 연합↔추축) | image(D-Day·스탈린그라드 PD)·chart(병력·사상자) | 전환점 분석·동부전선 규모 |
| 4 | `pacific` 미국·태평양 | hook·cards·**map**·**movies1** | **battlemap**(진주만→미드웨이→이오지마→오키나와 island-hopping) | image(진주만·이오지마 깃발 PD)·chart(태평양 규모) | 총력전·동원·**원폭 결정 논쟁** |
| 5 | `asia` 일본·조선 | hook·why·cards·timeline (**가장 얇음**) | **territory/oldmap**(일본 제국 팽창·대동아공영권) + battlemap(만주·중일전쟁) | image(강제동원 — 수위조절)·people(**안중근** 추가)·voice(징용 imagined) | 식민지 동원·강제징용·**역사 논쟁** |
| 6 | `postwar` 종전·전후 | hook·cards·people2·**movies1** | **globe**(냉전 분할·철의 장막) + territory(전후 국경) | image(원폭·뉘른베르크 PD)·relations(미↔소) | 뉘른베르크·UN·핵시대·**냉전 시작** |
| 7 | `korea` 한국전쟁 | hook·cards·**map·compare·relations** | **battlemap**(남침→낙동강→인천상륙→1·4후퇴→휴전, reset 국면) | image(인천상륙·피란민 PD)·movies(태극기 등) | 냉전 대리전·휴전체제·분단 심화 |

## 3. imperialism 에피소드 — 섹션별 구체 업그레이드
| # | 섹션 | 현재(실측) | 🗺️ 지도 | 🎨 비주얼 | 📚 deepdive |
|---|---|---|---|---|---|
| 0 | `industry` 산업혁명 | hook·why·lens·cards·timeline | oldmap(공업도시 확산) | **chart**(생산량·도시화 폭증)·image(공장·증기기관 PD)·voice(공장 아동 노동 imagined) | 기술·자본·노동·계급·환경 |
| 1 | `why-empire` 제국주의 속마음 | hook·why·lens·cards | **globe**(열강 식민지 전 지구 분포) + relations(열강 경쟁) | chart(식민지 면적·인구 비교)·image(풍자화 PD) | **홉슨·레닌 이론**·사회진화론·문명화의 위선 |
| 2 | `scramble` 아프리카 분할 | hook·cards·**map·image**(africa1914 보유) | **oldmap**(베를린회의 분할지도) + battlemap(저항) | image(분할 풍자화)·chart(분할 속도)·voice(피분할 측) | 베를린회의·분할 논리·아프리카 저항 |
| 3 | `india` 인도 | hook·cards·people1(락슈미바이)·**map** | **battlemap**(세포이 항쟁 1857) + oldmap(영령 인도) | chart(면직 무역 역전)·image(세포이 PD)·voice | 동인도회사·면직 경제 파괴·식민 통치 |
| 4 | `opium-china` 아편전쟁 | hook·**voice**·cards·people1·**map·chart** | **battlemap**(아편전쟁 1·2차) + oldmap(난징조약 개항장) | image(아편·난징조약 PD)·relations | 불평등조약 체계·태평천국·반식민지화 |
| 5 | `japan-meiji` 메이지 | hook·cards·people1(이토)·**compare** | **territory/oldmap**(메이지 팽창) + battlemap(청일·러일 — korea와 공유) | **chart**(근대화 속도 — 위기의 조선 차트와 연결★)·image(이와쿠라 사절단 PD) | 메이지 개혁 상세·자유민권·천황제 |
| 6 | `korea` 위기의 조선 | ✅ **완료(기준 사례)** | — | — | — |
| 7 | `toward-war` 화약고 | hook·why·cards·timeline | **relations/globe**(동맹망) | image(1914 유럽 풍자화) | 발칸·동맹체제·**1차대전으로의 다리** (ww2#imperialism과 연결★) |

## 4. 새 페이지 / 새 콘텐츠 제안 (Nick 결정)
1. **새 에피소드 "냉전"(coldwar)** ★ — ww2 한국전쟁 이후 ~ 현대로 잇는 다리. 베를린 장벽·쿠바 미사일 위기·우주 경쟁·베트남·소련 붕괴. **globe/territory** 주력. 블록 전부 재사용, 데이터만. (시리즈 완결성↑)
2. **인물 도감 확장(19→약 25인)** — 섹션 신설 인물에 맞춰: **안중근**(ww2/asia)·**간디**(india)·**비스마르크**(why-empire)·**미프 히스**(anne)·**처칠/루스벨트**(europe/postwar)·**윤동주**(asia). 각 섹션 people 카드 + 도감 페이지(역링크).
3. **(선택) 비서구 관점 섹션** — imperialism에 **오스만 제국 쇠퇴** 또는 **동남아·라틴아메리카** 1섹션 추가(현재 아프리카·인도·청·일·조선 편중 보완). 우선순위 낮음.
4. **maplab 엔진 승격 산출물** — 위 표에서 쓰는 **globe**(전 지구 구조: ww2/postwar·imp/why-empire)·**territory**(영토 변화: outbreak·asia·meiji)·**scrolly**(내러티브)를 엔진 mode로 승격. 각 1개 콘텐츠로 검증(MAP_TOOLKIT §6).

## 5. 페이지 '풀 업그레이드' 표준 (= 위기의 조선 기준)
한 섹션 완료 = ▸ 지도 1~3종(콘텐츠에 맞는 mode) ▸ image 1~2(PD)·chart(필요시) ▸ voice(사료/편지) ▸ deepdive 3~5(인과·구조·논쟁·사료) ▸ 필요시 relations/compare/movies ▸ **order로 서사 흐름 재배열** ▸ G0~G3 + hist-audit + hist-page-review.

## 6. 작업 방식 (반복 루프)
페이지마다: `0608_page_<ep>_<section>.md` 생성 → 아이디어 정리 → **Nick 코멘트** → 구현(데이터) → 빌드/배포/검증 → audit → 다음 페이지(묻지 않고 순서대로). 엔진 신규 필요 시(globe 등)만 별도 승격 단계.

## 7. 규모/순서 감각
- 즉시 재사용으로 가능(엔진 추가 0): ww2#imperialism, outbreak, europe, pacific, asia, korea / imp: industry, scramble, india, opium-china, japan-meiji, toward-war.
- 엔진 승격 동반 권장: why-empire·postwar(globe), outbreak·asia·meiji(territory).
- 새 에피소드 냉전 = 별도 큰 작업(블록 재사용·데이터 신규).

## 8. Nick 코멘트
- (Nick) 
