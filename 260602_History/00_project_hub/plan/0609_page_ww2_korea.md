<!-- 00_project_hub/plan/0609_page_ww2_korea.md -->
# 0609 — 페이지 플랜: ww2 / "1950년 6월의 새벽 — 한국전쟁" (id=korea)

> 순차 7번째(ww2 섹션 7, ww2 마지막). 이미 map·compare·relations 보유 → battlemap 격상이 핵심.

## 0. 현재 (실측)
- hook · why · cards[5] · map · compare · relations · timeline[4] · connect · yt[2] · quiz · reflect[2]
- **이미 보유**: map · compare · relations (구조는 풍부).
- **없음**: image, chart, voice, deepdive, people, oldmap, order, battlemap.
- 내용: 한국전쟁 — 남침·반격·휴전·분단.

## 1. 🗺️ 지도
1. **battlemap(★, 기존 map 격상)** — 전선의 극적 이동을 국면 reset으로:
   - phase① 1950.6 남침(낙동강까지 후퇴, red 남하)
   - phase② 1950.9 인천상륙(반격, green 북상) → 압록강
   - phase③ 1950.10~ 중공군 개입 → 1·4후퇴(red 재남하)
   - phase④ 1951~53 교착·휴전선(38선 부근 고착)
   - reset로 전선이 위아래로 출렁이는 비극을 시각화.

## 2. 🎨 비주얼
- **image(배열)**: ① 인천상륙작전 또는 흥남철수 PD(美 기록) ② 피란민 행렬/대동강 철교 피란("Flight of Refugees", AP 그러나 → PD/저작권 안전 대체) PD.
- **chart**: 사상자·이산가족·피해 규모 또는 참전국 수(UN 16개국). relatable("지금도 만나지 못하는 이산가족").
- **voice**: 피란민 소년·소녀/학도병/이산가족(✍️상상, 감성 — ww2 마지막을 정서적으로 닫기).
- **people(선택)**: 보류 또는 맥아더·이승만 등 신중(균형).

## 3. 📚 deepdive
- **냉전의 대리전(★)**: 한국전쟁 = 미·소 냉전이 한반도에서 터진 첫 열전. postwar와 직결.
- **휴전체제**: 종전이 아닌 정전(1953) — 평화협정 없는 분단의 지속(현재까지).
- **국제전의 성격**: UN군 16개국 + 중공군 — 한반도 내전이자 국제전.
- **분단의 심화**: 전쟁이 남긴 적대·이산·체제 고착.
- **(연결)** ww2 → 냉전 → 분단 → 오늘. ww2 에피소드의 **귀결**로 닫기.

## 4. 제안 흐름(order)
hook → why → image:0(흥남철수) → cards → battlemap(4국면 reset) → relations(남↔북/미↔중·소) → compare → chart(피해/이산) → voice(피란민, 감성) → timeline → connect → deepdive(대리전·휴전) → yt → quiz → reflect

## 5. 엔진
- battlemap·image·chart·voice·deepdive·order 재사용. 기존 단순 map → battlemap 데이터로 격상. relations·compare 유지.

## 6. Nick 코멘트
- (Nick)

---
## Round 1 — 구현 완료 ✅ 배포 (2026-06-09)
- ✅ **battlemap 4국면**(기존 단순 map 격상): ①남침→낙동강 ②인천상륙→압록강 북진 ③중공군 개입→1·4후퇴 ④교착·정전. 화살표 방향이 국면마다 뒤집히는 "출렁임"을 시각화. (compare의 4단계 텍스트와 모달리티 보완)
- ✅ **chart**: 전쟁 3년 vs 분단 73년 — "총성은 멎었지만". (정전 1953→2026 경과, 정확·균형)
- ✅ **voice**(1·4후퇴 피란 아이, ✍️상상) — "잠깐이라 믿은 피란길", ww2 전체를 정서적으로 닫음.
- ✅ **deepdive 5**: 냉전 첫 열전(대리전)·정전과 휴전체제(끝나지 않은 전쟁)·국제전(UN 16개국+중공군)·제한전과 문민통제(트루먼-맥아더)·분단이 남긴 것(오늘로 연결).
- ✅ **image**: 흥남철수 피란민(NARA/美해군, **PD**; Max Desfor AP건은 저작권 논란 회피). order 상단 배치.
- ✅ **order**(15). compare(4단계)·relations(6인 진영) 유지 → ww2 마지막 섹션답게 가장 풍부.
- 엔진 변경 0. 소스·배포 push 완료.
