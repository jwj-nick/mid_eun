# 00_PLAN — mid-sci (중학 과학 PhET·하이브리드 앱) 마스터 플랜

> 저작 홈: `C:\Kids\30_MiddleSchool\Mid_Science` (과학 콘텐츠 SSOT) · 배포: `github.io/mid-sci`
> 대상: **세은(딸, 중2)** — 단, 콘텐츠는 **중1~3 전체**. 흥미·직관 레이어(시험 점수 도구 아님 → 반드시 "문제 착지").
> 등록: 2026-07-20. 상위 규약: `C:\idea\migration\_COMMON.md` · `seeun-phet.md` · `seeun-sci-phet.md`.

---

## 0. Nick 확정 결정 (2026-07-20)

| 결정 | 값 | 이유 |
|---|---|---|
| **앱 구조** | **단일 앱 `mid-sci` + 학년 탭(중1/2/3)** | history식 2D 랜딩(학년×영역). 포털 카드 1개·학년 간 이동 매끄러움·배포 단순 |
| **엔진 깊이** | **하이브리드 슬라이스** (PhET 임베드 + 네이티브 SVG 카드 동시) | 첫 슬라이스부터 이원 모드 과시. PhET 강한 곳=임베드, 약한 곳=네이티브 |
| **P1 앵커** | **중1 힘과 운동** (`forces-and-motion-basics` + 자유물체도 SVG) | PhET 강함 + 네이티브 카드로 자유물체도(시험 실제 출제) → 두 모드 상보성 즉시 증명 |

---

## 1. 아키텍처

### 1.1 저작 ↔ 배포 분리
- **저작(여기, `Mid_Science`)** — 개념↔시뮬 매핑, 예측/확인 질문, 네이티브 카드 데이터, 세션 로그.
- **배포(`C:\Nick\30_Apps\jwj-nick.github.io\mid-sci`)** — 무빌드 바닐라 JS. `content.js` 데이터 구동. 포털 `index.html` `EXTRA_APPS` 카드 등록 → `git pull` → push → Pages.
- **데이터/코드 분리:** 앱 로직은 `app.js`, 콘텐츠 전부는 `content.js` 하나. 학습 진척 시 `content.js`만 갱신.

### 1.2 앱 구조 (배포 산출물)
```
github.io/mid-sci/
├── index.html      학년×영역 2D 랜딩 (history 랜딩 패턴 참조) + 학년 탭 中1|中2|中3
├── app.js          렌더 엔진: 랜딩·카드·PhET 임베드·SVG 카드·예측/확인 인터랙션
├── sci.css         테마(라이트/다크)·시그니처색·카드 컴포넌트
├── content.js      ★ SSOT 데이터 (아래 스키마)
└── svg.js          네이티브 SVG 렌더러 모음 (freebody, bohr, circuit … 필요할 때 증식)
```

### 1.3 content.js 스키마 (제안)
```js
const SCI = { grades:[ {
  id:'m1', label:'중1', color:'#4f92d6', areas:[ {
    area:'힘과 운동', concepts:[ {
      id:'m1-force-net',
      title:'여러 힘과 알짜힘',
      hook:'상자를 밀면 왜 어느 순간 갑자기 움직일까?',   // 실생활 진입 질문
      sim:{ type:'phet', slug:'forces-and-motion-basics' }, // type: phet | native | none
      card:{ type:'freebody', params:{ /* 힘 화살표 배열·알짜힘 */ } }, // 네이티브(옵션)
      predict:[ {q:'미는 힘을 키우면?', observe:'가속도가?', why:'왜?'} , ... x3 ],
      confirm:[ '알짜힘 0이면 물체는?', ... x3 ],   // 문제 착지
      drawingPoints:['작용점','방향','크기 비교'],  // 시험 그림 체크(chem-card 패턴)
      examHook:'알짜힘 = 한 방향 힘의 합, 반대는 뺀다'
    } ] } ] } ] };
```

### 1.4 시뮬 3-모드 (하이브리드 핵심)
| 모드 | 언제 | 구현 |
|---|---|---|
| **PhET 임베드** | PhET 강한 곳 (힘·회로·중력·산염기·에너지…) | `…/<slug>/latest/<slug>_all.html?locale=ko` iframe, 무거우면 딥링크 버튼 |
| **네이티브 SVG 카드** | PhET 약한 곳 (원자·이온·결합·자유물체도…) | `svg.js` 렌더러 + `content.js` 파라미터. chem-card 스킬 패턴 이식 |
| **"시뮬 없음" 정직 후크** | PhET·네이티브 둘 다 약함 (광합성 세부·판구조·별 등급·세포 구조) | 영상/그림 링크 + 한 줄 설명. 억지 시뮬 금지 |

