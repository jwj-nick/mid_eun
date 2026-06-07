<!-- 10_docs/MAP_TOOLKIT.md -->
# 지도 툴킷 & 규칙 (공식 레퍼런스)

> 이 문서 = 역사 이야기 앱에서 **지도를 어떤 방식으로, 언제, 어떻게** 쓸지에 대한 **공식 기준**.
> 원칙: **하나의 '기본'은 없다 — 모든 기법은 도구상자, 콘텐츠마다 맞는 것을 고른다.**
> 라이브 데모(모든 도구 비교): `/history/maplab/` (소스 `40_build/maplab.html`).

## 0. 절대 규칙 (모든 지도 공통)
1. **키 0 / 바닐라 / CDN만** — 공개 GitHub Pages라 비밀키 불가. 토큰 필요한 서비스(Mapbox 등) 금지. 벡터가 필요하면 **MapLibre(무키)**.
2. **출처·라이선스 표기** — 모든 베이스맵/이미지/타일은 PD 또는 명시 가능한 출처. 파일페이지 검증 후 레포 호스팅.
3. **데이터↔엔진 분리** — 지도 종류는 엔진의 `mode`로, 좌표·국면은 episode.json 데이터로.
4. **관점** — 전쟁/침탈 지도는 **침탈(붉은색) vs 저항(초록)** 색·문구로 균형. 정복 미화 금지.
5. **시대 적합성** — **현대 도시 3D(예: 지금 서울 빌딩) 미사용**(역사물에 시대 부적합). 시대감은 **고지도(古地圖)**로.
6. **손그림 금지** — 지도는 실제 지도/사료 기반.
7. **접근성** — 색에만 의존 금지(아이콘/라벨 병행), 모바일에서 라벨 겹침 점검, alt·키보드.

## 1. 도구상자 (mode 카탈로그)
| mode | 엔진 | 무엇 | 쓸 때 | 피할 때 |
|---|---|---|---|---|
| **battlemap** | Leaflet + leaflet-ant-path | 진짜 지도에 실좌표 마커·**흐르는 화살표**·격전지·단계 스테퍼 | 정확한 위치+진군(국지·광역 전투) | 시대감이 핵심일 때(현대 타일) |
| **marchmap** | SVG 오버레이 | 지도 **이미지** 위 곡선 진격로 단계 연출 | 한 장면의 드라마, 고지도 위 연출 | 정밀 좌표·줌이 필요할 때 |
| **oldmap** | 이미지/타일 | **실제 고지도(PD)** 베이스(+선택적 마커) | **시대감**이 중요한 장면 | 정밀 핀(투영 부정확) |
| **scrolly** | Leaflet + IntersectionObserver | 스크롤 따라 지도가 flyTo·전환 | 이야기 **순서**가 핵심인 내러티브 | 짧은 단일 장면 |
| **territory** | MapLibre + GeoJSON | 영역 채색·국경 morph(연도 토글) | 영토/세력권 변화(제국 팽창·분단) | 단순 위치 표시(과함) |
| **globe** | globe.gl | 3D 지구본 + 본국→식민지 arc | **전 지구 구조**(제국·냉전·교역) | 한 지역 상세 |

> MapLibre(territory/벡터)는 **3D 지형·시대별 커스텀 스타일** 같은 꼭 필요한 경우에만. **현대 도시 3D는 미사용.**

## 2. 콘텐츠 → mode 선택 가이드 (핵심)
| 콘텐츠 성격 | 1순위 | 대안 |
|---|---|---|
| 한 지역 전투·봉기 흐름(동학) | **battlemap**(줌) | marchmap, oldmap |
| 넓은 다지역 전쟁(청일·러일·태평양) | **battlemap**(광역) | 격전지 oldmap 인서트 |
| 이야기 순서가 핵심(한 사건 따라가기) | **scrolly** | battlemap 스테퍼 |
| 전 지구 구조(제국↔식민지·냉전·교역) | **globe** | (D3 흐름) |
| 영토·세력권 변화(제국 팽창·분단) | **territory** | 연표 image |
| 시대감이 중요한 장면 | **oldmap** | 세피아 타일 |

## 3. 통합 `geo` 블록 스키마 (목표 — 엔진 일원화)
> 현재는 mode별 블록이 따로(`map`,`marchmap`,`relations`…). 점차 단일 `geo`로 수렴.
```jsonc
"geo":{
  "mode":"battlemap|marchmap|oldmap|scrolly|territory|globe",
  "engine":"leaflet|svg|maplibre|globe",   // mode가 함의하면 생략 가능
  "base":{"src":"img/...","tiles":"...","style":"..."},  // mode에 맞는 것만
  "view":{"center":[lat,lng],"zoom":N,"bounds":[[..],[..]]},
  "phases":[{"label":"...","show":[...],"arrows":[{"from","to","tone":"resist|invade","label"}]}],
  "legend":[{"color":"#..","label":"..."}],
  "caption":"출처(PD)·라이선스"
}
```

## 4. 자산 수배 절차 (G2)
- 이미지: Wikipedia REST `originalimage` → 다운로드 → `file`로 실물 확인 → `30_content/<slug>/img/`(또는 maplab 자산) 호스팅 → 출처표기.
- 위경도/한국어 위키 제목: 표준 location-map bounds, en→ko langlinks API.
- 외부 타일/링크: **실제 200 검증**(추측 금지). 무키만.

## 5. 리뷰 게이트
- **G0** 빌드 무오류 · **G1** JS_OK(엔진 변경 시 node --check) · **G2** 자산·링크 200·실물 · **G3** 라이브(대기루프+캐시버스트)
- **R1** 시각(데스크톱/모바일) · **R2** 멀티 페르소나(카토그래퍼·교사·디자이너·역사학자) · **R3** 성능(60fps·용량) · **R4** 키 노출 0 · **R5** 사용자 반응=최종 KPI
- 같은 사건 **A/B 비교**로 mode 적합성 판단(기본형을 못박지 않음).

## 6. 현황 (도구 확보 상태)
| mode | 상태 |
|---|---|
| **battlemap** | ✅ **엔진 승격(위기의 조선: 동학·청일/러일 라이브)** — Leaflet+ant-path |
| marchmap | ✅ 엔진 보유 |
| map(기본 Leaflet 마커) | ✅ 보유 |
| relations(역학도) | ✅ 보유(지도 아님, 구도) |
| scrolly / oldmap / territory / globe | 🔬 maplab 데모 검증됨 → 엔진 mode 승격 대기 |

> 다음 승격 추천: oldmap → scrolly → globe → territory. 각 승격 시 콘텐츠 1개로 검증.
> (참고) 계층적 깊이 = `deepdive` 블록(EPISODE_SCHEMA) — 지도와 함께 고등/일반 심화 제공.
