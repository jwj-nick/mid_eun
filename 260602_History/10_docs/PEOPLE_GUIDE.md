<!-- 10_docs/PEOPLE_GUIDE.md -->
# PEOPLE_GUIDE — 인물 도감 제작 가이드 (SSOT) ★

> 인물 도감의 **스키마·제작 절차·품질 체크리스트**의 단일 진실 원천.
> 관련 문서: 스키마 요약 = `EPISODE_SCHEMA.md §People-gallery` · 설계 사상 = `0606_people_gallery_upgrade.md` · 개선 계획 = `plan/0612_plan_people_v3.md`
> 데이터 = `30_content/people/people.json` / 빌더 = `40_build/build_people.py` / 산출 = `50_app/people/`

## 1. 페이지 구성 (v3 렌더 순서)
| # | 패널 | 필드 | 수준 | 비고 |
|---|---|---|---|---|
| 1 | 초상 | `portrait{src,alt,source,license,note}` | 공통 | PD/명확한 CC만, note에 사후·논쟁 초상 명시 |
| 2 | **10초 카드** | `quickCard{era,keywords[],oneQuestion}` | **중1 quick** | 시대 한 줄 + 키워드 3 + 여는 질문 1 |
| 3 | 이름 | `names{native,roman,pronun_ko,en,ko,alias}` | 공통 | 검색·탐구 진입로 |
| 4 | 메타 | `nationality`, `lifespan` | 공통 | |
| 5 | **왜 이 사람인가** | `whyHere` | 공통 | 도감 선정 이유 = 시리즈의 시선 1문단 |
| 6 | 생애 | `bio[]` (3~5문단) | 중1 | 이야기체, 장면 중심 |
| 7 | **어록** | `quotes[{text,context,source}]` | 공통 | **출처 필수**, 전언·요지는 그렇게 표기 |
| 8 | 연표 | `personTimeline[{yr,t}]` | 공통 | 5~8행, 세계사 맥락 1~2행 포함 권장 |
| 9 | 빛과 그림자 | `lightShadow` | 공통 | 영웅화·악마화 금지의 장치 |
| 10 | **더 깊이** | `deepDive[{h,body,source}]` | **성인/전문** | 접이식 3~5: 평가사·논쟁·사료 이야기·국제법/이론 |
| 11 | **사람의 그물** | `network[{slug,name,relation}]` | 공통 | 도감 내 인물 연결(대척·동시대·계보) |
| 12 | 이야기 역링크 | `related[]` + `figuresLink{section,label}` | 공통 | 에피소드 + 인물 이야기(figures) |
| 13 | **더 공부하기** | `study{books[],primary[],media[],places[]}` | **성인/시발점** | 평전·1차 사료·다큐/영화·가 볼 곳 |
| 14 | 더 알아보기 | `links[]` | 공통 | 백과·공식기관 — **200 검증 필수** |
| 15 | 편지 | `reflect` | 중1 | 메모(localStorage) |
- **(v3.1) 시각자료** `gallery[{src,title,alt,caption,source,license}]` — 유묵·서신·현장 사진 등(어록 패널 앞, 그리드+클릭 확대). PD/명확한 CC만, 영화 포스터·책 표지는 **저작권상 이미지 금지 → 링크로 대체**(study의 url).
- **(v3.1) 경로 지도** `journey{h,intro,markers[{at:[lat,lng],kind,label,desc}],path[[lat,lng]…],caption}` — Leaflet 지도(연표 앞). kind: start/city/battle/win/loss/capital. journey 있는 페이지에만 Leaflet 로드. caption에 '현재 지도' 명시.
- **v2 호환**: 굵은 필드(2·5·7·10·11·13)와 v3.1 필드는 전부 선택 — 없으면 그 패널만 생략(점진 보강 가능).
- 두 수준의 분리 원칙: 중1은 1~9에서 완결(quick review), 성인은 10·13이 학습 시발점. **deepDive는 에피소드 deepdive와 같은 정신**(접으면 안 보임).

## 2. study(더 공부하기) 작성 규칙
- 항목 = `{title, by?, note}` — **URL 없이도 가치 있게**(제목·저자·한 줄 안내). URL은 200 검증된 것만 `url`로.
- books: 국내서 우선 1~2 + 표준 전기(원서) 1. primary: 1차 사료(공판기록·회고록·일기 등)와 소장처. media: 다큐/영화(수위 신호등 🟢🟡🔴). places: 기념관·박물관.
- 실존 확인 안 되는 서지는 싣지 않는다(추측 금지 — links의 '죽은 링크 금지'와 같은 원칙).

## 3. 제작 절차 (인물 1명 추가/보강 = 7단계)
1. **선정** — `whyHere`를 먼저 쓴다(이유를 못 쓰면 선정 보류). 시리즈 모티프(빛·그림자/맞선 자/폭로자…)와의 연결 확인.
2. **리서치** — 사실·연도 교차 확인, **어록은 원출처 추적**(전언이면 '전해진다'로), 논쟁 지점 메모.
3. **작성** — v3 필드 채움. 중1 문장(bio)과 성인 문단(deepDive)을 의식적으로 분리.
4. **초상 소싱** — Commons API(extmetadata로 라이선스 실측) → PIL 리사이즈(폭 ~700) → **육안 검수 필수**(오선정 사례: 데스마스크·전투도면). 사후 초상은 note 명시.
5. **빌드** — `PYTHONIOENCODING=utf-8 python 40_build/build_people.py` (EP_ORDER 밖 ep는 fallback 그룹+경고).
6. **인물 audit** — §4 체크리스트. 기록은 해당 에피소드 audit.md 또는 `20_research/people/`에.
7. **배포** — 트리 전체 복사(`cp -r 50_app/people/. <repo>/history/people/`) → push → 라이브 200 확인.

## 4. 품질 체크리스트 (인물 audit)
- [ ] 사실·연도 교차 확인 / 추정·논쟁은 표기
- [ ] **어록 전수 출처 확인** — 직접 인용 vs 요지 vs 전언 구분 표기
- [ ] 빛과 그림자 모두 실체 있게(영웅화·악마화 금지) / 패배자·피해자는 주체로
- [ ] 초상 라이선스 실측 + 육안 검수 + 사후 초상 note
- [ ] links 전부 200 / study 서지 실존 확인
- [ ] network·figuresLink의 slug 실존 확인
- [ ] 중1 수위(잔혹 절제) / 두 수준 분리(quick는 1~9에서 완결되는가)

## 5. 운영 메모
- EP_ORDER(색인 그룹·시대순) = build_people.py 상단. 새 에피소드 추가 시 갱신.
- 도감 인물 vs 섹션 인물카드: 도감 등재는 '시리즈를 가로지르거나 깊이 팔 가치'가 기준 — 모든 섹션 인물을 등재하지 않는다.
