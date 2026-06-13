<!-- 00_project_hub/plan/0614_plan_hub_coldwar.md -->
# 0614 — 신규 허브 계획: 「냉전 — 총성 없는 50년 전쟁」 (slug: coldwar)

> Nick 지시(0614): 시간 사슬을 현재로 연장하는 첫 칸. ww2(~1953 한국전쟁) 다음 = **냉전(1945–1991)**.
> 마스터 플랜(`0614_masterplan_renaissance_to_ai.md`) ❶. **인물 다수가 이미 도감 floor → 최저비용 최고가치.**
> **수위: 고교생 레벨로 상향** — 기본 사실(연도·인명·개념)을 풍부하게, deepdive는 더 깊은 논쟁·1차 사료.

## 0. 정체성 / 구조 결정
- **형식:** 새 에피소드 `/history/coldwar/` — imperialism/powers와 같은 엔진·블록 전부 재사용, 데이터만.
- **컨셉:** "총 한 발 직접 쏘지 않고도 50년간 세계를 둘로 쪼갠 전쟁." 두 초강대국(미·소)이 핵·이념·우주·대리전으로 맞선 시대. 직접 충돌은 없었으되(열전 회피) 세계 곳곳이 그 대리 무대가 됨.
- **대상 수준:** **고교 레벨 본문** + deepdive(대학/일반 심화). 중1도 입구는 따라오되, 사실 밀도·용어를 한 단계 올림. terms 툴팁으로 보강.
- **사슬 위치:** ww2#postwar → **coldwar** → (다음) globalization. 한국전쟁(1950–53)은 ww2#korea가 이미 다룸 → 여기선 **중복 피하고** 베트남·제3세계·쿠바·우주·장벽에 집중. 한국전쟁은 '냉전의 첫 열전'으로 짧게 참조·교차링크.

## 1. 섹션 구성 (8개)
| # | id | 제목 | 핵심 | 주력 블록 | 인물(재사용/신규) |
|---|---|---|---|---|---|
| 0 | `origin` | 두 진영의 탄생 | 얄타→포츠담→철의 장막. 트루먼 독트린·마셜플랜 ↔ 코민포름·코메콘 | relations(서방 vs 동구)·timeline | 스탈린·트루먼(재사용) |
| 1 | `balance` | 공포의 균형 | 핵 독점 깨짐(1949 소련 핵실험)·수소폭탄·MAD·군비경쟁 | chart(핵탄두 수 미·소)·deepdive(MAD 이론) | 오펜하이머(재사용) |
| 2 | `berlin` | 갈라진 베를린 | 1948 봉쇄·공수작전 → 1961 베를린 장벽 → 분단의 상징 | map(베를린)·image(장벽 PD)·voice | — |
| 3 | `cuba` | 13일, 핵전쟁 직전 | 1962 쿠바 미사일 위기 — 인류가 가장 가까이 간 핵전쟁 | map(쿠바·터키)·choice(케네디의 선택)·timeline | **케네디·흐루쇼프(신규)** |
| 4 | `proxy` | 대리전과 제3세계 | 한국(참조)→베트남→아프가니스탄. 비동맹·제3세계의 선택 | battlemap(베트남)·compare(열강의 대리전)·deepdive | 마오·김일성(재사용·참조) |
| 5 | `space` | 우주를 향한 경쟁 | 스푸트니크(1957)→가가린(1961)→아폴로11(1969). 과학=국력 | chart(우주 이정표)·image(PD NASA)·deepdive | — (sci-tech 트랙 교차) |
| 6 | `detente` | 잠시의 해빙 | 닉슨-마오 데탕트·SALT 군축·프라하의 봄(1968)·헬싱키 | relations·compare(긴장↔완화)·voice | — |
| 7 | `fall` | 장벽이 무너지다 | 고르바초프(글라스노스트·페레스트로이카)→1989 동유럽→1991 소련 해체 | timeline·image(장벽붕괴 PD/CC)·choice | **고르바초프(신규)** |

- 도입 입구(★): `origin` 또는 `cuba`(가장 극적). startStar=cuba 권장.
- connect 사슬: 각 섹션 끝 → 다음. fall#toward → globalization(다음 허브 예고).

