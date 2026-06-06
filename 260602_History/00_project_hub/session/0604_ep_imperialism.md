<!-- 00_project_hub/session/0604_ep_imperialism.md -->
# Session — Ep02 제국주의 제작 (0604)

> 파이프라인: plan→research→write→build→audit→deploy. seed 스킬 정련하며 진행(추출형).

## Round 0 — 착수
- 기획: `10_docs/content-map_imperialism.md` (8섹션, 비서구·렌즈·인물 분산)
- 단계 1 plan ✅ → 단계 2 research 병렬 착수(팩트체크 / 유튜브 / 관점·인물·인용)
- 결과 누적: `20_research/imperialism/`

### 진행 로그
- [x] plan (content-map)
- [x] research — ⚠️ 병렬 1/3만 발사됨(유튜브만). 팩트/관점은 NCC 지식+audit로 대체.
- [x] write (episode.json, 8섹션 + 인물 5 + 렌즈 2)
- [x] build (JS OK, parity)
- [x] audit (fact-check 에이전트: **치명 오류 0**, 3건 정밀화 패치 적용)
- [x] deploy → https://jwj-nick.github.io/history/imperialism/ (200) + 허브 Episode 02 카드

### audit 패치 (0604)
1. 락슈미바이 인용 = 검증된 직접발언 아님 → '전해진다'로 표기, 나이 스물아홉 명시
2. 임칙서 편지 = 빅토리아 여왕에 미전달 → "썼다"; 좌천 → 신장 유배(희생양)
3. 베를린회담 = "모든 국경을 자로" 과장 완화; 아프리카 갈등 "한 원인"

### 추출형 회고 (스킬 정련 메모)
- ⚠️ **병렬 에이전트 실전 교훈**: 한 메시지에 Agent 3개를 의도했으나 1개만 실제 호출됨 → `hist-research`/오케스트레이터에 "리서치 에이전트 N개를 반드시 한 메시지에 동시 발사, 누락 검증" 명시 필요.
- ✅ 빌드 파이프라인(JSON→템플릿) Ep02에서도 무수정 동작 — `hist-app-build` validated 재확인.
- ✅ lens/people 스키마 실전 검증(인물 quote 선택 필드 정상).

### 다음
- Nick/딸 리뷰 → 검색링크(🔍 2개: 아프리카·인도 한국어) 특정 영상 핀 교체
- `hist-distill`로 위 교훈을 스킬 body에 반영
