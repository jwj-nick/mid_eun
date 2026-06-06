---
name: hist-distill
description: 에피소드 제작·딸 반응에서 얻은 교훈을 모아 원칙/템플릿/스킬을 개선한다. learner-profile·APP_PRINCIPLES·템플릿 엔진·스킬 seed를 정련한다. 호출 예시 — "/hist-distill", "/hist-distill ww2 회고".
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  project: 260602_History
  stage: 7 회고·정련
  ssot: math-story-telling se-distill-principles 차용
  status: seed
---

# hist-distill — 회고·정련 (단계 7)

한 에피소드(또는 누적분)에서 패턴을 추출해 시스템을 개선. mst `se-distill-principles` 모델.

## 입력
- 해당 에피소드 audit·session, 딸 feedback(`*/feedback/`, 수정금지·읽기만), insight 누적분

## 동작
1. 무엇이 잘됐고/막혔는지 패턴화(흥미 포인트, 지루 포인트, 사실·톤 이슈, 빌드 마찰).
2. 반영 위치 결정:
   - 딸 반응 → `10_docs/01_learner-profile.md` 관찰 기록 추가.
   - 톤·구성 교훈 → `APP_PRINCIPLES.md`.
   - 렌더·구성요소 → `40_build/templates/episode.html`(+재빌드 전파).
   - 절차 교훈 → 해당 `hist-*` 스킬 seed 정련(status 갱신).
3. 다음 에피소드 우선순위 갱신(마스터플랜 §8 로드맵).

## 출력
- 갱신된 원칙/프로필/템플릿/스킬 + `00_project_hub/progress/` 회고 노트

## 품질 게이트
- [ ] 교훈이 "재사용 가능한 형태"로 반영됐나(다음 에피소드가 덕 보나)
- [ ] 딸 글 원본 미수정(읽기만)
