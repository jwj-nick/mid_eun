<!-- 00_project_hub/plan/0612_plan_people_visual_upgrade.md -->
# 0612 — 인물 도감 '안중근 레벨' 전수 업그레이드 계획 (시각화 floor)

> Nick 지시: ① 색인(index)에서 누가 어디 있는지 찾기 쉽게 — **간단 목록·정렬·검색**. ② "8인 v3 완료라지만 안중근 외엔 visualization이 약하다" → **모든 인물의 최소 수준 = 안중근 페이지 수준**. 전체를 단계별로 계획하고 차례대로 올린다.

## 0. 진단 — 왜 약해 보였나 (정직한 자기점검)
- batch-1(안네·사다코·링컨·워싱턴·나폴레옹·루터)은 **텍스트 v3만** 넣고 v3.1 자산(gallery·journey)과 검증 링크를 "후속 패스"로 미뤘다 → 화면상 안중근과 격차가 큼.
- 즉 **floor를 텍스트 v3로 잡은 게 오판**. Nick의 floor는 **안중근 페이지(=v3 + 갤러리 + 경로지도 + 검증 링크)**. 이 계획서가 floor를 그렇게 다시 못박는다.

## 1. '안중근 레벨' floor 정의 (이 수준이 되어야 '완료')
| # | 요소 | 최소 기준 |
|---|---|---|
| 1 | 텍스트 v3 | quickCard · whyHere · quotes ≥2(출처/전언 구분) · bio 4~5문단 · personTimeline 6~8 · lightShadow · **deepDive 5** · network 2~3 · (짝 있으면)figuresLink · study(books·primary·media·places) |
| 2 | **gallery (시각자료)** | **3~4점** — 유물·문서·현장·작품. PD/명확한 CC + **전점 육안 검수**. 포스터·표지=저작권→링크 |
| 3 | **journey (경로 지도)** | 생애 이동이 유의미하면 Leaflet 경로 5~7점(+path). 한 곳 정주형(예: 사다코)은 **소형 단일지역 지도 또는 생략**하고 gallery로 시각 부담 |
| 4 | **검증 링크** | study media=YouTube oembed+공식채널 / books=알라딘 200 / links=위키·공식 200 |
- **자산 없는 인물은 '완료' 아님.** journey는 조건부(이동성), gallery는 사실상 필수.

## 2. 현재 vs floor (47인)
| 상태 | 인원 | 명단 |
|---|---|---|
| ✅ floor 도달 | 1 | 안중근 |
| 🟡 텍스트만(자산·링크 결핍) | 7 | 비스마르크 + batch-1 6인(안네·사다코·링컨·워싱턴·나폴레옹·루터) |
| ⬜ 뼈대(v2) | 39 | 나머지 전원 |

## 3. 단계별 작업 순서 (depth-first — 각 배치를 floor까지)
> 이미 텍스트를 넣은 8인을 **먼저 floor로 끌어올리고**, 그다음 신규를 풀스펙으로. 신규보다 보강 우선(누적 투자 회수).
- **B0 (텍스트→floor 승격, 진행 중)**: 비스마르크 + batch-1 6인 = 7인에 journey/gallery/검증링크 추가.
- **B1 ★1순위 잔여 6인**: 볼리바르·투생·시팅불·메넬리크·갈릴레이·레오폴드2세 (전부 풀스펙).
- **B2 한국 연관 5인**: 이토·명성황후·전봉준·윤동주·임칙서.
- **B3~ 나머지 28인**: 에피소드 시대 사슬 순(르네상스→…→아메리카)으로.
- **페이스**: gallery 소싱+육안검수가 병목 → **풀 floor는 배치당 3~4인** 현실적. 전체 ~12회 세션 규모(정직한 추정).

## 4. 작업 분해 — 비용/안전별 (멈춤 없는 프로토콜 준수)
| 하위작업 | 성격 | 방식 |
|---|---|---|
| 텍스트 v3 | 로컬 | people.json 일괄 패치(json round-trip indent=1·ensure_ascii=False=포맷보존) |
| **journey 좌표** | **로컬**(지식 기반 실좌표) | 즉시 가능·고임팩트·안전 — 배치 폭 넓게 |
| **gallery 이미지** | **네트워크 격리** | urllib Commons API(extmetadata 라이선스 실측)→PIL 리사이즈→**Read 툴 전점 육안 검수**(데스마스크·전투도면 전례) |
| 링크 검증 | 네트워크 격리 | oembed(공식채널)·알라딘 200·위키 200. curl 단독·최소, 로컬 커밋 먼저 |
- 빌더 변경 0(하위호환). 배포 게이트 G0~G3. 소스(mid_eun)+배포(jwj-nick.github.io) 양 repo. 자산 PD/CC0/CC BY-SA 출처표기.

## 5. 색인 개편 (Nick ①) — ✅ 이번 구현
- `build_people.py` 색인을 **평면 리스트 + 도구막대**로 재구성: **검색창**(이름·나라·키워드·발음 즉시 필터) · **정렬**(에피소드 시대사슬 / 가나다 / 출생연도) · **카드↔목록 보기 토글** · 결과 카운트. 카드마다 에피소드 배지. ep 정렬 시 그룹 헤더 동적 삽입.
- 데이터 속성 `data-search/ko/ep/birth`로 클라이언트 JS 처리(빌드 없음·CDN 없음). node --check 통과.

