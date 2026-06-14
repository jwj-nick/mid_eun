<!-- 00_project_hub/plan/0614_plan_visual_enrichment_all.md -->
# 전 에피소드 시각자료 보강 — 마스터 계획 ★ (0614)

> Nick 지시(0614): "지금까지 만든 모든 자료의 시각자료 추가 업데이트. **그 시대의 대표 이미지들을 한 페이지(섹션)당 2개 이상** 추가 (건물·마스터피스·기념비·아이콘·상징). 워크플로우(스킬)도 업데이트. 세부 계획 후 **전체 자율 진행**."
> 직전 PD-역사지도 보강(0614 B1·B2)과 별개의 **2차 비주얼 캠페인** = '대표 이미지' = 사진·회화·판화·건축·기념물(지도/차트 아님).

## 0. 표준 (SSOT)
- **규칙:** 모든 섹션에 **대표 이미지(image/oldmap 블록) ≥ 2점**. 건물·마스터피스(명화/조각)·기념비·문화 아이콘·상징물 위주.
- **카운트 정의:** `image`(단일=1, 배열=개수) + `oldmap`(=1)만 대표이미지로 카운트. `map`(Leaflet)·`battlemap`·`chart`는 **공간/데이터 시각화 → 제외**.
- **자산 규칙(불변):** PD 또는 명확한 CC만. 출처·라이선스 caption 표기. **전점 Read 검수**(검색 1위 신뢰 금지). 손그림·AI생성·API키 금지. 포스터/책표지/현대 화폐·로고 = 저작권 → 제외. 현역 정치인 영웅샷·잔혹 묘사 회피.
- **블록:** 사진/회화 = `image`(여러 장이면 배열 + `image:0/1` order 토큰). 옛 고지도 = `oldmap`(세피아). 기존 단일 image는 배열로 승격(`aslist`).

## 1. 실측 현황 (40_build/_audit_visuals.py)
- **총 84섹션 중 69섹션이 대표이미지 2개 미만.** 신규 필요 ≈ **80점**.

| 허브 | 섹션 | <2 섹션 | 필요 이미지 | 비고 |
|---|---:|---:|---:|---|
| ww2 | 8 | 7 | 7 | battlemap 다수 보유(대표사진 1→2) |
| imperialism | 8 | 5 | 5 | |
| renaissance | 7 | 4 | 4 | printing·scientific·absolutism·toward-modern |
| exploration | 8 | 7 | 7 | battlemap多, 대표이미지 빈약 |
| powers | 7 | 7 | 7 | 국가별 1점뿐 |
| revolutions | 7 | 6 | 6 | nationalism만 충분 |
| north-america | 6 | 6 | 6 | 전 섹션 |
| latin-america | 5 | 3 | **3+** | ★진행중(유적·은산·아이티) |
| coldwar | 8 | 6 | 7 | cuba +2 |
| globalization | 7 | 5 | 8 | one-market/union/flat-world +2 |
| new-order | 7 | 7 | 8 | us-china +2 |
| figures | 6 | 6 | 12 | 짝읽기 = 두 인물 초상 2점씩(도감 자산 재사용 가능) |

## 2. 허브별 대표이미지 쇼핑리스트 (가이드 — 실제는 PD/CC 가용성 따라 fetch시 확정)

### latin-america ★(B-LA, 진행중)
- civilizations: **치첸이트사 엘카스티요(마야)·템플로마요르(아스텍)·사크사이와만(잉카)** + 마추픽추(기존) → 4점
- conquest: 코르테스–몬테수마 회견 / 테노치티틀란 함락 회화 (+1)
- colonial: **포토시 세로리코 은산**(섹션 제목 직결) (+1, 기존 casta+tordesillas와 합 3)
- independence: **수호돌스키 〈산토도밍고 전투〉**(아이티 혁명) (+1)
- modern: 충분(2)

### ww2 (B-WW2)
- outbreak: 뉘른베르크 전당대회(Bundesarchiv CC-BY-SA) 또는 뮌헨협정
- anne: 암스테르담 안네 프랑크 동상 / 일기 복제본
- europe: 노르망디 상륙(US PD) / 스탈린그라드 폐허
- pacific: 진주만 USS Arizona(US Navy PD)
- asia: 루거우차오(마르코폴로교) / 카이로회담 (비참혹)
- postwar: UN총회 / 뉘른베르크 재판 (PD)
- korea: 인천상륙 / 38선 표지 / 한국전 기념비 (US Army PD, 비참혹)

