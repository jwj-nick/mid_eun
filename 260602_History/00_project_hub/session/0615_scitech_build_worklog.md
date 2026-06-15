<!-- 00_project_hub/session/0615_scitech_build_worklog.md -->
# WORKLOG — tracks/sci-tech 제작 (★ 압축 생존용 단일 진실)

> **이 파일을 먼저 읽으면 어느 NCC 세션이든 "여기서 이어서" 가능.** compact 후 품질 유지의 핵심.
> 계획 SSOT = `plan/0615_plan_track_scitech.md`. 스키마 = `10_docs/EPISODE_SCHEMA.md`. 프로토콜 = `CLAUDE.md`(인코딩·네트워크·cwd·이미지검수).
> 갱신 규칙: **매 작업 단위 끝에 체크박스 갱신 + 맨 아래 로그에 1줄.** 추측 아닌 실측만.

## 🎯 목표 한 줄
9정거장 과학기술 통사 SPA(`/history/tracks/sci-tech/`) + `tracks/` 5칸 랜딩. 中1 본문 + (Nick검수) codec/NPU deepdive 척추.

## ✅ Nick 확정 (0615)
9정거장(화학·의학 추가) / codec deepdive=NCC초안→Nick검수(a) / AI수위 보수성↓ / 랜딩 지금 5칸 / 이 세션 B부터 자율.

## 🚧 RESUME HERE (다음 할 일)
- **현재 Phase: C/D 진행 중** — S0~S5 (6정거장) 1층+2층 완료·빌드검증 OK(6섹션 77908자, JSON 유효).
- **다음 액션: S6 computer(★칩씨앗) → S7 internet(★codec씨앗#2, 압축) → S8 ai-chip(★클라이맥스, NPU·codec↔AI) 를 sections 배열에 append.** S7·S8 deepdive가 Nick 교집합 본론 — 작성 후 **Nick 검수 대기** 표시.
- 그 후: Phase E(이미지 ≥2/정거장, 재사용+신규) → F(audit) → G(랜딩 5칸+배포) → H(SSOT).
- 빌드: `PYTHONIOENCODING=utf-8 python 40_build/build.py tracks/sci-tech`.

## 📋 정거장 체크리스트 (9) — 칸별 [B리서치 C1층 D딥다이브 E시각 F감수]
| # | id | 정거장 | B | C | D | E | 비고(★=codec척추) |
|---|---|---|---|---|---|---|---|
| 0 | revolution | 과학혁명 | ✅ | ✅ | ✅ | ☐ | copernican_system 재사용 |
| 1 | industry | 산업혁명 | ✅ | ✅ | ✅ | ☐ | crystal_palace 재사용 |
| 2 | chemistry | 화학·물질 | ✅ | ✅ | ✅ | ☐ | 신규(라부아지에·주기율표·하버) |
| 3 | electric | 전기·통신 | ✅ | ✅ | ✅ | ☐ | ★codec씨앗#1(신호) — '아빠의 분야 ①' |
| 4 | life | 의학·생명 | ✅ | ✅ | ✅ | ☐ | 신규(세균설·DNA·프랭클린·mRNA) |
| 5 | atom-space | 원자·우주 | ✅ | ✅ | ✅ | ☐ | apollo11 재사용 · choice(과학자책임) |
| 6 | computer | 컴퓨터 | ☐ | ☐ | ☐ | ☐ | ★칩씨앗 — **다음** |
| 7 | internet | 인터넷·디지털 | ☐ | ☐ | ☐ | ☐ | ★codec씨앗#2(압축) |
| 8 | ai-chip | AI·반도체 | ☐ | ☐ | ☐ | ☐ | ★클라이맥스(NPU·codec↔AI) |

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
- 0615 #3: S3 electric(★codec씨앗#1 '아빠의 분야 ①')·S4 life(세균설·DNA·프랭클린 공로·mRNA)·S5 atom-space(퀴리·E=mc²·choice 과학자책임) 추가 + 용어 11개. 빌드 OK(6섹션 77908자), choice·codec씨앗#1 주입 확인. 다음=S6~S8.
- 0615 #2: episode.json 신설 — meta·terms(8) + S0 과학혁명·S1 산업혁명·S2 화학(각 1층 hook/why/lens/cards/timeline/connect/yt/quiz/reflect + 2층 deepdive + order). 빌드 검증 OK(3섹션 69672B), deepdive 주입 확인. 이미지 없음(Phase E). 다음=S3~.
- 0615: Phase A 완료 — plan 0615 9정거장 확정, worklog 신설, 태스크 등록. Phase C 착수(episode.json).