### 1.5 카드 해부 (착지 루프 — 모든 개념 공통)
`실생활 후크 질문` → `개념 한 입` → `시뮬(3-모드 중 하나) 만져보기` → `예측·관찰·왜 3문항` → `확인 질문 3개(문제 착지)`. (출처 `seeun-phet.md`·vision doc §2)

---

## 2. 학년별 개념 ↔ 시뮬 매핑 (SSOT 시드)

> `seeun-sci-phet.md §4` 시드 + **하이브리드 주석**(네이티브 카드 후보·정직 후크). P2에서 `content.js`로 이관하며 검증.

### 중1
| 영역 | 개념 | PhET | 네이티브 카드 후보 | 비고 |
|---|---|---|---|---|
| 힘과 운동 | 여러 힘·마찰·알짜힘 | `forces-and-motion-basics` | **자유물체도(freebody)** ★P1 | PhET강 |
| 기체 | 압력·부피 | `gas-properties`, `states-of-matter-basics` | 입자 모형 카드 | PhET강 |
| 빛·파동 | 굴절·파동 | `bending-light`, `wave-on-a-string` | 굴절 광선도 | PhET강 |
| 생물(세포) | 세포 구조 | — | 세포 라벨 그림 | **정직 후크**(PhET약) |
| 지권 | 판구조 변화 | — | — | **정직 후크**(영상) |

### 중2
| 영역 | 개념 | PhET | 네이티브 카드 후보 | 비고 |
|---|---|---|---|---|
| 물질의 구성 | 원자·이온·동위원소 | `build-an-atom`, `isotopes-and-atomic-mass` | **보어모형·이온화(bohr)** — chem-card 재사용 | 하이브리드 최적 |
| 전기·자기 | 전류·회로·전자기 | `circuit-construction-kit-dc`, `faradays-law` | 회로 기호도 | PhET강 |
| 태양계 | 중력·공전 | `gravity-and-orbits`, `my-solar-system` | — | PhET강 |
| 물질의 특성 | 밀도·용해도·농도 | `density`, `concentration` | 밀도 비교 카드 | PhET강 |

### 중3
| 영역 | 개념 | PhET | 네이티브 카드 후보 | 비고 |
|---|---|---|---|---|
| 화학반응 | 반응식·산염기 | `balancing-chemical-equations`, `ph-scale` | **루이스 구조·반응식 균형(chem-card)** | 하이브리드 |
| 운동·에너지 | 에너지 보존 | `energy-skate-park`, `energy-forms-and-changes` | 에너지 막대 카드 | PhET강 |
| 생식·유전 | 유전·형질 | `gene-expression-essentials`, `natural-selection` | 유전 격자(Punnett) | PhET중 |
| 기권·에너지 | 온실효과 | `greenhouse-effect` | — | PhET강 |
| 생물(광합성) | 광합성 세부 | — | — | **정직 후크**(영상) |

---

## 3. Phase 계획

### P0 감사 — 완료 (`seeun-sci-phet.md §2`)
- mid1에 과학 콘텐츠 없음 → mid-sci 신규(중복 아님). github.io 형제 서브폴더.

### ★ P1 슬라이스 = 중1 힘과 운동 (하이브리드 카드 1개) — 다음 세션
**산출: 배포된 mid-sci 골격 + 카드 1개 + 포털 카드 등록.** 루프 증명.
1. `mid-sci/` 골격: `index.html`(학년 탭 + 랜딩) · `app.js` · `sci.css` · `content.js` · `svg.js`.
2. `content.js`에 **중1 `m1-force-net` 1개만** 채움 (§1.3 스키마).
3. **PhET 반쪽:** `forces-and-motion-basics_all.html?locale=ko` iframe 카드 (무거우면 딥링크 버튼).
4. **네이티브 반쪽:** `svg.js`에 `freebody` 렌더러 1개 — 상자 + 힘 화살표(밀기·마찰·중력·수직항력) + 알짜힘 표시. chem-card SVG 파라미터 방식 이식.
5. 예측·관찰·왜 3문항 + 확인 질문 3개(문제 착지) + drawingPoints/examHook.
6. **검증:** github.io `serve.ps1` 로컬 프리뷰로 iframe 로드·딥링크·SVG·인터랙션 확인. 사적 데이터 repo 밖.
7. **배포:** `git pull` → 커밋(주제 단위) → push → Pages. `index.html EXTRA_APPS`에 mid-sci 카드 등록.
8. **로그:** `00_meta/sessions/<날짜>_mid-sci.md` 1줄 + P2 자율개선 1줄 + 다음 액션.

