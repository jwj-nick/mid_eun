<!-- 00_project_hub/session/0615_scitech_build_worklog.md -->
# WORKLOG — tracks/sci-tech 제작 (★ 압축 생존용 단일 진실)

> **이 파일을 먼저 읽으면 어느 NCC 세션이든 "여기서 이어서" 가능.** compact 후 품질 유지의 핵심.
> 계획 SSOT = `plan/0615_plan_track_scitech.md`. 스키마 = `10_docs/EPISODE_SCHEMA.md`. 프로토콜 = `CLAUDE.md`(인코딩·네트워크·cwd·이미지검수).
> 갱신 규칙: **매 작업 단위 끝에 체크박스 갱신 + 맨 아래 로그에 1줄.** 추측 아닌 실측만.

## 🎯 목표 한 줄
9정거장 과학기술 통사 SPA(`/history/tracks/sci-tech/`) + `tracks/` 5칸 랜딩. 中1 본문 + (Nick검수) codec/NPU deepdive 척추.

## ✅ Nick 확정 (0615)
9정거장(화학·의학 추가) / codec deepdive=NCC초안→Nick검수(a) / AI수위 보수성↓ / 랜딩 지금 5칸 / 이 세션 B부터 자율.

## ⚡ 방향 전환 (0615 #2 — Nick) ★★ 중대
- **sci-tech 트랙 대상 수위: 中1 → 고등학생/일반인 전면 상향.** 모든 9정거장 재작성 + 웹앱 배포(볼 수 있게).
- **이유:** 中1 과학 수준은 너무 낮아 이 앱이 불필요. 목적=고등학생/일반인이 과학사에 흥미 갖고 지식·지평 확장.
- **앞으로 만드는 분야 트랙 콘텐츠는 모두 고등/일반 수준.** (시간축 9허브+figures+americas+people = 中1 딸용 유지 — 이중 대상 모델.)
- **상향 방식(NCC 기본값):** ①문체 친근반말→**교양 과학서 평서체(~다/이다)** ②deepdive 2층=中1심화→**대학+/현업 심화**(codec/NPU 실제 공학: DCT·움직임예측·MAC어레이·dataflow 등) ③"아빠의 분야"→**"엔지니어의 시선"** 일반화(codec↔NPU 척추 내용 유지). ④terms도 고등 수준 정의.
- **전체 컨텍스트 업데이트 대상:** plan 0615 · CLAUDE.md(이중대상) · hist-content-write/hist-audit 스킬 · EPISODE_SCHEMA(deepdive 노트) · SERIES_ROADMAP · 메모리.

## ⚡ 모델 재정의 (0615 #3 — Nick) ★★ 중대
- **접이식 deepdive '레벨링' 폐기.** 전체가 고등/일반이면 '같은 수준으로 더 깊이 펼치기'는 동어반복 → **본문을 처음부터 높은 수준으로.**
- **학교 과학 교과와 자연 연결**(정거장↔물리/화학/생명과학/지구과학 단원). 실제 수업과 바로 이어지게.
- **외부 심화 링크**: 위키백과·권위 자료로 자연 연결 → **신규 `links` 블록**(항상 표시, 200 검증).
- **전용 워크플로 셋업 완료:** 신규 스킬 **`tracks-write`**(중1 `hist-content-write`와 분리). plan §3·§4 갱신 완료.
- **상태:** 셋업·계획 완료. **9페이지 콘텐츠 재정비 + `links` 엔진블록 = Nick 확인 후 실행 대기.**

## 🚧 RESUME HERE (다음 할 일)
- **모델 #3 실행 완료 + 라이브:** 엔진 `links` 블록 추가(JS검사 통과), 9정거장 deepdive 제거·교과연결·외부 위키백과 링크(27개 200검증), 재배포·G3 PASS. → https://jwj-nick.github.io/history/tracks/sci-tech/
- **현재 진행 = Phase E (시각효과 개선, Nick 지시 '계속 진행'):**
  1. 재사용 5점 복사+블록: copernican_system→S0, crystal_palace→S1, apollo11→S5, smartphones·data_center→S7. (원허브 img/ 복사 + 라이선스 메타)
  2. 신규 소싱(urllib 단독·timeout): S2 라부아지에·주기율표 / S3 전화·맥스웰 / S4 파스퇴르·DNA도식 / S6 에니악·트랜지스터·튜링 / S8 칩다이·웨이퍼. **전점 Read 검수**, PD/CC.
  3. 각 정거장 **≥2** 되게 image 블록 + order에 image:0,image:1 삽입. 재빌드 → 재배포 → G3.
- **그 후:** ★Nick 코덱/NPU 본문 검수(S7 why·S8 why) / 컨텍스트 문서(CLAUDE·hist-* 스킬·SERIES_ROADMAP·메모리) / 소스 push.
- 빌드: `PYTHONIOENCODING=utf-8 python 40_build/build.py tracks/sci-tech`. 배포 cp/push 프로토콜 아래.

