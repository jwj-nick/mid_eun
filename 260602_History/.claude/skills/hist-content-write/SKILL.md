---
name: hist-content-write
description: 리서치 자료를 Episode Content Schema(episode.json)로 작성한다. 섹션별 hook·why·cards·timeline·connect·yt·reflect와 인물·"그때의 생각" 렌즈·용어 풀이를 따뜻한 톤으로 채운다. **지명은 현재 위치(map/주석)로 그라운딩하고, 유명 설화는 legend 블록으로 소개해 페이지가 밋밋하지 않게 한다.** 호출 예시 — "/hist-content-write imperialism", "제국주의 콘텐츠 작성".
allowed-tools: Read, Write, Grep
metadata:
  project: 260602_History
  stage: 3 콘텐츠 작성
  ssot: 10_docs/EPISODE_SCHEMA.md
  status: seed
---

# hist-content-write — 콘텐츠 작성 (단계 3)

리서치(단계 2) → **순수 JSON 스키마**. 작성=데이터, 렌더=엔진(분리 원칙).

## ★ 기본 수준 = 고등학교 (2026-06-21 Nick, 필수)
- **본문 깊이는 고등학교 수준을 기본**으로 한다 — 개념·인과·구조·논쟁·사료를 본격적으로(단순 사건 나열 금지). "무엇"을 넘어 **"왜·어떤 구조·어떻게 아는가"** 까지.
- **입구(hook·정서·또래의 눈)는 누구나 진입** 가능하게 유지(사람·장면·수수께끼). 깊이↑ 하되 차가운 교과서 X.
- 어려운 용어는 `terms{}`로 풀되, **용어·어휘 자체는 고교 수준을 회피하지 않는다.** 더 깊은 층은 `deepdive`(계층적 깊이)로.
- 잔혹·자극 *수위*는 여전히 절제(정서 보호) — **지식 수준(고교)과 자극 수위(보호)는 별개 축.** 상세 = `10_docs/01_learner-profile.md §수준 기준`.

## 입력
- `10_docs/content-map_<slug>.md`, `20_research/<slug>/*.md`
- 규격: `10_docs/EPISODE_SCHEMA.md` / 톤: `APP_PRINCIPLES.md` / 원칙: 마스터플랜 §9

## 동작
1. `meta`(brand/home/시작버튼) 작성 — 강조 입구(star) 지정.
2. 섹션마다: **여는 장면(hook)** = 인물·장면·질문으로 시작(연표 나열 금지) → why → cards(3~6) → timeline → connect(다음 섹션 다리) → yt → reflect(빈칸 1~2).
3. 마스터플랜 의무 반영: 적절한 섹션에 **`lens`(그때의 생각)** + **`people`(꼭 알아야 할 인물)**.
4. `terms{}` — 어려운 말 쉬운 풀이(첫 등장 자동 점선).
5. 사실은 리서치 출처대로, 논쟁은 "이런 시각도, 저런 시각도"로 균형.
6. **대표 이미지 ≥2/섹션:** 각 섹션에 그 시대 대표 이미지(건물·명화·기념물·문화아이콘·상징) **2점 이상**(image 배열) 계획. PD/CC·출처·alt 필수. 소싱·검수 절차 = **hist-visuals 스킬**.

## 서사·정서 레이어 (S0 — 엔진 비용 0, 콘텐츠/프레이밍 패턴)
역사 무관심 아이를 끄는 핵심. 블록보다 먼저 글에 입힌다. (근거: `10_docs/0605_viz_creative_review.md`)
- **D7 과거에 답장하기:** `reflect` 질문을 **그 시대 인물/또래에게 보내는 편지·메시지** 형식으로. 예) "안네에게 한 줄 편지를 쓴다면?" "100년 전 그 또래에게 묻고 싶은 한 가지는?" → notes-export가 모아 발표 원고가 됨. (사실 아님·감정/상상 영역이라 안전)
- **D9 미스터리 훅:** `hook`을 설명이 아닌 **수수께끼/질문**으로 연다. 예) "바다에 던져진 2만 상자, 무엇이었을까?" "열세 살 소녀의 일기장이 왜 전 세계가 읽는 책이 됐을까?" 답은 본문에서. 단 **과장·낚시 금지**(사실 왜곡 X).
- **D1 또래의 눈:** 각 섹션에 **13~15세 또래**의 시선을 한 줄 심는다(hook 또는 home.intro). 사실 확인된 인물(안네)·일반화된 또래(공장 소년, 피란길 아이)만. 영웅화·날조 금지.
- **D8 역사 탐정:** `home.intro`에 "너는 단서를 모으는 역사 탐정/기자" 프레이밍 + reflect를 "오늘의 단서"로 연결. 마지막에 "나의 사건 파일"(=메모 모아보기).

