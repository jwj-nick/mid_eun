<!-- 00_project_hub/session/0611_worklog_powers.md -->
# 0611 — Worklog: `powers` 허브(유럽 열강 열전) 자율 제작

> Nick 지시(0610): "compact 이후 실제 다음 만들 허브(유럽 열강)를 자율진행. worklog 파일 하나 남기고, 앞서 완성했던 hub page 수준으로. 진행하며 개선 아이디어는 기존 plan 파일에 append."
> 계획 SSOT: `plan/0610_plan_hub_powers.md` · 구조 SSOT: `10_docs/SERIES_ROADMAP.md`

## Round 1 — 착수·범위 확정 (NCC)

**1차 릴리스 범위 (plan §1·§4 그대로):**
- 섹션 5개: `overview`(도입·선발vs후발) → `britain`(영국) → `france`(프랑스) → `germany`(독일) → `belgium`(벨기에/콩고)
- 신규 인물 4명: 비스마르크 · 세실 로즈 · 레오폴드 2세 · 빅토리아 (도감 21→25인)
- 러시아·후발주자(latecomers)는 2차분으로 보류 (plan 명시)

**품질 기준 = 완성 허브(ww2·imperialism) 동일:**
- 섹션마다: hook·why·(lens)·cards·timeline·connect·yt·quiz·reflect + **image(PD/CC 실물)** + **voice** + **deepdive 5** + **chart/relations/oldmap·battlemap** + order
- 균형 원칙: 침탈 구조와 피해의 존엄 함께(특히 벨기에/콩고·독일/헤레로), 잔혹 직접묘사 절제, 중1 입구+deepdive 고등 깊이

**작업 순서 (네트워크 격리 프로토콜 준수):**
1. [로컬] episode.json 5섹션 전체 초안 (이미지 placeholder, yt는 기검증 ID 재사용+search형)
2. [로컬] people.json 4인 추가 (초상 placeholder) → 로컬 커밋
3. [네트워크·단독] Commons API 이미지 소싱(섹션 6장 내외+초상 4장) + WebSearch/oembed로 yt 신규 검증
4. [로컬] 이미지 연결·빌드(G0 빌드, G1 node --check, G2 이미지/참조) + hist-audit 셀프 패스
5. [로컬] 허브 카드(EP03)·imperialism 교차링크 → 커밋
6. [네트워크·단독] 소스 push → 배포 repo 복사·push → 라이브 검증
7. 문서 마감: plan에 개선 아이디어 append, SERIES_ROADMAP·PROGRESS 상태 갱신

**결정 사항:**
- slug = `powers`, 경로 `/history/powers/` (SERIES_ROADMAP 허브 4)
- 에피소드 번호 = **EP 03** (허브 랜딩 카드·사이드바)
- 시대색(accent): 나라별로 구분 — 도입 #5a5a7a(강철 청회), 영국 #7a3a4a(버건디), 프랑스 #3a5a7a(청), 독일 #555f66(철회색), 벨기에 #6b4a2a(고무 갈색) — 엔진 accent 필드만으로 적용 가능
- imperialism과 companion: powers 각 섹션에서 imperialism 해당 섹션으로 교차링크(연결문), imperialism#why-empire connect에 "나라별로 더 보기 →" 1줄 추가

(진행하며 라운드 append)
