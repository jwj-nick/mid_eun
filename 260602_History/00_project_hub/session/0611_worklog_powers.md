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

## Round 2 — 제작 완료 기록 (NCC, 0611)

**진행 순서와 실측 결과:**
1. ✅ [로컬] `30_content/powers/episode.json` — 5섹션 작성(섹션별 임시 JSON → 파이썬 조립·검증). 86KB, terms 16개, 전 섹션 deepdive 5. 커밋 `c027811`.
2. ✅ [로컬] people.json 21→25인 (victoria·cecil-rhodes·bismarck·leopold-ii).
3. ✅ [네트워크·단독] Commons API 검색 → 후보 목록 검토 → 8점 다운로드(PIL 리사이즈, q82):
   - 섹션: Imperial Federation map 1886(PD, 1600px)·파쇼다 1898 사진(PD)·Dropping the Pilot 1890(PD)·In the Rubber Coils 1906(PD)
   - 초상: 빅토리아(Bassano 1882)·로즈(Mills 사진)·비스마르크(Lenbach 유화 1890)·레오폴드 2세(Bassano 1889) — 전부 PD
   - **전 8점 육안 검수** — 파쇼다가 '만남 삽화'가 아닌 **마르샹 원정대 실사진**으로 판명 → image 블록 story/alt/caption 사실 교정 (자동선택 맹신 금지 교훈 재적용).
4. ✅ 게이트: G0 빌드 OK / G1 node --check를 **데이터 스크립트(window.EPISODE)와 엔진 스크립트 각각** 검사로 강화(기존 정규식이 속성 있는 script 태그를 놓치던 것 발견) / G2 이미지 참조 4:4 일치·JPEG 검증.
5. ✅ hist-audit (4 페르소나 인라인): 수정 2건 — 보어전쟁 흑인 희생 '수만'→'2만가량 추정', 비스마르크 발칸 경고 전언 표기. 기록 = `20_research/powers/audit.md`.
6. ✅ imperialism#why-empire에 companion 교차링크 추가 + 재빌드.
7. ✅ 허브 랜딩(배포 repo): 사이드바 EP03 + 흐름 밴드(유럽 열강 ↔ 제국주의) + EP03 카드.
8. ✅ 배포 repo 복사: powers/ + people/(25인) + imperialism/index.html.
9. ✅ 문서: PROGRESS·SERIES_ROADMAP 상태 갱신, plan §7 구현 기록·§8 개선 아이디어 6건 append.

**결정/교훈:**
- 콘텐츠 분량: 5섹션 86KB — imperialism(8섹션 ~110KB)보다 섹션당 밀도 높음. 나라별 파일 형식이라 deepdive가 자연스럽게 깊어짐. 적정.
- 벨기에 섹션 균형 설계: '수탈의 길(red) ↔ 진실을 전한 길(green)' 2국면 지도로, 어두운 이야기를 '폭로와 연대의 이야기'로 닫음 — 감성적 입구(딸 성향)와 무게의 균형.
- G1 강화 절차(데이터+엔진 분리 검사)는 다음 에피소드부터 표준으로.

## Round 3 — 배포·라이브 검증 (NCC, 0611, 실측)

| 항목 | 실측 결과 |
|---|---|
| 소스 push | `mid_eun` main `4c89611..2fafc00` ✅ (1차 push는 도구결과 손실 → 멱등 프로브로 미반영 확인 후 재시도 성공 — 프로토콜 C 작동) |
| 배포 push | `jwj-nick.github.io` main `126459c..c79bfbe` ✅ |
| 라이브 `/history/powers/` | 200 (캐시버스트 유한 폴링, 약 3분 내 전파) + HTML 내 비스마르크·rubber_coils 마커 확인 ✅ |
| 라이브 허브 `/history/` | EP03 카드 + 사이드바 03 표시 확인(WebFetch) ✅ |
| 라이브 자산 | `powers/img/rubber_coils_1906.jpg` 200·345KB / `people/bismarck/` 200 ✅ |

**URL**: https://jwj-nick.github.io/history/powers/ · 인물 도감 25인 https://jwj-nick.github.io/history/people/
**비고**: 커밋 2fafc00에 0608 plan 파일의 미커밋 Nick 코멘트 확정 기록(2줄)이 함께 포함됨 — 정상 세션 기록이라 유지.
**다음 후보**: powers 2차분(러시아·latecomers) 또는 `exploration`(대항해시대) 신규 — plan §8 개선 아이디어(도감 균형 인물·companion 배지·oldmap 라이트박스) 참조.

## Round 4 — 2차분 완성 (NCC, 0611, Nick 지시 "americas 이후 powers 2차분")
1. ✅ `russia`(40)·`latecomers`(60) 작성 — 섹션 삽입·벨기에 50 재배열·connect 사슬 재연결(독일→러시아→벨기에→후발)·홈 intro 갱신. **7/7 완성.**
2. ✅ 메넬리크 2세 도감 등재(38인) — '맞선 자' 축 보강(plan §8-1 아이디어 실행), 그 자신의 정복도 그림자로 명시.
3. ✅ [네트워크·단독] 자산 3점: 프로쿠딘-고르스키 카마강 철교(PD 컬러)·아도와 에티오피아 전통화(CC BY-SA 4.0 — '붓의 주인 교체' 해설)·메넬리크 어좌 사진(PD). 육안 검수.
4. ✅ audit 2차분(연도 교정 1건: 시베리아 동진 64년→약 57년). G1·G2 PASS.
5. 설계 노트: latecomers는 '후발 3국(독·이·일)→추축국' 패턴과 '아도와 예외'를 함께 닫는 에피소드 피날레 — "구조는 경향을 만들고, 선택이 결말을 가른다"로 종결. 미국 태평양 battlemap에 −360 경도 기법 재사용.
