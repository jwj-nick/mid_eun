# CLAUDE.md — 30_MiddleSchool (세은 중학 저작 홈 · 세션 디스패처)

> 새 Claude 세션이 `C:\Kids\30_MiddleSchool`에서 시작되면 이 파일을 **먼저** 읽는다.
> 승격: 2026-07-18 — 세준 `70_HighSchool`에 대응하는 세은 저작 홈.

## 정체성
세은(딸, 중2)의 **중학 교과 학습 앱 저작 홈.** 자체 git repo · 자기완결.
- 여기서 **계획·매핑·콘텐츠·세션 로그**를 저작. **앱 코드/배포는 github.io**(`C:\Nick\30_Apps\jwj-nick.github.io`).

---

## ★ 세션 시작 프로토콜 (여러 NCC가 각 주제를 별도로)
**한 세션 = 한 주제.** 새 NCC를 열 때마다 아래를 따른다.

1. 이 파일(디스패처)을 읽는다 → 정체성·규칙 파악.
2. **아래 주제 레지스트리에서 딱 하나** 고른다.
3. 그 **진입 가이드**를 읽고 그 주제만 진행한다. (다른 주제 파일은 열지 않는다 — 세션을 좁게 유지.)
4. 세션 끝: `00_meta/sessions/<날짜>_<주제slug>.md`에 1줄 로그 (P2).

### 주제 레지스트리
| 주제 | 진입 가이드 (읽고 시작) | 배포/코드 | 상태 |
|---|---|---|---|
| **mid2 수학 PhET** | `C:\idea\migration\seeun-math-phet.md` | `github.io/mid2` (편집) | P0 감사 완료 → **P1 준비** |
| **중학 과학 앱(mid-sci)** | `Mid_Science/00_PLAN.md` (마스터) + `C:\idea\migration\seeun-sci-phet.md` | `github.io/mid-sci` (신규) | **P1 계획 확정**(하이브리드·학년탭·중1 힘과 운동 앵커) → P1 실행 |
| 수학텔링 | `260426_MathTelling_Idea/CLAUDE.md` | `github.io/mid1` 계열 | 기존 프로젝트 |
| 역사 앱 | `260602_History/README.md` | `github.io/history` | 기존 프로젝트 |
| EBS 메모 | `260601_Study_Seeun/` | — | 참고 자료 |
| *(PhET 공통 규약)* | `C:\idea\migration\seeun-phet.md` | — | 위 두 PhET 주제가 공유 |

> 새 주제가 생기면: 이 표에 한 줄 추가 + 진입 가이드 1개 작성. (규칙은 `_COMMON.md`)

### 병렬 NCC 규율 (동시에 여러 세션)
- 각 세션은 **자기 주제의 파일만** 건드린다 (mid2 vs mid-sci vs history는 폴더가 달라 충돌 없음).
- **github.io repo는 공유**다 → push 전 `git pull`, 커밋은 주제 단위로. 같은 파일 동시 편집을 피한다.
- 세션 로그는 주제별 파일이라 서로 안 겹친다.

---

## 규칙 (요약 — 상세 `C:\idea\migration\_COMMON.md`)
- **P1** 콘텐츠가 엔진을 당긴다. 슬라이스 1개로 루프 증명 후 확장. speculative 금지.
- **P2** 품질 상시 자율 개선 + 세션 끝 1줄 로그 → `00_meta/sessions/`.
- 흥미 ≠ 점수: 시뮬 → 문제 연결로 착지.
- 아이 사적 기록(점수·일기) repo 밖.
- 도메인 스킬이 실제로 필요해지면 `.claude/skills`에 추가(70_HighSchool의 `se-figcrop`·`se-science-chem-card` 참고). 미리 만들지 않는다.

## 장기 (체계화)
세은 학습 OS = **daughter-hub**(청사진 `_INDEX.md`, son-hub fork 예정). 완성 시 이 폴더 흡수. 재편 계획서 = `C:\idea\migration\kids-reorg.md`.
