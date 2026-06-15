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
- **Phase C(1층) + D(2층 초안) 전 9정거장 완료** — 빌드 OK(9섹션 87322자, JSON 유효, 용어 32, star=ai-chip, codec척추 4칸).
- **다음 액션 = Phase E (시각, 정거장당 ≥2):**
  1. 재사용 자산 복사: copernican_system→S0, crystal_palace→S1, apollo11→S5, smartphones·data_center→S7. (원허브 img/에서 복사 + 라이선스 메타 가져오기)
  2. 신규 소싱(urllib·단독·최소): S0 갈릴레이망원경/뉴턴, S2 라부아지에·주기율표, S3 전화/전구/맥스웰, S4 파스퇴르/DNA도식, S5 아인슈타인, S6 에니악/트랜지스터/튜링, S8 칩다이/웨이퍼. 전점 Read 검수.
  3. image 블록 추가 + 각 정거장 order에 image:0,image:1 삽입.
- **★ Nick 검수 대기(배포 전 필수): S7 deepdive(코덱 원리) · S8 deepdive(코덱→NPU). + S3·S6도 codec척추라 확인 권장.** 검수 전이라도 E·F는 진행 가능.
- 그 후: F(audit) → G(랜딩 5칸+시간허브 역링크+배포) → H(SSOT). 빌드: `PYTHONIOENCODING=utf-8 python 40_build/build.py tracks/sci-tech`.

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
- 0615 #4: S6 computer(0/1·무어법칙 '아빠의 분야 ②')·S7 internet(★코덱 압축 원리 '③')·S8 ai-chip(★클라이맥스 코덱→NPU '④' + choice AI미래) 추가 + 용어 14개. **전 9정거장 1층+2층 완료**, 빌드 OK(9섹션 87322자). codec척추 deepdive 4칸 확인. S7·S8(+S3·S6) Nick 검수 대기. 다음=Phase E 시각.
- 0615 #3: S3 electric(★codec씨앗#1 '아빠의 분야 ①')·S4 life(세균설·DNA·프랭클린 공로·mRNA)·S5 atom-space(퀴리·E=mc²·choice 과학자책임) 추가 + 용어 11개. 빌드 OK(6섹션 77908자), choice·codec씨앗#1 주입 확인. 다음=S6~S8.
- 0615 #2: episode.json 신설 — meta·terms(8) + S0 과학혁명·S1 산업혁명·S2 화학(각 1층 hook/why/lens/cards/timeline/connect/yt/quiz/reflect + 2층 deepdive + order). 빌드 검증 OK(3섹션 69672B), deepdive 주입 확인. 이미지 없음(Phase E). 다음=S3~.
- 0615: Phase A 완료 — plan 0615 9정거장 확정, worklog 신설, 태스크 등록. Phase C 착수(episode.json).