### P2 전개 — §2 매핑 순서로
- 중1 나머지 영역 → 중2(원자·이온에서 chem-card 이식 본격) → 중3.
- `content.js` 확장 + `svg.js` 렌더러를 **필요할 때** 증식(speculative 금지). 학년 탭 랜딩 채움.

### P3+ (후순위 — content pulls the engine)
- **도감형 컬렉션**(history 도감 패턴): 원소 도감·힘 도감·유전 도감.
- **게임화**: 예측 게임·남매 챌린지·5초 도전(vision doc §2).
- **figcrop**로 교과서 도식 첨부.

---

## 4. 재사용 자산 & 스킬 로드맵

### 지금 재사용 (검증된 것)
| 자산 | 출처 | 쓰임 |
|---|---|---|
| 개념여정 엔진 컴포넌트 | `mid2/concept.js` (사이드바·진도·테마·`x`탐험 탭) | app.js가 패턴 차용(통째 포크 X) |
| 네이티브 과학 SVG | `70_HighSchool/.claude/skills/se-science-chem-card` | 보어모형·루이스·이온화 → svg.js 이식 |
| 2D 랜딩·도감 | `github.io/history` | 학년×영역 랜딩, 후기 도감 |
| 배포 포털 | `github.io/index.html EXTRA_APPS` + `serve.ps1` | 카드 등록·로컬 프리뷰 |
| 교육 철학·후크 | `04_PhET_Kids_Math_Science.md` | 실생활 후크·예측게임·흥미≠점수 |
| 도식 크롭 | global `figcrop` / son `se-figcrop` | 교과서 그림 첨부 |

### 신규 스킬 후보 (**필요해질 때만** — _COMMON P1 규율)
- `mid-sci-card` — 개념 하나를 받아 content.js 카드(hook·sim·predict·confirm·drawingPoints) 생성. (카드가 반복 노동이 될 때)
- `mid-sci-svg` — 네이티브 SVG 렌더러 추가/재생성. (freebody 다음 렌더러가 필요할 때)
- ※ chem-card가 이미 원자/결합을 커버 → 중2/3 화학은 그 스킬 이식으로 충분할 수 있음. 중복 스킬 금지.

---

## 5. 열린 질문 (다음에 Nick 확정)
- 슬러그 `mid-sci` 확정? (대안 `mid-science`, `sci-lab`) — 잠정 `mid-sci`로 진행.
- 학년 탭 초기 노출: 중1~3 전부 vs 세은 현재 학년(중2) 우선 강조? — 잠정 3탭 동시, 중2 강조.
- 도감/게임화 도입 시점 — P3, content가 당길 때.

## 6. 다음 액션 (다음 NCC 재개 트리거)
1. `C:\Kids\30_MiddleSchool`에서 세션 열기 → 이 `Mid_Science/00_PLAN.md` 읽기.
2. **P1 실행:** §3 P1 스텝대로 `github.io/mid-sci` 골격 + 중1 힘과 운동 하이브리드 카드 1개 → 배포.
3. 종료 로그 → `00_meta/sessions/`.

**불변 원칙:** 해요체(앱 콘텐츠) · 흥미≠점수(반드시 확인 3문항 착지) · speculative 금지(P1은 카드 1개) · 저작권 자료 복제 금지 · 사적 데이터 repo 밖.

---

## 7. 지구와 달 실험실 (2026-11-07 추가 · 수행평가 대응)
- 위치: `github.io/mid-sci/earth-moon/` (독립 모듈, mid-sci 카드 `m1-earth-moon`에서 진입).
- 파일: `em-draw.js`(렌더 API·천구 계산) · `em-lab.js`(5장 콘텐츠 SSOT+시뮬) · `em-game.js`(미션 게임) · `em-app.js`(라우터·백지 답안) · `em.css`.
- **v1 = 콘텐츠 우선판(완료).** 평가요소 5개 1:1, 모범답안·함정·게임·백지 체크리스트.
- **v2 = 시네마틱 그래픽 (예정).** 후보 방향:
  1. three.js 3D 씬(태양-지구-달 실제 조명, 카메라 컷: 우주 → 지구 표면 시점 전환).
  2. GSAP 타임라인 모션그래픽: 장마다 15~30초 인트로 시퀀스(타이포+카메라 무브).
  3. 일주운동 타임랩스(실사풍 하늘·은하수·지형 실루엣), 일식 코로나/다이아몬드 링 셰이더.
  4. 사운드 디자인·햅틱(정답/콤보). 성능: 폰 60fps 목표, 저사양 시 v1 Canvas로 폴백.
  - 교체 지점: `em-draw.js` API(moonPhase·skyTrails·earthTop·orbitScene) 유지 → 렌더러만 교체.