## 사용 가능한 블록 (누적 — EPISODE_SCHEMA 카탈로그)
- **quiz** (R1): 섹션 끝 "잠깐, 기억나니?" 1~2문. `{q, options[], answer(0-base), explain}`. 정답 강요 X, 해설로 배우게. 핵심 섹션부터 적용(전 섹션 확장 가능).
- **notes-export** (R2): 엔진 자동 기능(데이터 불필요). 작성 시 reflect 질문을 "발표/보고서에 옮겨 적기 좋은" 형태로.
- **map** (R3): **실제 지도(Leaflet+OSM)**. `{caption, source, center:[lat,lng], zoom, line?, markers:[{lat,lng,label,desc}]}`. 손그림 금지·실좌표 사용. 옛 국경 핵심이면 caption 명시 또는 향후 역사지도 image 보강. 장소가 중요한 섹션(분할·전선·분단)에 적용.
- **image** (S1): **PD 역사지도/사진** + 선택적 hotspot. `{h?, src:"img/..", alt, story?, caption, source, license, hotspots?:[{x,y,label,desc}]}`. 자산은 `30_content/<slug>/img/`에 두면 빌드가 복사. PD/명확한 CC만, 출처·라이선스 필수, 손그림 금지. 옛 국경(map=현대 지도와 역할 분담). 손그림 SVG 금지. hotspot 좌표 불확실하면 생략.
- **voice** (S3): 일기·편지체 1인칭. `{h?, imagined:bool, body, speaker, era?, source}`. `imagined:false`=실제 사료(인용·출처 정확)·초록 배지 / `true`=사실 기반 상상·✍️ 배지(근거 명시). 날조 금지. hook/why 뒤 렌더.
- **legend** (설화 ★): "전해 오는 이야기" 콜아웃. `{title, body, source?, moral?}`. 그 시대·나라의 **유명 설화/전승**을 한 편 들려준다(주몽·박혁거세·온달과 평강공주·서동요·연오랑 세오녀·만파식적 등 / 세계사=길가메시·트로이·로물루스·건국신화). **신화·전승임을 분명히**(사실과 구분), `moral`에 "이야기가 남긴 의미" 한 줄. 사실 단정·날조 금지.
- **lineage** (왕조 계보 ★): 클릭/터치로 펼쳐지는 임금·통치자 목록(네이티브 `<details>`, JS무관). `{h?, intro?, rulers:[{n,name,reign,note,star?}]}` 또는 `{dynasties:[{label,intro?,rulers}]}`(여러 계보 그룹). `star:true`=핵심 임금(★ red border). 보통 **별도 경량 페이지**(1섹션: hook+lineage+reflect+links)로 만들고, **시대 허브의 `meta.home.lineage={label,url}`** 로 홈 버튼+사이드바에서 진입(★ Nick 0621: 계보는 메인 랜딩 아닌 **각 시대 허브 내부**에서 접근). 왕 많으면 주요 왕만(대수 띄엄 표기).
- **chart** (S4): CSS 막대 + 체감 비교. `{h?, title, unit?, data:[{label,value,disp?}], relatable?, source}`. 통계 출처 필수·불확실하면 '대략값'. `relatable`로 아이 세계 단위(반 인원 등)에 빗대기(D4).
- **compare** (S5): 단계 토글/before·after. `{h?, intro?, states:[{label,title,body,img?,alt?,caption?}]}`. 탭 2~4개. `img`는 선택·PD/CC만. 그때↔지금 사진(D6)은 양쪽 라이선스 확보 시만, 아니면 텍스트 상태로.
- **choice** (S7): '너라면?' 도덕적 딜레마. `{h?, prompt, options:[{label,result}], after?}`. 2~3 선택지, 정답 강요·단정 금지, 각 선택 균형 해설(실제 사례). 공감·관점 전환 목적(D5).
- **people-gallery** (S6): 인물은 각 섹션/최상위 `people[]`에 쓰면 `build_people.py`가 `/history/people/`로 자동 집계. Person 구조는 §Person.

## 생동감 — 지명 위치 + 설화 (★ Nick 0620, 필수)
페이지가 '밋밋'하지 않으려면 두 가지를 반드시 넣는다. (계기: korea 페이지가 지명만 나열돼 위치 감각·이야기가 없어 단조롭다는 피드백)
- **지명의 실제 위치(그라운딩):** 본문에 옛 지명(졸본·국내성·위례성·웅진·사비·금성/서라벌·상경 등)이 나오면 **"지금 어디인지"를 함께 밝힌다.** 특정이 어려우면 "대략 ~ 지역(추정)"으로 정직하게.
  - 방법 ① 그 섹션에 **`map` 블록**(현대 지도 + 마커, 각 마커 `desc`에 "지금의 충남 공주" 식 현재 위치)을 둔다 — **건국·도읍·전쟁·영토 섹션엔 가급적 map 필수.**
  - 방법 ② map이 과하면 `cards`/`why`/`terms`에 괄호 주석("졸본 = 지금의 중국 랴오닝성 환런")으로라도 반드시 위치를 준다.
  - 좌표 불확실·국경 미상이면 caption/desc에 "대략·추정" 명시(거짓 정밀 금지).
- **유명 설화(legend):** 각 나라/시대의 **대표 설화를 `legend` 블록으로 한 편 이상** 소개한다. 신화·전승임을 분명히 하고 `moral`로 의미를 한 줄. (예: 고구려=주몽 탄생·온달과 평강공주·호동왕자와 낙랑공주 / 백제=서동요·도미 부인 / 신라=박혁거세·석탈해·김알지(계림)·연오랑 세오녀·김유신과 천관녀·만파식적 / 고조선=단군·고대=알·난생 신화.)
- 두 요소는 **모든 시대·인물 페이지의 기본기**다. 적어도 지명 등장 섹션 = 위치 그라운딩, 페이지당 = 설화 1편 이상.

## 출력
- `30_content/<slug>/episode.json` (스키마 준수, 단계 4가 소비)

## 품질 게이트
- [ ] `python 40_build/build.py <slug>` 무오류 (JSON 유효 + 렌더)
- [ ] 모든 hook이 사람/장면/질문으로 시작
- [ ] reflect 빈칸·연결 고리·용어 풀이 존재
- [ ] 논쟁 균형 / 비서구 관점 반영
- [ ] 영상 yt가 리서치(video/search) 분류와 일치
- [ ] **지명 등장 섹션 = 현재 위치 그라운딩(map 또는 주석) 존재** (★)
- [ ] **페이지당 유명 설화 `legend` 1편 이상** (★)
- [ ] `python 40_build/_validate.py <slug>` issues=0 (order 토큰↔필드) · 헤드리스 전 섹션 hero=2
