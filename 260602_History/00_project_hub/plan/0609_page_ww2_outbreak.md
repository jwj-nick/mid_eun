<!-- 00_project_hub/plan/0609_page_ww2_outbreak.md -->
# 0609 — 페이지 플랜: ww2 / "분노에서 전쟁으로 — 2차 세계대전의 시작" (id=outbreak)

> 순차 2번째(ww2 섹션 1). 기준=위기의 조선/ww2#imperialism 풀 업그레이드. 데이터만(엔진 재사용).

## 0. 현재 (실측)
- hook · why · cards[4] · chart · timeline[4] · connect · yt[2] · quiz · reflect[1]
- **없음**: 지도, image, voice, relations, deepdive, oldmap, people, order.
- 내용: 1차대전 후 베르사유 → 대공황 → 나치 집권 → 침략·개전.
- ww2#imperialism("사건이 사건을 부른다")의 **직접 후속** → 연결 모티프 유지.

## 1. 🗺️ 지도
1. **oldmap/territory — "베르사유 → 독일 팽창 1936~39"(★)** — 라인란트 재무장·오스트리아 병합·주데텐·체코·폴란드. territory 엔진 승격 후보(영토 변화 애니메이션). 1차로는 **battlemap의 phases**(국면별 reset)로 팽창 단계 표현 가능 → 엔진 추가 0.
2. **relations — 추축 ↔ 연합 형성** — 🟥추축(독·이·일) ↔ 🟦연합(영·프, 후 미·소). 긴장선(베르사유 굴욕·유화정책·불가침조약).

## 2. 🎨 비주얼
- **image(배열)**: ① 뮌헨협정 1938(체임벌린 "우리 시대의 평화" PD/CC) ② 베르사유 조약 서명 또는 대공황 실업 행렬 PD.
- **chart**(기존 보유 — 점검·보강): 독일 실업률/물가(하이퍼인플레) 또는 배상금 규모. relatable 추가.
- **voice**: 대공황기 가족/실업 노동자(✍️상상) 또는 히틀러 연설에 열광한 군중 목격 한 줄.
- **(2차)movies**: 〈히틀러: 악의 등장〉류 보류, 신중.

## 3. 📚 "더 깊이 ▾" (deepdive)
- **전간기 경제**: 배상금 → 하이퍼인플레(1923) → 잠깐의 안정 → 대공황(1929) 직격.
- **바이마르 공화국의 붕괴**: 민주주의가 왜 무너졌나 — 비례대표·극단정당·거리 폭력.
- **유화정책(Appeasement)의 실패**: 뮌헨협정의 논리와 오판. "평화를 원해 전쟁을 불렀다."
- **나치의 권력 장악**: 합법적 집권 → 전권위임법 → 일당 독재. (민주주의가 스스로를 폐지한 과정)
- **불가침조약**(독소 1939): 이념의 적이 손잡은 계산 → 폴란드 분할.

## 4. 제안 흐름(order)
hook → why → image:0(뮌헨협정) → cards → relations(추축↔연합) → battlemap(팽창 단계) → chart(대공황) → voice(실업 가족) → timeline → connect(→ 안네/유럽전선) → deepdive → yt → quiz → reflect

## 5. 엔진
- 전부 재사용. (territory 승격은 보류 — battlemap phases로 대체. Nick이 원하면 승격.)

## 6. Nick 코멘트
- (Nick)

---
## Round 1 — 구현 완료 ✅ 배포 (2026-06-09)
- ✅ **relations**: 추축(독·이·일) ↔ 연합(영·프·소) + 긴장선 3(베르사유 굴욕·독소 불가침조약·침략 압박).
- ✅ **battlemap**(3국면): 라인란트·오스트리아 병합 → 뮌헨협정·체코 점령 → 폴란드 침공(영·프 선전포고). 침탈(red)/저항(green).
- ✅ **voice**(대공황기 독일 청년, ✍️상상) — "누군가를 탓하는 마음"의 위험.
- ✅ **deepdive 5**: 전간기 경제(배상금→초인플레→대공황)·바이마르 붕괴·합법적 권력장악(전권위임법)·유화정책 실패·독소 불가침조약.
- ✅ **image**: 뮌헨협정 1938 정상들(Bundesarchiv Bild 183-R69173, **CC BY-SA 3.0 de**) — "평화라 믿은 순간".
- ✅ **order** 재배열(14): hook→why→image→cards→relations→battlemap→chart→voice→timeline→connect→deepdive→…
- 엔진 변경 0(전부 재사용·데이터만). 기존 chart(대공황 실업률) 유지.
- 소스(mid_eun)·배포(jwj-nick.github.io) 양쪽 커밋·push 완료. Pages 자동 빌드.
- **보류**: territory 엔진 승격(battlemap phases로 대체), movies.
