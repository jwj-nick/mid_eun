<!-- 00_project_hub/session/0612_worklog_improvements.md -->
# 0612 — Worklog: 개선 아이디어 백로그 적용 (plan §7·§8 실행)

> Nick 지시(0612): "개선 아이디어 적용바람. 이후에 남은 두개 에피소드 진행. 그 다음 인물 이야기 계획 및 실행."
> 이 파일 = 1단계(개선 적용) 기록. 2단계 = revolutions·renaissance, 3단계 = 인물 이야기(별도 worklog).

## Round 1 — 적용 내역 (NCC)

### 엔진 (1회 수정 → 전 에피소드 6 SPA 혜택)
1. ✅ **라이트박스** (powers §8-3): image/oldmap 이미지 클릭 → 전체 화면 확대(캡션=alt). zoom-in/out 커서, 스크롤 잠금. — 고해상 지도(Imperial Federation·블라우 1635 등) 디테일 감상 가능.
2. ✅ **companion 배지** (powers §8-2): `meta.companion:{slug,label}` → 사이드바 허브 링크 아래 '🔗 짝 에피소드' 점선 배지 자동 노출. powers↔imperialism 양방향 적용.

### 데이터
3. ✅ **'제국 스타일' compare** (powers §8-4): overview에 3상태 토글(영국 간접통치 ↔ 프랑스 동화주의 ↔ 벨기에 사유지) — 엔진 compare가 N상태 지원함을 확인 후 적용.
4. ✅ **도감 균형 인물 +2 → 40인** (powers §8-1·americas §8-2): **프레더릭 더글러스**(북미/남북전쟁 — 해방을 '쟁취'한 쪽의 얼굴), **E. D. 모렐**(powers/벨기에 — 폭로자 계보). 초상 PD 2점 육안 검수(모렐은 보존판 테두리 사진 → Elliott & Fry 깨끗한 판으로 교체).
5. ✅ **시팅 불 ↔ 안중근 교차 모티프** (americas §8-5): 두 인물 reflect에 상호 참조 한 줄 — 도감 가로지르기 학습 장치.
6. ✅ **yt 핀 교체 4건** (exploration §7-1): WebSearch로 ID 확보 → **oembed 실재 검증** 후 교체 — pioneers=CC#21(콜럼버스·다가마·정화), columbus=TED-Ed 'History vs. Columbus', slave-trade=CC#24, toward-modern=CC#23(콜럼버스 교환). 허위 ID 0.

### 보류 (큰 공사 — 백로그 유지, 사유 명시)
- 마젤란 globe.gl 승격(exploration §7-2) / territory 단계 지도(americas §8-3): 엔진 신규 모드 — maplab 검증 후 별도 라운드 권장.
- 북미·남미 비교 페이지(americas §8-1): 신규 페이지 — '인물 이야기'(3단계)와 함께 페이지 신설 패턴으로 묶는 게 효율적.
- 랜딩 패턴 추출(americas §8-4): 지역 허브 2호 등장 시점에.
- 콜럼버스 교환 비주얼(exploration §7-3): 전용 도해 — 차기.

### 게이트
- 전 6 에피소드 재빌드(엔진 변경 반영) — G1 데이터/엔진 분리 node check **전부 PASS**, 라이트박스 포함 확인. 도감 40인 재빌드(morel까지 확인).

**1단계 배포 검증(실측)**: 소스 `87e6ba6` / 배포 `638fe9d` push. 라이브 — powers 라이트박스·companion 마커 11건, morel 200, exploration 핀(GD3dgiDreGc 등) 확인 ✅.

## Round 2 — 2단계: EP05·EP06 제작 (0612)
- **renaissance(EP05, 7섹션)**: 르네상스→인쇄술→종교개혁★→종교전쟁→과학혁명→절대왕정→근대의 문(부품 배선도 relations). 직지 78년(유네스코 표현)·켈리의 질문·마녀사냥·조선 동시대사 2건. companion=exploration.
- **revolutions(EP06, 7섹션)**: 계몽→명예혁명→미국독립(다리, 아메리카 허브 교차)→프랑스혁명★→공포정치→나폴레옹→민족주의(배선도). 드 구주·아이티 시험지·방데 논쟁·메테르니히 변호론·조선 1789. companion=renaissance.
- 인물 +7 → **도감 47인**. EP_ORDER 시대순 재배열(renaissance 선두).
- 자산 21점(전부 PD/CC0, 육안 검수 — **데스마스크 오선정 1건 즉시 교체**, 라파예트·워싱턴 크롭). audit ×2 수정 0건.
- 허브: 시대 사슬 밴드 완성형(05→04→06→03↔02→01), EP05·06 카드. exploration '준비 중'→라이브 링크.
- 커밋 `72ed569`→`ab91602` / 배포 `a92d963`. 라이브 검증: renaissance·revolutions·자산·도감(luther·napoleon) 전부 200 ✅.

## Round 3 — 3단계: 인물 이야기(figures) 기획·실행 (0612)
- **계획**: `plan/0612_plan_hub_figures.md` — '짝으로 읽기' 컨셉(도감 47인의 모티프 승격), '시간을 건너는 편지' 장치, 신규 자산 0 설계.
- **실행**: `/history/figures/` 6섹션 — how-to(비교의 기술) + 안네↔사다코★ + 시팅불↔안중근 + 갈릴레이↔오펜하이머 + 워싱턴↔볼리바르 + 레오폴드↔모렐. 마지막 미션='나만의 짝 만들기'.
- 허브 '도감·인물' 구획 신설. audit(신규 검증 항목만) 수정 0건. 커밋 `da4f6ff` / 배포 `a529aa5`.

**시리즈 최종 현황(0612)**: 본편 6에피소드(43섹션) + 아메리카 허브(2에피소드 11섹션) + 인물 이야기(6섹션) = **9개 SPA, 60섹션, 도감 47인**. 시대 사슬 전 칸 완성.
