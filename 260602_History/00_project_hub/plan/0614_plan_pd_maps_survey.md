<!-- 00_project_hub/plan/0614_plan_pd_maps_survey.md -->
# PD 역사지도 전수 조사 — 전 허브 페이지 지도 보강 계획 ★

> Nick 지시(0614): 모든 역사 허브 내부 페이지에 **PD 역사지도 이미지**를 추가할 아이디어를 전수 조사해 분석·계획으로 정리.
> 근거 = `episode.json` 실측 스캔(12 SPA · 88 섹션). 최근 채택한 방식(coldwar#origin 진영 색칠지도, soviet-collapse 15공화국 지도) 확장.

## 0. 목표 / 원칙
- **목표:** 지도가 없어 공간 감각이 약한 섹션에 **PD/CC 역사지도**를 더해 '어디서·어떻게'를 시각화.
- **자산 규칙:** PD 또는 명확한 CC만, 출처·라이선스 표기, **전점 Read 검수**(Commons 검색 1위 신뢰 금지). 손그림 금지.
- **블록 3종 선택 가이드:**
  | 블록 | 쓰임 | 예 |
  |---|---|---|
  | `image` (PD 지도) | **색칠·주제 지도**(진영·제국·종교·통일 등 한눈 분류) | coldwar#origin 진영지도, soviet-collapse 15공화국 |
  | `oldmap` | **옛 고지도**(세피아 프레임, 시대감) | powers#britain Imperial Federation, exploration#toward-modern 블라우 1635 |
  | `map` (Leaflet) | **위치·도시 마커**(클릭 팝업 소개) | new-order#us-china, china-rises 도시들 |
- 우선순위: **P1**(지리/영토가 핵심인데 지도 없음) > **P2**(있으면 도움) > **P3**(선택·비핵심) > **—**(지도 부적합: 사상·과학·정서 섹션, figures).

## 1. 현황 요약 (실측)
- 총 88 섹션. **battlemap/oldmap/Leaflet map 보유**: ww2·exploration·powers·imperialism·아메리카 = 전쟁/탐험/제국 에피소드는 촘촘.
- **이미 PD지도 image 보강 완료(0614):** coldwar#origin(진영 색칠 세계지도)·globalization#soviet-collapse(15공화국+옛/현재 유고 2장)·china-rises(도시 Leaflet)·new-order#us-china(서태평양 Leaflet)·union(EU Leaflet).
- **지도 공백 집중 구역:** renaissance(7중 6 공백)·revolutions(7중 5)·new-order(7중 6, 단 일부는 주제상 부적합)·coldwar 후반.

## 2. 에피소드별 전수 표 (현재 → PD지도 아이디어 → 우선순위)

### ww2 (대부분 battlemap 보유 — 보강 소폭)
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| imperialism(1차대전) | battle·chart | (옵션) 1914 유럽 동맹 색칠지도 image | P3 |
| postwar | MAP·chart | (옵션) 1945 전후 분단(독·한) image | P3 |
| 그 외 6 | battle 다수 | 충분 | — |

### imperialism
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| **why-empire** | img·chart·rel (지도X) | **1914 세계 식민제국 지도**(제국별 색칠, world empires 1914) image | **P1** |
| **toward-war** | img·rel (지도X) | **1914 발칸 화약고 / 유럽 동맹** 지도(삼국동맹↔삼국협상 색칠) image | **P1** |
| industry | img·chart (지도X) | 산업혁명 확산/철도망 지도(영→유럽) oldmap | P2 |
| japan-meiji | battle | 충분 | — |
| 그 외 4 | MAP/OLDMAP/battle | 충분 | — |

### powers
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| overview | img·chart·rel | ※ 이미 1914 식민제국 지도(CC) 보유 추정 — **확인**, 없으면 P1 | P2 |
| 6개국 | oldmap/battle | 충분(나라별 식민지도) | — |

### exploration
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| **commerce** | img·chart (지도X) | **삼각무역·은 유통 세계 교역로** 지도 image | P2 |
| toward-modern | oldmap·rel | 충분(블라우 1635) | — |
| 그 외 6 | battle 다수 | 충분 | — |

### renaissance (지도 공백 최다 — 단 일부는 주제상 부적합)
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| **wars-religion** | img·chart (지도X) | **1648 베스트팔렌 후 유럽 / 신·구교 분포** 지도 image | **P1** |
| reformation | battle | (보강)종교개혁 확산 지도 | P2 |
| renaissance | img | 르네상스 이탈리아 도시국가 지도 oldmap | P2 |
| printing | img·chart | 인쇄술 유럽 확산 지도 image | P2 |
| absolutism | img | 루이14세기 유럽 / 베르사유 시대 지도 | P3 |
| scientific | img | (과학 주제 — 지도 부적합) | — |
| toward-modern | img·rel | (요약 — 부적합) | — |

### revolutions
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| **nationalism** | img·rel (지도X) | **1815 빈 체제 유럽 + 독일·이탈리아 통일** 지도(전/후) image | **P1** |
| american-rev | img (지도X) | 13개 식민지 지도 oldmap (※ north-america/revolution과 중복 주의) | P3 |
| napoleon | battle | 충분(나폴레옹 원정) | — |
| french-rev | battle | 충분 | — |
| enlightenment·glorious·terror | img | (사상·정변 — 지도 부적합) | — |

### coldwar (origin 완료)
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| origin | **image(진영지도) ✅** | 완료(0614) | ✅ |
| **fall** | img (지도X) | **1989 동유럽 혁명 / 독일 통일** 지도 image | P2 |
| detente | rel (지도X) | 중·소 분쟁/공산권 분열 지도 image | P2 |
| balance | img·chart | (핵 — 미사일 배치 지도 가능하나 비핵심) | P3 |
| space | img | (우주 — 부적합) | — |
| berlin·cuba·proxy | MAP/battle | 충분 | — |

### globalization (soviet-collapse·china·union 완료)
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| soviet-collapse | **image×4(15공화국+유고) ✅** | 완료(0614) | ✅ |
| china-rises | **MAP(도시) ✅** | 완료 | ✅ |
| union | **MAP(EU) ✅** | (옵션)EU 확대 연도별 색칠지도 image | P3 |
| one-market | chart (지도X) | 세계 무역로/컨테이너 항로 지도 | P3 |
| connected·nine-eleven·flat-world | img | (부적합) | — |

### new-order (us-china 완료)
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| us-china | **MAP(서태평양) ✅** | 완료 | ✅ |
| chip-war | img·chart (지도X) | 반도체 공급망 지도(대만·한국·일본·미국·네덜란드 표시) Leaflet/image | P2 |
| crack·multipolar·connected-crisis·ai-arrives·your-turn | img | (현대 주제 — 대체로 부적합, multipolar는 us-china 지도로 충분) | — |

### americas
| 섹션 | 현재 | PD지도 아이디어 | P |
|---|---|---|---|
| la/colonial | img·chart (지도X) | **토르데시야스 분할 / 스페인·포르투갈 식민지** 지도 oldmap | P2 |
| la/modern | img·chart (지도X) | 라틴아메리카 독립국 지도 image | P2 |
| na/modern | img·chart (지도X) | 미국 영토 확장/이민 지도(※ expansion과 중복 주의) | P3 |
| 그 외 9 | battle 다수 | 충분 | — |

### figures (6)
- 인물 '짝 읽기' 섹션 — 지도 부적합(인물별 journey 지도는 도감에 이미 존재). **제외.**

## 3. 우선순위 종합 — P1 (먼저, 5건)
1. **imperialism#why-empire** — 1914 세계 식민제국 색칠지도 (제국주의의 '지도를 색칠하던' 주제와 직결)
2. **imperialism#toward-war** — 1914 유럽 동맹/발칸 화약고 지도 (1차대전 발단)
3. **revolutions#nationalism** — 1815 빈 체제 + 독일·이탈리아 통일 (전/후 대비)
4. **renaissance#wars-religion** — 1648 베스트팔렌/신·구교 분포 (근대 국가의 탄생)
5. **powers#overview** — 1914 제국 지도 보유 여부 확인 후 없으면 추가

> 모두 '진영/영토가 색으로 갈리는' 주제 → coldwar#origin과 같은 **image(색칠 PD지도)** 패턴이 잘 맞음.

## 4. P2 (그다음, ~9건)
exploration#commerce(교역로)·renaissance(reformation·renaissance·printing)·coldwar(fall·detente)·la(colonial·modern)·new-order#chip-war.

## 5. 소싱·검수 방법 (확립된 절차)
- Commons API(urllib, 격리 네트워크) `generator=search` → **PD/CC 필터 + 이미지 확장자** → thumburl(SVG는 PNG 썸네일) 다운로드.
- **전점 Read 검수**(엉뚱본/저해상/책스캔/중복 차단) → 필요시 PIL 크롭(여백 제거).
- 후보 키워드 예: "world empires 1914", "Europe alliances 1914", "Congress of Vienna 1815 map", "unification of Germany/Italy map", "Peace of Westphalia 1648 map Europe religious", "triangular trade map".
- 429 레이트리밋 시 정확 파일명+지연(time.sleep). 출처/라이선스 caption 표기.

## 6. 단계 실행안
- **B1 (P1 5건):** 한 배치로 소싱·검수·패치(image 블록 + order 삽입)·빌드·배포·G3. 균형/캡션 점검.
- **B2 (P2 9건):** 2배치로 분할.
- 각 배치: 소스 커밋 → 배포 cp·커밋 → push(소스/배포 cwd 분리) → G3 폴링. 엔진 변경 0(데이터만).
- 완료 시 PROGRESS·이 파일 §체크 갱신.

## 7. 진행 기록
- 0614: 전수 조사·계획 수립. 이미 완료(0614): coldwar#origin·globalization#soviet-collapse·china-rises·new-order#us-china·union.
- **0614 ✅ B1 완료·배포·라이브(G3)**: imperialism#why-empire(1914 식민제국 CC BY)·toward-war(1914 동맹 CC BY-SA)·revolutions#nationalism(1815 빈체제+독일통일 1871)·renaissance#wars-religion(1648 베스트팔렌). powers#overview는 기보유로 제외. 소스 `d1e9510`·배포 `dcce7ed`.
- **0614 ✅ B2 완료·배포·라이브(G3)**: exploration#commerce(삼각무역 CC BY-SA)·coldwar#detente(중소분쟁 CC BY-SA)·latin-america#modern(독립연도 PD)·latin-america#colonial(토르데시야스 PD oldmap)·renaissance#renaissance(이탈리아1494 PD oldmap)·renaissance#reformation(유럽종교1560 PD oldmap). 소스 `8d8ccbd`·배포 `5320059`.
- **보류(깔끔한 PD지도 부재):** renaissance#printing(인쇄술 확산)·coldwar#fall(1989 동유럽 혁명)·new-order#chip-war(반도체 공급망). 추후 적합 자산 발견 시 추가.
- **★ 지도 보강 마무리.** 0614 신규 PD지도/이미지 총 ~18점(전점 Read 검수, PD/CC). 전쟁/탐험/제국 편은 battlemap으로 이미 충분.