### imperialism (B-IMP)
- industry: 수정궁 1851 / 증기기관차 (PD)
- scramble: 베를린회의 1884 판화 (PD)
- india: 델리 더르바르 1903 / 빅토리아 터미너스 (PD)
- opium-china: 원명원(옛 여름궁전) 폐허 / 아편 소각 (PD)
- japan-meiji: 메이지 천황 / 도미오카 제사장 / 로쿠메이칸 (PD)

### renaissance (B-REN)
- printing: 구텐베르크 성경 페이지 / 인쇄기 복원 (PD)
- scientific: 코페르니쿠스 태양중심 도해 / 갈릴레오 망원경·초상 (PD)
- absolutism: **베르사유 궁전**(건축) + 리고 〈루이14세 초상〉 (PD)
- toward-modern: 백과전서 권두화 / 계몽 살롱 (PD)

### exploration (B-EXP)
- why-sea: 카라벨선 / 아스트롤라베·나침반 (PD)
- pioneers: 리스본 발견기념비(CC) / 엔히크 왕자
- columbus: 〈콜럼버스의 상륙〉(PD) / 산타마리아 복제선
- magellan: 빅토리아호 / 마젤란해협 / 마젤란 초상 (PD)
- conquest: 코르테스/피사로 (LA와 중복 회피 — 정복자 초상 중심)
- slave-trade: **브룩스 노예선 도해**(PD, 도식·비참혹) + 엘미나 성(노예 요새, 건축 CC)
- toward-modern: VOC 상선 / 암스테르담 항 (PD, 기존 oldmap과 합 2)

### powers (B-POW) — 국가 상징/건축/지도자 초상
- overview: 대박람회 / 식민 산물 (PD)
- britain: 빅토리아 여왕 초상 (PD, 기존 oldmap과 합 2)
- france: 에펠탑 1889 (건축 상징)
- germany: 비스마르크 초상 / 제국의회 건물
- russia: 겨울궁전(건축) / 시베리아 횡단철도
- belgium: 테르뷰런 중앙아프리카박물관 / 레오폴2세 동상 (콩고 잔혹 회피)
- latecomers: 자유의 여신상 / 이탈리아·일본 상징 콜라주

### revolutions (B-REV) — 명화·기념물 풍부
- enlightenment: 백과전서 / 볼테르·루소 초상 (PD)
- glorious: 권리장전 / 윌리엄&메리 (PD)
- american-rev: 〈독립선언〉(트럼불) / 〈델라웨어 도하〉 (PD)
- french-rev: 〈민중을 이끄는 자유〉(들라크루아) / 바스티유 (PD)
- terror: 기요틴 / 로베스피에르 (PD, 비참혹)
- napoleon: 다비드 〈알프스를 넘는 나폴레옹〉 / 〈대관식〉 (PD)

### north-america (B-NA)
- natives: 원주민 추장 사진(에드워드 커티스 PD) / 토템·티피
- colonies: 메이플라워 / 제임스타운 / 청교도 상륙 (PD)
- revolution: 〈독립선언〉 / 벙커힐 (PD, LA·revolutions와 주제 분리)
- expansion: 대륙횡단철도 골든스파이크 / 오리건 트레일 / 자유의 여신상 (PD)
- civil-war: 링컨 초상 / 게티즈버그 / 노예해방 (PD)
- modern: 엠파이어스테이트 / 자유의 여신상 / 아폴로11 (PD)

### coldwar (B-CW)
- origin: 얄타회담 3거두 / 처칠 '철의 장막' (PD)
- balance: 핵폭발 버섯구름 / 핵 대피 훈련 (PD)
- berlin: 베를린 장벽 / 검문소 찰리 (PD/CC)
- cuba: U-2 정찰사진 / 쿠바 미사일 / 케네디 (+2, PD)
- detente: 닉슨–마오 악수 / 아폴로–소유즈 (PD)
- fall: 베를린장벽 붕괴 1989 / 브란덴부르크문 (CC)

