---
name: hist-content-write
description: 리서치 자료를 Episode Content Schema(episode.json)로 작성한다. 섹션별 hook·why·cards·timeline·connect·yt·reflect와 인물·"그때의 생각" 렌즈·용어 풀이를 중1 눈높이 따뜻한 톤으로 채운다. 호출 예시 — "/hist-content-write imperialism", "제국주의 콘텐츠 작성".
allowed-tools: Read, Write, Grep
metadata:
  project: 260602_History
  stage: 3 콘텐츠 작성
  ssot: 10_docs/EPISODE_SCHEMA.md
  status: seed
---

# hist-content-write — 콘텐츠 작성 (단계 3)

리서치(단계 2) → **순수 JSON 스키마**. 작성=데이터, 렌더=엔진(분리 원칙).

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
- **chart** (S4): CSS 막대 + 체감 비교. `{h?, title, unit?, data:[{label,value,disp?}], relatable?, source}`. 통계 출처 필수·불확실하면 '대략값'. `relatable`로 아이 세계 단위(반 인원 등)에 빗대기(D4).
- **compare** (S5): 단계 토글/before·after. `{h?, intro?, states:[{label,title,body,img?,alt?,caption?}]}`. 탭 2~4개. `img`는 선택·PD/CC만. 그때↔지금 사진(D6)은 양쪽 라이선스 확보 시만, 아니면 텍스트 상태로.
- **choice** (S7): '너라면?' 도덕적 딜레마. `{h?, prompt, options:[{label,result}], after?}`. 2~3 선택지, 정답 강요·단정 금지, 각 선택 균형 해설(실제 사례). 공감·관점 전환 목적(D5).
- **people-gallery** (S6): 인물은 각 섹션/최상위 `people[]`에 쓰면 `build_people.py`가 `/history/people/`로 자동 집계. Person 구조는 §Person.

## 출력
- `30_content/<slug>/episode.json` (스키마 준수, 단계 4가 소비)

## 품질 게이트
- [ ] `python 40_build/build.py <slug>` 무오류 (JSON 유효 + 렌더)
- [ ] 모든 hook이 사람/장면/질문으로 시작
- [ ] reflect 빈칸·연결 고리·용어 풀이 존재
- [ ] 논쟁 균형 / 비서구 관점 반영
- [ ] 영상 yt가 리서치(video/search) 분류와 일치
