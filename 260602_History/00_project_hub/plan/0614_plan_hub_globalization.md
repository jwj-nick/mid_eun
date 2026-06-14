<!-- 00_project_hub/plan/0614_plan_hub_globalization.md -->
# 0614 — 신규 허브 계획: 「탈냉전과 세계화 — 하나가 된 세계」 (slug: globalization)

> 마스터 플랜(`0614_masterplan_renaissance_to_ai.md`) ❷. 냉전(coldwar) 다음 칸 = **탈냉전·세계화(1991–2008)**.
> 사슬: …→세계대전→냉전→**탈냉전·세계화**→(다음) 다극·미중·AI(new-order). **수위 고교 레벨**(coldwar 계승).

## 0. 정체성 / 구조
- **형식:** 새 에피소드 `/history/globalization/` — 엔진·블록 전부 재사용, 데이터만.
- **컨셉:** "벽이 무너지고, 세계가 하나의 시장·하나의 네트워크로 묶였다 — 그 빛과 그림자." 단극(미국)의 시대, 세계화, 인터넷 혁명, 그리고 그 낙관에 금이 간 9·11과 중국의 부상.
- **사슬 위치:** coldwar#fall → globalization#soviet-collapse → (다음) new-order. 냉전의 '평화로운 끝'이 '하나의 세계'라는 낙관으로, 다시 새로운 경쟁으로.

## 1. 섹션 구성 (7개)
| # | id | 제목 | 핵심 | 주력 블록 | 신규인물 |
|---|---|---|---|---|---|
| 0 | `soviet-collapse` | 소련이 사라지다 | 1991 쿠데타 실패→소련 해체→15개국 독립→단극 개막 | timeline·image(크렘린 국기 하강)·relations(단극) | **옐친** |
| 1 | `one-market` | 하나의 시장 | 세계화·WTO(1995)·컨테이너·다국적기업·자유무역 | chart(세계 무역량)·compare(보호무역↔자유무역) | — |
| 2 | `connected` | 연결되는 세계 | WWW 공개(1991)·인터넷·휴대폰·정보혁명 (sci-tech 트랙 예고) | image(초기 웹/서버)·deepdive | — |
| 3 | `nine-eleven` | 흔들린 단극 (9·11) | 2001 테러→테러와의 전쟁(아프간·이라크)→단극의 한계 | image(**추모 — 그라운드제로/추모공원, 공격 직접묘사 회피**)·timeline·choice(신중) | — |
| 4 | `union` | 통합의 실험 (EU) | 마스트리흐트(1993)·유로(2002)·EU 확대 | map(EU)·compare(국가↔연합) | — |
| 5 | `china-rises` | 잠에서 깬 중국 | 덩샤오핑 개혁개방·WTO 가입(2001)·세계의 공장·2008 올림픽 | image(상하이 푸둥 스카이라인)·chart(GDP 추이) | **덩샤오핑** |
| 6 | `flat-world` | 평평해진 세계 | 세계화의 빛(성장·연결)↔그림자(불평등·2008 금융위기 전조)·'역사의 종말'과 반론 → new-order 예고 | compare·choice·deepdive | — |

- startPrimary=soviet-collapse. startStar=china-rises("★ 다음 시대를 바꿀 거인").

## 2. 인물 추가 (people.json → build_people) — 도감 50→52 (저작권 게이트)
- **옐친(Boris Yeltsin)** — RIA 아카이브 CC BY-SA 가능성. soviet-collapse.
- **덩샤오핑(Deng Xiaoping)** — 1979 방미 미연방 PD 사진 가능성. china-rises.
> ⚠️ **현대 인물 = PD/CC 초상 확보 실패 시 道감 등재 보류**, 섹션 카드(요약)로만. 고르바초프(coldwar)·만델라는 network/참조. 소싱 결과로 결정.

## 3. 자산 (전부 PD/CC + Read 검수 + 출처표기) — 현대라 신중
- soviet-collapse: 크렘린 소련기 하강(1991)·옐친(RIAN CC).
- one-market: 컨테이너선·항만(CC)·WTO 본부(CC).
- connected: CERN 초기 웹서버(CC)·해저케이블/초기 인터넷.
- **nine-eleven: 공격 장면 직접묘사 회피 → 그라운드제로 추모공원(반사못)·Tribute in Light(추모 빛기둥, CC). FEMA(미연방 PD)도 가능하나 잔해보다 추모 중심.**
- union: EU기·유로 도입·유럽의회(CC).
- china-rises: 상하이 푸둥 스카이라인(CC)·베이징 2008 새둥지 경기장(CC)·덩샤오핑(PD 가능 시).
- flat-world: 지구 야경(NASA PD).

## 4. ⚠️ 균형심판·수위 (현대사 — 최우선)
- **9·11**: 중1 수위 — 추모·결과·의미 중심, 잔혹·공포 직접묘사 회피. 테러를 정당화하지도, 특정 종교·민족 일반화하지도 않기. '왜 일어났나'는 deepdive로 절제.
- **세계화**: 낙관('역사의 종말', 하나의 번영)과 반론(불평등·문화 획일화·금융 불안)을 **양쪽** 제시. 승자만 비추지 않기.
- **중국 부상**: 경제 성장의 빛과 인권·격차의 그림자 함께. 다음 허브(미중경쟁)의 다리.
- **단극 미국**: '자유의 승리' 서사와 그 한계(이라크전 명분 논란) 균형.
- choice/after = '진행 중 역사라 평가가 갈림' 명시.

## 5. 연결
- coldwar#fall → globalization#soviet-collapse. connected ↔ tracks/sci-tech. china-rises → new-order(미중경쟁). flat-world#2008 → new-order#금융위기.

## 6. 제작 순서 / 게이트
episode.json 7섹션 → 이미지 격리 소싱+Read 검수 → (가능 시)인물 2인 → build → G0~G3 → 배포·양repo 커밋 → SERIES_ROADMAP/PROGRESS 갱신 → hist-audit.

## 7. 진행 기록 (NCC)
- 0614: 계획 수립. 착수 = episode.json soviet-collapse~flat-world.
- **0614 ✅ 완료·배포·라이브**: 7섹션 전부 작성·빌드·배포. https://jwj-nick.github.io/history/globalization/ (G3 200·83KB·마커2).
  - 자산 5점 전점 Read 검수(크렘린상원 CC BY-SA·CERN 웹서버 CC BY-SA·9·11추모못 CC BY-SA·푸둥 CC BY-SA·새둥지 CC BY-SA). terms 17·deepdive 16.
  - 9·11=공격 직접묘사 회피→추모못·voice(상상)·균형 lens(종교/민족 일반화 금지 quiz).
  - **도감 2인 floor(50→52)**: 옐친·덩샤오핑. 자산 11점 Read 검수(전부 PD/CC BY-SA). 오선정 2건 교정(soviet_flag·deng_shenzhen). 외부링크 200(yeltsin.ru·wiki·Aladin).
  - 허브 랜딩 EP08 카드+flow밴드. SERIES_ROADMAP·PROGRESS 갱신. 소스 `c755177`·배포 `0c7c3b8`.
  - **hist-audit 통과**: `20_research/globalization/audit.md` (사실오류 0, 세계화 명암·9·11·중국 균형).
- **다음 = 마스터플랜 P3(tracks/sci-tech 분야축 1호·AI 상세) 또는 ❸ new-order(다극·미중·AI 시간축 마지막칸).**
