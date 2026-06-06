<!-- 00_project_hub/plan/0604_buildsystem_and_skills.md -->
# Plan — 빌드 시스템 & 스킬 셋업 (0604)

> 워크플로우 셋업 세션(`session/260603_workflow_setup.md`)의 결정을 실행한 결과 + 다음 단계.
> 파일명 규칙: 이후 plan/session 파일은 **`mmdd_` 프리픽스**.

## 확정된 결정 (Nick: 모두 동의)
- 진행 방식 = **추출형**(템플릿 추출 → Ep02 실전 → 스킬 정련)
- 다음 에피소드 = **제국주의(B1, slug=`imperialism`)** — 거슬러 올라가기 첫 칸
- 스킬 저장 = 1차 **`.claude/skills/` 직접**(안정화 후 SSOT+sync 승격)
- 빌드 표준 = **frontend-design 플러그인** 활용

## 완료 (0603~0604)
- ✅ **디렉토리 재구성** (아래 구조)
- ✅ **빌드 시스템 추출**: `40_build/templates/episode.html`(렌더 엔진) + `40_build/build.py`(렌더러)
- ✅ **Episode Content Schema** 계약 문서 `10_docs/EPISODE_SCHEMA.md`
- ✅ **Ep01(ww2) 스키마화**: `30_content/ww2/episode.json` → 빌드 → `50_app/ww2/index.html` (JS OK·parity 통과) → 라이브 재배포 (`/history/ww2/` 200)
- ✅ **스킬 7개**(`.claude/skills/hist-*`) + **오케스트레이터**(`.claude/agents/hist-episode-orchestrator.md`)
  - `hist-app-build` = **validated**(ww2 재현), 나머지 = **seed**(Ep02에서 정련)

## 디렉토리 구조 (현재)
```
260602_History/
├── CLAUDE.md / README.md / APP_PRINCIPLES.md
├── .claude/
│   ├── skills/hist-{episode-plan,research,content-write,app-build,audit,deploy,distill}/SKILL.md
│   └── agents/hist-episode-orchestrator.md
├── 00_project_hub/
│   ├── plan/        (260602_, 260603_*, 0604_*)
│   ├── session/     (라운드 대화)
│   └── progress/    PROGRESS.md ← 추적 대시보드
├── 10_docs/         learner-profile, content-map_*, EPISODE_SCHEMA.md
├── 20_research/<slug>/   facts·perspective·people·videos·audit
├── 30_content/<slug>/    episode.json  ← Content Schema(데이터 SSOT)
├── 40_build/
│   ├── templates/episode.html   ← 렌더 엔진(디자인 1곳)
│   └── build.py                 ← JSON → 단일 HTML
├── 50_app/<slug>/index.html     ← 빌드 산출물(자기완결)
└── 90_video/        (영상, 추후)
```

## 파이프라인 한눈에
```
hist-episode-plan → hist-research → hist-content-write → hist-app-build → hist-audit → hist-deploy ( → hist-distill )
  content-map        20_research/      episode.json        50_app/<slug>     audit·수정    /history/<slug>/    개선
                         (오케스트레이터: hist-episode-orchestrator 가 자율 실행·게이트·기록)
```

## 다음 단계 (Ep02 = 제국주의)
1. `hist-episode-plan imperialism` → content-map (8섹션·비서구·렌즈·인물)
2. `hist-research imperialism` → 검증 자료 (아편전쟁·식민지 인도/아프리카/동남아·메이지·조선 포함)
3. `hist-content-write` → `30_content/imperialism/episode.json` (lens·people 본격 적용)
4. `hist-app-build imperialism` → 앱
5. `hist-audit` → 다중 페르소나 감수·수정
6. `hist-deploy imperialism` → `/history/imperialism/` + 허브 카드
7. 진행하며 각 스킬 seed→정련(추출형), 안정화 후 오케스트레이터 자율도 상향

## 비고
- 옛 단일 소스 `50_app/index.html` 제거(빌드 산출물 `50_app/ww2/`로 대체).
- ww2 메모 localStorage 키가 슬러그 기반(`ww2_m_*`)으로 변경 — 베타라 영향 미미.
- superpowers 플러그인 미설치(공식 마켓에 없음). 핵심 경로 불필요. 필요 시 마켓 추가 검토.