## 📋 정거장 체크리스트 (9) — 칸별 [B리서치 C1층 D딥다이브 E시각 F감수]
| # | id | 정거장 | B | C | D | E | 비고(★=codec척추) |
|---|---|---|---|---|---|---|---|
| 0 | revolution | 과학혁명 | ✅ | ✅ | ✅ | ☐ | copernican_system 재사용 |
| 1 | industry | 산업혁명 | ✅ | ✅ | ✅ | ☐ | crystal_palace 재사용 |
| 2 | chemistry | 화학·물질 | ✅ | ✅ | ✅ | ☐ | 신규(라부아지에·주기율표·하버) |
| 3 | electric | 전기·통신 | ✅ | ✅ | ✅ | ☐ | ★codec씨앗#1(신호) — '아빠의 분야 ①' |
| 4 | life | 의학·생명 | ✅ | ✅ | ✅ | ☐ | 신규(세균설·DNA·프랭클린·mRNA) |
| 5 | atom-space | 원자·우주 | ✅ | ✅ | ✅ | ☐ | apollo11 재사용 · choice(과학자책임) |
| 6 | computer | 컴퓨터 | ✅ | ✅ | ✅ | ☐ | ★칩씨앗 '아빠의 분야 ②'(0/1·무어법칙) |
| 7 | internet | 인터넷·디지털 | ✅ | ✅ | 🔶 | ☐ | ★codec '아빠의 분야 ③'(압축 원리) — **Nick검수 대기** |
| 8 | ai-chip | AI·반도체 | ✅ | ✅ | 🔶 | ☐ | ★클라이맥스 '아빠의 분야 ④'(코덱→NPU) + choice — **Nick검수 대기** |

## 📦 Phase 체크리스트
- [x] **A 계획·정렬** — plan 0615 + 이 worklog + (대기:ROADMAP/PROGRESS 갱신)
- [ ] **B 리서치** — `20_research/tracks-scitech/` (정거장별 facts·출처; 시간허브 기존 재활용)
- [ ] **C 1층 본문** — `30_content/tracks/sci-tech/episode.json` (build 무오류)
- [ ] **D 2층 deepdive** — ★4칸 Nick 검수 게이트
- [ ] **E 시각** — 정거장당 ≥2 (재사용+신규 소싱, 전점 Read검수)
- [ ] **F 빌드·감수** — hist-audit 4페르소나 + 시각게이트
- [ ] **G 랜딩·배포·교차링크** — tracks/index.html 5칸 + 시간허브 역링크 + 배포 + G3
- [ ] **H SSOT 마감** — ROADMAP 🟢 + PROGRESS + 메모리 + 커밋·푸시

## 🔁 재사용 자산 (이미 소싱·검수 완료 — 신규 소싱 절감)
- `copernican_system`(renaissance) → S0
- `crystal_palace`(imperialism) → S1
- `apollo11`(north-america) → S5
- `smartphones`·`data_center`(globalization) → S7
> 경로: `30_content/<원허브>/img/<name>.*` → S 정거장 img/로 복사. (라이선스 메타는 원본 episode.json에서 가져와 동일 표기)

## ⚠️ 프로토콜 리마인더 (반드시)
- 빌드: `python 40_build/build.py tracks/sci-tech` (중첩 slug OK, 엔진변경0).
- **PYTHONIOENCODING=utf-8** 항상. 콘솔에 한글 길게 X. heredoc 금지(Write→실행→rm).
- 네트워크(이미지 소싱 urllib)는 **단독·최소**, 로컬 먼저 커밋. curl/wget/gh ask-list 주의.
- 배포 git 후 **cwd가 `C:\Kids\30_MiddleSchool`로 리셋** → 이후 명령 `cd /c/Kids/30_MiddleSchool/260602_History` 프리픽스. repo별 OWN cwd에서 push(두 push 한 줄 금지).
- 이미지: 전점 Read 육안검수, PD/CC0/CC BY(-SA)만, 출처·라이선스·alt. 현대 제품·로고·표지=링크. AI생성·손그림 금지.
- 결과없음 → 추론 금지, 멱등 프로브로 실측.
- 커밋 푸터: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. settings.local.json 제외. 260426_MathTelling/260601_Study_Seeun 손대지 않음.

## 📝 로그 (최신 위)
- 0615 #6: 모델 #3 실행·배포 완료 — 엔진 `links` 블록(linksHTML+CSS, JS node --check OK) + 9정거장 deepdive 제거·교과연결·위키백과 링크 27개(전부 200검증). 빌드 9섹션 87872자, 배포 push(2d9c8bd)·G3 PASS(size 88769→87872). EPISODE_SCHEMA `links` 스펙 추가. 다음=Phase E 시각.
- 0615 #5: (셋업) tracks-write 스킬 신설 + plan §3·§4 모델 재정의 + CLAUDE.md §D 제어권 규칙 강화(e8c456c).
- 0615 #4: S6 computer(0/1·무어법칙 '아빠의 분야 ②')·S7 internet(★코덱 압축 원리 '③')·S8 ai-chip(★클라이맥스 코덱→NPU '④' + choice AI미래) 추가 + 용어 14개. **전 9정거장 1층+2층 완료**, 빌드 OK(9섹션 87322자). codec척추 deepdive 4칸 확인. S7·S8(+S3·S6) Nick 검수 대기. 다음=Phase E 시각.
- 0615 #3: S3 electric(★codec씨앗#1 '아빠의 분야 ①')·S4 life(세균설·DNA·프랭클린 공로·mRNA)·S5 atom-space(퀴리·E=mc²·choice 과학자책임) 추가 + 용어 11개. 빌드 OK(6섹션 77908자), choice·codec씨앗#1 주입 확인. 다음=S6~S8.
- 0615 #2: episode.json 신설 — meta·terms(8) + S0 과학혁명·S1 산업혁명·S2 화학(각 1층 hook/why/lens/cards/timeline/connect/yt/quiz/reflect + 2층 deepdive + order). 빌드 검증 OK(3섹션 69672B), deepdive 주입 확인. 이미지 없음(Phase E). 다음=S3~.
- 0615: Phase A 완료 — plan 0615 9정거장 확정, worklog 신설, 태스크 등록. Phase C 착수(episode.json).
