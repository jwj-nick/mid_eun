# 00_GUIDE — 이 폴더 사용 설명서

> **목적**: 이 폴더를 처음 여는 사람(또는 새 Claude 세션)이 어떤 파일을 어떤 순서로 읽고 무엇을 해야 하는지 알려준다.
> **최종 업데이트**: 2026-05-05

---

## 1. 프로젝트 한 줄

중1 딸을 위해 중1 수학 단원을 **인물 이야기 + 수학 언어 메타 학습 + 인터랙티브 도구 + 문제 연습**으로 체계적으로 구성하는 학습 시스템.

핵심 (절대 잊지 말 것):
- **우선순위**: (a) 흥미·이해·자신감 > (b) 기본 문제 실전력 > (c) AI 경험
- **4축 구조**: A.개념이해 / B.흥미유발 / C.수학언어 / D.문제연습
- **작업 방식**: `00_project_hub/chatlog/` 파일에서 라운드 기반 대화
- **딸의 결정적 사례**: `y=a/x, a=-2` 일 때 `y=-2/x` 로 못 씀 → 축 C 발견 계기

---

## 2. 새 Claude 세션 시작 시

**CLAUDE.md를 읽으면 충분합니다.** CLAUDE.md가 전체 구조·원칙·스킬 목록을 담고 있음.

추가 맥락이 필요할 때:

| 순서 | 파일 | 내용 |
|---|---|---|
| 1 | `CLAUDE.md` | 전체 구조, 원칙, 스킬, 파이프라인 |
| 2 | `10_docs/01_learner-profile.md` | 딸이 누구인지 |
| 3 | `10_docs/02_concept.md` | 인물 서사 5단계 흐름 |
| 4 | `10_docs/03_literacy-track.md` | 수학 언어 트랙 L1~L7 |

---

## 3. 디렉토리 구조

```
260426_MathTelling_Idea/
├── CLAUDE.md                     ← Claude 진입점 (가장 중요)
├── APP_PRINCIPLES.md             ← HTML 앱 디자인 원칙
├── 00_GUIDE.md                   ← 이 파일
├── 01_README.md                  ← 비전·구조
├── 00_project_hub/
│   ├── chatlog/                  ← 라운드 기반 대화 (핵심 작업 방식)
│   ├── plan/                     ← current-plan.md
│   └── history/                  ← 의사결정 기록
├── 01_dev_study/                 ← Nick의 개발 학습 (앱, 영상 제작)
├── 10_docs/                      ← 핵심 문서
├── 20_research/                  ← Deep research 결과
├── 40_BaseDocs/                  ← 13단원 개념 뼈대 + 수학 언어 (참조 자료)
│   ├── 00_literacy/              ← 수학 언어 트랙 L1~L7 (단원 횡단)
│   └── 01_소인수분해/ ~ 13_*/    ← 단원별 개념 MD
└── 50_units/                     ← 단원별 통합 작업 디렉토리
    ├── 01_소인수분해/
    │   ├── index.html           ← 단원 허브 ⭐ (Solution B: app/ 서브폴더 없음)
    │   ├── story.html           ← 인물 서사 인터랙티브
    │   ├── concepts.html        ← 개념 탐구 인터랙티브
    │   ├── story/               ← 인물 서사 텍스트 .md
    │   ├── video/               ← 영상
    │   ├── problems/            ← basic_app, type_*, deep_* HTML + types.md 등
    │   └── feedback/            ← 딸의 글 (수정 금지)
    └── 02~13_*/
```

---

## 4. 작업별 참조

| 작업 | 참조 파일 |
|---|---|
| 단원 제작 시작 | `/unit-plan` 스킬 실행 |
| 개념 검수 | `/concept-review` + `40_BaseDocs/` |
| 인물 서사 | `/story-write` + `20_research/02_R2-people-map.md` |
| 문제·오답 | `/math-error-note` + `/math-practice` |
| 앱 품질 | `app-reviewer` 에이전트 + `APP_PRINCIPLES.md` |
| 영상 | `/video-make` + `50_units/NN/video/` |
| 의사결정 기록 | `00_project_hub/history/01_project-genesis.md` |

---

## 5. 현재 진행 상황 (2026-05-05 기준)

**완료**
- Setup: CLAUDE.md, APP_PRINCIPLES.md, .claude/ 스킬 6개 + 에이전트 2개
- 40_BaseDocs: 13단원 x 42개 개념 MD 뼈대 + 00_literacy/L2 완성
- 50_units/: 단원별 통합 구조 확정 (01~04 디렉토리)
- Unit 1 시범: 이야기·앱·영상 → `50_units/01_소인수분해/` 통합 완료 (딸 미사용)

**진행 중**
- 5월: Ch1(소인수분해)~Ch4(일차방정식) 자료 완성
- 6월: 딸과 본격 시작

---

## 6. 절대 원칙

1. **(a) > (b) > (c)** 순서.
2. 페이스: 단원 1개 = 2~3주. 진도보다 깊이.
3. `60_her-writings/` 딸 글은 임의 수정 금지.
4. 4축 모두 운영.
5. 빈칸·미완성을 의도적으로 남겨라.
6. chatlog/ 파일 기반 대화. 주요 결정은 파일에 기록.
