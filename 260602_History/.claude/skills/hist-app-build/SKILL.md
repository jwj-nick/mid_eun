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
2. **검증(G1 JS_OK)**:
   - **엔진(템플릿) 변경 시**: 템플릿에서 가장 큰 `<script>` 추출 → `/*__EPISODE_DATA__*/ null`을 스텁 객체로 치환 → `node --check`(상세 = hist-deploy §검증 G1). 새 블록 렌더 함수(movies·relations·voice 등)는 반드시 이 게이트 통과 후 배포.
   - 데이터 인라인은 런타임 렌더 → 신규 블록은 **그 데이터가 들어간 섹션이 실제로 렌더되는지** 핵심 문자열 grep으로 확인.
   - 핵심 문자열 grep(섹션 라벨·영상 ID·인용·신규 블록 데이터) 존재 + JSON↔렌더 섹션 수 일치.
3. 새 `motif`·구성요소가 필요하면 템플릿(`MOTIF`/엔진)에 추가 후 재빌드(전 에피소드 호환 유지).

## 출력
- `50_app/<slug>/index.html`

## 품질 게이트
- [ ] build 무오류 + JS_SYNTAX_OK
- [ ] 섹션/영상/인용 문자열 존재(parity)
- [ ] 모바일(사이드바 햄버거)·툴팁·메모저장 동작 (frontend-design 기준 점검)

## 플러그인
- 비주얼 개선·접근성 점검 시 **frontend-design** 플러그인 활용(빌드 표준).
