---
name: hist-episode-plan
description: 역사 허브의 새 에피소드(시리즈)를 기획한다. 시리즈 정체성·8섹션 아웃라인·인물 섹션 대상·"그때의 생각" 렌즈 포인트·slug를 정하고 폴더를 scaffold한다. 호출 예시 — "/hist-episode-plan imperialism 제국주의", "에피소드 냉전 기획".
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion
metadata:
  project: 260602_History
  stage: 1 기획
  ssot: 00_project_hub/plan/260603_history_hub_master_plan.md
  status: seed
---

# hist-episode-plan — 에피소드 기획 (단계 1)

마스터플랜(§1~9)을 기준으로 한 에피소드의 설계도를 만든다.

## 입력
- slug(영문, kebab) + 주제(예: `imperialism` "제국주의와 19세기")
- 마스터플랜의 해당 시리즈 행(BACKWARD/FORWARD/주제), learner-profile, APP_PRINCIPLES

## 동작
1. 마스터플랜·content-map 읽고 시리즈 정체성 1줄 확정.
2. **8섹션 아웃라인** 작성: 각 섹션 id/num/label/kicker/era/motif/핵심질문 + 이전·다음 연결.
3. **비서구·약소국 포인트**와 **`lens`("그때의 생각")** 후보를 섹션별로 명시(마스터플랜 §9-1,2 의무).
4. **"꼭 알아야 할 인물"** 대상 선정(섹션별 또는 에피소드 공통, 비서구 비중 의식).
5. 리서치가 필요한 항목(팩트체크 대상·인물·인용·유튜브 키워드) 목록화 → 단계 2로 전달.
6. scaffold: `30_content/<slug>/`, `20_research/<slug>/` 생성, `content-map_<slug>.md` 기록.

## 출력
- `10_docs/content-map_<slug>.md` (8섹션 설계 + 인물 + 렌즈 + 리서치 To-Do)
- 빈 `30_content/<slug>/`, `20_research/<slug>/`

## 품질 게이트
- [ ] 8섹션이 "하나의 흐름"으로 이어지나(connect 사슬)
- [ ] 비서구·약소국 관점이 최소 2개 섹션 이상
- [ ] 렌즈/인물 후보가 명시됐나
- [ ] 논쟁 주제는 "균형 서술" 표시
