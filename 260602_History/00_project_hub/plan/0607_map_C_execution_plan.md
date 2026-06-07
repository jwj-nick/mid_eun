<!-- 00_project_hub/plan/0607_map_C_execution_plan.md -->
# 0607 — 지도 C(하이브리드) 실행 플랜

> 결정(Nick): **C = A(Leaflet 실좌표) + B(역사지도 위 SVG 진격로), B 적극 사용.** Mapbox 제외(키 노출·과금·불필요), 필요 시 미래 MapLibre.
> 다음 레벨 비전은 별도: `10_docs/0607_map_next_level.md`.

## 0. 원칙 (불변)
- 바닐라·CDN·**키 0**(공개 Pages). 데이터↔엔진 분리(엔진 1곳, episode.json 데이터).
- 검증은 hist-deploy §G0~G3(빌드/JS_OK/자원200·실물/라이브). **추론 금지, 실측만.**
- 관점: 전투지도는 **침탈 vs 저항** 프레이밍 + 격전지에 민중 피해 한 줄(미화 금지, 중1 수위).

## 1. 신규 엔진 블록 2종
### (B) `marchmap` — 역사지도 위 SVG 진격로 ★먼저
- 베이스(고지도/외곽 SVG·PNG) 위에 **장소 점(%)** + **곡선 화살표(SVG path)** + **단계 스테퍼**(▶ 다음 → 국면 누적 공개).
- 화살표 그리기 애니: `stroke-dasharray/dashoffset` CSS 트랜지션(키 없음, GSAP 없이도 됨).
- 스키마(안):
```jsonc
"marchmap":{
 "title":"...","intro":"...","caption":"출처(PD)·라이선스",
 "base":{"src":"img/<map>.svg","ar":"4 / 3"},          // 베이스 이미지(레포 호스팅)
 "places":[{"id":"gobu","x":34,"y":74,"label":"고부","kind":"start|battle|win|loss|capital"}], // x,y=%
 "phases":[
   {"label":"1. 고부 봉기","show":["gobu"],"arrows":[]},
   {"label":"2. 북상·전주 점령","show":["jeonju"],"arrows":[{"from":"gobu","to":"jeonju","label":"북상","tone":"resist"}]},
   {"label":"3. 우금치 대패","show":["ugeumchi"],"arrows":[{"from":"jeonju","to":"ugeumchi","tone":"resist"},{"from":"japan","to":"ugeumchi","tone":"invade"}]}
 ]
}
```
- `tone`: resist(저항)·invade(침탈)로 화살표 색 구분.

### (A) `battlemap` — Leaflet 단계형 전투지도
- Leaflet + **leaflet-ant-path**(CDN, 키 없음, 흐르는 화살표) + **⚔️ divIcon 격전지** + 동일 스테퍼.
- 스키마(안):
```jsonc
"battlemap":{
 "center":[37.5,126.9],"zoom":5,
 "phases":[
   {"label":"1. 풍도 해전","battles":[{"at":[37.0,126.1],"label":"풍도 해전","kind":"sea"}],
    "arrows":[{"from":[34.7,135.5],"to":[37.0,126.1],"tone":"invade"}]}
 ]
}
```
- 두 블록 **스테퍼 UI·tone 색·격전지 아이콘 공통** → CSS/JS 재사용.

## 2. 적용 대상 (콘텐츠)
| 대상 | 블록 | 베이스맵 | 단계 |
|---|---|---|---|
| **동학(우금치)** ★시범 | B marchmap | 조선(한반도) 외곽 SVG | 고부봉기→백산→황토현·황룡촌(승)→전주성→**우금치 대패**→순창 체포 |
| 청일전쟁 | A battlemap (+B 보강) | 동아시아(황해·만주·한반도) | 풍도해전→평양→압록강→뤼순→웨이하이웨이 |
| 러일전쟁 | A battlemap | 만주·동해 | 뤼순 포위→펑톈→**쓰시마 해전** |
| 조선 각축 역학도(기존) | relations(보유) | — | 지도 옆에 배치(역학+지도 연계) |

## 3. 실행 순서 (게이트 동반)
1. **자산 수배**: PD 한반도/동아시아 베이스맵 SVG(Wikimedia, 파일페이지 라이선스 확인 → 다운로드 → `30_content/<slug>/img/`). [G2]
2. **B `marchmap` 엔진 블록** 신설(렌더+CSS+스테퍼) → JS_OK [G1].
3. **우금치 시범** 데이터(imperialism/korea) → 빌드 → **로컬 스크린샷 리뷰**(데스크톱+모바일).
4. 좋으면 **A `battlemap`** 엔진 블록(ant-path CDN) → 청일·러일 데이터.
5. 배포 [G3 라이브] + EPISODE_SCHEMA/PROGRESS/스킬 갱신 + 소스 카테고리 커밋.

## 4. 리뷰 방법 (이번 작업 한정)
- **시각**: 배포 전 데스크톱+모바일 스크린샷 before/after.
- **관점 audit**: 침탈/저항 색·문구, 격전지 피해 한 줄(역사학자·교사 페르소나).
- **기술**: G0~G3 + 키 노출 0 grep.
- **A/B**: 우금치를 B로 먼저, 이후 청일을 A로 — 두 방식 비교해 향후 기본형 결정.

## 5. 산출/완료 기준
- 우금치 marchmap 라이브(단계별 진격로 동작) + 청일·러일 battlemap 라이브.
- 엔진 2블록 재사용 가능(타 에피소드 데이터만으로 전투지도 생성).