## 6. 이번 세션 실행 범위 (정직)
- ✅ ① 색인 개편(검색·정렬·목록) 구현·배포.
- ✅ B0 일부: **journey 경로지도** 추가(로컬·안전·고임팩트) — 안네·링컨·워싱턴·나폴레옹·루터·비스마르크(이동성 유의미한 6인). 사다코=정주형→gallery 패스에서 처리.
- ⏭ **gallery 이미지 + 검증 링크 = 다음 세션 네트워크 격리 배치**(병목·육안검수 필요 → 별도 집중 패스). journey만으로는 floor 미달임을 명시.

## 7. 진행 로그
- **0612 — 색인 개편 ✅ 라이브**: 검색·정렬(에피소드/가나다/출생연도)·카드↔목록 토글·결과 카운트. build_people.py 평면 리스트 재구성. node --check 통과. 소스 `6407c41`.
- **0612 — B0 journey 6인 ✅ 라이브**: 안네(프랑크푸르트→베르겐벨젠 6점)·링컨(켄터키→포드극장 6)·워싱턴(버지니아→뉴욕, 트렌턴/요크타운 6)·나폴레옹(코르시카→세인트헬레나 7, 대서양까지)·루터(아이슬레벤↔비텐베르크·보름스 6)·비스마르크(쇤하우젠→베르사유 6). Leaflet 주입·journey JS node --check 통과.
- **남은 floor 작업(B0)**: 위 6인 + 사다코 + (figuresLink 없는 비스마르크) → **gallery 이미지 + 검증 링크**(다음 세션 네트워크 격리 배치). 사다코 journey=정주형이라 gallery 우선.
- **0612 — 색인 지역×시대 패싯 ✅ 라이브 (Nick 추가 지시)**: 검색·정렬 위에 **지역(출신 7) × 시대(출생연도 6버킷)** 칩 패싯. 선택 카테고리만 표시·조합 가능(입체적). 라이브 기능검증: 한국→7, 한국×제국주의절정→4, 라틴→5, 리셋→47, 칩 하이라이트 OK. region_of/era_tag(빈 1600s 버킷 자동 제외). data-region/era 속성+JS sel{}.
- **0612 — B0a gallery 4인 floor 도달 ✅ 라이브**: 나폴레옹·루터·링컨·워싱턴 각 PD 3점. urllib Commons API 소싱(extmetadata 라이선스 실측 11 PD+마운트버넌 CC BY-SA)→thumburl 760px→**Read 툴 전점 12장 육안검수(오선정 0)**. 라이브: gallery 이미지 200·렌더(naturalWidth>0)·journey 7마커 확인. **이 4인 = v3+journey+gallery = 안중근 floor 첫 도달군.** 커밋 소스 `591445e`·배포 `95751b0`.
- **0612 — B0 검증 링크 + bismarck gallery ✅ 라이브 (Nick: "제목만 말고 실제 링크")**: napoleon·luther·lincoln·washington study에 실제 url 주입 — **영상=oembed로 title+채널 검증한 공식 예고편**(나폴레옹=Sony Pictures Releasing Australia / 링컨·루터=Rotten Tomatoes (Classic) Trailers / 워싱턴=감독 Roel Reiné 업로드), **책=Aladin 검색 200**, **1차사료=NARA 노예해방선언·LOC 게티즈버그친필·Napoleonic Code·95개조(위키)**, **장소=NPS Lincoln/Gettysburg·Wartburg 200**. ⚠️검증으로 죽은 URL 배제(나폴레옹 트레일러 후보 1건 404). 검증 방식=urllib oembed/200(curl 회피, ask-list 우회). bismarck gallery 3점(초상·베르사유 황제선포·Dropping the Pilot, 육안검수 PD). 커밋 소스 `1831185`·배포 `50ee946`.
- **floor 도달 누계: 6인**(안중근 + 나폴레옹·루터·링컨·워싱턴·비스마르크). 링크 정책=책(Aladin 검색)·영상(oembed 공식)·사료/장소(기관 200 or 신뢰 위키) 모두 검증 url.
- **0612 — B0 완료: 안네·사다코 ✅ 라이브 (저작권 주의군 처리법 확립)**: 인물 사진(AFF/가족 저작권) 회피 → PD/CC 유물·기념물로. 안네 gallery 3(회전책장 PD·안드리센 동상 CC BY-SA·베르겐벨젠 추모비 CC BY-SA)+AFH 공식영상(7o8jSbCanv0)+annefrank.org. 사다코 gallery 3(원폭돔·천마리종이학·어린이평화비 CC)+**micro-journey 3점**(집→적십자병원→평화비, 정주형도 '한 도시 안' 지도로 의미화)+BBC News(TbI3an0h5h0)·NPS·hpmmuseum. 전점 육안검수. 커밋 소스 `f8e563f`·배포 `5901017`.
- **★ B0 완료 = floor 도달 8인** (안중근·나폴레옹·루터·링컨·워싱턴·비스마르크·안네·사다코). 남은 39. 다음 = **B1 ★잔여 6인**(볼리바르·투생·시팅불·메넬리크·갈릴레이·레오폴드2세, journey 다수 적합).

## 8. Nick 코멘트
- (Nick)
