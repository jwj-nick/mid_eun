<!-- 00_project_hub/plan/0609_page_ww2_europe.md -->
# 0609 — 페이지 플랜: ww2 / "거대한 전선 — 유럽과 러시아에서" (id=europe)

> 순차 3번째(ww2 섹션 3). 데이터만(엔진 재사용).

## 0. 현재 (실측)
- hook · why · cards[5] · people[2] · map · timeline[5] · connect · yt[2] · movies[2] · quiz · reflect[1]
- **이미 보유**: people2 · map · movies2 (비교적 풍부).
- **없음**: image, chart, voice, relations, deepdive, oldmap, order.
- 내용: 서부(됭케르크·영국 전투) + 동부(바르바로사·스탈린그라드) + 노르망디 D-Day.

## 1. 🗺️ 지도
1. **battlemap(★)** — 기존 단순 map → 국면 battlemap으로 격상:
   - phase① 1940 전격전(폴란드·프랑스 침공, 됭케르크) — 침탈(red) 화살표
   - phase② 1941 바르바로사(독→소 진격) + phase③ 1942~43 스탈린그라드(저항·반격, green)
   - phase④ 1944 노르망디 D-Day(서쪽 상륙) + 동서 협공 → 베를린
2. **relations** — 🟦연합(영·미·소) ↔ 🟥추축(독·이). 동맹 내 긴장(미·소 불신 = 전후 냉전 복선).

## 2. 🎨 비주얼
- **image(배열)**: ① 노르망디 상륙(Into the Jaws of Death, PD 美 국립기록보관소) ② 스탈린그라드 폐허 또는 영국 본토 공습(런던 대공습) PD.
- **chart**: 동부전선 규모 충격 — 주요 전투 병력/사상자(스탈린그라드 등) 또는 국가별 사망자. relatable.
- **voice**: 스탈린그라드 병사/레닌그라드 봉쇄 시민(✍️상상 또는 사료).
- **movies(기존2 점검)**: 〈덩케르크〉·〈most dangerous〉 등 — 적합성 신호등·실화 vs 각색 보강.

## 3. 📚 deepdive
- **전환점 분석**: 왜 스탈린그라드·미드웨이·엘알라메인이 "전환점"인가 — 주도권 이동.
- **동부전선의 규모**: 2차대전 사망자의 압도적 비중이 동부에서. "유럽 전쟁의 진짜 무게."
- **됭케르크의 기적과 영국 전투**: 항복 직전의 영국, 제공권 사수.
- **전격전(Blitzkrieg)**: 전차·항공 결합 기동전이 1차대전 참호전과 어떻게 다른가.
- **(연결)** 미·소 공조의 균열 → postwar 냉전으로.

## 4. 제안 흐름(order)
hook → why → image:0(D-Day) → cards → battlemap(4국면) → relations(연합↔추축) → chart(동부 규모) → people(처칠·… ) → voice(스탈린그라드) → movies → timeline → connect → deepdive → yt → quiz → reflect

## 5. 엔진
- 전부 재사용. 기존 map → battlemap 데이터로 교체(map 블록 제거 또는 order에서 제외).

## 6. Nick 코멘트
- (Nick)

---
## Round 1 — 구현 완료 ✅ 배포 (2026-06-09)
- ✅ **battlemap 4국면**: ①전격전(폴란드·파리·됭케르크) ②바르바로사(레닌그라드·모스크바·스탈린그라드 침공) ③스탈린그라드 반격(전환점) ④D-Day+소련 서진 협공→베를린. 침탈/저항 색.
- ✅ **relations**: 연합(영·미·소) ↔ 추축(독·이) + 긴장선(바르바로사·**영미↔소 냉전 씨앗**·영국 항공전).
- ✅ **chart**: 나라별 사망자(소련 2700만 vs 미국 42만) — "동부전선이 전쟁의 진짜 무게".
- ✅ **voice**(레닌그라드 900일 봉쇄 소녀, ✍️상상) — 메트로놈.
- ✅ **deepdive 5**: 전환점의 의미·동부전선 규모·됭케르크·전격전 vs 참호전·연합 균열(냉전 씨앗).
- ✅ **image**: 노르망디 D-Day "Into the Jaws of Death"(R.F.Sargent, 美해안경비대, **PD**) — 1400px 리사이즈(207KB).
- ✅ **order**(16) 재배열. 기존 단순 map → battlemap으로 격상(삭제). people(쉰들러·슈필만)·movies(쉰들러 리스트·피아니스트) 유지.
- 엔진 변경 0. 소스·배포 push 완료.
