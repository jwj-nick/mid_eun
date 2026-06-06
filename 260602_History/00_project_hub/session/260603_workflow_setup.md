<!-- 00_project_hub/session/260603_workflow_setup.md -->
# Session — 워크플로우/스킬 셋업 (2026-06-03)

> 목적: "에피소드 1개 만들기"를 (0) 세부 작업 → (1) 스킬(AgentSkill 스펙) → (2) 스킬을 엮는 공식 워크플로우(오케스트레이터)로 정리.

## Round 0 — NCC 평가 + 설계 제안

### A. Nick 제안에 대한 평가 (창의·비판)

**동의하는 점**
- 스킬-우선 접근 맞음. math-story-telling(mst)이 이미 증명: **SSOT 스킬 + 오케스트레이터 에이전트 + sync 스크립트** 구조가 양산에 강함.
- 플러그인 적극 활용도 좋음 — 특히 **frontend-design(이미 설치됨)** 은 앱 비주얼 품질에 직접 도움.

**비판적 개선 아이디어 (중요)**
1. **스킬을 추측으로 미리 다 만들지 말 것 (YAGNI).** Ep01(세계대전)은 스킬 없이 한 번에 잘 나왔다. mst도 스킬을 *exp-002 실제 실행을 reverse-engineering* 해서 만들었다. → **"추측형"이 아니라 "추출형"**: Ep02를 반쯤 수동으로 만들면서 *반복되는 단계*를 그때 스킬로 굳힌다. 첫 실전 빌드가 곧 스킬 명세의 출처.
2. **스킬(재사용 절차) ≠ 오케스트레이터(워크플로우).** mst처럼 분리: 단계별 스킬 + 그걸 엮는 에이전트 1개. 단, 역사는 영상처럼 외부 API 체인이 아니라 **콘텐츠 파이프라인**이라 스킬 수가 적다(영상 8 STEP → 역사 6단계면 충분). 영상 API 스킬(이미지·TTS)은 *영상 단계 시작할 때* 추가(지금은 보류).
3. **가장 큰 레버리지 = "콘텐츠 스키마 + 템플릿 렌더링".** Ep01 앱의 `SECTIONS` 데이터 구조를 **Episode Content Schema(계약)** 로 고정하고, 빌드 스킬은 *그 데이터 → 표준 템플릿 SPA* 로 찍어낸다. 효과:
   - 작성(write)과 렌더(build)를 **분리** → 일관성·속도.
   - 템플릿(WWII 앱)이 **버전 관리되는 "렌더 엔진"** 이 됨 → 버그 수정/디자인 개선이 *모든 에피소드에 전파*.
   - 같은 스키마에서 나중에 **영상 대본·퀴즈** 까지 파생 생성 가능.
4. **감수(audit)는 다중 페르소나로.** mst의 se-audit-* 처럼, 역사 허브 편집 원칙(탈서구중심·"그때의 생각" 렌즈·논쟁 균형·수위·출처)을 *명시적 체크*로 박은 **다중 페르소나 감수 스킬**.
5. **SSOT/sync는 처음엔 가볍게.** mst는 `10_system/30_skills`(SSOT)→`sync-skills.sh`→`.claude/skills`로 운영. 강력하지만 무겁다. → **1차는 `.claude/skills/`에 직접** 만들고, 스킬이 안정되면 SSOT+sync로 승격.
6. **플러그인 레버리지(구체)**: 앱 빌드=frontend-design, 리서치=deep-research 스킬/병렬 에이전트, 인간 결정(slug·인물 선정)=AskUserQuestion. (superpowers는 미설치 — 필요 시 마켓 추가 검토. 핵심 경로엔 불필요.)

---

### 0. 에피소드 1개 제작 — 세부 작업 (워크플로우 단계)

Ep01 경험 + 마스터플랜 기준. **(괄호)=산출물.**

| # | 단계 | 세부 할 일 | 산출물 |
|---|---|---|---|
| 1 | **기획/스코프** | 시리즈 정체성, 8섹션 아웃라인, 인물 섹션 대상 선정, 비서구·"그때의 생각" 렌즈 포인트, slug 확정, 폴더 scaffold | `content-map(에피소드).md`, `30_content/<slug>/` |
| 2 | **리서치·팩트체크** | (병렬) 날짜·인명 검증 / 비서구·약소국 관점 보강 / 논쟁 균형 가이드 / 인물 자료 / 인용문 저작권 안전 발췌 / 유튜브 실제 영상(한·영) 큐레이션 | `20_research/<slug>/*.md` (출처 포함) |
| 3 | **콘텐츠 작성** | 섹션별 hook·why·cards·timeline·connect·yt·reflect + **인물 섹션** + **"그때의 생각" 렌즈** + 용어 풀이(terms) → 스키마 데이터로 | `episode.json`(Content Schema) |
| 4 | **앱 빌드** | 스키마 → 표준 템플릿 SPA(단일 HTML): 사이드바·시대색·툴팁·진행바·메모저장. (frontend-design 활용) | `50_app/<slug>/index.html` |
| 5 | **감수(audit)** | 다중 페르소나: ①역사학자=사실 ②교사=수위·톤·눈높이 ③균형심판=탈서구·논쟁 ④편집자=APP_PRINCIPLES·접근성. 위반 수정 | audit 리포트 + 수정 반영 |
| 6 | **배포** | `/history/<slug>/` 복사, 허브 카드 추가, (필요시 mid1 링크), Pages 200 검증 | 라이브 URL |
| 7 | **기록·회고** | session 기록, learner-profile 업데이트(딸 반응), 인물 갤러리 색인 갱신, insight 누적 → 원칙/템플릿 개선 | session/insight |
| (8) | **영상(선택)** | 스키마에서 대본 뼈대 추출 → mst 영상 프로세스 차용(`90_video/`) | mp4 |

