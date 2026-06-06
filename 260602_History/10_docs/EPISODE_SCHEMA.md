<!-- 10_docs/EPISODE_SCHEMA.md -->
# Episode Content Schema (SSOT 계약)

> 모든 에피소드는 이 스키마(`30_content/<slug>/episode.json`)로 작성한다.
> `hist-content-write`가 **생산**, `hist-app-build`(`40_build/build.py`)가 **소비**해서 단일 HTML로 렌더한다.
> 같은 스키마에서 나중에 영상 대본·퀴즈도 파생 가능. **작성(데이터) ↔ 렌더(엔진) 분리가 핵심.**

## 최상위
```jsonc
{
  "meta":   { ... },          // 에피소드 메타 + 홈 화면
  "terms":  { "용어": "쉬운 풀이", ... },   // 본문에 자동으로 점선+툴팁 적용
  "sections": [ Section, ... ],            // 8개 내외 (한 흐름)
  "people": [ Person, ... ]                // (선택) 에피소드 공통 인물 갤러리
}
```

## meta
```jsonc
{
  "lang":"ko", "slug":"ww2",
  "title":"...", "description":"...",                 // <title>/메타
  "brand":{ "title":"사이드바 제목", "sub":"부제" },
  "foot":"사이드바 하단 (html 허용)",
  "home":{
    "h1":"홈 큰제목(br 허용)", "sub":"홈 부제",
    "quote":{ "text":"인용", "by":"출처" },            // 선택
    "intro":"홈 소개 (html 허용)",
    "startPrimary":{ "label":"처음부터 →", "to":"<섹션id>" },
    "startStar":{ "label":"★ ...", "to":"<섹션id>" },  // 선택(강조 입구)
    "pathLabel":"이야기 흐름"
  }
}
```

## Section
```jsonc
{
  "id":"imperialism", "num":"00", "label":"사이드바 라벨",
  "star": true,                       // (선택) 강조 섹션
  "accent":"#3f6f74",                 // 히어로 그라데이션 끝색 (시대 분위기)
  "kicker":"작은 머리말", "era":"1870년대 ~ 1918",
  "motif":"flag",                     // 히어로 SVG (아래 목록)
  "title":"섹션 큰 제목",
  "hook":"여는 장면 (인물/장면/질문, T()로 용어 자동처리)",
  "quote":{ "qt":"인용문", "qs":"출처" },     // (선택) hook 아래
  "why":"왜 중요할까 (html <b> 허용)",
  "lens":"'그때 사람들은 이렇게 생각했어요' 비판적 렌즈 (선택)",
  "cards":[ { "yr":"연도/라벨", "h":"카드 제목", "p":"설명(T())" }, ... ],   // 3~6
  "quote2":{ "qt":"...", "qs":"..." },        // (선택) 카드 뒤
  "people":[ Person, ... ],                    // (선택) 섹션 단위 인물
  "map": Map,                                   // (선택) 그림 지도 + 클릭 핀 (R3)
  "timeline":[ { "yr":"1914.6", "t":"사건" }, ... ],
  "connect":"이전/다음 섹션과의 연결 한 줄 (html <b>)",
  "yt":[ Video|Search, ... ],                  // 1~3
  "quiz":[ Quiz, ... ],                         // (선택) 섹션 끝 "잠깐, 기억나니?" 미니 체크
  "reflect":[ "내 생각 질문", ... ]            // 1~2 (빈칸 textarea, 자동저장)
}
```

## Quiz (퀴즈 항목, R1 블록)
```jsonc
{ "q":"질문", "options":["보기1","보기2","보기3"], "answer":1, "explain":"정답 해설(틀려도 배우게)" }
```
- `answer` = 정답 보기의 인덱스(0부터). 클릭 시 정답 초록·오답 빨강 + 해설 공개, 점수/강박 없음.
- 1섹션당 1~2문 권장. 정답 강요 X, "기억나니?" 톤.

