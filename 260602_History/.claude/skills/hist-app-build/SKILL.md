---
name: hist-app-build
description: Episode Content Schema(episode.json)를 표준 템플릿으로 렌더해 자기완결형 단일 HTML 앱을 만든다. 사이드바·시대색 히어로·용어 툴팁·읽기 진행바·메모 자동저장 포함. 호출 예시 — "/hist-app-build ww2", "제국주의 앱 빌드".
allowed-tools: Read, Write, Bash, Edit
metadata:
  project: 260602_History
  stage: 4 앱 빌드
  ssot: 40_build/build.py, 40_build/templates/episode.html
  status: validated   # Ep01(ww2) 재현 검증 완료 (2026-06-04)
---

# hist-app-build — 앱 빌드 (단계 4)

데이터(JSON) → 단일 HTML. **템플릿이 렌더 엔진** — 디자인/버그 수정은 템플릿 1곳, 재빌드로 전 에피소드 전파.

## 입력
- `30_content/<slug>/episode.json` (단계 3)
- 엔진: `40_build/templates/episode.html` (CSS+JS, `MOTIF` 라이브러리, `window.EPISODE` 소비)

## 동작
1. 빌드: `python 40_build/build.py <slug>` → `50_app/<slug>/index.html` (자기완결, 더블클릭/Pages 모두 동작).
2. **검증**:
   - 생성 HTML의 `<script>` 추출 → `node --check` 통과.
   - 핵심 문자열 grep(섹션 라벨·영상 ID·인용) 존재 확인.
   - JSON↔렌더 섹션 수 일치.
3. 새 `motif`·구성요소가 필요하면 템플릿(`MOTIF`/엔진)에 추가 후 재빌드(전 에피소드 호환 유지).

## 출력
- `50_app/<slug>/index.html`

## 품질 게이트
- [ ] build 무오류 + JS_SYNTAX_OK
- [ ] 섹션/영상/인용 문자열 존재(parity)
- [ ] 모바일(사이드바 햄버거)·툴팁·메모저장 동작 (frontend-design 기준 점검)

## 플러그인
- 비주얼 개선·접근성 점검 시 **frontend-design** 플러그인 활용(빌드 표준).
