# 2026-07-20 · mid-sci 계획 수립

- **한 일:** 중학 과학 앱(mid-sci) 마스터 플랜 저작 (`00_PLAN.md`). 환경 탐색으로 재사용 자산 매핑(math concept.js·chem-card SVG·history 도감·배포 포털·figcrop).
- **Nick 확정 3결정:** ① 단일 앱+학년탭(중1/2/3) ② 하이브리드 슬라이스(PhET+네이티브 SVG) ③ P1 앵커=중1 힘과 운동(forces-and-motion-basics + 자유물체도 SVG).
- **P2 자율개선:** `Mid_Science`를 과학 저작 홈(SSOT)으로 골격화(00_meta/·docs/). 기존 seeun-sci-phet.md 계획을 하이브리드 3-모드로 구체화.
- **P1 실행·배포 완료(같은 세션):** `github.io/mid-sci` 앱 신규 — 학년탭(중1/2/3) 2D 랜딩 + **16개 개념**(PhET 14·영상후크 2·**하이브리드 2**). 3-모드 시뮬(PhET iframe/딥링크 · 네이티브 SVG `자유물체도`+`보어 원자모형/이온` · 정직 후크) + 예측/확인/문제착지/한줄암기. 무빌드 바닐라, content.js SSOT, 라이트·다크.
  - 검증(실측): content.js 데이터 무결성 PASS(16개념) + DOM 스텁 하니스로 렌더 경로 5종 무예외 + SciSVG(freebody·bohr) 실제 마운트 확인. 버그 1개(하이브리드 네이티브 미렌더) 발견·수정.
  - 커밋: github.io `3fa7d82`, mid_eun(플랜) `f39e68c`. 배포: Pages 빌드 완료(commit 3fa7d82). 라이브=https://jwj-nick.github.io/mid-sci/ . 포털 카드 등록.
- **다음 액션(P2):** `content.js`를 §2 매핑 순서로 확장(개념당 hook/predict/confirm/draw) + 네이티브 렌더러는 필요할 때 증식(예: 회로 기호도·에너지 막대). ⚠️ 브라우저 확장 미연결로 시각 스크린샷은 못 함 → 다음 세션에서 실제 폰/브라우저로 iframe 로드·인터랙션 한 번 눈으로 확인 권장.