## Video / Search (yt 항목)
```jsonc
{ "type":"video",  "id":"유튜브ID", "title":"...", "channel":"채널", "length":"약 6분", "lang":"ko|en", "desc":"무엇을 볼 수 있나" }
{ "type":"search", "q":"검색어",     "title":"...", "lang":"ko|en", "desc":"이런 영상을 찾아보세요" }
```
- `video` = 검증된 특정 영상(직접 링크). `search` = 아직 핀 안 한 검색 진입(🔍).
- **정책**: 고신뢰만 `video`. 불확실하면 `search` (죽은 링크 방지).

## Person (인물 카드)
```jsonc
{ "face":"👤(이모지/이니셜)", "name":"이름", "who":"한 줄 정체성·시대",
  "why":"왜 꼭 알아야 하나", "quote":"기억에 남을 한 마디(출처는 desc/별도)",
  "shadow":"빛과 그림자(한계·논쟁) — 영웅화 금지" }
```

## Map (지도 블록, R3 — 실제 지도 Leaflet+OSM)
```jsonc
{ "caption":"설명", "source":"OpenStreetMap",
  "center":[위도, 경도], "zoom":3,
  "line":[[lat,lng],[lat,lng]],          // (선택) 점선 경계선(예: 38선)
  "markers":[ { "lat":52.52, "lng":13.40, "label":"지명", "desc":"클릭 팝업 설명" } ] }
```
- **실제 지도 타일(OpenStreetMap)** 위에 마커(원형) + 팝업. 손그림 금지.
- 엔진이 Leaflet으로 렌더(CDN). `scrollWheelZoom` 꺼짐(페이지 스크롤 보호), 드래그/버튼 줌 가능.
- 현대 지도라 옛 국경은 안 보임 → caption에 "현재 지도 위 표시" 명시. (옛 국경이 핵심이면 → 향후 `image`로 공개도메인 역사지도 보강)

## Image (이미지 블록, S1 — PD 역사지도/사진 + 선택적 hotspot)
```jsonc
{ "h":"블록 제목(선택, 기본 '자료로 보기 🖼️')",
  "src":"img/파일.svg",                 // 30_content/<slug>/img/ 에 두면 빌드가 50_app으로 복사
  "alt":"대체 텍스트(접근성 필수)",
  "story":"이미지 위 도입 문단(선택, T()·<b> 허용)",
  "caption":"설명", "source":"출처(예: Wikimedia Commons · 저자)", "license":"퍼블릭 도메인(PD) | CC BY-SA 4.0 …",
  "hotspots":[ { "x":42, "y":31, "label":"지점 이름", "desc":"클릭 시 설명" } ] }   // (선택) x,y = 이미지 기준 %
```
- **자산은 `30_content/<slug>/img/`에 저장** → `build.py`가 `50_app/<slug>/img/`로 복사, 배포 시 index.html과 함께 옮긴다. **상대경로 `img/...` 사용.**
- 이미지는 **공개도메인(PD-old) 또는 명확한 CC** 만. 출처·라이선스 표기 필수. **손그림 금지.** 옛 국경/세력은 여기서(map=현대 지도와 역할 분담).
- hotspot: 이미지 위 번호 점 → 클릭하면 아래에 한국어 설명. 좌표는 % (좌상단 0,0). 정확한 위치를 모르면 생략(엔진은 hotspot 없어도 동작).

## Voice (목소리 블록, S3 — 일기·편지체 1인칭)
```jsonc
{ "h":"블록 제목(선택, 기본 '그 사람의 목소리 🗣️')",
  "imagined": false,                      // false=실제 기록(초록 배지) / true=사실에 기반한 상상(✍️ 배지)
  "body":"1인칭 본문(T() 적용)",
  "speaker":"화자", "era":"때·곳(선택)",
  "source":"출처(실제) 또는 '~을 바탕으로 상상' 설명" }
```
- `imagined:false`면 **실제 사료**(인용·출처 정확), `true`면 **사실 기반 상상**(반드시 배지로 구분, source에 근거 명시). 날조·왜곡 금지.
- hook/why 뒤(카드 앞)에 렌더 — 감정 몰입 입구. 섹션당 1개 권장.

