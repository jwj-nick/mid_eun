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
1. `cp 50_app/<slug>/index.html  <repo>/history/<slug>/index.html`. **이미지 자산 있으면** `50_app/<slug>/img/` → `<repo>/history/<slug>/img/`도 복사(S1 image 블록).
1b. **인물 도감**: `python 40_build/build_people.py` → `cp 50_app/people/index.html <repo>/history/people/index.html` (인물 늘면 갱신, S6).
2. **허브 카드 추가**: `<repo>/history/index.html`의 에피소드 목록에 새 카드(Episode NN, 제목, 설명, `→ <slug>/`) 삽입. 다음 에피소드 "준비 중" 블록은 유지/갱신.
3. **그 에피소드 파일만** 스테이징·커밋·푸시 (`git add history/<slug>/index.html history/index.html`). **다른 미커밋 변경(예: mid1/map) 건드리지 않기.**
4. 검증: Pages 빌드 후 `curl -o /dev/null -w %{http_code}` = 200, `<title>`·핵심 문자열 확인.

## 출력
- 라이브 URL `https://jwj-nick.github.io/history/<slug>/` + 허브 갱신

## 품질 게이트
- [ ] 에피소드 URL 200 + 제목 정상
- [ ] 허브 카드에서 진입 동작
- [ ] 무관한 변경 미포함(커밋 범위 점검)
