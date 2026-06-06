---
name: hist-deploy
description: 빌드된 에피소드를 GitHub Pages(jwj-nick.github.io/history/<slug>/)에 배포하고 허브 카드를 갱신한 뒤 라이브를 검증한다. 호출 예시 — "/hist-deploy ww2", "제국주의 배포".
allowed-tools: Read, Write, Edit, Bash
metadata:
  project: 260602_History
  stage: 6 배포
  ssot: reference — jwj-nick.github.io 레포 /history/
  status: seed
---

# hist-deploy — 배포 (단계 6)

산출물(`50_app/<slug>/index.html`)을 Pages 레포로 복사·푸시하고 허브에 에피소드 카드를 추가.

## 사전
- Pages 레포: `C:/Nick/30_Apps/jwj-nick.github.io` (gh 인증된 jwj-nick)
- 계층: `/history/`=허브, `/history/<slug>/`=에피소드. (mid1에도 역사 링크 존재)

## 동작
0. **배포 전 빌드·검증 게이트(G0~G2) 통과 필수** — 아래 §검증 워크플로우.
1. `cp 50_app/<slug>/index.html  <repo>/history/<slug>/index.html`. **이미지 자산 있으면** `50_app/<slug>/img/` → `<repo>/history/<slug>/img/`도 복사.
1b. **인물 도감 v2**: `python 40_build/build_people.py` → **트리 전체 복사**(index + 인물별 `<slug>/` + `img/`): `rm -rf <repo>/history/people && cp -r 50_app/people/. <repo>/history/people/`.
2. **허브 카드**: `<repo>/history/index.html` 에피소드 목록에 카드 삽입/갱신.
3. **변경 파일만** 스테이징·커밋·푸시. **무관 변경(mid1/map 등) 금지.** 커밋 푸터 `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
4. **라이브 검증(G3)** — 아래.

## 검증 워크플로우 (★공식 게이트 — 0606 정식화)
> 원칙: **추론 금지, 실측만.** 매 게이트는 명령 출력으로 통과를 확인한다.

- **G0 빌드 무오류**: `python 40_build/build.py <slug>` 정상 종료(에러 0). 인물 도감은 `build_people.py`.
- **G1 JS_OK(엔진 변경 시 필수)**: 템플릿에서 가장 큰 `<script>` 추출 → `/*__EPISODE_DATA__*/ null`을 스텁 객체로 치환 → `_chk.js`로 저장 → `node --check _chk.js` → `rm _chk.js`. (런타임 렌더가 깨지지 않음을 정적 확인)
- **G2 자원 검증(데이터 추가 시)**:
  - **외부·위키 링크는 반드시 실제 200**: `curl -s -o /dev/null -w '%{http_code}' -L "<url>"`. **추측 ID 금지**(encykorea 오링크 사고 — 추측 article ID가 엉뚱한 글이었음). 죽거나 틀린 링크는 배제.
  - **이미지 직접 URL**: Wikipedia REST summary API(`/api/rest_v1/page/summary/<제목>`의 `originalimage.source`). 다운로드 후 `file <img>`로 JPEG/PNG/WebP 실물 확인.
  - **한국어 위키 제목**: en→ko 언어링크 API(`/w/api.php?action=query&prop=langlinks&lllang=ko&titles=<EN>`)로 정확 제목 확보(한글 경로는 브라우저 OK, 데이터엔 퍼센트 인코딩 권장).
- **G3 라이브 검증**: Pages 빌드 지연 대비 **대기 루프** →
  `until [ "$(curl -s -o /dev/null -w '%{http_code}' "<url>?cb=$RANDOM")" = "200" ] || [ $n -ge 18 ]; do n=$((n+1)); sleep 5; done`
  통과 후: 페이지 + **이미지 자산** 200, 핵심 문자열·신규 데이터 spot-check(캐시버스트 `?cb=$RANDOM`).

## 출력
- 라이브 URL `https://jwj-nick.github.io/history/<slug>/` (+ `/history/people/`) + 허브 갱신

## 품질 게이트
- [ ] G0 빌드 무오류 / G1 JS_OK(엔진 변경 시)
- [ ] G2 링크 200·이미지 실물·ko 제목 검증(추측 금지)
- [ ] G3 라이브 200(페이지+이미지) + 신규 데이터 spot-check
- [ ] 무관한 변경 미포함(커밋 범위 점검)