## Chart (차트 블록, S4 — 자체 막대 + 체감 비교)
```jsonc
{ "h":"제목(선택, 기본 '숫자로 보기 📊')",
  "title":"차트 제목", "unit":"축 설명(선택)",
  "data":[ { "label":"1929년", "value":3, "disp":"약 3%" } ],   // value=막대 길이용 숫자, disp=표시 문구(선택)
  "relatable":"체감 비교 한 줄(예: '4명 중 1명') — D4", "source":"출처" }
```
- 외부 라이브러리 없이 CSS 막대로 렌더(모바일 반응형). `value` 최대값 기준 상대 길이.
- **통계는 출처 표기, 불확실하면 '대략값' 명시.** `relatable`로 아이의 세계 단위(반 인원·서울 인구 등)에 빗대기.

## Compare (비교 블록, S5 — 단계 토글 / before·after)
```jsonc
{ "h":"제목(선택, 기본 '견주어 보기 ⚖️')", "intro":"안내(선택)",
  "states":[ { "label":"탭 이름", "title":"제목", "body":"설명(T())",
              "img":"img/..(선택)", "alt":"(img시)", "caption":"(img시 출처)" } ] }
```
- 탭(2~4개)을 눌러 상태를 바꿔 비교. 전후·단계 변화에. `img`는 선택(있으면 **PD/명확한 CC만**, 출처 표기).
- **그때↔지금 사진(D6)** 은 양쪽 PD/CC 확보 시 `img`로. 현대 사진은 보통 저작권 → 확보 못 하면 텍스트 상태만으로도 충분.

## People-gallery (인물 도감, S6 — 크로스 에피소드 색인)
- 데이터는 **각 에피소드의 `people[]`(섹션/최상위)에서 자동 수집** → `python 40_build/build_people.py` → `50_app/people/index.html` 생성 → 배포 `/history/people/`.
- 새 에피소드의 `people`가 늘면 빌더만 다시 돌리면 색인 자동 갱신(별도 스키마 없음). Person 구조는 위 §Person과 동일.
- 허브(`/history/index.html`) 사이드바 '도감' + 메인 카드에서 진입.

## Choice (선택 블록, S7 — '너라면?' 도덕적 딜레마)
```jsonc
{ "h":"제목(선택, 기본 '너라면? 🤔')",
  "prompt":"상황·딜레마(T())",
  "options":[ { "label":"선택지", "result":"선택 후 해설(균형·단정 회피, 실제 사례)" } ],
  "after":"마무리 한 줄(선택, '정답은 없어요' 류)" }
```
- 2~3 선택지. 클릭하면 그 선택의 해설이 펼쳐지고 여러 선택을 눌러 비교 가능(잠금 없음).
- **정답 강요·단정 금지.** 어느 선택도 인격적으로 폄하하지 않게. 공감·관점 전환이 목적(D5).

## 내 메모 모아보기 (R2, 엔진 기능 — 데이터 불필요)
사이드바 "📝 내 메모 모아보기" → 전 섹션 reflect 메모(localStorage)를 한 화면에 모아 **인쇄/PDF·전체 복사**. 모든 에피소드 자동 제공(스키마 변경 없음). 탐구학습 발표·보고서 초안용.

## motif 목록 (히어로 SVG, 엔진 내장)
`flag, crowd, book, map, wave, sun, split, dove, globe, ship, torch, gear`
→ 부족하면 `40_build/templates/episode.html`의 `MOTIF`에 추가.

## 빌드
```
python 40_build/build.py <slug>     # 30_content/<slug>/episode.json → 50_app/<slug>/index.html
```
출력은 자기완결형 단일 파일(더블클릭·GitHub Pages 모두 동작). 엔진/디자인 수정은 템플릿 1곳 → 재빌드로 전 에피소드 전파.

## 편집 원칙 연결
`APP_PRINCIPLES.md`(중1 톤·빈칸) + `plan/260603_history_hub_master_plan.md` §9(탈서구중심·렌즈·논쟁 균형)을 준수. `lens`·`people`은 마스터플랜 요구사항의 스키마 반영.