---

### 1. 스킬 셋업 (AgentSkill 스펙 준수)

규칙: 폴더명=name(lowercase-hyphen), `SKILL.md` frontmatter에 `name`/`description`(3인칭·트리거 풍부)/`allowed-tools`/`metadata`. 접두사 **`hist-`**.

| 스킬 | 단계 | 역할 | 비고 |
|---|---|---|---|
| `hist-episode-plan` | 1 | 시리즈/에피소드 8섹션 설계 + scaffold | mst `se-unit-plan` 대응 |
| `hist-research` | 2 | 병렬 리서치(팩트체크·비서구 보강·유튜브 큐레이션·인물·인용) | Ep01에서 검증한 3-에이전트 패턴 |
| `hist-content-write` | 3 | research → **Episode Content Schema** 작성 | 핵심 계약 산출 |
| `hist-app-build` | 4 | 스키마 → 표준 템플릿 SPA 렌더 | 템플릿=렌더 엔진, frontend-design |
| `hist-audit` | 5 | **다중 페르소나 감수**(사실/수위/균형/원칙) | mst `se-audit-*` 통합판 |
| `hist-deploy` | 6 | `/history/<slug>/` 배포 + 허브 카드 갱신 + 검증 | |
| `hist-distill` | 7 | insight 누적 → 원칙/템플릿 개선 | mst `se-distill-principles` 차용 |

> **공유 자산**: `Episode Content Schema`(SSOT) — `SECTIONS[]`(섹션·카드·타임라인·yt·reflect) + `people[]`(인물 카드) + `terms{}`(용어) + `lens[]`("그때의 생각"). write가 생산, build·(추후)영상·퀴즈가 소비.
> **표준 템플릿**: Ep01 `index.html`을 `templates/episode.html`(데이터 주입형)로 일반화 → 모든 에피소드 공통 렌더 엔진.

---

### 2. 공식 워크플로우 = 오케스트레이터 에이전트

`hist-episode-orchestrator` (agent): **"에피소드 <slug> 만들어"** 한 줄 →
`plan → research → write → build → audit → deploy` 자율 실행, 각 단계 후 **품질 게이트**(실패 시 재시도/격리), 진행을 `session/`에 기록. **batch**(여러 에피소드)·**rate-limit 인식** 지원. (mst `se-*-orchestrator` 모델)

```
[plan] → content-map ─▶ [research] → 검증자료 ─▶ [write] → episode.json
   ─▶ [build] → SPA ─▶ [audit] (게이트) ─▶ [deploy] → 라이브 ─▶ [distill] → 개선
```

---

### B. 권장 진행안 (추출형)

1. **표준 템플릿 추출**: Ep01 `index.html` → `templates/episode.html` + `episode.json`(Ep01을 스키마로 역추출). *Ep01이 그대로 재현되는지* 검증.
2. **Ep02(제국주의 or 냉전)를 이 스키마로 반쯤 수동 제작** → 그 과정에서 `hist-research`/`hist-content-write`/`hist-app-build`/`hist-audit`를 **실제 단계에서 추출**해 작성.
3. 스킬 안정화 후 `hist-episode-orchestrator`로 묶고, `hist-deploy`/`hist-distill` 추가.
4. 스킬이 굳으면 SSOT(`10_system`)+sync로 승격(선택).

---

### Nick에게 질문
- Q1. 진행 방식: **추출형(B안: 템플릿 추출 → Ep02 실전 → 스킬화)** 동의? 아니면 스킬부터 풀로?
- Q2. 첫 스킬화 대상 에피소드: **제국주의(B1)** vs **냉전(F2)**?
- Q3. 스킬 저장: 1차 `.claude/skills/` 직접 vs 바로 mst식 SSOT+sync?
- Q4. frontend-design 플러그인을 빌드 단계 표준으로 채택? (추천: 예)

---

## Round 1 — Nick 답변 + 시스템 구축 (0604)

**Nick:** "모두 동의 및 yes. 계획대로 자율진행. 세션·플랜 파일로 추적 쉽게, 파일명 `mmdd_` 프리픽스, 디렉토리 깔끔하게."
→ Q1 추출형 ✅ / Q2 **제국주의(imperialism)** ✅ / Q3 `.claude/skills/` 직접 ✅ / Q4 frontend-design ✅

**NCC 실행 (완료)**
- 디렉토리 재구성(40_build·30_content/<slug>·50_app/<slug>·progress; 빈 placeholder 정리)
- 빌드 시스템 추출: `40_build/templates/episode.html`(엔진) + `build.py` + `10_docs/EPISODE_SCHEMA.md`
- Ep01 스키마화: `30_content/ww2/episode.json` → 빌드 → `50_app/ww2/index.html`(JS OK·parity) → `/history/ww2/` 재배포(200)
- 스킬 7개(`.claude/skills/hist-*`, app-build=validated 나머지 seed) + 오케스트레이터(`.claude/agents/hist-episode-orchestrator.md`)
- 추적: `plan/0604_buildsystem_and_skills.md`, `progress/PROGRESS.md`

**다음:** Ep02 `imperialism` 제작(추출형으로 seed 스킬 정련). 상세 = `plan/0604_*` §다음 단계.

### 다음 라운드 대기
"제국주의 에피소드 만들어" 하면 파이프라인 착수.