### globalization (B-GLO)
- one-market: 컨테이너항 / 증권거래소 / 세계화 상징 (+2, CC)
- connected: 인터넷·해저케이블 / 휴대폰 (CC)
- nine-eleven: 9·11 추모(Tribute in Light)·그라운드제로 추모 (공격영상 아님, CC)
- union: EU 깃발·브뤼셀 본부 / 유로화 도입 (+2, CC)
- flat-world: 스마트폰·SNS / 글로벌 공급망 컨테이너 (+2, CC)

### new-order (B-NO)
- crack: 리먼 사태 / 증시 폭락 트레이딩플로어 (CC)
- multipolar: G20 단체사진 (정부 CC)
- us-china: 미·중 국기·컨테이너 무역 (+2, 특정 정치인 회피, CC)
- chip-war: 실리콘 웨이퍼·클린룸·EUV (CC, Nick 전문)
- connected-crisis: 기후시위 / 빈 도시 2020 / 지구 (CC)
- ai-arrives: 데이터센터·GPU·신경망 시각화 (CC, AI생성 금지)
- your-turn: 지구(블루마블 NASA PD) — 기존과 합 2

### figures (B-FIG) — 짝읽기 = 두 인물 초상
- 각 섹션 = 두 인물 비교. **도감(`50_app/people/img/`)의 PD 초상 2점**을 `compare`/`image` 배열로. 신규 소싱 최소(도감 재사용).
- anne-sadako / sitting-bull-an(중근) / galilei-oppenheimer / washington-bolivar / leopold-morel / how-to(안내=대표 콜라주 1, 예외 허용)

## 3. 소싱·검수·게이트 절차 (확립)
1. **소싱(네트워크 단독):** Commons API(urllib) `generator=search` 또는 정확 `titles=File:...`. 라이선스 필터(PD/CC) + 이미지 확장자. `iiurlwidth` 썸네일. **429 잦음 → time.sleep(4~10), 정확 파일명 우선, 허브 단위 1배치.**
2. **검수:** 받은 후보 전점 **Read 도구로 시각 확인**(엉뚱본·저해상·책스캔·화폐/로고·중복 차단). 필요시 PIL 크롭.
3. **패치:** `30_content/<slug>/img/`에 채택본 복사 → episode.json image 배열+`image:N` order 토큰 삽입(헬퍼 `after`/`aslist`). caption=내용+출처+라이선스, alt 텍스트.
4. **빌드·게이트:** `build.py` → G0(빌드) · G1(`node --check` 최대 인라인 script, 엔진 변경 시만) · G2(이미지 ref 실재+라이선스 표기, jpg/png) · G3(배포 후 라이브 200·마커 substring, `?cb=`·유한루프·sleep12).
5. **배포·커밋:** `50_app/<slug>` → deploy repo `history/<slug>` 복사. **소스/배포 repo 각각 자기 cwd에서 push**(이중푸시 버그 주의). 허브 단위 커밋.
6. **갱신:** 이 파일 §6 진행기록 + 메모리.

## 4. 실행 순서 (허브 단위 배치)
B-LA(진행중) → B-REV → B-NA → B-EXP → B-IMP → B-REN → B-POW → B-WW2 → B-CW → B-GLO → B-NO → B-FIG.
- 명화/기념물이 PD로 풍부한 허브(revolutions·exploration·renaissance·na) 먼저 = 성공률↑·429위험↓.
- 현대(globalization·new-order)·figures는 후반(저작권·도감재사용 신중).
- **각 배치 독립 커밋·배포**로 중단되어도 누적 보존. 멈춤 없는 인라인 순차(에이전트 블로킹 await 금지).

## 5. 워크플로우(스킬) 업데이트
- **신설 `hist-visuals` 스킬**: 본 절차(소싱·검수·패치·게이트·배포)를 집행. 기존/신규 에피소드 비주얼 보강 표준.
- **hist-content-write**: "섹션당 대표이미지 ≥2 (건물·명화·기념물·아이콘)" 작성 표준 1줄 추가.
- **hist-audit**: 게이트 체크에 "각 섹션 대표이미지 ≥2" 추가.
- **EPISODE_SCHEMA**: image 배열·대표이미지 표준 명시.

## 6. 진행 기록 (NCC)
- 0614: 전 에피소드 실측(84섹션/69 under) + 본 계획·표준 수립. 스킬 hist-visuals 신설 예정.
- (이후 배치별 ✅ 추가)