## 2. 인물 추가 (people.json → build_people) — 도감 47→50
신규 3인(전부 PD 초상 목표):
- **존 F. 케네디** (미국 대통령, 쿠바 위기·우주 선언) — 백악관/NASA 사진 = 미연방 PD 풍부.
- **니키타 흐루쇼프** (소련 서기장, 쿠바 위기·스탈린 격하·"우리가 당신들을 묻겠다") — 소련/RIA 사진 PD 여부 개별 확인.
- **미하일 고르바초프** (소련 마지막 지도자, 개혁·냉전 종식, 2022 별세) — **저작권 주의**(근현대) → CC BY 확보 우선, 없으면 장소·상징 + 링크.
> 각 인물 v3 floor 표준(quickCard·whyHere·quotes≥2·deepDive≥3·network·gallery≥3·study·journey). network로 스탈린·트루먼·마오와 연결. figuresLink는 해당 짝 생기면.

## 3. 자산 / 지도 (전부 PD/CC + Read 검수 + 출처표기)
- **map(Leaflet):** 베를린(브란덴부르크·체크포인트 찰리), 쿠바·터키(미사일 사거리), 분단 유럽.
- **battlemap:** 베트남(북·남, 호치민 루트) — phase로.
- **chart:** 핵탄두 수 추이(출처: 대략값 명시), 우주 이정표 연표.
- **image(PD):** 베를린 장벽·체크포인트 찰리, 스푸트니크/아폴로(NASA PD), 1989 장벽붕괴(CC 확보 시). 핵실험 버섯구름(미군 PD).
- **저작권 라인:** 현대 보도사진 다수 저작권 → NASA/미연방/소련 초기 PD·Commons CC만. 확보 못 하면 텍스트·지도로.

## 4. ⚠️ 균형심판 (현대사·진영 — 최우선 주의)
- **어느 진영도 미화/악마화 금지.** "그때 양쪽이 본 세계" 렌즈. 자유진영의 매카시즘·중남미 개입, 공산진영의 굴라크·프라하 진압을 **양쪽 다** 비판적으로.
- **김일성:** 도감 원칙 유지 — 우상화 이미지·인용 배제, 전쟁·분단 맥락만.
- **베트남전:** 미국 시점 일방화 금지 — 제3세계·탈식민 맥락 병기. 고엽제·민간 피해도 절제하되 명시.
- **인용 caveat:** "우리가 당신들을 묻겠다"(흐루쇼프) 등 유명 인용은 **맥락·번역 논쟁**을 deepdive로.
- choice/after는 '진행 중 역사라 단정 어려움'을 분명히.

## 5. 연결 (서사 그물)
- ww2#postwar/#korea → coldwar#origin (전후 질서가 곧 냉전의 씨앗). 한국전쟁 = 냉전 첫 열전으로 교차링크.
- coldwar#space ↔ (예정) tracks/sci-tech (우주·컴퓨터 경쟁).
- coldwar#fall → (예정) globalization#soviet-collapse.
- 도감: 케네디·흐루쇼프·고르바초프 ↔ 스탈린·트루먼·마오(network).

## 6. 제작 순서 / 게이트
1. episode.json 작성(8섹션) — 본문 고교 수위.
2. 인물 3인 people.json + 이미지 소싱(Commons API 격리, sleep) → build_people.
3. 이미지 소싱(섹션 자산) → 전점 Read 검수.
4. `python 40_build/build.py coldwar` → 50_app/coldwar/.
5. 게이트 G0(build)·G1(node --check 인라인)·G2(이미지 참조 실재+라이선스)·G3(라이브 폴링).
6. 배포(jwj-nick.github.io/history/coldwar) + 양 repo 커밋.
7. SERIES_ROADMAP 표 1줄 + PROGRESS 갱신.
8. hist-audit(4 페르소나) → audit.md.

## 7. Nick 코멘트
- (Nick)

## 8. 진행 기록 (NCC)
- 0614: 계획 수립. 착수 = episode.json origin~fall 작성.
